import sys, win32com.client

'''
OK:
* Objects
	- GuiComponent
	- GuiContainer
	- GuiComponentCollection Collection
	- GuiApplication
	- GuiUtils
	- GuiConnection
	- GuiSession
	- GuiCollection

TODO Components:

* Priority:
    * Objects:
	- GuiScrollbar
	- GuiScrollContainer
	- GuiSessionInfo
	- GuiShell
	- GuiFrameWindow
	- GuiContainerShell
	- GuiContextMenu
	- GuiTableColumn Collection
	- GuiTableControl
	- GuiTableRow Collection221
	- GuiTabStrip

* Objects:
	- GuiAbapEditor - N/a
	- GuiApoGrid - N/a
	- GuiBarChart
	- GuiBox
	- GuiButton
	- GuiCalendar
	- GuiChart
	- GuiCheckBox
	- GuiColorSelector
	- GuiComboBox
	- GuiComboBoxControl
	- GuiComboBoxEntry
	- GuiCTextField
	- GuiCustomControl
	- GuiDialogShell
	- GuiEAIViewer2D
	- GuiEAIViewer3D
	- GuiEnum
	- GuiGOSShell
	- GuiGraphAdapt
	- GuiGridView
	- GuiHTMLViewer
	- GuiInputFieldControl
	- GuiLabel
	- ContentGuiMainWindow
	- GuiMap
	- GuiMenu
	- GuiMenubar
	- GuiMessageWindow
	- GuiModalWindow
	- GuiNetChart
	- GuiOfficeIntegration
	- GuiOkCodeField
	- GuiPasswordField
	- GuiPicture
	- GuiRadioButton
	- GuiSapChart
	- GuiSimpleContainer
	- GuiSplit
	- GuiSplitterContainer
	- GuiStage
	- GuiStatusbar
	- GuiStatusPane
	- GuiTab
	- GuiTextedit
	- GuiTextField231
	- GuiTitlebar
	- GuiToolbar
	- GuiToolbarControl
	- GuiTree
	- GuiUserArea
	- GuiVComponent
	- GuiVContainer
	- GuiVHViewSwitch
	- 
* Events
	- Change Event- Additional Remarks

* Enumerations
	- GuiComponentType
	- GuiErrorType
	- GuiEventType281
	- GuiImageType
	- GuiMagicDispIDs
	- GuiMessageBoxOption
	- GuiMessageBoxResult
	- GuiMessageBoxType
	- GuiScrollbarType
	- GuiTableSelectionType
'''

class SapNumbersTypes():
    GuiApplication = 10
    GuiBox = 62
    GuiButton = 40
    GuiCheckBox = 42
    GuiCollection = 120
    GuiComboBox = 34
    GuiComponent = 0
    GuiComponentCollection = 128
    GuiConnection = 11
    GuiContainer = 70
    GuiContainerShell = 51
    GuiContextMenu = 127
    GuiCTextField = 32
    GuiCustomControl = 50
    GuiDialogShell = 125
    GuiDockShell = 126
    GuiFrameWindow = 20
    GuiGOSShell = 123
    GuiLabel = 30
    GuiListContainer = 73
    GuiMainWindow = 21
    GuiMenu = 110
    GuiMenubar = 111
    GuiMessageWindow = 23
    GuiModalWindow = 22
    GuiOkCodeField = 35
    GuiPasswordField = 33
    GuiRadioButton = 41
    GuiScrollbar = 100
    GuiScrollContainer = 72
    GuiSession = 12
    GuiSessionInfo = 121
    GuiShell = 122
    GuiSimpleContainer = 71
    GuiSplitterContainer = 75
    GuiSplitterShell = 124
    GuiStatusbar = 103
    GuiStatusPane = 43
    GuiTab = 91
    GuiTableColumn = 81
    GuiTableControl = 80
    GuiTableRow = 82
    GuiTabStrip = 90
    GuiTextField = 31
    GuiTitlebar = 102
    GuiToolbar = 101
    GuiUnknown = -1
    GuiUserArea = 74
    GuiVComponent = 1
    GuiVContainer = 2
    GuiVHViewSwitch = 129

