import win32com.client

class GuiSessionInfo:
    """ GuiSessionInfo é membro de todos os objetos GuiSession.
    Disponibiliza informações técnicas sobre a sessão. Algumas de suas propriedades são exibidas na
    área de informações do sistema (na barra de status ou na área de título dependendo do tema SAP GUI utilizado).
    """

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    @property
    def application_server(self) -> str:
        """ O nome do servidor de aplicação é definido somente se a sessão pertencer a uma conexão
        iniciada sem balanceamento de carga, especificando um servidor de aplicação.
        """
        return self.component.ApplicationServer

    @property
    def client(self) -> str:
        """ O cliente selecionado na tela de login.
        """
        return self.component.Client

    @property
    def codepage(self) -> int:
        """ A página de códigos especificada no SAP Logon nas propriedades da conexão.
        """
        return self.component.Codepage

    @property
    def flushes(self) -> int:
        """ A propriedade Flushes conta o número de liberações na fila de automação durante a comunicação do servidor.
        """
        return self.component.Flushes

    @property
    def group(self) -> str:
        """ As informações do grupo de login estarão disponíveis somente se a sessão
        pertencer a uma conexão que foi iniciada usando balanceamento de carga.
        """
        return self.component.Group

    @property
    def gui_codepage(self) -> int:
        """ Uma lista de codepages está disponível na tabela TCP00A do sistema SAP.
        Em um cliente executando Microsoft Windows com página de código 1252 (Latin I), a propriedade guiCodepage é 1160.
        """
        return self.component.GuiCodepage

    @property
    def i18n_mode(self) -> bool:
        """ O modo I18N do SAP GUI é necessário para conjuntos de caracteres multibyte.
        """
        return self.component.I18NMode

    @property
    def interpretation_time(self) -> int:
        """ O tempo de interpretação começa após a chegada dos dados do servidor.
        Compreende a análise dos dados e distribuição para os elementos SAP GUI. A unidade é milissegundos.
        """
        return self.component.InterpretationTime

    @property
    def is_low_speed_connection(self) -> bool:
        """ A propriedade é True se a conexão à qual pertence à sessão roda com flag de conexão de baixa velocidade.
        Esse sinalizador pode ser definido na página de propriedades de conexão avançadas da caixa de diálogo SAPLogon.
        O suporte ao SAP GUI Scripting é muito limitado para conexões de baixa velocidade, porque as informações necessárias
        para identificar objetos SAP GUI não estão sendo enviadas.
        """
        return self.component.IsLowSpeedConnection

    @property
    def language(self) -> str:
        """ O idioma especificado na tela de login.
        """
        return self.component.Language

    @property
    def message_server(self) -> str:
        """ As informações do servidor de mensagens estarão disponíveis somente se a
        sessão pertencer a uma conexão que foi iniciada usando balanceamento de carga.
        """
        return self.component.MessageServer

    @property
    def program(self) -> str:
        """ O nome do programa de origem que está sendo executado no momento.
        """
        return self.component.Program

    @property
    def response_time(self) -> int:
        """ Este é o tempo gasto na comunicação da rede desde o momento em que os dados são
        enviados ao servidor até o momento em que chega a resposta do servidor. A unidade é milissegundos.
        """
        return self.component.ResponseTime

    @property
    def round_trips(self) -> int:
        """ Antes do SAP GUI enviar dados ao servidor, ele bloqueia a interface do usuário.
        Em muitos casos, ele não desbloqueará a interface quando os dados chegarem do servidor,
        mas enviará uma nova solicitação ao servidor imediatamente. Os controles, em particular,
        usam essa tecnologia para carregar os dados necessários para visualização.
        A contagem dessas alternâncias de token entre o SAP GUI e o servidor é a propriedade roundTrips.
        """
        return self.component.RoundTrips

    @property
    def screen_number(self) -> int:
        """ O número da tela exibida atualmente.
        """
        return self.component.ScreenNumber

    @property
    def scripting_mode_read_only(self) -> bool:
        """ O modo somente leitura pode ser ativado usando um parâmetro de perfil do servidor de aplicativos.
        Neste modo o estado das aplicações SAP não pode ser alterado através da API de Scripting, o que significa:
        * As propriedades só podem ser lidas, mas não definidas
        * As funções só podem ser chamadas se não alterarem o estado do controle.
        Observações:
        Neste modo, os scripts podem ser gravados e as informações sobre o aplicativo podem ser lidas no SAP GUI,
        no entanto, uma transação não pode ser executada a partir de um script.
        """
        return self.component.ScriptingModeReadOnly

    @property
    def scripting_mode_recording_disabled(self) -> bool:
        """ O modo de gravação desabilitada pode ser habilitado usando um parâmetro de perfil do servidor de aplicativos.
        Neste modo, o SAP GUI Scripting não dispara nenhum evento. Isso implica que a interação do usuário não pode ser registrada.
        No entanto, os dados podem ser lidos no SAP GUI e os scripts podem ser usados para executar transações.
        """
        return self.component.ScriptingModeRecordingDisabled

    @property
    def session_number(self) -> int:
        """ O número da sessão também é exibido no SAP GUI na barra de status.
        """
        return self.component.SessionNumber

    @property
    def system_name(self) -> str:
        """ Este é o nome do sistema SAP.
        """
        return self.component.SystemName

    @property
    def system_number(self) -> int:
        """ O número do sistema é definido somente se a sessão pertencer a uma
        conexão iniciada sem balanceamento de carga, especificando um servidor de aplicação.
        """
        return self.component.SystemNumber

    @property
    def system_session_id(self) -> str:
        """ Todas as sessões SAP GUI da mesma conexão são representadas no servidor com o mesmo SystemSessionId.
        Usando SystemSessionId e SessionNumber, é possível encontrar uma sessão SAP GUI correspondente a partir de um aplicativo ABAP.
        """
        return self.component.SystemSessionId

    @property
    def transaction(self) -> str:
        """ A transação que está sendo executada atualmente.
        """
        return self.component.Transaction

    @property
    def ui_guideline (self) -> str:
        """ Esta propriedade pode ser utilizada para identificar se a sessão SAP GUI está rodando com Fiori Visual Theme (Belize) ou não.
        O valor de retorno é
        1 se a sessão estiver sendo executada sem Fiori Visual Theme (Belize)
        2 se a sessão estiver rodando com Fiori Visual Theme (Belize)
        """
        return self.component.UI_GUIDELINE

    @property
    def user(self) -> str:
        """ O nome SAP do usuário conectado ao sistema.
        """
        return self.component.User
