from PySavvyApi.Modules.SapGui import SapGui
from PySavvyApi.StdTCodes import SapTransactions
from PySavvyApi.SapGuiWrapper import GuiApplication, GuiConnection, GuiSession
from PySavvyApi.Modules.MultiCredentials import MultiCredentials


class ErrCredentiailsInvalid(Exception):
    def __init__(self):
        super().__init__('Credenciais do usuário inválidos')

class ErrFillCredentials(Exception):
    def __init__(self):
        super().__init__('Erro ao preencher as credenciais na tela de login')


class SessionsManager:
    """ Classe para gerenciar as sessões do SAP

    Essa classe realiza o gerenciamento de sessões do SAP para automatizações paralelas, ou seja,
    tem a capacidade de lidar com várias sessões do SAP ao mesmo tempo.

    Para isso, esse gerenciador mantém uma lista de transações disponíveis para uso,
    qualquer transação nessa lista é considerada livre para uso, e qualquer transação
    fora dessa lista é considerada ocupada, e não pode ser usada até que seja liberada.

    Essa classe depende da classe MultiCredentials para obter as credenciais do usuário para logar no SAP.

    Notes:
        - Ao finalizar alguma automação, é importante liberar a sessão do SAP para que outras automações possam usar,
        para isso, basta ir para uma transção da lista de transações disponíveis, por padrão o menu principal do SAP é
        uma transação disponível, é possivel ir para o menu principal usando a função `return_to_menu()` o objeto
        da sessão.
    """

    _credentials: MultiCredentials
    _sap_app: GuiApplication

    _transactions_is_available: list[str]

    def __init__(self, credentials: MultiCredentials = None):
        self.credentials = credentials
        self._transactions_is_available = [SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN]

    @property
    def credentials(self) -> MultiCredentials:
        """ Obtém o gereciador de credenciais do SAP.
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: MultiCredentials = None):
        """ Define o gereciador de credenciais do SAP.
        """
        if credentials is None:
            credentials = MultiCredentials()
            credentials.load_creds_file()
        self._credentials = credentials

    @property
    def sap_app(self) -> GuiApplication:
        """ Obtém o objeto da plaicação do SAP Gui.
        """
        if self._sap_app is None or not self._sap_app.connected_sap():
            self._sap_app = SapGui.get_sap_application()
        return self._sap_app

    @property
    def transactions_is_available(self) -> list[str]:
        """ Retorna a lista de transações disponíveis para uso.
        """
        return self._transactions_is_available.copy()

    @transactions_is_available.setter
    def transactions_is_available(self, transactions: list[str]):
        """ Define a lista de transações disponíveis para uso.
        """
        self._transactions_is_available = transactions.copy()

    def add_transaction_is_available(self, transaction: str):
        """ Adiciona uma transação a lista de transações disponíveis para uso.
        """
        self._transactions_is_available.append(transaction)

    def remove_transaction_is_available(self, transaction: str):
        """ Remove uma transação da lista de transações disponíveis para uso.
        """
        self._transactions_is_available.remove(transaction)





