class SapEnums:
    MSG_OPTION_OK = 0 # A caixa de mensagem mostrará um botão "OK".
    MSG_OPTION_YESNO = 1 # A caixa de mensagem mostrará um botão “Sim” e um botão “Não”.
    MSG_OPTION_OKCANCEL = 2 # A caixa de mensagem mostrará um botão “OK” e um botão “Cancelar”.
    
    MSG_RESULT_CANCEL = 0 # A caixa de mensagem foi fechada através do botão “Cancelar”.
    MSG_RESULT_OK = 1 # A caixa de mensagem foi fechada através do botão "OK".
    MSG_RESULT_YES = 2 # A caixa de mensagem foi fechada através do botão “Sim”.
    MSG_RESULT_NO = 3 # A caixa de mensagem foi fechada através do botão “Não”.
    
    MSG_TYPE_INFORMATION = 0 # A caixa de mensagem mostra o respectivo ícone para uma mensagem informativa.
    MSG_TYPE_QUESTION = 1 # A caixa de mensagem mostra o respectivo ícone de uma pergunta.
    MSG_TYPE_WARNING = 2 # A caixa de mensagem mostra o respectivo ícone para uma mensagem de aviso.
    MSG_TYPE_ERROR = 3 # A caixa de mensagem mostra o respectivo ícone para uma mensagem de erro.
    MSG_TYPE_PLAIN = 4 # A caixa de mensagem não mostra nenhum ícone.

class SapTypeInstance():
    @staticmethod
    def GetInstance(sap_object: object):
        return SapGuiComponent(sap_object)

class SapGuiComponent():
    ''' GuiComponent é a classe base para a maioria das classes na API de script do SAP.
    '''
    
    def __init__(self, component: object):
        self.class_attrs = ['component']
        self.component = component

    def __getattr__(self, attr):
        return getattr(self.component, attr)

    def __setattr__(self, attr, value):
        if attr in self.__dict__ or attr == 'class_attrs' or attr in self.class_attrs:
            super().__setattr__(attr, value)
        else:
            setattr(self.component, attr, value)

    def IsContainerType(self) -> bool:
        ''' Retorna True se o objeto é um container
        '''
        return self.component.ContainerType
    
    def GetId(self) -> str:
        ''' Um ID de objeto é um identificador textual exclusivo para o objeto.
        Isso é construído em uma formatação semelhante a URL, começando no GuiApplication
        e detalhando o respectivo objeto.
        '''
        return self.component.Id
    
    def GetName(self) -> str:
        ''' A propriedade name é especialmente útil ao trabalhar com scripts simples que acessam apenas campos de tela.
        Nesse caso um campo pode ser encontrado usando seu nome e informações de tipo,
        que é mais fácil de ler do que um ID possivelmente muito longo. No entanto,
        não há garantia de que não existam dois objetos com o mesmo nome.
        '''
        return self.component.Name
    
    def GetParent(self) -> object:
        ''' O objeto pai acima na hierarquia de tempo de execução.
        Um objeto está sempre na coleção filhos de seu pai.
        '''
        return SapTypeInstance.GetInstance(self.component.Parent)
    
    def GetType(self) -> str:
        ''' Nome do tipo do objeto.
        As informações de tipo de GuiComponent podem ser usadas para determinar quais propriedades e métodos um objeto suporta.
        '''
        return self.component.Type
    
    def GetTypeAsNumber(self) -> int:
        '''Embora a propriedade Type seja um valor de string,
        A propriedade TypeAsNumber é um valor numerico que pode ser usado alternativamente para identificar o tipo de um objeto.
        Foi adicionado para melhor desempenho em métodos como FindByIdEx.
        '''
        return self.component.TypeAsNumber

class SapGuiComponentCollection(SapGuiComponent):
    ''' O GuiComponentCollection é usado para elementos de coleções, como a propriedade Children de contêineres.
    Cada elemento da coleção é uma extensão do GuiComponent.
    '''
    
    def ElementAt(self, index: int, on_raise: bool = True) -> SapGuiComponent:
        ''' Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        '''
        if on_raise: return self.component.ElementAt(index)
        else:
            try: return self.component.ElementAt(index)
            except: return None
    
    def Item(self, index: int, on_raise: bool = True) -> SapGuiComponent:
        ''' Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        '''
        if on_raise: return self.component.Item(index)
        else:
            try: return self.component.Item(index)
            except: return None
    
    def Count(self) -> int:
        ''' O número de elementos na coleção.
        '''
        return self.component.Count
    
    def Length(self) -> int:
        ''' O número de elementos na coleção.
        '''
        return self.component.Length
    
    def ToArray(self) -> [object]:
        ''' Retorna uma array com todos os itens da coleção
        '''
        itens = []
        for index in range(0, self.Count()):
            itens.append(self.Item(index))
        return itens

