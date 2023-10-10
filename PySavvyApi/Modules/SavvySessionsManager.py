from PySavvyApi.SapGuiWrapper import *
from PySavvyApi.StdTCodes import SapTransactions
from PySavvyApi.Modules.SapGui import SapGui
from PySavvyApi.Modules.SavvySessionsFilter import SavvySessionsFilter
from PySavvyApi.Modules.SavvyCredentials import SavvyCredentials
from PySavvyApi.Modules.SavvySingIn import SavvySingIn, SingInResult, MultiLoginOption

class SavvySessionsManager:

    filter: SavvySessionsFilter
    credentials: SavvyCredentials

    main_menu_available: bool
    max_sessions: int
    save_creds: bool
    conn_names: list[str]
    _sap_app: GuiApplication

    def __init__(self, *conn_names: str, main_menu_available: bool = True, max_sessions_per_conn: int = 6, save_creds: bool = True):
        """
        Args:
            main_menu_available: se deseja considerar as sessões no menu principal como sessões disponiveis
            max_sessions_per_conn: número de sessões máximas por conexão
            save_creds: se deseja salvar as credenciais obtidas em um arquivo na pasta pessoal do usuário
            *conn_names: nome das conexões para fazer o gerenciamento das conexões
        """
        self.filter = SavvySessionsFilter()
        self.credentials = SavvyCredentials()
        self.credentials.read_all_in_file()

        self.main_menu_available = main_menu_available
        self.max_sessions = max_sessions_per_conn
        self.save_creds = save_creds
        self.conn_names = list(conn_names)
        # noinspection PyTypeChecker
        self._sap_app = None

    @property
    def sap_app(self) -> GuiApplication:
        if self._sap_app is None or not self._sap_app.connected_sap():
            self._sap_app = SapGui.get_sap_application()
        return self._sap_app


    def connections(self) -> list[GuiConnection]:
        return self._sap_app.connections_list()

    def sessions(self) -> list[GuiSession]:
        return self._sap_app.sessions_list()

    def sessions_available(self) -> dict[str, int]:
        quantity_available = {}
        for conn in self.conn_names:
            quantity_available[conn] = self.max_sessions

        connections = self.sap_app.connections_list()
        for connection in connections:
            if connection.description in quantity_available.keys():
                if connection.sessions_list[0].is_loged():
                    if self.main_menu_available:
                        quantity_available[connection.description] -= len(connection.sessions_not_in_transaction(SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN))
                    else:
                        quantity_available[connection.description] -= connection.sessions.count


        return quantity_available

    def sessions_available_conn(self, conn_name: str) -> int:

        connections = self.sap_app.connections_list(conn_name)
        if not len(connections) > 0:
            return self.max_sessions

        quantity_available = 0
        for connection in connections:
            if connection.description == conn_name:
                if connection.sessions_list[0].is_loged():
                    if self.main_menu_available:
                        quantity_available += self.max_sessions - len(connection.sessions_not_in_transaction(SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN))
                    else:
                        quantity_available += self.max_sessions - connection.sessions.count

        return quantity_available

    def singin_session(self, session: GuiSession, new_try_on_fail: bool = True) -> Optional[GuiSession]:
        conn_name = session.parent_cast.GuiConnection().description
        username, password = self.credentials.get_credentials(conn_name=conn_name, save_in_file=self.save_creds)
        result_login = SavvySingIn.send_credentials(session, username,password)

        if result_login == SingInResult.Sucess:
            return session

        if result_login == SingInResult.WrongCredentials:
            self.credentials.clear_credentials(conn_name)
            if new_try_on_fail:
                if not session.connected_sap():
                    session = self.sap_app.open_connection(conn_name, True).sessions_list[0]
                return self.singin_session(session, False)

            return None

        if result_login == SingInResult.PopupMultiLogin:
            SavvySingIn.multi_login_select(session, MultiLoginOption.Exit)
            return None

        if result_login == SingInResult.ErrorFill:
            return None

    def get_available_session(self, conn_name: str) -> Optional[GuiSession]:
        if conn_name not in self.credentials.credentials.keys():
            self.credentials.get_credentials(conn_name=conn_name, save_in_file=self.save_creds)

        if conn_name not in self.credentials.credentials.keys():
            return None

        if not SapGui.sap_running():
            SapGui.start_sap_logon()

        usernames = [self.credentials.credentials[conn_name][0]]
        connections = self.sap_app.connections_list(conn_name)

        for connection in connections:
            sessions = connection.sessions_in_transaction(SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN)
            if len(sessions) > 0:
                return sessions[0]

        for connection in connections:
            sessions = connection.sessions_list
            if not sessions[0].is_loged():
                connection.close_connection()
                continue

            if len(sessions) < self.max_sessions:
                return connection.create_session()

            username = sessions[0].info.user
            if username in usernames:
                usernames.remove(username)

        if len(usernames) > 0:
            session_to_login = self.sap_app.open_connection(conn_name, True).sessions_list[0]
            session_to_login = self.singin_session(session_to_login)
            return session_to_login

        return None
