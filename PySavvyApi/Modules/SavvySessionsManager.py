from PySavvyApi.SapGuiWrapper import *
from PySavvyApi.StdTCodes import SapTransactions
from PySavvyApi.Modules.SapGui import SapGui
from PySavvyApi.Modules.SavvyCredentials import SavvyCredentials
from PySavvyApi.Modules.SavvySingIn import SavvySingIn, SingInResult, MultiLoginOption

class ErrCredentiailsInvalid(Exception):
    def __init__(self):
        super().__init__('Credenciais do usuário inválidos')

class ErrStartSAPLogon(Exception):
    def __init__(self):
        super().__init__('Não foi possível iniciar o SAP Logon')

class ErrFillCredentials(Exception):
    def __init__(self):
        super().__init__('Erro ao preencher as credenciais na tela de login')

class SavvySessionsManager:
    """ Essa classe permiter o gerenciamento de sessões do SAP.
    O objetivo dessa classe é servir como suporte para a distribuição
    de sessões para diferentes scripts, ela vai permitir saber quantas sessões
    tem disponíveis para uso de scripts, obter essas sessões disponíveis.

    Os cálculos de sessões disponíveis considera o limite de sessões por
    conexão do SAP, mesmo que não tenha sessões abertas ou não esteja usando
    o limite de sessões do SAP ele irá somar essas sessões que podem ser abertas.

    Ao obter uma sessão disponível para uso a classe irá fazer o preparo para
    obter a sessão, isso inclui abrir o SAP Logon, abrir conexões, abrir sessões
    em conexões já abertas.
    """

    _credentials: SavvyCredentials
    _sap_app: GuiApplication

    _transactions_is_available: list[str]
    _max_sessions_per_conn: int
    _save_crededentials: bool
    _conn_descriptions: list[str]

    def __init__(self, *conn_descriptions: str):
        """
        Args:
            *conn_descriptions: nome das conexões para fazer o gerenciamento
        """
        self._credentials = SavvyCredentials()
        self._credentials.read_all_in_file()

        self._conn_descriptions = list(conn_descriptions)
        self._transactions_is_available = [SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN]
        self._max_sessions_per_conn = 6
        self._save_crededentials = True
        # noinspection PyTypeChecker
        self._sap_app = None

    @property
    def sap_app(self) -> GuiApplication:
        """ Obtém o objeto da plaicação do SAP Gui
        """
        if self._sap_app is None or not self._sap_app.connected_sap():
            self._sap_app = SapGui.get_sap_application()
        return self._sap_app

    @property
    def list_transactions_is_available(self) -> list[str]:
        """ Uma lista de transações, quando uma sessão está em uma dessas
        transações será considerada uma sessão disponivel.
        """
        return self._transactions_is_available

    @list_transactions_is_available.setter
    def list_transactions_is_available(self, list_transactions_is_available: list[str]) -> None:
        self._transactions_is_available = list_transactions_is_available

    @property
    def max_sessions_per_conn(self) -> int:
        """ O limite de sessões abertas por conexão do SAP.
        O limite padrão do SAP é 6 sessões por conexão, mas isso pode ser alterado
        pelo adiministrador do SAP.
        """
        return self._max_sessions_per_conn

    @max_sessions_per_conn.setter
    def max_sessions_per_conn(self, max_sessions_per_conn: int) -> None:
        self._max_sessions_per_conn = max_sessions_per_conn

    @property
    def save_crededentials(self) -> bool:
        """ Se as credenciais lidas do usuário serão salvas em um arquivo na
        pasta pessoal do usuário.
        """
        return self._save_crededentials

    @save_crededentials.setter
    def save_crededentials(self, save_crededentials: bool) -> None:
        self._save_crededentials = save_crededentials

    def sessions_available(self) -> dict[str, int]:
        """ Cálcula a quantidade de sessões disponiveis para uso.
        Returns:
            dict[str, int]: Um dicionário sendo a chave o nome da conexão e o valor a qauntidade de conexões disponiveis.
        """
        quantity_available = {}

        connections = self.sap_app.connections_list()
        for connection in connections:
            conn_description = connection.description
            if conn_description in self._conn_descriptions and connection.sessions_list[0].is_loged():
                if conn_description in quantity_available:
                    quantity_available[conn_description] += self._max_sessions_per_conn
                else:
                    quantity_available[conn_description] = self._max_sessions_per_conn
                quantity_available[conn_description] -= len(connection.sessions_not_in_transaction(*self._transactions_is_available))

        for conn_description in self._conn_descriptions:
            if conn_description not in quantity_available:
                quantity_available[conn_description] = self._max_sessions_per_conn

        return quantity_available

    def sessions_available_conn(self, conn_description: str) -> int:
        """ Cálcula a quantidade de sessões disponiveis para uso para uma conexão.
        """
        connections = self.sap_app.connections_list(conn_description)
        if not len(connections) > 0:
            return self._max_sessions_per_conn

        quantity_available = -1
        for connection in connections:
            if connection.sessions_list[0].is_loged():
                quantity_available += self._max_sessions_per_conn - len(connection.sessions_not_in_transaction(*self._transactions_is_available))

        return quantity_available if quantity_available >= 0 else self._max_sessions_per_conn

    def singin_session(self, session: GuiSession) -> SingInResult:
        """ Realiza o login de uma sessão que está na tela de login.
        Para fazer login a função usa o gerenciador de credenciais SavvyCredentials, que
        faz a leitura das credenciais do usuário e armazena em arquivo na pasta pessoal
        do usuário.
        Args:
            session: sessão na tela de login
        """
        conn_name = session.parent_cast.GuiConnection().description
        username, password = self._credentials.get_credentials(conn_name=conn_name, save_in_file=self._save_crededentials)
        return  SavvySingIn.send_credentials(session, username,password)

    def sessions_in_transactions_available(self, conn_description: str) -> list[GuiSession]:
        """ Busca todas as sessões que estão na lista de transações disponíveis.
        Args:
            conn_description: descrição da conexão no SAP para fazer a busca
        """
        sessions = []
        if self.sap_app is not None and len(self._transactions_is_available) > 0:
            connections = self.sap_app.connections_list(conn_description)
            for connection in connections:
                sessions.extend(connection.sessions_in_transaction(*self._transactions_is_available))
        return sessions

    def get_available_session(self, conn_description: str, transaction_start: str) -> Optional[GuiSession]:
        """ Busca e obtém uma sessão disponível para uso.
        Essa função prepara uma sessão para uso, isso inclui abrir o SAP Logon, abrir uma conexão e
        abrir uma nova sessão, caso necessário, ele somente não irá retornar uma sessão caso o limite
        de sessões abertas silmutanamentes foi atingindo.
        Args:
            conn_description: descrição da conexão no SAP
            transaction_start: transação para iniciar a sessão
        Returns:

        """
        if conn_description not in self._credentials.credentiails.keys():
            self._credentials.get_credentials(conn_name=conn_description, save_in_file=self._save_crededentials)

        if not SapGui.sap_running():
            if not SapGui.start_sap_logon():
                raise ErrStartSAPLogon()
        else:
            sessions = self.sessions_in_transactions_available(conn_description)
            if len(sessions) > 0:
                session = sessions[0]
                session.start_transaction(transaction_start)
                return session

        usernames = [self._credentials.credentiails[conn_description][0]]
        connections = self.sap_app.connections_list(conn_description)

        for connection in connections:
            if not connection.is_loged():
                continue

            if connection.sessions.count < self._max_sessions_per_conn:
                session = connection.create_session()
                if session is not None:
                    session.start_transaction(transaction_start)
                    return session

            username = connection.user_loged()
            if username in usernames:
                usernames.remove(username)

        has_wrong_pass: bool = False
        while len(usernames) > 0:
            session = self.sap_app.open_connection(conn_description, True).sessions.item_cast(0).GuiSession()
            result = self.singin_session(session)

            if result == SingInResult.Sucess:
                session.start_transaction(transaction_start)
                return session

            elif result == SingInResult.PopupMultiLogin:
                SavvySingIn.multi_login_select(session, MultiLoginOption.Exit)

            elif result == SingInResult.WrongCredentials:
                self._credentials.clear_credentials(conn_description)
                has_wrong_pass = True

            elif result == SingInResult.ErrorFill:
                session.parent_cast.GuiConnection().close_connection()
                raise ErrFillCredentials()

        if has_wrong_pass:
            raise ErrCredentiailsInvalid()

        return None