class SapGuiContainer(SapGuiComponent):
    ''' Um objeto herda a interface GuiContainer se ela puder ter filhos.
    Exemplos desta interface são janelas e subtelas, barras de ferramentas ou controles com filhos, como o controle divisor.
    '''
    
    def FindById(self, id: str, on_raise: bool = False) -> object:
        ''' Pesquise nos descendentes do objeto um determinado objeto que corresponde ao ID.
        Se nenhum descendente com o ID fornecido puder ser encontrado, a função gera uma exceção,
        a menos que o parâmetro opcional on_raise seja definido como False.
        '''
        return SapTypeInstance.GetInstance(self.component.findById(id, on_raise))
    
    def Children(self) -> SapGuiComponentCollection:
        ''' Esta coleção contém todos os filhos diretos do objeto.
        '''
        return SapGuiComponentCollection(self.component.Children)

class SapGuiUtils():
    
    def __init__(self, component: object):
        self.component = component
        
    def CloseFile(self, file: int) -> None:
        ''' Esta função fecha um arquivo que foi aberto usando OpenFile.
        '''
        self.component.CloseFile(file)
    
    def OpenFile(self, name: str) -> int:
        ''' O arquivo será criado na pasta de documentos SAP GUI.
        O valor de retorno é um identificador para o arquivo.
        name: Nome do arquivo de texto a ser criado. Por motivos de segurança, este nome não deve conter nenhuma informação de caminho.
        '''
        return self.component.OpenFile(name)
    
    def ShowMessageBox(self, title: str, text: str, msg_icon: int, msg_type: int) -> int:
        ''' Mostra uma caixa de mensagem.
        O valor de retorno será uma das constantes GuiMessageBoxResult.
        title: Título da caixa de mensagem
        text: Texto da caixa de mensagem.
        msg_icon: MsgIcon define o ícone a ser usado para a caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxType.
        msg_type: MsgType define os botões disponíveis na caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxOption.
        '''
        return self.component.ShowMessageBox(title, text, msg_icon, msg_type)
    
    def Write(self, file: int, text: str) -> None:
        ''' Escreva texto em um arquivo aberto sem uma nova linha no final.
        '''
        return self.component.Write(file, text)
    
    def WriteLine(self, file: int, text: str) -> None:
        ''' Escreva o texto em um arquivo aberto com uma nova linha no final.
        '''
        return self.component.WriteLine(file, text)

class SapGuiCollection():
    ''' GuiCollection é semelhante à coleção GuiComponentCollection, mas seus membros não são necessariamente extensões do objeto GuiComponent.
    Pode ser usado para passar uma coleção como parâmetro para funções de objetos programáveis.
    Um objeto desta classe é criado chamando a função CreateGuiCollection do objeto GuiApplication.
    '''
    
    def __init__(self, component: object):
        self.component = component
    
    def Add(self, item):
        ''' Após a criação de uma GuiCollection, os itens podem ser adicionados chamando a função add.
        '''
        self.component.Add(item)
    
    def ElementAt(self, index) -> object:
        ''' Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o index fornecido, uma exceção será gerada.
        '''
        return self.component.ElementAt(index)
    
    def Item(self, index) -> object:
        ''' Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Foi adicionado para compatibilidade com coleções do Microsoft Visual Basic.
        Se nenhum membro puder ser encontrado para o index fornecido, uma exceção será gerada.
        '''
        return self.component.Item(index)
    
    def Count(self) -> int:
        ''' O número de elementos na coleção. Esta propriedade foi adicionada para compatibilidade com coleções do Microsoft Visual Basic.
        '''
        return self.component.Count
    
    def Length(self) -> int:
        ''' O número de elementos na coleção.
        '''
        return self.component.Length
    
    def GetType(self) -> str:
        ''' As informações de tipo podem ser usadas para determinar quais propriedades e métodos um objeto suporta.
        O valor é o nome do tipo retirado desta documentação.
        O valor para GuiCollection é 'GuiCollection'.
        '''
        return self.component.Type
    
    def GetTypeAsNumber(self) -> int:
        ''' Embora a propriedade Type seja um valor de string, a propriedade TypeAsNumber é um valor longo
        que pode ser usado alternativamente para identificar o tipo de um objeto. 
        Foi adicionado para melhor desempenho em métodos como FindByIdEx.
        Os valores possíveis para esta propriedade são obtidos da enumeração GuiComponentType.
        '''
        return self.component.TypeAsNumber
        

