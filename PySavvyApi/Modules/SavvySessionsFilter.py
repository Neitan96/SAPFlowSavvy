from PySavvyApi.Modules.SapGui import SapGui
from PySavvyApi.SapGuiWrapper import GuiApplication, GuiSession

class SavvySessionsFilter:
    """ Classe feita para facilitar a obtenção de sessões a partir de filtros.
    """

    _sap_app: GuiApplication
    _conn_names: list[str]
    _users: list[str]
    _in_transactions: list[str]
    _not_in_transactions: list[str]
    _p_only_loged: bool
    _p_only_not_loged: bool
    _sessions_app_count_min: int
    _sessions_app_count_max: int

    def __init__(self, sap_app: GuiApplication = None):
        self._sap_app = sap_app

        self._conn_names = []
        self._users = []
        self._in_transactions = []
        self._not_in_transactions = []
        self._p_only_loged = False
        self._p_only_not_loged = False
        self._sessions_app_count_min = -1
        self._sessions_app_count_max = -1

    def conn_name(self, *conn_name: str) -> None:
        self._conn_names.extend(conn_name)

    def user(self, *user: str) -> None:
        self._users.extend(user)

    def in_transaction(self, *transaction: str) -> None:
        self._in_transactions.extend(transaction)

    def not_is_transaction(self, *transaction: str) -> None:
        self._not_in_transactions.extend(transaction)

    def only_loged(self) -> None:
        self._p_only_loged = True

    def only_not_loged(self) -> None:
        self._p_only_not_loged = True

    def conn_sessions_count_min(self, min_sessions: int) -> None:
        self._sessions_app_count_min = min_sessions

    def conn_sessions_count_max(self, max_sessions: int) -> None:
        self._sessions_app_count_max = max_sessions

    def get_sessions(self) -> list[GuiSession] | None:
        """ Faz a busca das sessões conforme os filtros definidos.
        Returns:
            list[GuiSession]: Sessões filtradas
        """
        sap_app = self._sap_app
        if sap_app is None or not sap_app.connected_sap():
            sap_app = SapGui.get_sap_application()

        if sap_app is None or not sap_app.connected_sap():
            return None

        sessions: list[GuiSession]
        sessions = sap_app.sessions_list()

        if len(self._conn_names) > 0:
            sessions = list(filter(lambda session: session.parent_cast.GuiConnection().description in self._conn_names, sessions))

        if len(self._users) > 0:
            sessions = list(filter(lambda session: session.info.user in self._users, sessions))

        if len(self._in_transactions) > 0:
            sessions = list(filter(lambda session: session.info.transaction in self._in_transactions, sessions))

        if len(self._not_in_transactions) > 0:
            sessions = list(filter(lambda session: session.info.transaction not in self._not_in_transactions, sessions))

        if self._p_only_loged:
            sessions = list(filter(lambda session: session.is_loged(), sessions))

        if self._p_only_not_loged:
            sessions = list(filter(lambda session: not session.is_loged(), sessions))

        if self._sessions_app_count_min > 0:
            sessions = list(filter(lambda session: session.parent_cast.GuiConnection().sessions.count >= self._sessions_app_count_min, sessions))

        if self._sessions_app_count_max > 0:
            sessions = list(filter(lambda session: session.parent_cast.GuiConnection().sessions.count <= self._sessions_app_count_max, sessions))

        return sessions

