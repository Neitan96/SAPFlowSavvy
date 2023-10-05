from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiConnection import GuiConnection
from PySavvyApi.SapGuiWrapper.Objects.GuiSession import GuiSession
from PySavvyApi.SapGuiWrapper.Objects.GuiUtils import GuiUtils
from PySavvyApi.SapGuiWrapper.Objects.GuiComponentCollection import GuiComponentCollection


class GuiApplication(GuiContainer):
    """ O GuiApplication representa o processo no qual ocorre toda a atividade SAP GUI.
    Se o componente de script for acessado anexando-se a um processo SAP Logon, então GuiApplication representará SAP Logon.
    GuiApplication é uma classe criável. Contudo, deve haver apenas um componente deste tipo em qualquer processo.
    GuiApplication estende o objeto GuiContainer.
    """

    def add_history_entry(self, field_name: str, value: str) -> bool:
        """ SAP GUI para Windows possui uma funcionalidade de histórico de entrada,
        que exibe para campos de texto as entradas feitas no passado como sugestão.
        Com esta função, uma entrada pode ser adicionada ao banco de dados de histórico para estar disponível na
        próxima vez que o usuário final acessar o campo de texto com o nome de campo fornecido.
        """
        return self.component.AddHistoryEntry(field_name, value)

    def create_gui_collection(self) -> object:
        """ Algumas funções aceitam coleções como parâmetros.
        Esta função cria um objeto de coleção independente da linguagem de script usada.
        """
        # TODO
        return self.component.CreateGuiCollection()

    def drop_history(self) -> bool:
        """ Chamar esta função excluirá todas as entradas do histórico de entrada.
        A função retorna True se os dados do histórico foram excluídos com sucesso.
        Atenção: Após eliminar o banco de dados de histórico, ele não poderá ser restaurado.
        Portanto, esta função deve ser usada com cautela.
        """
        return self.component.DropHistory()

    def open_connection(self, description: str, sync=False, on_raise: bool = True) -> GuiConnection:
        """ O parâmetro Descrição deverá conter uma das descrições exibidas no SAP Logon, por exemplo, "XYZ [PÚBLICO]".
        Se você deseja criar uma nova instância SAP GUI e colocá-la em sua aplicação, você pode adicionar o sufixo "/INPLACE".

        Esta função irá gerar a exceção E_ACCESSDENIED se o suporte a scripts tiver sido desabilitado pelo administrador ou pelo usuário.
        """
        conn = self.component.OpenConnection(description, sync, on_raise)
        return GuiConnection(conn)

    def open_connection_by_connection_string(self, connect_string: str, sync=False,
                                             on_raise: bool = True) -> GuiConnection:
        """ O parâmetro ConnectString é a string de conexão do servidor SAP, por exemplo “/R/ALR/G/SPACE”.
        Consulte a descrição do método openConnection para uma discussão sobre os parâmetros de sincronização e aumento.
        """
        conn = self.component.OpenConnection(connect_string, sync, on_raise)
        return GuiConnection(conn)

    @property
    def get_active_session(self) -> GuiSession:
        """ Retorna a Sessão com a qual o usuário está trabalhando atualmente, que será a janela superior.
        """
        return GuiSession(self.component.ActiveSession)

    @property
    def allow_system_messages(self) -> bool:
        """ As mensagens do sistema são exibidas quando um administrador as invoca no servidor para enviar uma notificação aos usuários atualmente logados.
        Isso pode acontecer a qualquer momento e interferir na gravação ou reprodução de um script.
        Definir esta propriedade como FALSE impedirá que mensagens do sistema sejam exibidas.
        """
        return self.component.AllowSystemMessages

    @allow_system_messages.setter
    def allow_system_messages(self, enable: bool = None) -> None:
        """ As mensagens do sistema são exibidas quando um administrador as invoca no servidor para enviar uma notificação aos usuários atualmente logados.
        Isso pode acontecer a qualquer momento e interferir na gravação ou reprodução de um script.
        Definir esta propriedade como FALSE impedirá que mensagens do sistema sejam exibidas.
        """
        self.component.AllowSystemMessages = enable

    @property
    def buttonbar_visible(self) -> bool:
        """ Definir esta propriedade como FALSE oculta a barra de ferramentas da aplicação na janela principal para conexões recém-abertas.
        """
        return self.component.ButtonbarVisible

    @buttonbar_visible.setter
    def buttonbar_visible(self, enable: bool = None) -> None:
        """ Definir esta propriedade como FALSE oculta a barra de ferramentas da aplicação na janela principal para conexões recém-abertas.
        """
        self.component.ButtonbarVisible = enable

    @property
    def connection_error_text(self) -> str:
        """ Esta propriedade contém o texto de uma mensagem de erro de conexão.
        Se OpenConnection falhar, será possível recuperar informações sobre a causa da falha dessa propriedade.
        """
        return self.component.ConnectionErrorText

    @property
    def connections(self) -> GuiComponentCollection:
        """ Esta propriedade é outro nome para a propriedade Children.
        Foi adicionado para melhor legibilidade, pois todos os filhos do GuiApplication são conexões.
        """
        return GuiComponentCollection(self.component.Connections)

    def connections_list(self, description: str = None) -> list[GuiConnection]:
        """ Retorna uma list com as conexões
        """
        if description is None:
            # noinspection PyTypeChecker
            return self.connections.to_list()

        return list(filter(lambda conn: conn.description == description, self.connections_list(None)))

    @property
    def history_enabled(self) -> bool:
        """ A função de histórico local pode ser habilitada ou desabilitada usando esta propriedade.
        Desativá-lo melhorará significativamente o desempenho do SAP GUI, o que pode ser crucial durante testes de carga, por exemplo.
        """
        return self.component.HistoryEnabled

    @history_enabled.setter
    def history_enabled(self, enable: bool = None) -> None:
        """ A função de histórico local pode ser habilitada ou desabilitada usando esta propriedade.
        Desativá-lo melhorará significativamente o desempenho do SAP GUI, o que pode ser crucial durante testes de carga, por exemplo.
        """
        self.component.HistoryEnabled = enable

    @property
    def major_version(self) -> int:
        """ Versão da versão SAP GUI, por exemplo '7.60'.
        """
        return self.component.MajorVersion

    @property
    def new_visual_design(self) -> bool:
        """ Retorna se o modo Novo Design Visual ou Clássico é usado para a interface do usuário.
        """
        return self.component.NewVisualDesign

    @property
    def patchlevel(self) -> int:
        """ Nível de patch do SAP GUI.
        """
        return self.component.Patchlevel

    @property
    def revision(self) -> int:
        """ Revisão da versão SAP GUI. No SAP GUI para Windows, este é o número de compilação.
        """
        return self.component.Revision

    @property
    def statusbar_visible(self) -> bool:
        """ Definir esta propriedade como FALSE oculta a barra de status da janela principal para conexões recém-abertas.
        """
        return self.component.StatusbarVisible

    @statusbar_visible.setter
    def statusbar_visible(self, visible: bool = None) -> None:
        """ Definir esta propriedade como FALSE oculta a barra de status da janela principal para conexões recém-abertas.
        """
        self.component.StatusbarVisible = visible

    @property
    def titlebar_visible(self) -> bool:
        """ Definir esta propriedade como FALSE oculta a barra de título da janela principal para conexões recém-abertas.
        """
        return self.component.TitlebarVisible

    @titlebar_visible.setter
    def titlebar_visible(self, visible: bool = None) -> None:
        """ Definir esta propriedade como FALSE oculta a barra de título da janela principal para conexões recém-abertas.
        """
        self.component.TitlebarVisible = visible

    @property
    def toolbar_visible(self) -> bool:
        """ Definir esta propriedade como FALSE oculta a barra de ferramentas do sistema da janela principal para conexões recém-abertas.
        """
        return self.component.ToolbarVisible

    @toolbar_visible.setter
    def toolbar_visible(self, visible: bool = None) -> None:
        """ Definir esta propriedade como FALSE oculta a barra de ferramentas do sistema da janela principal para conexões recém-abertas.
        """
        self.component.ToolbarVisible = visible

    @property
    def utils(self) -> GuiUtils:
        """ Esta propriedade retorna um objeto GuiUtils global.
        """
        return GuiUtils(self.component.Utils)