class SapGuiSession(SapGuiContainer):
    ''' A GuiSession fornece o contexto no qual um usuário executa uma determinada tarefa, como trabalhar com uma transação.
    É, portanto, o ponto de acesso para aplicações, que gravam as ações de um usuário em relação a uma tarefa específica ou reproduzem essas ações.
    '''
    
    def AsStdNumberFormat(self, number: str) -> str:
        ''' Dependendo do formato numérico do sistema, o sinal de menos dos números pode ser colocado à direita do número.
        Usando esta função, o sinal de menos é movido para a esquerda.
        '''
        return self.component.AsStdNumberFormat(number)
    
    def ClearErrorList(self) -> None:
        ''' Este método limpa a lista de erros que podem ser criados quando controles ActiveX são encontrados em uma tela que não suporta scripts SAP GUI.
        Caso contrário, a lista será limpa após um evento de erro ser gerado. Isso acontece no final de uma viagem de ida e volta.
        '''
        return self.component.ClearErrorList()
    
    def CreateSession(self) -> None:
        ''' Esta função abre uma nova sessão, que é então visualizada por uma nova janela principal.
        Isso se assemelha ao comando "/o" que pode ser executado no campo de comando.
        '''
        # TODO: Retorna a sessão aberta
        return self.component.CreateSession()
    
    def EnableJawsEvents(self) -> None:
        ''' Habilite o envio de eventos para o leitor de tela Freedom Scientific JAWS,
        que se comunica com SAP GUI para Windows através da API de Scripting.
        Por padrão o envio de eventos está ativado.
        '''
        return self.component.EnableJawsEvents()
    
    def EndTransaction(self) -> None:
        ''' Chamar esta função tem o mesmo efeito que SendCommand("/n").
        '''
        return self.component.EndTransaction()
    
    def FindByPosition(self, x: int, y: int, on_raise: bool = True) -> SapGuiCollection:
        ''' Este método pode ser usado para fazer um hittest em uma sessão SAP GUI.
        Os parâmetros x e y devem ser fornecidos em coordenadas de tela.
        Se nenhum componente for encontrado, uma exceção será gerada, a menos que raise seja definido como False.
        Nesse caso, um objeto None é retornado.
        '''
        return SapGuiCollection(self.component.FindByPosition(x, y, on_raise))
    
    def GetIconResourceName(self, text: str) -> str:
        ''' No SAP GUI, os ícones são frequentemente descritos como texto no formato @nn@, onde nn é um número.
        A função getIconResourceName traduz a notação @nn@ no nome do recurso em sapbtmp.dll.
        '''
        return self.component.GetIconResourceName(text)
    
    def GetVKeyDescription(self, v_key: int) -> str:
        ''' Quando um script é gravado, ele geralmente contém chamadas sendVKey(n), onde n é um número.
        O método getVKeyDescription traduz esses números em um texto legível. Por exemplo, o número 0 é traduzido no texto “Enter”.
        '''
        return self.component.GetVKeyDescription(v_key)
    
    def LockSessionUI(self) -> None:
        ''' Este método bloqueia a sessão para que nenhuma interação do usuário seja possível até que a sessão seja desbloqueada usando UnlockSessionUI.
        '''
        return self.component.LockSessionUI()
    
    def UnlockSessionUI(self) -> None:
        ''' Este método desbloqueia a sessão após ela ter sido bloqueada usando LockSessionUI.
        '''
        return self.component.UnlockSessionUI()
    
    def SendCommand(self, command: str) -> None:
        ''' Usando esta função você pode executar qualquer string de comando,
        que de outra forma poderia ser inserida na caixa de combinação do campo de comando.
        '''
        return self.component.SendCommand(command)
    
    def StartTransaction(self, transaction: str) -> None:
        ''' Chamar esta função com o parâmetro "xyz" tem o mesmo efeito que SendCommand("/nxyz").
        '''
        return self.component.StartTransaction(transaction)
    
    def AccEnhancedTabChain(self, option: bool = None) -> bool:
        ''' Esta propriedade será True se a respectiva opção "Incluir elementos somente leitura e desabilitados na cadeia de guias"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        '''
        if option is None: return self.component.AccEnhancedTabChain
        else:
            self.component.AccEnhancedTabChain = option
            return self.component.AccEnhancedTabChain
    
    def AccSymbolReplacement(self, option: bool = None) -> bool:
        ''' Esta propriedade é True se a respectiva opção "Exibir símbolos em listas como letras"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        '''
        if option is None: return self.component.AccSymbolReplacement
        else:
            self.component.AccSymbolReplacement = option
            return self.component.AccSymbolReplacement
    
    def ActiveWindow(self) -> SapGuiFrameWindow:
        ''' Todas as janelas podem ser encontradas na coleção Children do GuiSession.
        No entanto, na maioria das vezes, um aplicativo acessará a janela da sessão atualmente ativada,
        pois essa é a janela com a qual o usuário provavelmente irá interagir. Esta propriedade pretende ser um atalho para esta janela.
        '''
        return SapGuiFrameWindow(self.component.ActiveWindow)
    
    def Busy(self, option: bool = None) -> bool:
        ''' Enquanto o SAP GUI aguarda dados do servidor, nenhuma chamada de script será retornada,
        o que bloqueia o thread em execução. Isto pode não ser aceitável para aplicações avançadas.
        Uma forma de evitar isso é verificar a propriedade Busy da sessão.
        Se esta propriedade for True, então uma chamada de Scripting subsequente aguardará o término da comunicação com o servidor.
        '''
        if option is None: return self.component.Busy
        else:
            self.component.Busy = option
            return self.component.Busy
    
    def ErrorList(self, errors: SapGuiCollection = None) -> SapGuiCollection:
        if errors is None: return self.component.ErrorList
        else:
            self.component.ErrorList = errors
            return SapGuiCollection(self.component.ErrorList)
    
    def Info(self) -> SapGuiSessionInfo:
        ''' As informações são do tipo GuiSessionInfo.
        Ele contém informações técnicas sobre a conexão atual, os dados de login, o aplicativo SAP em execução e muito mais.
        '''
        return SapGuiSessionInfo(self.component.Info)
    
    def IsActive(self, option: bool = None) -> bool:
        ''' TRUE se a janela da sessão estiver ativa.
        '''
        if option is None: return self.component.IsActive
        else:
            self.component.IsActive = option
            return self.component.IsActive
    
    def IsListBoxActive(self) -> bool:
        ''' Esta propriedade é True se uma caixa de listagem estiver aberta no momento (para um GuiComboBox).
        '''
        return self.component.IsListBoxActive
    
    def ListBoxCurrEntry(self) -> int:
        ''' O índice da entrada da caixa de listagem atualmente selecionada.
        '''
        return self.component.ListBoxCurrEntry
    
    def ListBoxCurrEntryHeight(self) -> int:
        ''' A altura da entrada atual da caixa de listagem em pixels.
        '''
        return self.component.ListBoxCurrEntryHeight
    
    def ListBoxCurrEntryLeft(self) -> int:
        ''' A posição esquerda da entrada atual da caixa de listagem em pixels.
        '''
        return self.component.ListBoxCurrEntryLeft
    
    def ListBoxCurrEntryTop(self) -> int:
        ''' A posição superior da entrada atual da caixa de listagem em pixels.
        '''
        return self.component.ListBoxCurrEntryTop
    
    def ListBoxCurrEntryWidth(self) -> int:
        ''' A largura da entrada atual da caixa de listagem em pixels.
        '''
        return self.component.ListBoxCurrEntryWidth
    
    def ListBoxHeight(self) -> int:
        ''' A altura da caixa de listagem aberta em pixels.
        '''
        return self.component.ListBoxHeight
    
    def ListBoxLeft(self) -> int:
        ''' A posição esquerda da caixa de listagem aberta em pixels.
        '''
        return self.component.ListBoxLeft
    
    def ListBoxTop(self) -> int:
        ''' A posição superior da caixa de listagem aberta em pixels.
        '''
        return self.component.ListBoxTop
    
    def ListBoxWidth(self) -> int:
        ''' A largura da caixa de listagem aberta em pixels.
        '''
        return self.component.ListBoxWidth
    
    def PassportPreSystemId(self, option: str = None) -> str:
        ''' O ID do pré-sistema. Parte das informações do passaporte.
        '''
        if option is None: return self.component.PassportPreSystemId
        else:
            self.component.PassportPreSystemId = option
            return self.component.PassportPreSystemId
    
    def PassportSystemId(self, option: str = None) -> str:
        ''' O ID do sistema. Parte das informações do passaporte.
        '''
        if option is None: return self.component.PassportSystemId
        else:
            self.component.PassportSystemId = option
            return self.component.PassportSystemId
    
    def PassportTransactionId(self, option: str = None) -> str:
        ''' O ID exclusivo da transação. Parte das informações do passaporte.
        '''
        if option is None: return self.component.PassportTransactionId
        else:
            self.component.PassportTransactionId = option
            return self.component.PassportTransactionId
    
    def ProgressPercent(self) -> int:
        ''' A porcentagem exibida pelo indicador de progresso do SAP GUI.
        '''
        return self.component.ProgressPercent
    
    def ProgressText(self) -> str:
        ''' O texto exibido pelo indicador de progresso.
        '''
        return self.component.ProgressText
    
    def Record(self, option: bool = None) -> bool:
        ''' Definir esta propriedade como True habilita o modo de gravação da sessão.
        Neste modo, as alterações nos elementos da interface do usuário são registradas no SAP GUI e enviadas 
        para um aplicativo de gravação usando o evento Change descrito posteriormente.
        Observações:
        Alguns elementos da interface do usuário podem se comportar de maneira diferente no modo de gravação e durante a reprodução ou interação manual.
        * A caixa de diálogo de ajuda F4 é sempre exibida como uma janela modal.
        * Arrastar e soltar está desativado.
        '''
        if option is None: return self.component.Record
        else:
            self.component.Record = option
            return self.component.Record
    
    def RecordFile(self, option: str = None) -> str:
        ''' Uma maneira simples de gravar um script é definir a propriedade recordFile com um nome de arquivo válido e, 
        em seguida, ativar a propriedade record. Um arquivo Visual Basic Script com o nome fornecido será criado na 
        pasta SAP GUI Scripts no PC cliente.
        Observações: Esta propriedade aceita apenas nomes de arquivos simples sem informações de caminho.
        '''
        if option is None: return self.component.RecordFile
        else:
            self.component.RecordFile = option
            return self.component.RecordFile
    
    def SaveAsUnicode(self, option: bool = None) -> bool:
        ''' Se esta propriedade estiver configurada como TRUE, os scripts gravados serão salvos na codificação UNICODE.
        Overwise é a página de código do sistema atual.
        '''
        if option is None: return self.component.SaveAsUnicode
        else:
            self.component.SaveAsUnicode = option
            return self.component.SaveAsUnicode
    
    def ShowDropdownKeys(self, option: bool = None) -> bool:
        ''' Se esta propriedade for TRUE, os menus suspensos mostrarão não apenas o texto das entradas suspensas, mas também as chaves.
        '''
        if option is None: return self.component.ShowDropdownKeys
        else:
            self.component.ShowDropdownKeys = option
            return self.component.ShowDropdownKeys
    
    def SuppressBackendPopups(self, option: bool = None) -> bool:
        if option is None: return self.component.SuppressBackendPopups
        else:
            self.component.SuppressBackendPopups = option
            return self.component.SuppressBackendPopups
    
    def TestToolMode(self, option: int = None) -> int:
        ''' Durante os testes internos, alguns aspectos da interface do usuário mostraram-se difíceis de lidar com
        ferramentas de teste que usam a API de script para automatizar o SAP GUI. Por esta razão foi adicionado um
        modo especial no qual as seguintes alterações são administradas.
        
        * Embora as mensagens de sucesso (S), aviso (W) e erro (E) sejam sempre exibidas na barra de status, 
            as mensagens de informação (I) e de aborto (A) são exibidas como janelas pop-up, a menos que testToolMode esteja definido.
        * O modo de atualização do servidor de aplicativos é alterado para modo imediato para a conexão.
        * As mensagens do sistema são ignoradas para não interromper a gravação ou reprodução de scripts.
        
        0: Desativar TestToolMode
        1: Habilite TestToolMode
        '''
        if option is None: return self.component.TestToolMode
        else:
            self.component.TestToolMode = option
            return self.component.TestToolMode

