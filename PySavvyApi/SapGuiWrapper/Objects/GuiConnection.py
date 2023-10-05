from typing import Optional

from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiApplication import GuiApplication
from PySavvyApi.SapGuiWrapper.Objects.GuiSession import GuiSession
from PySavvyApi.SapGuiWrapper.Objects.GuiComponentCollection import GuiComponentCollection


class GuiConnection(GuiContainer):
    """ Um GuiConnection representa a conexão entre o SAP GUI e um servidor de aplicativos.
    As conexões podem ser abertas a partir do SAP Logon ou dos métodos openConnection e openConnectionByConnectionString do GuiApplication.
    """

    def parent(self) -> GuiApplication:
        return GuiApplication(self.component.Parent)

    def close_connection(self) -> None:
        """ Este método fecha uma conexão com todas as suas sessões.
        """
        self.component.CloseConnection()

    def close_session(self, id_session: str) -> None:
        """ Uma sessão pode ser encerrada chamando este método de conexão
        Fechar a última sessão de uma conexão também fechará a conexão.
        O parâmetro "id" deve conter o id da sessão a ser fechada (como "/app/con[0]/ses[0]").
        """
        self.component.CloseSession(id_session)

    @property
    def connection_string(self) -> str:
        """ Esta propriedade contém a cadeia de conexão que define a conexão de backend.
        É mais difícil de ler, mas não depende das entradas do SAP Logon.
        Mais informações sobre strings de conexão podem ser encontradas no capítulo Método OpenConnectionByConnectionString.
        """
        return self.component.ConnectionString

    @property
    def description(self) -> str:
        """ Esta descrição só estará disponível se a conexão tiver sido iniciada a partir do SAP Logon ou usando GuiApplication.OpenConnection.
        Em ambos os casos, a descrição pode ser usada ao chamar o método OpenConnection para reproduzir um script no mesmo sistema.
        """
        return self.component.Description

    @property
    def disabled_by_server(self) -> bool:
        """ Esta propriedade será configurada como True se o suporte a scripts não tiver sido ativado para o servidor de aplicativos.
        """
        return self.component.DisabledByServer

    @property
    def sessions(self) -> GuiComponentCollection:
        """ Esta propriedade é outro nome para a propriedade Children.
        Foi adicionado para melhor legibilidade, pois todos os filhos do GuiConnection são sessões.
        """
        return GuiComponentCollection(self.component.Sessions)

    @property
    def sessions_list(self) -> list[GuiSession]:
        """ Retorna uma list com as sessões
        """
        # noinspection PyTypeChecker
        return self.sessions.to_list()

    def create_session(self) -> Optional[GuiSession]:
        """ Abre uma nova sessão na conexão.
        """
        sessions = self.sessions_list
        sessions.reverse()
        session_count = len(sessions)
        for session in sessions:
            session.CreateSession()
            if self.sessions.count > session_count:
                # noinspection PyTypeChecker
                return self.sessions.last_item()
        return None

    def sessions_user(self, user_name: str) -> list[GuiSession]:
        """ Obtém todas as sessões do usuário.
        """
        return list(filter(lambda session: session.info.user == user_name, self.sessions_list))

    def sessions_in_transaction(self, transaction: str) -> [GuiSession]:
        """ Obtém todas as sessões que está na transação.
        """
        return list(filter(lambda session: session.info.transaction == transaction, self.sessions_list))