class SapGuiConnection(SapGuiContainer):
    ''' Um GuiConnection representa a conexão entre o SAP GUI e um servidor de aplicativos.
    As conexões podem ser abertas a partir do SAP Logon ou dos métodos openConnection e openConnectionByConnectionString do GuiApplication.
    '''
    
    def CloseConnection(self) -> None:
        ''' Este método fecha uma conexão junto com todas as suas sessões.
        '''
        self.component.CloseConnection()
    
    def CloseConnection(self, id: str) -> None:
        ''' Uma sessão pode ser encerrada chamando este método de conexão
        Fechar a última sessão de uma conexão também fechará a conexão.
        O parâmetro "id" deve conter o id da sessão a ser fechada (como "/app/con[0]/ses[0]").
        '''
        self.component.CloseSession(id)
    
    def ConnectionString(self) -> str:
        ''' Esta propriedade contém a cadeia de conexão que define a conexão de backend.
        É mais difícil de ler, mas não depende das entradas do SAP Logon.
        Mais informações sobre strings de conexão podem ser encontradas no capítulo Método OpenConnectionByConnectionString.
        '''
        return self.component.ConnectionString
    
    def Description(self) -> str:
        ''' Esta descrição só estará disponível se a conexão tiver sido iniciada a partir do SAP Logon ou usando GuiApplication.OpenConnection.
        Em ambos os casos, a descrição pode ser usada ao chamar o método OpenConnection para reproduzir um script no mesmo sistema.
        '''
        return self.component.Description
    
    def DisabledByServer(self) -> bool:
        ''' Esta propriedade será configurada como True se o suporte a scripts não tiver sido ativado para o servidor de aplicativos.
        '''
        return self.component.DisabledByServer
    
    def Sessions(self) -> SapGuiComponentCollection:
        ''' Esta propriedade é outro nome para a propriedade Children.
        Foi adicionado para melhor legibilidade, pois todos os filhos do GuiConnection são sessões.
        '''
        return SapGuiComponentCollection(self.component.Sessions)
    
    def SessionsArray(self) -> [SapGuiSession]:
        ''' Retorna uma array com as sessões
        '''
        return self.Sessions().ToArray()

class SapGuiApplication(SapGuiContainer):
    ''' O GuiApplication representa o processo no qual ocorre toda a atividade SAP GUI.
    Se o componente de script for acessado anexando-se a um processo SAP Logon, então GuiApplication representará SAP Logon.
    GuiApplication é uma classe criável. Contudo, deve haver apenas um componente deste tipo em qualquer processo. GuiApplication estende o objeto GuiContainer.
    '''
    
    def AddHistoryEntry(self, field_name: str, value: str) -> bool:
        ''' SAP GUI para Windows possui uma funcionalidade de histórico de entrada,
        que exibe para campos de texto as entradas feitas no passado como sugestão.
        Com esta função, uma entrada pode ser adicionada ao banco de dados de histórico para que esteja disponível na 
        próxima vez que o usuário final acessar o campo de texto com o nome de campo fornecido.
        '''
        return self.component.AddHistoryEntry(field_name, value)
    
    def CreateGuiCollection(self) -> object: #TODO
        ''' Algumas funções aceitam coleções como parâmetros.
        Esta função cria um objeto de coleção independente da linguagem de script usada.
        '''
        return self.component.CreateGuiCollection()
    
    def DropHistory(self) -> bool:
        ''' Chamar esta função excluirá todas as entradas do histórico de entrada.
        A função retorna True se os dados do histórico foram excluídos com sucesso.
        Atenção: Após eliminar o banco de dados de histórico, ele não poderá ser restaurado.
        Portanto esta função deve ser usada com cautela.
        '''
        return self.component.DropHistory()
    
    def OpenConnection(self, description: str, sync = False, on_raise: bool = True) -> SapGuiConnection:
        ''' O parâmetro Descrição deverá conter uma das descrições exibidas no SAP Logon, por exemplo "XYZ [PÚBLICO]".
        Se você deseja criar uma nova instância SAP GUI e colocá-la em sua aplicação, você pode adicionar o sufixo "/INPLACE".
        
        Esta função irá gerar a exceção E_ACCESSDENIED se o suporte a scripts tiver sido desabilitado pelo administrador ou pelo usuário.
        '''
        return SapGuiConnection(self.component.OpenConnection(description, sync, on_raise))
    
    def OpenConnectionByConnectionString(self, connect_string: str, sync = False, on_raise: bool = True) -> SapGuiConnection:
        ''' O parâmetro ConnectString é a string de conexão do servidor SAP, por exemplo “/R/ALR/G/SPACE”.
        Consulte a descrição do método openConnection para uma discussão sobre os parâmetros de sincronização e aumento.
        '''
        return SapGuiConnection(self.component.OpenConnection(connect_string, sync, on_raise))
    
    def GetActiveSession(self) -> SapGuiSession:
        ''' Retorna a Sessão com a qual o usuário está trabalhando atualmente, que será a janela superior.
        '''
        return SapGuiSession(self.component.ActiveSession)
    
    def AllowSystemMessages(self, enable: bool = None) -> bool:
        ''' As mensagens do sistema são exibidas quando um administrador as invoca no servidor para enviar uma notificação aos usuários atualmente logados.
        Isso pode acontecer a qualquer momento e interferir na gravação ou reprodução de um script.
        Definir esta propriedade como FALSE impedirá que mensagens do sistema sejam exibidas.
        '''
        if enable is None: return self.component.AllowSystemMessages
        else:
            self.component.AllowSystemMessages = enable
            return self.component.AllowSystemMessages
    
    def ButtonbarVisible(self, enable: bool = None) -> bool:
        ''' Definir esta propriedade como FALSE oculta a barra de ferramentas da aplicação na janela principal para conexões recém-abertas.
        '''
        if enable is None: return self.component.ButtonbarVisible
        else:
            self.component.ButtonbarVisible = enable
            return self.component.ButtonbarVisible
    
    def ConnectionErrorText(self) -> str:
        ''' Esta propriedade contém o texto de uma mensagem de erro de conexão.
        Se OpenConnection falhar, será possível recuperar informações sobre a causa da falha dessa propriedade.
        '''
        return self.component.ConnectionErrorText
    
    def Connections(self) -> SapGuiComponentCollection:
        ''' Esta propriedade é outro nome para a propriedade Children.
        Foi adicionado para melhor legibilidade, pois todos os filhos do GuiApplication são conexões.
        '''
        return SapGuiComponentCollection(self.component.Connections)
    
    def ConnectionsArray(self) -> [SapGuiConnection]:
        ''' Retorna uma array com as conexões
        '''
        return self.Connections().ToArray()
    
    def HistoryEnabled(self, enable: bool = None) -> bool:
        ''' A função de histórico local pode ser habilitada ou desabilitada usando esta propriedade.
        Desativá-lo melhorará significativamente o desempenho do SAP GUI, o que pode ser crucial durante testes de carga, por exemplo.
        '''
        if enable is None: return self.component.HistoryEnabled
        else:
            self.component.HistoryEnabled = enable
            return self.component.HistoryEnabled
    
    def MajorVersion(self) -> int:
        ''' Versão da versão SAP GUI, por exemplo '7.60'.
        '''
        return self.component.MajorVersion
    
    def NewVisualDesign(self) -> bool:
        ''' Retorna se o modo Novo Design Visual ou Clássico é usado para a interface do usuário.
        '''
        return self.component.NewVisualDesign
    
    def Patchlevel(self) -> int:
        ''' Nível de patch do SAP GUI.
        '''
        return self.component.Patchlevel
    
    def Revision(self) -> int:
        ''' Revisão da versão SAP GUI. No SAP GUI para Windows, este é o número de compilação.
        '''
        return self.component.Revision
    
    def StatusbarVisible(self, visible: bool = None) -> bool:
        ''' Definir esta propriedade como FALSE oculta a barra de status da janela principal para conexões recém-abertas.
        '''
        if visible is None: return self.component.StatusbarVisible
        else:
            self.component.StatusbarVisible = visible
            return self.component.StatusbarVisible
    
    def TitlebarVisible(self, visible: bool = None) -> bool:
        ''' Definir esta propriedade como FALSE oculta a barra de título da janela principal para conexões recém-abertas.
        '''
        if visible is None: return self.component.TitlebarVisible
        else:
            self.component.TitlebarVisible = visible
            return self.component.TitlebarVisible
    
    def ToolbarVisible(self, visible: bool = None) -> bool:
        ''' Definir esta propriedade como FALSE oculta a barra de ferramentas do sistema da janela principal para conexões recém-abertas.
        '''
        if visible is None: return self.component.ToolbarVisible
        else:
            self.component.ToolbarVisible = visible
            return self.component.ToolbarVisible
    
    def Utils(self) -> SapGuiUtils:
        ''' Esta propriedade retorna um objeto GuiUtils global.
        '''
        return self.component.Utils
        