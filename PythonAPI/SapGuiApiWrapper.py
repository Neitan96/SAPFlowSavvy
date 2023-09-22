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
	- GuiSessionInfo
	- GuiVComponent
	- GuiVContainer
	- GuiFrameWindow
	- GuiScrollbar
	- GuiScrollContainer
	- GuiTabStrip
	- GuiTab
	- GuiTableRow
	- GuiTableColumn
	- GuiMenu
	- GuiContextMenu
	- GuiBox
	- GuiButton
	- GuiCheckBox
	- GuiEnum
	- GuiShell
	- GuiContainerShell
	- GuiTableControl
	- GuiGridView
	- GuiModalWindow
	- GuiComboBox
	- GuiComboBoxEntry
	- GuiComboBoxControl
	- GuiSapChart
	- GuiChart
	- GuiUserArea
	- GuiToolbar
	- GuiTitlebar
	- GuiStatusbar
	- GuiStatusPane
	- GuiTree
	- GuiToolbarControl
	- GuiTextField
	- GuiTextedit
	- GuiRadioButton
	- GuiPasswordField
	- GuiLabel
	- GuiCTextField
	- GuiCustomControl
	- GuiInputFieldControl
	- GuiSimpleContainer
	- GuiSplit
	- GuiSplitterContainer
	- GuiAbapEditor
	- GuiApoGrid
	- GuiBarChart
	- GuiCalendar
	- GuiColorSelector
	- GuiDialogShell
	- GuiEAIViewer2D

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
 
TODO Components:

* Objects:
	- GuiEAIViewer3D
	- GuiGOSShell
	- GuiGraphAdapt
	- GuiHTMLViewer
	- ContentGuiMainWindow
	- GuiMap
	- GuiMenubar
	- GuiMessageWindow
	- GuiNetChart
	- GuiOfficeIntegration
	- GuiOkCodeField
	- GuiPicture
	- GuiStage
	- GuiVHViewSwitch
	- 
'''

'''
- Application - Representa a aplicação SAP GUI.
  - Connection - Representa a conexão a um servidor SAP.
    - Session - Representa uma sessão SAP.
      - StatusBar - Representa a barra de status na sessão SAP.
      - Scripting - Permite acesso ao ambiente de script da sessão.
        - GuiFrameWindow - Representa uma janela de quadro na sessão SAP.
          - GuiMainWindow - Representa a janela principal na sessão SAP.
            - GuiVContainer - Contêiner vertical para abas e componentes.
              - GuiVTab - Representa uma aba no contêiner vertical.
                - GuiShell - Uma área de trabalho para exibir informações e interações.
                  - GuiGridView - Uma grade para exibir dados tabulares.
                  - GuiShellObject - Um objeto na área de trabalho do shell.
                  - GuiGridView - Uma grade para exibir dados tabulares.
                - GuiComponent - Componente de entrada de dados.
                  - GuiCTextField - Campo de texto simples.
                  - GuiCTextEdit - Área de edição de texto.
                  - GuiComboBox - Caixa de combinação (lista suspensa).
                  - GuiCTextField - Campo de texto simples.
                  - GuiCTextEdit - Área de edição de texto.
                  - GuiComboBox - Caixa de combinação (lista suspensa).
              - GuiContainer - Um contêiner genérico.
                - GuiShell - Uma área de trabalho para exibir informações e interações.
                - GuiFrameWindow - Representa uma janela de quadro na sessão SAP.
                - GuiContainer - Outro contêiner genérico.
                  - GuiTab - Representa uma aba em um contêiner.
                  - GuiTree - Uma árvore para exibir hierarquias.
                  - GuiTreeItem - Um item em uma árvore.
                  - GuiToolbar - Uma barra de ferramentas com botões.
                - GuiVContainer - Contêiner vertical para abas e componentes.
                  - GuiVTab - Representa uma aba no contêiner vertical.
                    - GuiShell - Uma área de trabalho para exibir informações e interações.
                    - GuiGridView - Uma grade para exibir dados tabulares.
                - GuiComponent - Componente de entrada de dados.
                  - GuiCTextField - Campo de texto simples.
                  - GuiCTextEdit - Área de edição de texto.
                  - GuiComboBox - Caixa de combinação (lista suspensa).
'''

class SapGuiComponentType:
    GuiApplication = 10  # Aplicação: Representa a aplicação SAP GUI em si, permitindo interagir com todo o ambiente SAP.
    GuiBox = 62  # Caixa: Uma caixa de diálogo ou janela usada para exibir informações ou solicitar entrada do usuário.
    GuiButton = 40  # Botão: Um botão clicável que normalmente dispara ações ou comandos quando pressionado.
    GuiCheckBox = 42  # Caixa de Seleção: Uma caixa que pode ser marcada ou desmarcada para indicar uma escolha ou opção.
    GuiCollection = 120  # Coleção: Representa uma coleção de elementos ou objetos SAP GUI, permitindo operações em massa.
    GuiComboBox = 34  # Caixa de Combinação: Uma caixa de texto com uma lista suspensa de opções que o usuário pode selecionar.
    GuiComponent = 0  # Componente: O componente base que pode representar qualquer elemento na interface do SAP GUI.
    GuiComponentCollection = 128  # Coleção de Componentes: Uma coleção de componentes SAP GUI, útil para gerenciar vários elementos.
    GuiConnection = 11  # Conexão: Representa uma conexão com um servidor SAP, permitindo a seleção de diferentes sessões.
    GuiContainer = 70  # Contêiner: Um elemento que pode conter outros componentes, como um grupo de botões ou campos.
    GuiContainerShell = 51  # Shell de Contêiner: Um shell que contém componentes em uma hierarquia de árvore.
    GuiContextMenu = 127  # Menu de Contexto: Um menu contextual que oferece opções específicas do contexto para um componente.
    GuiCTextField = 32  # Campo de Texto Curto: Um campo de entrada de texto para entrada de dados breve.
    GuiCustomControl = 50  # Controle Personalizado: Um componente personalizado criado para atender a requisitos específicos.
    GuiDialogShell = 125  # Shell de Diálogo: Uma janela de diálogo que normalmente exibe informações detalhadas ou solicitações ao usuário.
    GuiDockShell = 126  # Shell de Ancoragem: Um shell de ancoragem usado para ancorar janelas em áreas específicas da interface.
    GuiFrameWindow = 20  # Janela de Quadro: Uma janela de quadro que pode conter outros elementos, como caixas de diálogo.
    GuiGOSShell = 123  # Shell de SOS: Um shell usado para exibir mensagens do sistema SAP e mensagens de erro.
    GuiLabel = 30  # Rótulo: Um rótulo de texto usado para exibir informações ou etiquetar outros componentes.
    GuiListContainer = 73  # Contêiner de Lista: Um contêiner que exibe uma lista de itens, como uma lista de seleção.
    GuiMainWindow = 21  # Janela Principal: A janela principal da aplicação SAP GUI, que contém a maioria dos elementos da interface.
    GuiMenu = 110  # Menu: Um menu suspenso que fornece acesso a várias opções e comandos.
    GuiMenubar = 111  # Barra de Menu: A barra de menu superior que contém menus e comandos.
    GuiMessageWindow = 23  # Janela de Mensagem: Uma janela que exibe mensagens e notificações do sistema SAP.
    GuiModalWindow = 22  # Janela Modal: Uma janela que bloqueia a interação com outras partes da interface até ser fechada.
    GuiOkCodeField = 35  # Campo de Código OK: Um campo de entrada de código que pode ser usado para inserir comandos específicos.
    GuiPasswordField = 33  # Campo de Senha: Um campo de entrada de senha usado para entrada segura de senhas.
    GuiRadioButton = 41  # Botão de Opção: Uma opção que pode ser selecionada entre várias opções mutuamente exclusivas.
    GuiScrollbar = 100  # Barra de Rolagem: Uma barra que permite rolar o conteúdo de uma área maior.
    GuiScrollContainer = 72  # Contêiner de Rolagem: Um contêiner que suporta rolagem de conteúdo.
    GuiSession = 12  # Sessão: Representa uma sessão de comunicação com um servidor SAP.
    GuiSessionInfo = 121  # Informações de Sessão: Fornece informações sobre a sessão SAP atual.
    GuiShell = 122  # Shell: Uma janela de nível superior que pode conter outros componentes.
    GuiSimpleContainer = 71  # Contêiner Simples: Um contêiner simples que contém outros componentes.
    GuiSplitterContainer = 75  # Contêiner de Divisão: Um contêiner que suporta divisão de áreas com barras divisórias.
    GuiSplitterShell = 124  # Shell de Divisão: Um shell que suporta divisão de áreas com barras divisórias.
    GuiStatusbar = 103  # Barra de Status: Uma barra na parte inferior da interface que exibe informações de status.
    GuiStatusPane = 43  # Painel de Status: Um painel dentro da barra de status que pode exibir informações adicionais.
    GuiTab = 91  # Guia: Uma guia que permite alternar entre diferentes conjuntos de conteúdo.
    GuiTableColumn = 81  # Coluna de Tabela: Uma coluna em uma tabela que contém dados tabulares.
    GuiTableControl = 80  # Controle de Tabela: Um controle que exibe dados tabulares em linhas e colunas.
    GuiTableRow = 82  # Linha de Tabela: Uma linha em uma tabela que contém dados tabulares.
    GuiTabStrip = 90  # Tira de Guia: Uma tira de guias que permite alternar entre várias guias.
    GuiTextField = 31  # Campo de Texto: Um campo de entrada de texto para entrada de dados.
    GuiTitlebar = 102  # Barra de Título: A barra superior de uma janela que exibe o título e os botões de controle.
    GuiToolbar = 101  # Barra de Ferramentas: Uma barra que contém botões de ação e comandos frequentemente usados.
    GuiUnknown = -1  # Desconhecido: Um componente cujo tipo não é reconhecido ou não está definido.
    GuiUserArea = 74  # Área do Usuário: Uma área que pode conter componentes personalizados ou elementos específicos do usuário.
    GuiVComponent = 1  # VComponent: Um tipo específico de componente visual.
    GuiVContainer = 2  # VContainer: Um tipo específico de contêiner visual.
    GuiVHViewSwitch = 129  # VHViewSwitch: Um tipo de interruptor de exibição usado em componentes visuais.

class SapGuiErrorType:
    Gui_Err_AccessDenied = 633 # Acesso negado.
    Gui_Err_Bad_Focus = 634 # Não é possível definir o foco neste objeto.
    Gui_Err_Bad_Index_Type = 618 # Tipo de índice inválido para acesso à coleção.
    Gui_Err_Control_Label = 615 # O controle não pôde ser encontrado pelo rótulo.
    Gui_Err_Control_Name = 608 # O controle não pôde ser encontrado pelo nome.
    Gui_Err_Control_Position = 616 # O controle não pôde ser encontrado pela posição.
    Gui_Err_Disconnected = 621 # O objeto invocado se desconectou de seus clientes.
    Gui_Err_Enumerator_Index = 614 # O enumerador da coleção não pode encontrar um elemento com o índice especificado.
    Gui_Err_Enumerator_Reset = 612 # O enumerador da coleção não pode ser redefinido.
    Gui_Err_FindById = 619 # O controle não pôde ser encontrado pelo ID.
    Gui_Err_FindByName = 620 # O controle não pôde ser encontrado pelo nome.
    Gui_Err_FindByPos = 632 # O controle não pôde ser encontrado pela posição.
    Gui_Err_Front_Module = 602 # O caminho do 'sapfront.dll' não pôde ser determinado.
    Gui_Err_Init = 601 # O mecanismo do Sapgui não pode ser inicializado.
    Gui_Err_Int_Get_Session_Failed = 629 # Não é possível obter a sessão do TLS.
    Gui_Err_Int_GetCtrl_Failed = 625 # Não foi possível obter o controle (Erro interno).
    Gui_Err_Int_GetFocusManFromSes_Failed = 627 # Não foi possível obter o gerenciador de foco da sessão (Erro interno).
    Gui_Err_Int_GetSesFromCtrl_Failed = 626 # Não foi possível obter a sessão do controle (Erro interno).
    Gui_Err_Int_Invalid_TestToolMode = 628 # Modo de ferramenta de teste inválido.
    Gui_Err_Int_View_Not_Set = 630 # Visão não definida (Erro interno).
    Gui_Err_Invalid_Argument = 613 # O método recebeu um argumento inválido.
    Gui_Err_Invalid_Context = 603 # Função chamada em contexto de thread inválido.
    Gui_Err_Invalid_Window = 611 # A janela requerida é inválida.
    Gui_Err_Logon_Module = 604 # O 'Componente de Logon do Sapgui' não pôde ser instanciado.
    Gui_Err_Menu_Disabled = 623 # O item de menu está desativado.
    Gui_Err_No_Memory = 607 # O sistema está sem memória.
    Gui_Err_No_Wrapper = 622 # Nenhum wrapper disponível para este controle.
    Gui_Err_Not_Implemented = 610 # O método ou propriedade não está atualmente implementado.
    Gui_Err_Permission_Denied = 637 # Permissão negada.
    Gui_Err_Property_Readonly = 609 # A propriedade é somente leitura.
    Gui_Err_Resize_Failed = 631 # Falha ao redimensionar.
    Gui_Err_Sapgui_Module = 605 # O 'Componente Sapgui' não pôde ser instanciado.
    Gui_Err_Save_Image = 635 # Erro ao salvar a imagem.
    Gui_Err_Scripting_Disabled_Srv = 624 # O scripting está desativado pelo servidor.
    Gui_Err_Session_Index = 606 # O índice da sessão está fora de alcance.
    Gui_Err_Shortcut_Evaluation = 636 # Falha na avaliação do atalho.
    Gui_Err_SL_No_Entry = 1000 # Não é uma entrada válida do SAPLogon.
    Gui_Err_VKey_Disabled = 617 # A tecla virtual não está habilitada.

class SapGuiEventType:
    SapApplicationCreateSessionEvent = 2002 # Evento de Criação de Sessão da Aplicação
    SapApplicationDestroySessionEvent = 2003 # Evento de Destruição de Sessão da Aplicação
    SapApplicationErrorEvent = 2004 # Evento de Erro da Aplicação
    SapApplicationIgnoreSessionEvent = 2005 # Evento de Ignorar Sessão da Aplicação
    SapContextMenuEvent = 1282 # Menu de Contexto
    SapCustomDataChangedEvent = 1280 # Evento de Dados Personalizados Alterados
    SapDefaultEvent = 0 # Evento Padrão
    SapHitSelectEvent = 1281 # Evento de Seleção de Hit
    SapSessionAbapScriptingEvent = 1289 # Evento de Abap Scripting da Sessão
    SapSessionActivatedEvent = 1285 # Evento de Ativação da Sessão
    SapSessionAutoFCodeEvent = 1284 # Evento de Auto FCode da Sessão
    SapSessionDestroyEvent = 1283 # Evento de Destruição da Sessão
    SapSessionEndRequestEvent = 515 # Evento de Fim de Requisição da Sessão
    SapSessionErrorEvent = 516 # Evento de Erro da Sessão
    SapSessionFocusChangedEvent = 1286 # Evento de Mudança de Foco da Sessão
    SapSessionHistoryOpenedEvent = 1287 # Evento de Histórico da Sessão Aberto
    SapSessionProgressIndicatorEvent = 1288 # Evento de Indicador de Progresso da Sessão
    SapSessionStartRequestEvent = 514 # Evento de Início de Requisição da Sessão

class SapGuiImageType:
    BMP = 0
    GIF = 2
    JPEG = 1
    PNG = 2

class SapGuiMagicDispIDs:
    GuiDispIDBTPress = 32200
    GuiDispIDCBChecked = 32011
    GuiDispIDCBCurListBoxEntry = 32305
    GuiDispIDCBEntries = 32302
    GuiDispIDCBEntryKey = 33800
    GuiDispIDCBEntryPos = 33802
    GuiDispIDCBEntryValue = 33801
    GuiDispIDCBIsListBoxActive = 32304
    GuiDispIDCBKey = 32300
    GuiDispIDCBKeySpace = 32303
    GuiDispIDCBShowKey = 32306
    GuiDispIDCBValue = 32301
    GuiDispIDCollAdd = 33103
    GuiDispIDCollCount = 33100
    GuiDispIDCollElAt = 33102
    GuiDispIDCollLength = 33101
    GuiDispIDConConnString = 33003
    GuiDispIDConDescription = 33002
    GuiDispIDConDisabled = 33001
    GuiDispIDConnClose = 32831
    GuiDispIDConSessions = 33000
    GuiDispIDCTFindAllByName = 32035
    GuiDispIDCTFindAllByNameEx = 32036
    GuiDispIDCTFindById = 32029
    GuiDispIDCTFindByLabel = 32027
    GuiDispIDCTFindByName = 32026
    GuiDispIDCTFindByNameEx = 32034
    GuiDispIDCTFindByPosition = 32028
    GuiDispIDDockerIsVertical = 34301
    GuiDispIDDockerPixelSize = 34300
    GuiDispIDEngAddHist = 32913
    GuiDispIDEngButtonB = 32903
    GuiDispIDEngCon = 32900
    GuiDispIDEngConnErr = 32924
    GuiDispIDEngCrColl = 32911
    GuiDispIDEngDropHist = 32914
    GuiDispIDEngGetEng = 1
    GuiDispIDEngHistEnabled = 32916
    GuiDispIDEngIgnore = 32908
    GuiDispIDEngInplace = 32907
    GuiDispIDEngMajor = 32909
    GuiDispIDEngMinor = 32910
    GuiDispIDEngNoSysMsg = 32925
    GuiDispIDEngOpenCon = 32905
    GuiDispIDEngOpenConEx = 32918
    GuiDispIDEngOpenWDCon = 32926
    GuiDispIDEngPatchlevel = 32919
    GuiDispIDEngQuit = 32906
    GuiDispIDEngRegister = 32921
    GuiDispIDEngRevision = 32920
    GuiDispIDEngRevoke = 32923
    GuiDispIDEngStatusB = 32902
    GuiDispIDEngTheme = 32912
    GuiDispIDEngTitleB = 32904
    GuiDispIDEngToolB = 32901
    GuiDispIDEngUtils = 32917
    GuiDispIDEngWDSessions = 32927
    GuiDispIDErrDesc1 = 33601
    GuiDispIDErrDesc2 = 33602
    GuiDispIDErrDesc3 = 33603
    GuiDispIDErrDesc4 = 33604
    GuiDispIDErrNo = 33600
    GuiDispIDGActiveSession = 32049
    GuiDispIDGActiveSession2 = 32075
    GuiDispIDGCAccDescription = 33703
    GuiDispIDGCAccLabelCol = 32043
    GuiDispIDGCAccText = 32044
    GuiDispIDGCAccTextOnReq = 32045
    GuiDispIDGCAccTooltip = 32042
    GuiDispIDGCChangeable = 32009
    GuiDispIDGCCharHeight = 32073
    GuiDispIDGCCharLeft = 32070
    GuiDispIDGCCharTop = 32071
    GuiDispIDGCCharWidth = 32072
    GuiDispIDGCChildren = 32019
    GuiDispIDGCClass = 32017
    GuiDispIDGCColorIndex = 32058
    GuiDispIDGCColorIntensified = 32059
    GuiDispIDGCColorInverse = 32060
    GuiDispIDGCCtxMnu = 33701
    GuiDispIDGCDefaultTooltip = 32069
    GuiDispIDGCDisplayedText = 32074
    GuiDispIDGCDragDrop = 33706
    GuiDispIDGCDumpState = 31194
    GuiDispIDGCFlushing = 33704
    GuiDispIDGCHeight = 32006
    GuiDispIDGCHwnd = 33702
    GuiDispIDGCIcon = 32037
    GuiDispIDGCId = 32025
    GuiDispIDGCIsContainer = 32033
    GuiDispIDGCIsHotspot = 32051
    GuiDispIDGCIsList = 32052
    GuiDispIDGCIsStepLoop = 32062
    GuiDispIDGCIsSymbolFont = 32061
    GuiDispIDGCLeft = 32003
    GuiDispIDGCLeftLabel = 32040
    GuiDispIDGCLoopCurrentCol = 32065
    GuiDispIDGCLoopCurrentRow = 32066
    GuiDispIDGCLoopHeight = 32064
    GuiDispIDGCLoopWidth = 32063
    GuiDispIDGCModified = 32030
    GuiDispIDGCName = 32001
    GuiDispIDGCOcxEvents = 33705
    GuiDispIDGCParent = 32038
    GuiDispIDGCParentFrame = 32050
    GuiDispIDGCRightLabel = 32041
    GuiDispIDGCRowText = 32053
    GuiDispIDGCScreenLeft = 32046
    GuiDispIDGCScreenTop = 32047
    GuiDispIDGCSession = 32018
    GuiDispIDGCSetFocus = 32024
    GuiDispIDGCShortId = 32031
    GuiDispIDGCShowContextMenu = 32068
    GuiDispIDGCSubType = 33700
    GuiDispIDGCText = 32000
    GuiDispIDGCTitle = 32048
    GuiDispIDGCTooltip = 32008
    GuiDispIDGCTop = 32004
    GuiDispIDGCType = 32015
    GuiDispIDGCTypeAsNum = 32032
    GuiDispIDGCVisualize = 32039
    GuiDispIDGCWidth = 32005
    GuiDispIDGECATTReplay = 32076
    GuiDispIDGetAbsoluteRow = 33407
    GuiDispIDGMSelect = 33300
    GuiDispIDGMWFocusedButton = 32433
    GuiDispIDGMWHelpButtonHelpText = 32440
    GuiDispIDGMWHelpButtonText = 32435
    GuiDispIDGMWMessageText = 32437
    GuiDispIDGMWMessageType = 32436
    GuiDispIDGMWOKButtonHelpText = 32439
    GuiDispIDGMWOKButtonText = 32434
    GuiDispIDGMWVisible = 32438
    GuiDispIDGUCharHeight = 32603
    GuiDispIDGUCharWidth = 32602
    GuiDispIDGUHorizontalScrollbar = 32600
    GuiDispIDGUListNav = 32605
    GuiDispIDGUOTFPreview = 32606
    GuiDispIDGUResize = 32604
    GuiDispIDGUVerticalScrollbar = 32601
    GuiDispIDGWButtonB = 32425
    GuiDispIDGWClose = 32414
    GuiDispIDGWCompBitmap = 32443
    GuiDispIDGWGuiFocus = 32422
    GuiDispIDGWHandle = 32420
    GuiDispIDGWHardCopy = 32415
    GuiDispIDGWHardCopyMem = 32441
    GuiDispIDGWIconic = 32400
    GuiDispIDGWIconify = 32408
    GuiDispIDGWIsPopupDialog = 32427
    GuiDispIDGWJumpBackward = 32432
    GuiDispIDGWJumpForward = 32431
    GuiDispIDGWMaximize = 32410
    GuiDispIDGWMoveWindow = 32407
    GuiDispIDGWPopupDialogText = 32428
    GuiDispIDGWRestore = 32409
    GuiDispIDGWSpyMode = 32413
    GuiDispIDGWStatusB = 32424
    GuiDispIDGWSysFocus = 32421
    GuiDispIDGWTabBackward = 32430
    GuiDispIDGWTabForward = 32429
    GuiDispIDGWTitleB = 32426
    GuiDispIDGWToolB = 32423
    GuiDispIDGWVKAllowed = 32412
    GuiDispIDGWWPHeight = 32417
    GuiDispIDGWWPMsgBox = 32419
    GuiDispIDGWWPResize = 32418
    GuiDispIDGWWPResizeEx = 32442
    GuiDispIDGWWPWidth = 32416
    GuiDispIDIsListBoxActive = 32840
    GuiDispIDLCursor = 32022
    GuiDispIDLHighlighted = 32100
    GuiDispIDLIsLeftLabel = 32101
    GuiDispIDLIsRightLabel = 32102
    GuiDispIDListBoxCurrEntry = 32849
    GuiDispIDListBoxCurrEntryHeight = 32848
    GuiDispIDListBoxCurrEntryLeft = 32846
    GuiDispIDListBoxCurrEntryTop = 32845
    GuiDispIDListBoxCurrEntryWidth = 32847
    GuiDispIDListBoxHeight = 32844
    GuiDispIDListBoxLeft = 32842
    GuiDispIDListBoxTop = 32841
    GuiDispIDListBoxWidth = 32843
    GuiDispIDLListProperty = 32103
    GuiDispIDLMaxLength = 32012
    GuiDispIDLNumerical = 32013
    GuiDispIDLPassword = 32016
    GuiDispIDLSimpleListProperty = 32104
    GuiDispIDMsgAsPopup = 34004
    GuiDispIDMsgId = 34001
    GuiDispIDMsgNumber = 34002
    GuiDispIDMsgPar = 34003
    GuiDispIDMsgType = 34000
    GuiDispIDOcxCallbackChange = 200889
    GuiDispIDOcxCallbackHighlight = 200890
    GuiDispIDOcxCallbackHit = 200891
    GuiDispIDOcxControl = 271062
    GuiDispIDOcxGetRect = 31192
    GuiDispIDOcxHit = 31195
    GuiDispIDOcxHitTest = 31193
    GuiDispIDOcxHover = 31196
    GuiDispIDOcxIsReadOnlyCall = 31191
    GuiDispIDOcxNotify = 31199
    GuiDispIDOcxNotifyContEvSink = 31197
    GuiDispIDOcxNotifyCtrlEvent = 31198
    GuiDispIDOKF1 = 32351
    GuiDispIDOKOpened = 32350
    GuiDispIDRBGroupColl = 32504
    GuiDispIDRBGroupCount = 32502
    GuiDispIDRBGroupPos = 32503
    GuiDispIDRBSelect = 32501
    GuiDispIDRBSelected = 32500
    GuiDispIDSBDblClick = 32750
    GuiDispIDScrollMax = 33904
    GuiDispIDScrollMin = 33905
    GuiDispIDScrollPage = 33903
    GuiDispIDScrollPos = 33902
    GuiDispIDScrollRange = 33900
    GuiDispIDSesActivWin = 32800
    GuiDispIDSesBusy = 32803
    GuiDispIDSesClearErrorList = 32825
    GuiDispIDSesClose = 32811
    GuiDispIDSesCmd = 32805
    GuiDispIDSesCmdAsync = 32806
    GuiDispIDSesCreate = 32812
    GuiDispIDSesEnableAccSymbols = 32830
    GuiDispIDSesEnableAccTabChain = 32829
    GuiDispIDSesEnableJaws = 32828
    GuiDispIDSesEndT = 32810
    GuiDispIDSesErrorList = 32824
    GuiDispIDSesFindByPos = 32818
    GuiDispIDSesIconDesc = 33525
    GuiDispIDSesInfo = 32802
    GuiDispIDSesInfoAppSr = 33508
    GuiDispIDSesInfoCl = 33509
    GuiDispIDSesInfoCP = 33512
    GuiDispIDSesInfoDisRec = 33521
    GuiDispIDSesInfoDynp = 33506
    GuiDispIDSesInfoFlush = 33503
    GuiDispIDSesInfoForceNot = 33522
    GuiDispIDSesInfoGrpN = 33515
    GuiDispIDSesInfoGuiCP = 33523
    GuiDispIDSesInfoI18N = 33524
    GuiDispIDSesInfoITime = 33501
    GuiDispIDSesInfoLang = 33511
    GuiDispIDSesInfoModeNo = 33517
    GuiDispIDSesInfoMsgSrc = 33514
    GuiDispIDSesInfoMsgSrv = 33513
    GuiDispIDSesInfoProg = 33505
    GuiDispIDSesInfoReadOnly = 33520
    GuiDispIDSesInfoRound = 33504
    GuiDispIDSesInfoRTime = 33500
    GuiDispIDSesInfoSesCtx = 33518
    GuiDispIDSesInfoSysN = 33507
    GuiDispIDSesInfoSysNo = 33516
    GuiDispIDSesInfoTrans = 33502
    GuiDispIDSesInfoUser = 33510
    GuiDispIDSesInfoWAN = 33519
    GuiDispIDSesIsActive = 32819
    GuiDispIDSesLockSessionUI = 32826
    GuiDispIDSesMenu = 32807
    GuiDispIDSesPPPSyId = 32821
    GuiDispIDSesPPSyId = 32822
    GuiDispIDSesPPTaId = 32820
    GuiDispIDSesProgressPercent = 32832
    GuiDispIDSesProgressText = 32833
    GuiDispIDSesRecFile = 32814
    GuiDispIDSesRecord = 32804
    GuiDispIDSesRunScrCtrl = 32816
    GuiDispIDSesSaveAsUnicode = 32823
    GuiDispIDSesShowKeys = 33527
    GuiDispIDSesStartT = 32809
    GuiDispIDSesStdNumFmt = 33526
    GuiDispIDSesSuppressBackendPopups = 32834
    GuiDispIDSesTestTool = 32813
    GuiDispIDSesUnlockSessionUI = 32827
    GuiDispIDSesVKey = 32808
    GuiDispIDSesVKeyDesc = 32817
    GuiDispIDSHSelCtxtMenIt = 34100
    GuiDispIDSHSelCtxtMenItPos = 34102
    GuiDispIDSHSelCtxtMenItTxt = 34101
    GuiDispIDSplitterIsVertical = 34400
    GuiDispIDSplitterSashPosition = 34401
    GuiDispIDTableBase = 33400
    GuiDispIDTableColBase = 33420
    GuiDispIDTableColFixed = 33421
    GuiDispIDTableColSelected = 33422
    GuiDispIDTableColSelectMode = 33401
    GuiDispIDTableColTitle = 33420
    GuiDispIDTableColumns = 33402
    GuiDispIDTableConfigureLayout = 33406
    GuiDispIDTableCurrentCol = 33410
    GuiDispIDTableCurrentRow = 33411
    GuiDispIDTableDeselAllCols = 33414
    GuiDispIDTableFieldName = 33409
    GuiDispIDTabLeftTab = 33200
    GuiDispIDTableGetCell = 33415
    GuiDispIDTableReorderTable = 33405
    GuiDispIDTableRowBase = 33430
    GuiDispIDTableRowCount = 33412
    GuiDispIDTableRows = 33404
    GuiDispIDTableRowSelectable = 33431
    GuiDispIDTableRowSelected = 33430
    GuiDispIDTableRowSelectMode = 33403
    GuiDispIDTableSelAllCols = 33408
    GuiDispIDTableVisRowCount = 33413
    GuiDispIDTabSelTab = 33201
    GuiDispIDTBSelect = 32700
    GuiDispIDTBToLeft = 32701
    GuiDispIDTHistoryCurEntry = 32057
    GuiDispIDTHistoryCurIndex = 32056
    GuiDispIDTHistoryIsActive = 32054
    GuiDispIDTHistoryList = 32055
    GuiDispIDTIsOField = 32067
    GuiDispIDTRequired = 32014
    GuiDispIDUtilCloseFile = 34202
    GuiDispIDUtilMsgBox = 34200
    GuiDispIDUtilMsgOptOK = 34220
    GuiDispIDUtilMsgOptOKCan = 34222
    GuiDispIDUtilMsgOptYesNo = 34221
    GuiDispIDUtilMsgResCancel = 34230
    GuiDispIDUtilMsgResNo = 34233
    GuiDispIDUtilMsgResOK = 34231
    GuiDispIDUtilMsgResYes = 34232
    GuiDispIDUtilMsgTypeE = 34208
    GuiDispIDUtilMsgTypeI = 34205
    GuiDispIDUtilMsgTypeP = 34209
    GuiDispIDUtilMsgTypeQ = 34206
    GuiDispIDUtilMsgTypeW = 34207
    GuiDispIDUtilOpenFile = 34201
    GuiDispIDUtilWriteFile = 34203
    GuiDispIDUtilWriteLnFile = 34204

class SapGuiMessageBoxOption:
    MSG_OPTION_OK = 0 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá apenas um botão 'OK'. (0)
    MSG_OPTION_YESNO = 1 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um botão 'Sim' e um botão 'Não'. (1)
    MSG_OPTION_OKCANCEL = 2 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um botão 'OK' e um botão 'Cancelar'. (2)

class SapGuiMessageBoxResult:
    MSG_RESULT_CANCEL = 0 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'Cancelar' é pressionado. (0)
    MSG_RESULT_OK = 1 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'OK' é pressionado. (1)
    MSG_RESULT_YES = 2 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'Sim' é pressionado. (2)
    MSG_RESULT_NO = 3 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'Não' é pressionado. (3)

class SapGuiMessageBoxType:
    MSG_TYPE_INFORMATION = 0 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá a letra 'i' como ícone da caixa de mensagem. (0)
    MSG_TYPE_QUESTION = 1 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um ponto de interrogação como ícone da caixa de mensagem. (1)
    MSG_TYPE_WARNING = 2 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um ponto de exclamação como ícone da caixa de mensagem. (2)
    MSG_TYPE_ERROR = 3 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um sinal de pare como ícone da caixa de mensagem. (3)
    MSG_TYPE_PLAIN = 4 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor não exibirá nenhum ícone na caixa de mensagem. (4)

class SapGuiScrollbarType:
    GuiScrollbarTypeUnknown = 0
    GuiScrollbarTypeVertical = 1
    GuiScrollbarTypeHorizontal = 2

class SapGuiTableSelectionType:
    MULTIPLE_INTERVAL_SELECTION = 2 # Várias colunas/linhas podem ser selecionadas. (2)
    NO_SELECTION = 0 # Nenhuma seleção é possível. (0)
    SINGLE_SELECTION = 1 # Uma coluna/linha pode ser selecionada. (1)

class SapTypeInstance():
    @staticmethod
    def GetInstance(sap_object: object):
        return SapGuiComponent(sap_object)

class SapGuiEnum():
    # TODO Fazer descrição
    # TODO Verificar retorno e descrições das funções dessa classe
    
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
    
    def Next(self, celt: int, rgvar, pceltFetched: int):
        return self.component.Next(celt, rgvar, pceltFetched)
    
    def Reset(self):
        return self.component.Reset()
    
    def Skip(self, celt: int):
        return self.component.Skip(celt)

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

class SapGuiScrollbar():
    ''' A classe GuiScrollbar é uma classe utilitária usada, por exemplo, em GuiScrollContainer ou GuiTableControl.
    '''
    
    #TODO Fazer mais funções de auxilio
    
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
    
    def Maximum(self) -> int:
        ''' Esta é a posição máxima da barra de rolagem.
        '''
        return self.component.Maximum
    
    def Minimum(self) -> int:
        ''' Esta é a posição mínima da barra de rolagem.
        '''
        return self.component.Minimum
    
    def PageSize(self) -> int:
        ''' Quando o usuário rola uma página para baixo, a posição será aumentada pelo valor de pageSize.
        '''
        return self.component.PageSize
    
    def Position(self, position: int = None) -> int:
        ''' A posição do polegar da barra de rolagem pode ser definida em valores do mínimo ao máximo.
        '''
        if position is not None: self.component.Position = position
        return self.component.Position

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

class SapGuiTableColumn(SapGuiComponentCollection):
    # TODO Fazer uma descrição
    
    def DefaultTooltip(self) -> str:
        ''' Texto de dica de ferramenta gerado a partir do texto curto definido no dicionário de dados para determinado tipo de elemento de tela.
        '''
        return self.component.DefaultTooltip
    
    def Fixed(self) -> bool:
        ''' Algumas colunas podem ser fixas, o que significa que não serão roladas com o restante das colunas.
        '''
        return self.component.Fixed
    
    def IconName(self) -> str:
        ''' Se ao objeto foi atribuído um ícone, então esta propriedade é o nome do ícone, caso contrário, é uma string vazia.
        '''
        return self.component.IconName
    
    def Selected(self, option: bool = None) -> bool:
        ''' Esta propriedade é verdadeira se a linha estiver selecionada.
        '''
        if option is not None: self.component.Selected = option
        return self.component.Selected
    
    def Title(self) -> str:
        ''' Esta é a legenda da coluna.
        '''
        return self.component.Title
    
    def Tooltip(self) -> str:
        ''' A dica de ferramenta contém um texto projetado para ajudar o usuário a entender o significado de um determinado campo de texto ou botão.
        '''
        return self.component.Tooltip

class SapGuiTableRow(SapGuiComponentCollection):
    # TODO colocar descrição
    
    # TODO Funções de auxilio
    
    def Selectable(self) -> bool:
        ''' Esta propriedade será True se a linha puder ser selecionada.
        '''
        return self.component.Selectable
    
    def Selected(self, option: bool = None) -> bool:
        ''' Esta propriedade é verdadeira se a linha estiver selecionada.
        '''
        if option is not None: self.component.Selected = option
        return self.component.Selected

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
        self.class_attrs = ['component']
        self.component = component

    def __getattr__(self, attr):
        return getattr(self.component, attr)

    def __setattr__(self, attr, value):
        if attr in self.__dict__ or attr == 'class_attrs' or attr in self.class_attrs:
            super().__setattr__(attr, value)
        else:
            setattr(self.component, attr, value)
        
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
        self.class_attrs = ['component']
        self.component = component

    def __getattr__(self, attr):
        return getattr(self.component, attr)

    def __setattr__(self, attr, value):
        if attr in self.__dict__ or attr == 'class_attrs' or attr in self.class_attrs:
            super().__setattr__(attr, value)
        else:
            setattr(self.component, attr, value)
    
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

class SapGuiVComponent(SapGuiComponent):
    ''' A interface GuiVComponent é exposta por todos os objetos visuais, como janelas, botões ou campos de texto.
    Assim como o GuiComponent, é uma interface abstrata. Qualquer objeto que suporte a interface GuiVComponent também expõe
    a interface GuiComponent. GuiVComponent estende o objeto GuiComponent.
    '''
    
    def DumpState(self, inner_object: str) -> SapGuiCollection:
        ''' Esta função despeja o estado do objeto. O parâmetro innerObject pode ser usado para especificar para qual
        objeto interno os dados devem ser despejados. Somente os componentes mais complexos, como o GuiCtrlGridView, suportam esse parâmetro.
        Todos os outros componentes sempre descartam seu estado completo. Todos os componentes que suportam este parâmetro têm em
        comum o fato de retornarem informações gerais sobre o estado do controle se o parâmetro “innerObject” contiver uma string vazia.
        Os valores disponíveis para o parâmetro innerObject são especificados como parte da descrição da classe dos componentes que o suportam.
        '''
        return SapGuiCollection(self.component.DumpState(inner_object))
    
    def SetFocus(self) -> None:
        ''' Esta função pode ser usada para definir o foco em um objeto. Se um usuário interagir com SAP GUI,
        ele moverá o foco sempre que a interação for com um novo objeto. Interagir com um objeto por meio do componente
        de script não altera o foco. Há alguns casos em que o aplicativo SAP verifica explicitamente o foco e
        se comporta de maneira diferente dependendo do objeto em foco.
        '''
        self.component.SetFocus()
    
    def Visualize(self, on: bool, inner_object: str) -> bool:
        ''' Chamar este método de um componente exibirá uma moldura vermelha ao redor do componente especificado se o parâmetro on for verdadeiro.
        O quadro será removido se on for falso. Alguns componentes, como GuiCtrlGridView, suportam a exibição do quadro em torno de objetos internos,
        como células. O formato da string innerObject é o mesmo do método dumpState.
        '''
        return self.component.Visualize(on, inner_object)
    
    def AccLabelCollection(self) -> SapGuiComponentCollection:
        ''' A coleção contém objetos do tipo GuiLabel que foram atribuídos a este controle no ABAP Screen Painter.
        '''
        return SapGuiComponentCollection(self.component.AccLabelCollection)
    
    def AccText(self) -> str:
        ''' Um texto adicional para suporte de acessibilidade.
        '''
        return self.component.AccText
    
    def AccTextOnRequest(self) -> str:
        ''' Um texto adicional para suporte de acessibilidade.
        '''
        return self.component.AccTextOnRequest
    
    def AccTooltip(self) -> str:
        ''' Um texto de dica adicional para suporte de acessibilidade.
        '''
        return self.component.AccTooltip
    
    def Changeable(self) -> bool:
        ''' Um objeto pode ser alterado se não estiver desabilitado nem somente leitura.
        '''
        return self.component.Changeable
    
    def DefaultTooltip(self) -> str:
        ''' Texto de dica de ferramenta gerado a partir do texto curto definido no
        dicionário de dados para determinado tipo de elemento de tela.
        '''
        return self.component.DefaultTooltip
    
    def IconName(self) -> str:
        ''' Se ao objeto foi atribuído um ícone, então esta propriedade é o nome do ícone, caso contrário, é uma string vazia.
        '''
        return self.component.IconName
    
    def IsSymbolFont(self) -> bool:
        ''' A propriedade é TRUE se o texto do componente for visualizado na fonte do símbolo SAP.
        '''
        return self.component.IsSymbolFont
    
    def Modified(self) -> bool:
        ''' Um objeto é modificado se seu estado tiver sido alterado pelo usuário e essa alteração ainda não tiver sido enviada ao sistema SAP.
        '''
        return self.component.Modified
    
    def ParentFrame(self) -> bool:
        ''' Se o controle estiver hospedado no objeto Frame, o valor da propriedade será esse quadro.
        '''
        # TODO
        return self.component.ParentFrame
    
    def Text(self, text: str = None) -> str:
        ''' O valor desta propriedade depende muito do tipo de objeto no qual ela é chamada.
        Isto é óbvio para campos de texto ou itens de menu. Por outro lado, esta propriedade está vazia para botões da
        barra de ferramentas e é o ID da classe para shells. Você pode ler a propriedade de texto de um rótulo, mas não
        pode alterá-la, enquanto só pode definir a propriedade de texto de um campo de senha, mas não lê-la.
        '''
        if text is None: return self.component.Text
        else:
            self.component.Text = text
            return self.component.Text
    
    def Tooltip(self) -> str:
        ''' A dica de ferramenta contém um texto projetado para ajudar o usuário a entender o significado de um determinado campo de texto ou botão.
        '''
        return self.component.Tooltip
    
    def ScreenLeft(self) -> int:
        ''' A posição y do componente nas coordenadas da tela.
        '''
        return self.component.ScreenLeft
    
    def ScreenTop(self) -> int:
        ''' A posição x do componente nas coordenadas da tela.
        '''
        return self.component.ScreenTop
    
    def Top(self) -> int:
        ''' Coordenada superior do elemento nas coordenadas da tela.
        '''
        return self.component.Top
    
    def Left(self) -> int:
        ''' Posição esquerda do elemento nas coordenadas da tela.
        '''
        return self.component.Left
    
    def Width(self) -> int:
        ''' Largura do componente em pixels.
        '''
        return self.component.Width
    
    def Height(self) -> int:
        ''' Altura do componente em pixels.
        '''
        return self.component.Height

class GuiLabel(SapGuiVComponent):
    # TODO criar descrição

    def GetListProperty(self, property: str) -> str:
        ''' Retorna propriedades de contêineres em geral.
        property: A propriedade que você deseja obter. Consulte a documentação para opções disponíveis.
        Retorna o valor da propriedade especificada.
        '''
        # TODO Verificar documentação novamente e fazer funções auxiliares
        return self.component.GetListProperty(property)

    def GetListPropertyNonRec(self, property: str) -> str:
        ''' Retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Veja GuiLabel::GetListProperty para uma descrição dos atributos disponíveis.
        Ao contrário do método GetListProperty, GetListPropertyNonRec só retornará informações definidas para o elemento específico 
        e ignorará as propriedades definidas para elementos pai.
        property: A propriedade que você deseja obter. Consulte a documentação para opções disponíveis.
        Retorna o valor da propriedade especificada.
        '''
        return self.component.GetListPropertyNonRec(property)

    def CaretPosition(self, caret_position: int = None) -> int:
        ''' Definir a posição do cursor dentro de um rótulo é possível, mesmo que não seja visualizada como um cursor pelo SAP GUI.
        No entanto, a posição é transmitida para o servidor, para que a lógica da aplicação ABAP possa depender dessa posição.
        '''
        if caret_position is not None:
            self.component.CaretPosition = caret_position
        return self.component.CaretPosition

    def ColorIndex(self) -> int:
        ''' Este número define o índice da cor da lista deste elemento.
        '''
        return self.component.ColorIndex

    def ColorIntensified(self) -> bool:
        ''' Esta propriedade é True se a flag Intensified estiver definida no screen painter para este elemento dynpro.
        '''
        return self.component.ColorIntensified

    def ColorInverse(self) -> bool:
        ''' Esta propriedade é True se o estilo de cor inversa estiver definido no screen painter para o elemento.
        '''
        return self.component.ColorInverse

    def DisplayedText(self) -> str:
        ''' Esta propriedade contém o texto conforme exibido na tela, incluindo espaços em branco precedentes ou subsequentes.
        Esses espaços em branco são removidos da propriedade de texto.
        '''
        return self.component.DisplayedText

    def Highlighted(self) -> bool:
        ''' Esta propriedade é True se a flag Highlighted estiver definida no screen painter para o elemento dynpro.
        '''
        return self.component.Highlighted

    def IsHotspot(self) -> bool:
        ''' Elementos dynpro, como rótulos, podem ser configurados para causar uma viagem de ida e volta quando clicados.
        Nesse caso, o cursor do mouse muda para a forma de mão. Isso é chamado de ponto de acesso.
        '''
        return self.component.IsHotspot

    def IsLeftLabel(self) -> bool:
        ''' Esta propriedade é definida se o rótulo foi atribuído como rótulo esquerdo de outro controle.
        '''
        return self.component.IsLeftLabel

    def IsListElement(self) -> bool:
        ''' Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        '''
        return self.component.IsListElement

    def IsRightLabel(self) -> bool:
        ''' Esta propriedade é definida se o rótulo foi atribuído como rótulo direito de outro controle.
        '''
        return self.component.IsRightLabel

    def MaxLength(self) -> int:
        ''' O comprimento máximo do texto de um rótulo é contado em unidades de código. Em clientes não Unicode, essas unidades são equivalentes a bytes.
        '''
        return self.component.MaxLength

    def Numerical(self) -> bool:
        ''' Esta bandeira é True se o rótulo só puder conter números.
        '''
        return self.component.Numerical

    def RowText(self) -> str:
        ''' Esta propriedade está disponível apenas em telas de lista ABAP. Ela retorna o texto da linha inteira que contém o componente atual.
        '''
        return self.component.RowText

class SapGuiRadioButton(SapGuiVComponent):
    ''' O prefixo do tipo é rad, o nome é o nome do campo retirado do dicionário de dados SAP.
    '''
    
    def Select(self) -> None:
        ''' Selecionar um botão de opção automaticamente desmarca todos os outros botões dentro do mesmo grupo.
        Isso pode causar uma viagem de ida e volta ao servidor, dependendo da definição do botão no screen painter.
        '''
        self.component.Select()
    
    def CharHeight(self) -> int:
        ''' Altura do GuiRadioButton em métrica de caracteres.
        '''
        return self.component.CharHeight

    def CharLeft(self) -> int:
        ''' Coordenada esquerda do GuiRadioButton em métrica de caracteres.
        '''
        return self.component.CharLeft

    def CharTop(self) -> int:
        ''' Coordenada superior do GuiRadioButton em métrica de caracteres.
        '''
        return self.component.CharTop

    def CharWidth(self) -> int:
        ''' Largura do GuiRadioButton em métrica de caracteres.
        '''
        return self.component.CharWidth

    def Flushing(self) -> bool:
        ''' Alguns componentes, como botões de rádio ou caixas de seleção, podem causar uma viagem de ida e volta quando seu valor é alterado. Se for o caso, a propriedade Flushing é True.
        '''
        return self.component.Flushing

    def GroupCount(self) -> int:
        ''' O número de botões de rádio no mesmo grupo ao qual o objeto atual pertence.
        '''
        return self.component.GroupCount

    def GroupMembers(self) -> object:
        ''' A coleção de objetos GuiRadioButton pertencentes ao mesmo grupo de botões de rádio.
        '''
        return self.component.GroupMembers

    def GroupPos(self) -> int:
        ''' A posição do botão de rádio no respectivo grupo de botões de rádio (varia de 1 a GroupCount).
        '''
        return self.component.GroupPos

    def IsLeftLabel(self) -> bool:
        ''' Esta propriedade é True se o componente tiver a flag 'assign left'.
        '''
        return self.component.IsLeftLabel

    def IsRightLabel(self) -> bool:
        ''' Esta propriedade é True se o componente tiver a flag 'assign right'.
        '''
        return self.component.IsRightLabel

    def LeftLabel(self) -> object:
        ''' Rótulo esquerdo do GuiRadioButton. O rótulo é atribuído no Screen Painter, usando a flag 'assign left'.
        '''
        return self.component.LeftLabel

    def RightLabel(self) -> object:
        ''' Rótulo direito do GuiRadioButton. Esta propriedade é definida no Screen Painter usando a flag 'assign right'.
        '''
        return self.component.RightLabel

class SapGuiTextField(SapGuiVComponent):
    ''' GuiTextField estende o objeto GuiVComponent. O prefixo do tipo é txt, o nome é o nome do campo retirado do dicionário de dados SAP.
    '''

    def GetListProperty(self, property_name: str) -> str:
        ''' Retorna uma propriedade de lista específica.
        Para mais informações, consulte a documentação sobre o método GetListProperty no objeto GuiLabel.
        '''
        return self.component.GetListProperty(property_name)

    def GetListPropertyNonRec(self, property_name: str) -> str:
        ''' Este método retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Consulte GuiLabel::GetListProperty para uma descrição dos atributos disponíveis. 
        Ao contrário do método GetListProperty, o GetListPropertyNonRec retornará apenas informações definidas para o elemento
        específico e ignorará propriedades de lista definidas para elementos pai.
        '''
        return self.component.GetListPropertyNonRec(property_name)

    def CaretPosition(self, caret_position: int = None) -> int:
        ''' A posição do cursor dentro de um campo de texto.
        '''
        if caret_position is not None:
            self.component.CaretPosition = caret_position
        return self.component.CaretPosition

    def DisplayedText(self) -> str:
        ''' Esta propriedade contém o texto conforme exibido na tela, incluindo espaços em branco precedentes ou subsequentes.
            Esses espaços em branco são removidos da propriedade de texto.
        '''
        return self.component.DisplayedText

    def Highlighted(self) -> bool:
        ''' Esta propriedade é True se a flag Highlighted estiver definida no screen painter para o elemento dynpro.
        '''
        return self.component.Highlighted

    def HistoryCurEntry(self) -> str:
        ''' Texto da entrada atualmente focada na lista de histórico.
        '''
        return self.component.HistoryCurEntry

    def HistoryCurIndex(self) -> int:
        ''' Índice atualmente focado na lista suspensa de histórico.
        '''
        return self.component.HistoryCurIndex

    def HistoryIsActive(self) -> bool:
        ''' Esta propriedade é True se o histórico local do campo de entrada estiver atualmente aberto.
        '''
        return self.component.HistoryIsActive

    def HistoryList(self) -> object:
        ''' Lista de entradas na caixa de histórico local.
        '''
        return self.component.HistoryList

    def IsHotspot(self) -> bool:
        ''' Elementos dynpro, como rótulos, podem ser configurados para causar uma ida e volta quando clicados. Nesse caso, o cursor do mouse muda para a forma de mão. Isso é chamado de hot spot.
        '''
        return self.component.IsHotspot

    def IsLeftLabel(self) -> bool:
        ''' Esta propriedade é True se o componente tiver a flag 'assign left'.
        '''
        return self.component.IsLeftLabel

    def IsListElement(self) -> bool:
        ''' Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        '''
        return self.component.IsListElement

    def IsOField(self) -> bool:
        ''' OField é um elemento especial de dynpro ABAP, o Output Field. Esses campos podem ser definidos programaticamente com um valor em tempo de execução. Nesse aspecto, eles diferem dos rótulos. No entanto, eles não podem ser usados para inserir dados, portanto, não são campos de entrada.
        '''
        return self.component.IsOField

    def IsRightLabel(self) -> bool:
        ''' Esta propriedade é True se o componente tiver a flag 'assign right'.
        '''
        return self.component.IsRightLabel

    def LeftLabel(self) -> object:
        ''' Este rótulo foi definido no ABAP Screen Painter para ser o rótulo esquerdo do controle.
        '''
        return self.component.LeftLabel

    def MaxLength(self) -> int:
        ''' O comprimento máximo do texto que pode ser escrito em um campo de texto é contado em unidades de código. Em clientes não Unicode, essas unidades são equivalentes a bytes.
        '''
        return self.component.MaxLength

    def Numerical(self) -> bool:
        ''' Se esta flag estiver definida, apenas números e caracteres especiais podem ser escritos no campo de texto.
        '''
        return self.component.Numerical

    def Required(self) -> bool:
        ''' Esta propriedade é True se o componente for um valor obrigatório para a tela.
        '''
        return self.component.Required

    def RightLabel(self) -> object:
        ''' Este rótulo foi definido no ABAP Screen Painter para ser o rótulo direito do controle.
        '''
        return self.component.RightLabel

class SapGuiCTextField(SapGuiTextField):
    ''' Se o cursor estiver definido em um campo de texto do tipo GuiCTextField,
    um botão de caixa de combinação será exibido à direita do campo de texto.
    Pressionar este botão equivale a pressionar a tecla F4. O botão não é representado no
    modelo de objeto de script como um objeto separado; é considerado parte do campo de texto.
    Não há outras diferenças entre GuiTextField e GuiCTextField. GuiCTextField estende o GuiTextField.
    O prefixo do tipo é ctxt, o nome é o Fieldname retirado do dicionário de dados SAP.
    '''
    
    # TODO Adicionar funções auxiliares
    
    pass

class SapGuiPasswordField(SapGuiTextField):
    ''' A única diferença entre GuiTextField e GuiPasswordField é que a propriedade Text não pode ser lida para um campo de senha.
    O texto retornado está sempre vazio. Durante a gravação a senha também não é salva no script gravado. GuiPasswordField
    estende o GuiTextField. O prefixo do tipo é pwd, o nome é o nome do campo retirado do dicionário de dados SAP.
    '''

    pass

class SapGuiStatusbar(SapGuiVComponent):
    ''' GuiStatusbar representa a mensagem que exibe parte da barra de status na parte inferior da janela SAP GUI.
    Ele não inclui as informações do sistema e de login exibidas na área mais à direita da barra de status,
    pois estão disponíveis no objeto GuiSessionInfo. GuiStatusbar estende o objeto GuiVComponent. O prefixo do tipo é sbar.
    '''
    
    def DoubleClick(self) -> None:
        self.component.DoubleClick
    
    def Handle(self) -> int:
        ''' O identificador de janela do controle que está conectado ao GuiShell.
        '''
        return self.component.Handle
    
    def MessageAsPopup(self) -> bool:
        ''' Algumas mensagens podem ser exibidas não apenas na barra de status, mas também como uma janela pop-up.
        Nesses casos, esta propriedade é definida como True para que um script saiba que precisa fechar um pop-up para continuar.
        '''
        return self.component.MessageAsPopup
    
    def MessageId(self) -> str:
        ''' Este é o nome da classe de mensagem usada na chamada de mensagem ABAP.
        '''
        return self.component.MessageId
    
    def MessageNumber(self) -> str:
        ''' Este é o nome do número da mensagem usado na chamada de mensagem ABAP.
        Geralmente será um número, mas isso não é imposto pelo sistema.
        '''
        return self.component.MessageNumber
    
    def MessageParameter(self) -> str:
        ''' Estes são os valores dos parâmetros usados para expandir os espaços reservados na definição do texto da mensagem no dicionário de dados.
        A propriedade text do GuiStatusbar já contém o texto expandido da mensagem. Um máximo de 8 valores de parâmetros podem
        ser fornecidos na codificação ABAP, portanto o índice deve estar na faixa de 0 a 7.
        '''
        return self.component.MessageParameter
    
    def MessageType(self) -> str:
        ''' Esta propriedade pode ter qualquer um dos seguintes valores:
        S - Success
        W - Warning
        E - Error
        A - Abort
        I - Information
        '''
        return self.component.MessageType

class SapGuiStatusPane(SapGuiVComponent):
    ''' O pai dos objetos GuiStatusPane é a barra de status (veja também Objeto GuiStatusbar).
    Os objetos GuiStatusPane refletem as áreas individuais da barra de status, por exemplo "pane[0]"
    refere-se à seção da barra de status onde as mensagens são exibidas. Veja também Objeto GuiStatusbar.
    '''
    
    pass

class SapGuiComboBoxEntry():
    
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
    
    def Key(self) -> str:
        ''' Valor-chave da entrada da caixa de combinação.
        '''
        return self.component.Key
    
    def Pos(self) -> int:
        ''' Posição da entrada da caixa de combinação. O intervalo vai de 1 ao número de entradas na caixa de combinação.
        '''
        return self.component.Pos
    
    def Value(self) -> str:
        ''' Value of the combo box entry.
        '''
        return self.component.Value

class SapGuiComboBox(SapGuiVComponent):
    ''' O GuiComboBox é um pouco semelhante ao GuiCTextField, mas tem uma implementação completamente diferente.
    Enquanto pressionar o botão da caixa de combinação de um GuiCTextField abrirá um novo dynpro ou controle no qual uma
    seleção pode ser feita, o GuiComboBox recupera todas as opções possíveis na inicialização do servidor, para que a
    seleção seja feita exclusivamente no cliente. GuiComboBox estende o objeto GuiVComponent. O prefixo do tipo é cmb, 
    o nome é o nome do campo retirado do dicionário de dados SAP.
    '''
    
    def SetKeySpace(self) -> None:
        ''' Esta função define a propriedade key da caixa de combinação para o caractere de espaço. Foi introduzido para eCATT.
        '''
        self.component.SetKeySpace()

    def CharHeight(self) -> int:
        ''' Altura do GuiComboBox em métrica de caracteres.
        '''
        return self.component.CharHeight

    def CharLeft(self) -> int:
        ''' Coordenada esquerda do GuiComboBox em métrica de caracteres.
        '''
        return self.component.CharLeft

    def CharTop(self) -> int:
        ''' Coordenada superior do GuiComboBox em métrica de caracteres.
        '''
        return self.component.CharTop

    def CharWidth(self) -> int:
        ''' Largura do GuiComboBox em métrica de caracteres.
        '''
        return self.component.CharWidth

    def CurListBoxEntry(self) -> SapGuiComboBoxEntry:
        ''' A entrada atualmente focada na lista suspensa.
        '''
        return self.component.CurListBoxEntry

    def Entries(self) -> SapGuiCollection:
        ''' Todos os membros desta coleção são do tipo GuiComboBoxEntry e têm apenas duas propriedades, chave e valor, ambas do tipo String. O key data pode ser exibido no SAP GUI configurando as opções 'Show keys...' no diálogo de opções do SAP GUI.
        '''
        return self.component.Entries

    def Flushing(self) -> bool:
        ''' Alguns componentes, como botões de rádio, caixas de seleção ou caixas de combinação, podem causar uma round trip quando seu valor é alterado. Se for o caso, a propriedade Flushing é Verdadeira.
        '''
        return self.component.Flushing

    def Highlighted(self) -> bool:
        ''' Esta propriedade é Verdadeira se a flag Highlighted estiver definida no Screen Painter para a caixa de combinação.
        '''
        return self.component.Highlighted

    def IsLeftLabel(self) -> bool:
        ''' Esta propriedade é Verdadeira se a caixa de combinação tiver a flag 'assign left'.
        '''
        return self.component.IsLeftLabel

    def IsListBoxActive(self) -> bool:
        ''' Esta propriedade é Verdadeira se a lista suspensa da caixa de combinação estiver atualmente aberta.
        '''
        return self.component.IsListBoxActive

    def IsRightLabel(self) -> bool:
        ''' Esta propriedade é Verdadeira se a caixa de combinação tiver a flag 'assign right'.
        '''
        return self.component.IsRightLabel

    def Key(self, key: str = None) -> str:
        ''' Esta é a chave do item atualmente selecionado. Você pode alterar este item definindo a propriedade Key para um novo valor.
        '''
        if key is not None:
            self.component.Key = key
        return self.component.Key

    def LeftLabel(self) -> str:
        ''' Este rótulo foi definido no ABAP Screen Painter para ser o rótulo esquerdo da caixa de combinação.
        '''
        return self.component.LeftLabel

    def Required(self) -> bool:
        ''' Se a flag Required estiver definida para uma caixa de combinação, a entrada vazia não poderá ser selecionada na lista.
        '''
        return self.component.Required

    def RightLabel(self) -> SapGuiVComponent:
        ''' Este rótulo foi definido no ABAP Screen Painter para ser o rótulo direito da caixa de combinação.
        '''
        return self.component.RightLabel

    def ShowKey(self) -> bool:
        ''' Esta propriedade é Verdadeira se a caixa de combinação mostrar tanto as chaves quanto os valores (isso pode ser configurado definindo as opções 'Show keys...' no diálogo de opções do SAP GUI).
        '''
        return self.component.ShowKey

    def Value(self, value: str = None) -> str:
        ''' Este é o valor do item atualmente selecionado. Você pode alterar este item definindo a propriedade Value para um novo valor.
        '''
        if value is not None:
            self.component.Value = value
        return self.component.Value

class SapGuiCheckBox(SapGuiVComponent):
    #TODO Fazer uma descrição
    
    def GetListProperty(self, property: str) -> str:
        ''' Para mais informações consulte a documentação sobre o método GetListProperty dentro do GuiLabel Object.
        '''
        return self.component.GetListProperty(property)
    
    def GetListPropertyNonRec(self, property: str) -> str:
        ''' Este método retorna informações que são compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Consulte GuiLabel::GetListProperty para obter uma descrição dos atributos disponíveis.
        Em contraste com o método GetListProperty, GetListPropertyNonRec retornará apenas informações definidas para o elemento específico e
        ignorará as propriedades da lista definidas para elementos pai.
        '''
        return self.component.GetListPropertyNonRec(property)
    
    def ColorIndex(self) -> int:
        ''' Este número define o índice da cor da lista deste elemento.
        '''
        return self.component.ColorIndex
    
    def ColorIntensified(self) -> bool:
        ''' Esta propriedade será True se o sinalizador Intensificado estiver definido no Screen Painter para este elemento dynpro.
        '''
        return self.component.ColorIntensified
    
    def ColorInverse(self) -> bool:
        ''' Esta propriedade será True se o estilo de cor inverso estiver definido no Screen Painter para o elemento.
        '''
        return self.component.ColorInverse
    
    def Flushing(self) -> bool:
        ''' Alguns componentes, como botões de opção ou caixas de seleção, podem causar uma viagem de ida e
        volta quando seu valor for alterado. Se for esse o caso, a propriedade Flushing é True.
        '''
        return self.component.Flushing
    
    def IsLeftLabel(self) -> bool:
        ''' Esta propriedade é True se o componente tiver o sinalizador 'atribuir à esquerda'.
        '''
        return self.component.IsLeftLabel
    
    def IsListElement(self) -> bool:
        ''' Esta propriedade é True se o elemento estiver em uma lista ABAP e não em uma tela dynpro.
        '''
        return self.component.IsListElement
    
    def IsRightLabel(self) -> bool:
        ''' Esta propriedade é True se o componente tiver o sinalizador 'assign right'.
        '''
        return self.component.IsRightLabel
    
    def LeftLabel(self) -> bool:
        ''' Etiqueta esquerda do componente. O rótulo é atribuído no Screen Painter, usando o sinalizador 'assign left'.
        '''
        return self.component.LeftLabel
    
    def RightLabel(self) -> bool:
        ''' Etiqueta direita do componente.
        Esta propriedade é definida no Screen Painter usando o sinalizador 'assign right'.
        '''
        return self.component.RightLabel
    
    def RowText(self) -> bool:
        ''' Esta propriedade só está disponível em telas de lista ABAP.
        Ele retorna o texto da linha while que contém o componente atual.
        '''
        return self.component.RowText
    
    def Selected(self) -> bool:
        ''' Assim como os botões de opção, marcar uma caixa de seleção pode
        causar comunicação com o servidor, dependendo da definição do ABAP Screen Painter.
        '''
        return self.component.Selected

class SapGuiButton(SapGuiVComponent):
    ''' GuiButton representa todos os botões que estão no dynpros, na barra de ferramentas ou nos controles da tabela.
    O prefixo do tipo é btn, a propriedade name é o nome do campo obtido do dicionário de dados SAP.
    Há uma exceção: para botões de tabstrip, é o ID do botão definido no pintor de tela que é obtido do dicionário de dados SAP.
    '''
    
    def Press(self) -> None:
        ''' Isso emula o pressionamento manual de um botão.
        Pressionar um botão sempre fará com que a comunicação do servidor ocorra,
        tornando inválidas todas as referências a elementos abaixo do nível da janela.
        '''
        self.component.Press()
    
    def Emphasized(self) -> bool:
        ''' Esta propriedade é True se o botão for exibido enfatizado
        (no Fiori Visual Themes: O botão mais à esquerda no rodapé e botões configurados como "Fiori Usage D Display<->Change").
        '''
        return self.component.Emphasized
    
    def LeftLabel(self) -> SapGuiVComponent:
        ''' Rótulo esquerdo do GuiButton. O rótulo é atribuído no Screen Painter, usando o sinalizador 'assign left'.
        '''
        return self.component.LeftLabel
    
    def RightLabel(self) -> SapGuiVComponent:
        ''' Rótulo direito do GuiButton. Esta propriedade é definida no Screen Painter usando o sinalizador 'assign right'.
        '''
        return self.component.RightLabel

class SapGuiBox(SapGuiVComponent):
    ''' Uma GuiBox é um quadro simples com um nome (também chamado de "Group Box").
    Os itens dentro da moldura não são filhos da caixa. O prefixo do tipo é "caixa".
    '''
    
    def CharHeight(self) -> int:
        ''' Altura do GuiBox em caracteres métricos.
        '''
        return self.component.CharHeight
    
    def CharLeft(self) -> int:
        ''' Coordenada esquerda do GuiBox em métrica de caracteres.
        '''
        return self.component.CharLeft
    
    def CharTop(self) -> int:
        ''' Coordenada superior do GuiBox em métrica de caracteres.
        '''
        return self.component.CharTop
    
    def CharWidth(self) -> int:
        ''' Largura do GuiBox em métrica de caracteres.
        '''
        return self.component.CharWidth

class SapGuiMenu(SapGuiVComponent):
    ''' Um GuiMenu pode ter outros objetos GuiMenu como filhos.
    O prefixo do tipo é menu, o nome é o texto do item de menu.
    Caso o item não possua texto, como é o caso dos separadores, então o nome é a última parte do id, menu[n].
    '''
    
    def Select(self) -> None:
        ''' Selecione o menu.
        '''
        self.component.Select()

class SapGuiContextMenu(SapGuiMenu):
    ''' Um GuiContextMenu pode ter outros objetos GuiContextMenu como filhos.
    O tipo é mnu, o nome é o código de função que é enviado ao sistema quando o item de menu é selecionado.
    '''
    
    def Select(self) -> None:
        self.component.Select

class SapGuiVContainer(SapGuiVComponent, SapGuiContainer):
    ''' Um objeto expõe a interface GuiVContainer se ela estiver visível e puder ter filhos.
    Exemplos dessa interface são janelas e subtelas, barras de ferramentas ou controles com filhos, como o controle divisor.
    GuiVContainer estende o objeto GuiContainer e o objeto GuiVComponent.
    '''
    
    def FindAllByName(self, name: str, type: str) -> SapGuiComponentCollection:
        ''' Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção quando FindAllByName ou FindAllByNameEx forem usados.
        '''
        return SapGuiComponentCollection(self.component.FindAllByName(name, type))
    
    def FindAllByNameEx(self, name: str, type: int) -> SapGuiComponentCollection:
        ''' Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção quando FindAllByName ou FindAllByNameEx forem usados.
        '''
        return SapGuiComponentCollection(self.component.FindAllByNameEx(name, type))
    
    def FindByName(self, name: str, type: str) -> SapGuiComponent:
        # TODO
        ''' Ao contrário de FindById, esta função não garante um resultado único.
        Ele simplesmente retornará o primeiro descendente que corresponda aos parâmetros de nome e tipo.
        Esta é uma descrição mais natural do objeto do que o ID complexo, mas só faz sentido em objetos dynpro,
        pois a maioria dos outros objetos não tem um nome significativo. Se nenhum descendente com nome
        e tipo correspondentes for encontrado, a função gera uma exceção.
        '''
        return SapTypeInstance.GetInstance(self.component.FindByName(name, type))
    
    def FindByNameEx(self, name: str, type: int) -> SapGuiComponent:
        # TODO
        return SapTypeInstance.GetInstance(self.component.FindByNameEx(name, type))

class SapGuiDialogShell(SapGuiVContainer):
    ''' O GuiDialogShell é uma janela externa usada como contêiner para outros shells, por exemplo,
    uma barra de ferramentas. O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    '''

    def Fechar(self):
        ''' Este método fecha a janela externa.
        '''
        self.component.Fechar()

    def Title(self) -> str:
        ''' Título do diálogo.
        '''
        return self.component.Title

class SapGuiSimpleContainer(SapGuiVContainer):
    ''' Este contêiner representa subtelas não roláveis. Ele não possui nenhuma funcionalidade
    além das interfaces herdadas.
    O prefixo do tipo é sub, o nome é gerado a partir das configurações do dicionário de dados.
    '''

    def GetListProperty(self, property: str) -> str:
        ''' Obtém uma propriedade da lista.
        property: A propriedade que você deseja obter. Consulte a documentação do objeto GuiLabel para obter mais informações.
        Retorna o valor da propriedade especificada.
        '''
        return self.component.GetListProperty(property)

    def GetListPropertyNonRec(self, property: str) -> str:
        ''' Obtém uma propriedade da lista sem considerar propriedades de elementos pai.
        property: A propriedade que você deseja obter. Consulte a documentação do objeto GuiLabel para obter mais informações.
        Retorna o valor da propriedade especificada, ignorando propriedades de elementos pai.
        '''
        return self.component.GetListPropertyNonRec(property)

    def IsListElement(self) -> bool:
        ''' Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        '''
        return self.component.IsListElement

    def IsStepLoop(self) -> bool:
        ''' Esta propriedade é True se o contêiner for um contêiner de loop de etapa.
        '''
        return self.component.IsStepLoop

    def LoopColCount(self) -> int:
        ''' Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de colunas no loop de etapa.
        '''
        return self.component.LoopColCount

    def LoopCurrentCol(self) -> int:
        ''' Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número atual da linha no loop de etapa.
        '''
        return self.component.LoopCurrentCol

    def LoopCurrentColCount(self) -> int:
        ''' Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de colunas na linha atual do loop de etapa.
        '''
        return self.component.LoopCurrentColCount

    def LoopCurrentRow(self) -> int:
        ''' Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número atual da coluna no loop de etapa.
        '''
        return self.component.LoopCurrentRow

    def LoopRowCount(self) -> int:
        ''' Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de linhas no loop de etapa.
        '''
        return self.component.LoopRowCount

class SapGuiCustomControl(SapGuiVContainer):
    ''' O GuiCustomControl é um objeto wrapper usado para colocar controles ActiveX em telas dynpro.
    Embora GuiCustomControl seja um elemento dynpro, seus filhos são do tipo GuiContainerShell, que é um contêiner
    para controles. GuiCustomControl estende o objeto GuiVContainer. O prefixo do tipo é cntl, o nome é o
    nome do campo retirado do dicionário de dados SAP.
    '''
    
    def CharHeight(self) -> int:
        ''' Altura do GuiCustomControl em métrica de caracteres.
        '''
        return self.component.CharHeight

    def CharLeft(self) -> int:
        ''' Coordenada esquerda do GuiCustomControl em métrica de caracteres.
        '''
        return self.component.CharLeft

    def CharTop(self) -> int:
        ''' Coordenada superior do GuiCustomControl em métrica de caracteres.
        '''
        return self.component.CharTop

    def CharWidth(self) -> int:
        ''' Largura do GuiCustomControl em métrica de caracteres.
        '''
        return self.component.CharWidth

class SapGuiToolbar(SapGuiVContainer):
    ''' Cada GuiFrameWindow possui uma GuiToolbar.
    O GuiMainWindow possui duas barras de ferramentas, a menos que a segunda tenha sido desativada pela aplicação ABAP.
    A barra de ferramentas superior é a barra de ferramentas do sistema, enquanto a segunda barra de ferramentas é a barra de ferramentas do aplicativo.
    Os filhos de uma GuiToolbar são botões. Os índices dos botões da barra de ferramentas são determinados pelos valores de chave virtual definidos para o botão.
    '''
    
    pass

class SapGuiToolbar(SapGuiVContainer):
    ''' A barra de título só é exibida e exposta como um objeto separado no modo Novo Design Visual.
    O prefixo do tipo e o nome do GuiTitlebar são titl.
    Em algumas transações a barra de título pode conter objetos do tipo GuiGosShell.
    '''

    pass

class SapGuiUserArea(SapGuiVContainer):
    ''' A GuiUserArea compreende a área entre a barra de ferramentas e a barra de status para janelas do
    tipo GuiMainWindow e a área entre a barra de título e a barra de ferramentas para janelas modais,
    podendo também ser limitada por controles docker. Os elementos dynpro padrão podem ser encontrados apenas
    nesta área, com exceção dos botões, que também são encontrados nas barras de ferramentas.
    '''
    
    def FindByLabel(self, text: str, type: str) -> SapGuiComponent:
        ''' Um método muito simples para encontrar um objeto é pesquisar especificando o texto do respectivo rótulo.
        '''
        return self.component.FindByLabel(text, type)
    
    def CurrentContextMenu(self) -> SapGuiContextMenu:
        ''' Esta propriedade só é definida quando um menu de contexto está disponível no objeto shell.
        '''
        return self.component.CurrentContextMenu
    
    def HorizontalScrollbar(self) -> SapGuiScrollbar:
        ''' A área do usuário é definida para ser rolável mesmo que as barras de rolagem nem sempre estejam visíveis.
        '''
        return self.component.HorizontalScrollbar
    
    def IsOTFPreview(self) -> bool:
        ''' Esta propriedade é TRUE, caso seja exibido um Controle de Preview SAPScript na área do usuário.
        '''
        return self.component.IsOTFPreview
    
    def VerticalScrollbar(self) -> SapGuiScrollbar:
        ''' A área do usuário é definida para ser rolável mesmo que as barras de rolagem nem sempre estejam visíveis.
        '''
        return self.component.VerticalScrollbar

class SapGuiShell(SapGuiVContainer):
    ''' GuiShell é um objeto abstrato cuja interface é suportada por todos os controles.
    GuiShell estende o objeto GuiVContainer. O prefixo do tipo é shell, o nome é a última parte do id, shell[n].
    '''
    
    def SelectContextMenuItem(self, function_code: str) -> None:
        ''' Selecione um item no menu de contexto do controle.
        '''
        return self.component.SelectContextMenuItem(function_code)
    
    def SelectContextMenuItemByPosition(self, position_desc: str) -> None:
        ''' Este método permite selecionar um item do menu de contexto usando a posição do item.
        Portanto, é independente do texto do item de menu.
        '''
        return self.component.SelectContextMenuItemByPosition(position_desc)
    
    def SelectContextMenuItemByText(self, text: str) -> None:
        ''' Selecione um item de menu de um menu de contexto usando o texto do item e possíveis menus de nível superior.
        '''
        return self.component.SelectContextMenuItemByText(text)
    
    def AccDescription(self) -> str:
        ''' Descrição de acessibilidade do shell. Esta descrição pode ser usada para shells que não possuem um elemento de título.
        '''
        return self.component.AccDescription
    
    def CurrentContextMenu(self) -> SapGuiContextMenu:
        ''' Esta propriedade só é definida quando um menu de contexto está disponível no objeto shell.
        '''
        return self.component.CurrentContextMenu
    
    def DragDropSupported(self) -> bool:
        ''' Esta propriedade é True se o shell permitir operações de arrastar e soltar.
        '''
        return self.component.DragDropSupported
    
    def Handle(self) -> int:
        ''' O identificador de janela do controle que está conectado ao GuiShell.
        '''
        return self.component.Handle
    
    def OcxEvents(self) -> SapGuiCollection:
        ''' Retorna uma coleção contendo os IDs de eventos do controle ActiveX. Estes são os eventos que o controle pode enviar ao servidor.
        '''
        return self.component.OcxEvents
    
    def SubType(self) -> str:
        ''' Informações adicionais de tipo para identificar o controle representado pelo shell, por exemplo Picture, TextEdit, GridView…
        '''
        return self.component.SubType

class SapGuiEAIViewer2D(SapGuiShell):
    ''' O controle GuiEAIViewer2D é utilizado para visualizar imagens gráficas bidimensionais no sistema SAP.
    O usuário pode realizar redlining sobre a imagem carregada. O wrapper de script para esse controle registra
    todas as ações do usuário durante o processo de redlining e reproduz as mesmas ações quando o script gravado é reproduzido.
    '''
    
    def annotationTextRequest(self, text: str) -> None:
        # TODO Criar descrição
        return self.component.annotationTextRequest(text)

    def AnnotationEnabled(self, enabled: int = None) -> int:
        ''' O valor desta propriedade é definido como 1 quando a marcação está ativada.
        O controle wrapper começa a gravar as ações do usuário assim que esta propriedade é definida como valor 1.
        '''
        if enabled is not None:
            self.component.AnnotationEnabled = enabled
        return self.component.AnnotationEnabled

    def AnnotationMode(self, mode: int = None) -> int:
        ''' Durante a marcação, o modo de marcação selecionado é armazenado nesta propriedade.
        '''
        if mode is not None:
            self.component.AnnotationMode = mode
        return self.component.AnnotationMode

    def RedliningStream(self, stream: str = None) -> str:
        ''' Esta propriedade armazena a camada de marcação como um objeto BLOB (Binary Large Data Object).
        Durante a gravação, todo o BLOB é copiado para o script gerado.
        '''
        if stream is not None:
            self.component.RedliningStream = stream
        return self.component.RedliningStream

class SapGuiColorSelector(SapGuiShell):
    ''' GuiColorSelector exibe um conjunto de cores para seleção.
    '''

    def ChangeSelection(self, i: int) -> None:
        ''' Esta função emula a seleção da cor pelo usuário na posição de índice especificada.
        '''
        self.component.ChangeSelection(i)

class SapGuiCalendar(SapGuiShell):
    ''' O controle de calendário pode ser usado para selecionar datas ou períodos únicos.
    '''

    def ContextMenu(self, CtxMenuId: int, CtxMenuCellRow: int, CtxMenuCellCol: int, DateBegin: str, DateEnd: str) -> None:
        ''' Chama esta função para abrir um menu de contexto.

        O parâmetro CtxMenuId indica o tipo de célula na qual o menu de contexto foi aberto:
        Valor   Tipo de Célula  Descrição
        0       Data            Invocação em uma célula com uma única data
        1       Dia da Semana   Invocação em um botão para um determinado dia da semana
        2       Semana          Invocação em um botão para uma semana específica
        '''
        self.component.ContextMenu(CtxMenuId, CtxMenuCellRow, CtxMenuCellCol, DateBegin, DateEnd)

    def CreateDate(self, day: int, month: int, year: int) -> str:
        ''' Cria uma data no formato "YYYYMMDD" a partir dos parâmetros de dia, mês e ano.
        '''
        return self.component.CreateDate(day, month, year)

    def GetColor(self, from_color: str) -> int:
        ''' Retorna a cor associada a partir do valor de cor especificado.
        '''
        return self.component.GetColor(from_color)

    def GetColorInfo(self, Color: int) -> str:
        ''' Retorna a explicação definida pela aplicação para cores semânticas usadas no GuiCalendar (começando com índice 0).
        '''
        return self.component.GetColorInfo(Color)

    def GetDateTooltip(self, date: str) -> str:
        ''' Retorna o texto de dica de ferramenta da data especificada no formato "YYYYMMDD".
        '''
        return self.component.GetDateTooltip(date)

    def GetDay(self, date: str) -> int:
        ''' Retorna o dia da data especificada no formato "YYYYMMDD".
        '''
        return self.component.GetDay(date)

    def GetMonth(self, date: str) -> int:
        ''' Retorna o mês da data especificada no formato "YYYYMMDD".
        '''
        return self.component.GetMonth(date)

    def GetWeekday(self, date: str) -> str:
        ''' Retorna o dia da semana da data especificada no formato "YYYYMMDD".
        '''
        return self.component.GetWeekday(date)

    def GetWeekNumber(self, date: str) -> int:
        ''' Retorna o número da semana da data especificada no formato "YYYYMMDD".
        '''
        return self.component.GetWeekNumber(date)

    def GetYear(self, date: str) -> int:
        ''' Retorna o ano da data especificada no formato "YYYYMMDD".
        '''
        return self.component.GetYear(date)

    def IsWeekend(self, date: str) -> int:
        ''' Retorna True se a data especificada pelo parâmetro estiver em um fim de semana.
        '''
        return self.component.IsWeekend(date)

    def SelectMonth(self, month: int, year: int) -> None:
        ''' Seleciona o mês especificado pelos parâmetros (começando com índice 1).
        '''
        self.component.SelectMonth(month, year)

    def SelectRange(self, from_date: str, to_date: str) -> None:
        ''' Seleciona o intervalo especificado pelos parâmetros (no formato "YYYYMMDD").
        '''
        self.component.SelectRange(from_date, to_date)

    def SelectWeek(self, week: int, year: int) -> None:
        ''' Seleciona a semana especificada pelos parâmetros (começando com índice 0).
        '''
        self.component.SelectWeek(week, year)

    def EndSelection(self) -> str:
        ''' O último dia do intervalo de datas selecionado (no formato "YYYYMMDD").
        '''
        return self.component.EndSelection

    def FirstVisibleDate(self, date: str = None) -> str:
        ''' Esta é a data mais antiga visível no controle de calendário.
        '''
        if date is not None:
            self.component.FirstVisibleDate = date
        return self.component.FirstVisibleDate

    def FocusDate(self, date: str = None) -> str:
        ''' A data atualmente focada (identificada pela borda de foco) no controle de calendário está disponível no formato "YYYYMMDD".
        '''
        if date is not None:
            self.component.FocusDate = date
        return self.component.FocusDate

    def FocusedElement(self) -> int:
        ''' Esta propriedade indica qual parte de um controle GuiCalendar composto atualmente tem o foco.
        Os valores possíveis são:
        0 - "InputField": O campo de entrada (seletor) para inserir manualmente uma data atualmente tem foco
        1 - "Button": O botão de pressão para abrir o painel de navegação atualmente tem foco
        2 - "Navigator": O painel de navegação pop-up está aberto e atualmente tem foco
        '''
        return self.component.FocusedElement

    def Horizontal(self) -> bool:
        ''' Esta propriedade contém True se o GuiCalendar tiver orientação horizontal, caso contrário, contém False.
        '''
        return self.component.Horizontal

    def LastVisibleDate(self, date: str = None) -> str:
        ''' A última data que está atualmente sendo exibida pelo GuiCalendar (no formato "YYYYMMDD").
        '''
        if date is not None:
            self.component.LastVisibleDate = date
        return self.component.LastVisibleDate

    def SelectionInterval(self, interval: str = None) -> str:
        ''' O intervalo é representado por duas strings de data concatenadas separadas por uma vírgula.
        '''
        if interval is not None:
            self.component.SelectionInterval = interval
        return self.component.SelectionInterval

    def StartSelection(self) -> str:
        ''' O primeiro dia do intervalo de datas selecionado (no formato "YYYYMMDD").
        '''
        return self.component.StartSelection

    def Today(self) -> str:
        ''' O dia atual (no formato "YYYYMMDD").
        '''
        return self.component.Today

class SapGuiBarChart(SapGuiShell):
    ''' O GuiBarChart é uma ferramenta poderosa para exibir e modificar diagramas de escala de tempo.
    O objeto é de natureza muito técnica. Deve ser utilizado apenas para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    '''

    def BarCount(self, chart_id: int) -> int:
        ''' Retorna o número de barras no gráfico especificado.
        '''
        return self.component.BarCount(chart_id)

    def GetBarContent(self, chart_id: int, bar_id: int, text_id: int) -> str:
        ''' Retorna o conteúdo da barra especificada.
        '''
        return self.component.GetBarContent(chart_id, bar_id, text_id)

    def GetGridLineContent(self, chart_id: int, grid_line_id: int, text_id: int) -> str:
        ''' Retorna o conteúdo da linha de grade especificada.
        '''
        return self.component.GetGridLineContent(chart_id, grid_line_id, text_id)

    def GridCount(self, chart_id: int) -> int:
        ''' Retorna o número de grades dentro do gráfico especificado.
        '''
        return self.component.GridCount(chart_id)

    def LinkCount(self, chart_id: int) -> int:
        ''' Retorna o número de links dentro do gráfico especificado.
        '''
        return self.component.LinkCount(chart_id)

    def SendData(self, dados: str) -> None:
        ''' Envia dados para o servidor.
        '''
        self.component.SendData(dados)

    def ChartCount(self) -> int:
        ''' Número de gráficos.
        '''
        return self.component.ChartCount

class SapGuiApoGrid(SapGuiShell):
    ''' Observações
    O GuiApoGrid é um objeto criado especificamente para aplicações SAP SCM.
    Ele implementa um quadro de planejamento, semelhante a um controle GuiGridView.

    As colunas e linhas são identificadas pela sua posição começando em zero:
    0 <= linha <Contagem de linhas
    0 <= coluna <Contagem de colunas
    Após uma busca detalhada, as linhas são renumeradas para que o número de qualquer linha possa mudar. A rolagem horizontal não afeta o número de uma coluna.
    '''

    def CancelCut(self) -> None:
        ''' Aborta a operação de corte.
        '''
        self.component.CancelCut()

    def ClearSelection(self) -> None:
        ''' Chamar clearSelection remove todas as seleções de linhas, colunas e células.
        '''
        self.component.ClearSelection()

    def ContextMenu(self, coluna: int, linha: int) -> None:
        ''' Chamar contextMenu emula a solicitação de menu de contexto.
        '''
        self.component.ContextMenu(coluna, linha)

    def Cut(self) -> None:
        ''' Corta as células selecionadas.
        '''
        self.component.Cut()

    def DeselectCell(self, coluna: int, linha: int) -> None:
        ''' Deseleciona as células especificadas. Esta função remove as células especificadas da coleção de células selecionadas.
        '''
        self.component.DeselectCell(coluna, linha)

    def DeselectColumn(self, coluna: int) -> None:
        ''' Esta função remove a coluna especificada da coleção de colunas selecionadas.
        '''
        self.component.DeselectColumn(coluna)

    def DeselectRow(self, linha: int) -> None:
        ''' Esta função remove a linha especificada da coleção de linhas selecionadas.
        '''
        self.component.DeselectRow(linha)

    def DoubleClickCell(self, coluna: int, linha: int) -> None:
        ''' Esta função emula um duplo clique do mouse em uma célula específica se os parâmetros forem válidos e gera uma exceção caso contrário.
        '''
        self.component.DoubleClickCell(coluna, linha)

    def GetBgdColorInfo(self, linha: int, coluna: int) -> str:
        ''' Esta função retorna a cor de fundo da célula especificada.
        '''
        return self.component.GetBgdColorInfo(linha, coluna)

    def GetCellChangeable(self, coluna: int, linha: int) -> bool:
        ''' Esta função retorna True se a célula especificada for editável.
        '''
        return self.component.GetCellChangeable(coluna, linha)

    def GetCellFormat(self, coluna: int, linha: int) -> str:
        ''' Retorna o formato da célula especificada.
        '''
        return self.component.GetCellFormat(coluna, linha)

    def GetCellTooltip(self, coluna: int, linha: int) -> str:
        ''' Esta função retorna a dica de ferramenta da célula especificada.
        '''
        return self.component.GetCellTooltip(coluna, linha)

    def GetCellValue(self, coluna: int, linha: int) -> str:
        ''' Esta função retorna o valor da célula especificada como uma string.
        '''
        return self.component.GetCellValue(coluna, linha)

    def GetFgdColorInfo(self, linha: int, coluna: int) -> str:
        ''' Esta função retorna a cor da fonte da célula especificada.
        '''
        return self.component.GetFgdColorInfo(linha, coluna)

    def GetIconInfo(self, linha: int, coluna: int) -> str:
        ''' Retorna informações do ícone da célula especificada.
        '''
        return self.component.GetIconInfo(linha, coluna)

    def IsCellSelected(self, coluna: int, linha: int) -> bool:
        ''' Retorna True se a célula especificada estiver selecionada.
        '''
        return self.component.IsCellSelected(coluna, linha)

    def IsColSelected(self, coluna: int) -> bool:
        ''' Retorna True se a coluna especificada estiver selecionada.
        '''
        return bool(self.component.IsColSelected(coluna))

    def IsRowSelected(self, linha: int) -> bool:
        ''' Retorna True se a linha especificada estiver selecionada.
        '''
        return bool(self.component.IsRowSelected(linha))

    def Paste(self, valores_celula: object, num_colunas: int) -> int:
        ''' Aciona uma operação de colar.
        '''
        return self.component.Paste(valores_celula, num_colunas)

    def PressEnter(self) -> None:
        ''' Emula a pressão da tecla Enter.
        '''
        self.component.PressEnter()

    def SelectAll(self) -> None:
        ''' Esta função seleciona todo o conteúdo da grade (ou seja, todas as linhas e colunas).
        '''
        self.component.SelectAll()

    def SelectCell(self, coluna: int, linha: int) -> None:
        ''' Seleciona a célula especificada.
        '''
        self.component.SelectCell(coluna, linha)

    def SelectColumn(self, coluna: int) -> None:
        ''' Seleciona a coluna especificada.
        '''
        self.component.SelectColumn(coluna)

    def SelectRow(self, linha: int) -> None:
        ''' Seleciona a linha especificada.
        '''
        self.component.SelectRow(linha)

    def SetCellValue(self, coluna: int, linha: int, valor: str) -> str:
        ''' Esta função insere o valor especificado na célula especificada.
        '''
        return self.component.SetCellValue(coluna, linha, valor)

    def ColumnCount(self) -> int:
        ''' Esta propriedade representa o número de colunas no controle.
        '''
        return self.component.ColumnCount

    def CurrentCellColumn(self) -> int:
        ''' O índice da coluna que contém a célula atual.
        '''
        return self.component.CurrentCellColumn

    def CurrentCellRow(self) -> int:
        ''' O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        '''
        return self.component.CurrentCellRow

    def FirstVisibleColumn(self) -> int:
        ''' Esta propriedade representa a primeira coluna visível da área rolável do controle APOGrid.
        '''
        return self.component.FirstVisibleColumn

    def FirstVisibleRow(self) -> int:
        ''' Este é o índice da primeira linha visível na grade. Definir esta propriedade para um índice de linha inválido gerará uma exceção.
        '''
        return self.component.FirstVisibleRow

    def FixedColumnsLeft(self) -> int:
        ''' O número de colunas fixas no lado esquerdo da grade.
        '''
        return self.component.FixedColumnsLeft

    def FixedColumnsRight(self) -> int:
        ''' O número de colunas fixas no lado direito da grade.
        '''
        return self.component.FixedColumnsRight

    def FixedRowsBottom(self) -> int:
        ''' O número de linhas fixas na parte inferior da grade.
        '''
        return self.component.FixedRowsBottom

    def FixedRowsTop(self) -> int:
        ''' O número de linhas fixas na parte superior da grade.
        '''
        return self.component.FixedRowsTop

    def RowCount(self) -> int:
        ''' Esta propriedade representa o número de linhas no controle.
        '''
        return self.component.RowCount

    def SelectedCells(self) -> object:
        ''' A coleção de células selecionadas. Tentar definir esta propriedade como um valor inválido gerará uma exceção.
        '''
        return self.component.SelectedCells

    def SelectedColumns(self) -> str:
        ''' As colunas selecionadas estão disponíveis como uma coleção. Configurar esta propriedade pode gerar uma exceção se a nova coleção contiver uma coluna inválida.
        '''
        return self.component.SelectedColumns

    def SelectedColumnsObject(self) -> object:
        ''' Retorna a coleção de colunas selecionadas como um objeto.
        '''
        return self.component.SelectedColumnsObject

    def SelectedRows(self) -> str:
        ''' As linhas selecionadas estão disponíveis como uma coleção. Configurar esta propriedade pode gerar uma exceção se a nova coleção contiver uma linha inválida.
        '''
        return self.component.SelectedRows

    def SelectedRowsObject(self) -> object:
        ''' Retorna a coleção de linhas selecionadas como um objeto.
        '''
        return self.component.SelectedRowsObject

    def VisibleColumnCount(self) -> int:
        ''' Recupera o número de colunas visíveis da grade.
        '''
        return self.component.VisibleColumnCount

    def VisibleRowCount(self) -> int:
        ''' Recupera o número de linhas visíveis da grade.
        '''
        return self.component.VisibleRowCount

class SapGuiAbapEditor(SapGuiShell):
    ''' O objeto GuiAbapEditor representa o novo controle do editor ABAP disponível a partir do SAP_BASIS release 6.20 (ver também SAP Note 930742).
    GuiAbapEditor estende GuiShell.
    '''
    
    def AutoBraceEnabled(self) -> bool:
        ''' Retorna True se a função de auto-colchetes estiver atualmente ativada. '''
        return self.component.AutoBraceEnabled()

    def AutoComplete(self):
        ''' Invoca a caixa de lista de auto-completar. '''
        self.component.AutoComplete()

    def AutoCorrectEnabled(self) -> bool:
        ''' Retorna True se a função de correção automática estiver atualmente ativada. '''
        return self.component.AutoCorrectEnabled()

    def AutoExpand(self):
        ''' Ativa o mecanismo de auto-expansão de modelos de código. '''
        self.component.AutoExpand()

    def AutoIndentEnabled(self) -> bool:
        ''' Retorna True se a função de auto-indentação estiver atualmente ativada. '''
        return self.component.AutoIndentEnabled()

    def Capitalize(self):
        ''' Torna maiúscula a primeira letra alfabética de cada palavra no texto selecionado. Todas as outras letras são transformadas em minúsculas. '''
        self.component.Capitalize()

    def ClipboardCopy(self):
        ''' Realiza uma operação de cópia para a área de transferência no texto atualmente selecionado. '''
        self.component.ClipboardCopy()

    def ClipboardCut(self):
        ''' Realiza uma operação de corte para a área de transferência no texto atualmente selecionado. '''
        self.component.ClipboardCut()

    def ClipboardPaste(self):
        ''' Cole o conteúdo atual da área de transferência a partir da posição atual do cursor. '''
        self.component.ClipboardPaste()

    def ClipboardRingPaste(self, Index: int):
        ''' Cole uma entrada do anel da área de transferência do editor no editor.
        Index: Índice com base em 1 da entrada da área de transferência conforme aparece no menu de contexto do editor ABAP.
        '''
        self.component.ClipboardRingPaste(Index)

    def CodeHintsEnabled(self) -> bool:
        ''' Retorna True se as dicas de código estiverem atualmente ativadas. '''
        return self.component.CodeHintsEnabled()

    def CommentSelectedLines(self):
        ''' Coloca as linhas selecionadas entre comentários. '''
        self.component.CommentSelectedLines()

    def CorrectCapsEnabled(self) -> bool:
        ''' Retorna True se a função de correção de maiúsculas estiver atualmente ativada. '''
        return self.component.CorrectCapsEnabled()

    def Delete(self):
        ''' Exclui o caractere que segue a posição atual do cursor. Equivalente a pressionar a tecla <DEL>. '''
        self.component.Delete()

    def DeleteBack(self):
        ''' Move o cursor para a coluna anterior, excluindo o caractere atualmente presente lá. Equivalente a pressionar a tecla de retrocesso. '''
        self.component.DeleteBack()

    def DeleteRange(self, LineStart: int, ColumnStart: int, LineEnd: int, ColumnEnd: int):
        ''' Define uma região de texto para exclusão.
        LineStart: Especifica o número da linha a partir da qual a exclusão deve começar.
        ColumnStart: Especifica o número da coluna a partir da qual a exclusão deve começar.
        LineEnd: Especifica o número da linha onde a exclusão terminará.
        ColumnEnd: Especifica o número da coluna onde a exclusão terminará.
        '''
        self.component.DeleteRange(LineStart, ColumnStart, LineEnd, ColumnEnd)

    def DeleteSelection(self) -> None:
        ''' Exclui o texto atualmente selecionado.
        '''
        self.component.DeleteSelection()

    def DeleteWord(self) -> None:
        ''' Exclui a palavra que precede a posição atual do cursor.
        '''
        self.component.DeleteWord()

    def DeleteWordBack(self) -> None:
        ''' Exclui a palavra que precede a posição atual do cursor.
        '''
        self.component.DeleteWordBack()

    def DuplicateLine(self) -> None:
        ''' Duplica o conteúdo da linha na qual o cursor está atualmente e insere uma cópia do conteúdo da linha abaixo do cursor.
        '''
        self.component.DuplicateLine()

    def FormatSelectedLines(self) -> None:
        ''' Formata as linhas selecionadas de acordo com as configurações de "Pretty Printer" e "Formatting", como Auto Indent e Smart Tab.
        '''
        self.component.FormatSelectedLines()

    def GetAutoCompleteEntryCount(self) -> int:
        ''' Retorna o número de entradas disponíveis exibidas na caixa de lista de auto-completar.
        '''
        return self.component.GetAutoCompleteEntryCount()

    def GetAutoCompleteEntryText(self, index: int) -> str:
        ''' Retorna uma string representando a entrada na caixa de lista de auto-completar correspondente ao índice fornecido como parâmetro.
        '''
        return self.component.GetAutoCompleteEntryText(index)

    def GetAutoCompleteIconType(self, index: int) -> int:
        ''' Retorna o índice da imagem associada à entrada de auto-completar especificada no índice. Retorna -1 se nenhuma imagem estiver associada.
        '''
        return self.component.GetAutoCompleteIconType(index)

    def GetAutoCompleteSubIconType(self, index: int) -> int:
        ''' Retorna o índice da subimagem associada à entrada de auto-completar especificada no índice. Retorna -1 se nenhuma subimagem estiver associada.
        '''
        return self.component.GetAutoCompleteSubIconType(index)

    def GetAutoCompleteToolbarButtonToolTip(self, index: int) -> str:
        ''' Retorna o texto de dica de ferramenta que é exibido pelo botão de barra de ferramentas de auto-completar especificado no índice.
        '''
        return self.component.GetAutoCompleteToolbarButtonToolTip(index)

    def GetAutoCompleteToolTipDelay(self) -> int:
        ''' Retorna o número de milissegundos que passam entre a realçar uma entrada na lista de auto-completar e a exibição da dica de ferramenta correspondente.
        '''
        return self.component.GetAutoCompleteToolTipDelay()

    def GetCurrentToolTipText(self) -> str:
        ''' Recupera o texto na dica de ferramenta atualmente exibida para dica de código ou lista de auto-completar. Múltiplas linhas são separadas por caracteres \n.
        '''
        return self.component.GetCurrentToolTipText()

    def GetCursorColumnPosition(self) -> int:
        ''' Retorna o número da coluna em que o cursor atualmente reside.
        '''
        return self.component.GetCursorColumnPosition()

    def GetCursorLinePosition(self) -> int:
        ''' Retorna o número da linha em que o cursor atualmente reside.
        '''
        return self.component.GetCursorLinePosition()

    def GetFirstVisibleLine(self) -> int:
        ''' Retorna o número da linha superior visível na sessão atual do editor.
        '''
        return self.component.GetFirstVisibleLine()

    def GetHTMLClipboardContents(self) -> str:
        ''' Retorna uma string contendo o conteúdo atual da área de transferência no formato HTML. Retorna uma string vazia se a área de transferência não contiver nada no formato HTML.
        '''
        return self.component.GetHTMLClipboardContents()

    def GetLastVisibleLine(self) -> int:
        ''' Retorna o número da linha inferior visível na sessão atual do editor.
        '''
        return self.component.GetLastVisibleLine()

    def GetLineCount(self) -> int:
        ''' Retorna o número total de linhas contidas no documento na sessão atual.
        '''
        return self.component.GetLineCount()

    def GetLineText(self, line: int) -> str:
        ''' Retorna uma string contendo o conteúdo da linha especificada pelo parâmetro Line.
        '''
        return self.component.GetLineText(line)

    def GetNumberedBookmarks(self, line: int) -> object:
        ''' Retorna uma coleção de números de marcadores atribuídos à linha especificada pelo parâmetro Line. O número do marcador pode variar de 0 a 9. Se nenhum marcador numerado estiver atribuído, a coleção estará vazia.
        '''
        return self.component.GetNumberedBookmarks(line)

    def GetRTFClipboardContents(self) -> str:
        ''' Retorna uma string contendo o conteúdo atual da área de transferência no formato Rich Text. Retorna uma string vazia se a área de transferência não contiver nada no formato Rich Text.
        '''
        return self.component.GetRTFClipboardContents()

    def GetSelectedAutoComplete(self) -> int:
        ''' Retorna o índice base zero da entrada atualmente selecionada na caixa de lista de auto-completar. O método retornará -1 se nenhuma entrada estiver selecionada.
        '''
        return self.component.GetSelectedAutoComplete()

    def GetSelectedText(self) -> str:
        ''' Retorna uma string contendo o texto atualmente destacado ou selecionado na sessão do editor. Se o texto selecionado abranger mais de uma linha, quaisquer caracteres de terminador de linha serão incluídos na string retornada por este método.
        '''
        return self.component.GetSelectedText()

    def GetStructureBlockEndLine(self, line: int) -> int:
        ''' Retorna a linha final do bloco de estrutura relevante para a linha especificada pelo parâmetro Line. Se a linha não estiver dentro de um bloco de estrutura, o método retorna -1.
        '''
        return self.component.GetStructureBlockEndLine(line)

    def GetStructureBlockStartLine(self, line: int) -> int:
        ''' Retorna a linha inicial do bloco de estrutura relevante para a linha especificada pelo parâmetro Line. Se a linha estiver dentro de um bloco de estrutura aninhado, a linha inicial do bloco mais interno será retornada. Se a linha não estiver dentro de um bloco de estrutura, o método retorna -1.
        '''
        return self.component.GetStructureBlockStartLine(line)

    def GetUndoPosition(self) -> int:
        ''' Retorna a posição atual do documento no buffer de desfazer/refazer.
        '''
        return self.component.GetUndoPosition()

    def GetWordWrapMode(self) -> int:
        ''' Retorna um número inteiro correspondente ao modo atual de quebra de linha:
        0 - Quebra de linha desativada.
        1 - Quebra na borda da janela.
        2 - Quebra pela largura da página.
        3 - Quebra pela largura da página inserindo quebra rígida.
        '''
        return self.component.GetWordWrapMode()

    def GetWordWrapPosition(self) -> int:
        ''' Retorna a largura da página atualmente atribuída à quebra de linha. O número retornado é o número de colunas após o qual a quebra de linha será aplicada.
        '''
        return self.component.GetWordWrapPosition()

    def GoNextBookMark(self) -> None:
        ''' Navega até a linha onde o próximo marcador não numerado está definido.
        '''
        self.component.GoNextBookMark()

    def GoNumberedBookmark(self, mark: int) -> None:
        ''' Navega até a linha onde o marcador numerado Mark está localizado.
        '''
        self.component.GoNumberedBookmark(mark)

    def GoPreviousBookMark(self) -> None:
        ''' Navega até a linha onde o marcador não numerado anterior está definido.
        '''
        self.component.GoPreviousBookMark()

    def InsertTab(self) -> None:
        ''' Insere uma TAB na posição atual do cursor. Equivalente a pressionar a tecla TAB.
        '''
        self.component.InsertTab()

    def InsertText(self, text: str, line: int, column: int) -> None:
        ''' Insere o texto especificado em Text na posição especificada em Line e Column como se o texto tivesse sido digitado no editor a partir do teclado.
        '''
        self.component.InsertText(text, line, column)

    def IsAutoCompleteEntryBold(self, index: int) -> bool:
        ''' Retorna True se a entrada de auto-completar especificada no índice estiver em negrito.
        '''
        return bool(self.component.IsAutoCompleteEntryBold(index))

    def IsAutoCompleteOpen(self) -> bool:
        ''' Retorna True se a caixa de lista de auto-completar estiver atualmente aberta.
        '''
        return bool(self.component.IsAutoCompleteOpen())

    def IsAutoCompleteToolbarButtonPressed(self, index: int) -> bool:
        ''' Retorna True se o botão da barra de ferramentas de auto-completar especificado no índice estiver atualmente pressionado. Caso contrário, retorna False.
        '''
        return bool(self.component.IsAutoCompleteToolbarButtonPressed(index))

    def IsAutoCompleteToolTipVisible(self) -> bool:
        ''' Retorna True se a dica de ferramenta correspondente a uma entrada na caixa de lista de auto-completar estiver atualmente visível.
        '''
        return bool(self.component.IsAutoCompleteToolTipVisible())

    def IsBookmark(self, line: int) -> bool:
        ''' Retorna True se a linha estiver marcada com um marcador padrão que não é numerado. O método não fornece informações sobre se a linha está marcada com um marcador numerado.
        '''
        return bool(self.component.IsBookmark(line))

    def IsBreakpointSet(self, line: int) -> bool:
        ''' Retorna True se um ponto de interrupção estiver definido na linha especificada pelo parâmetro Line.
        '''
        return bool(self.component.IsBreakpointSet(line))

    def IsLineCollapsed(self, line: int) -> bool:
        ''' Retorna True se o número da linha passado corresponder a uma linha que marca o início de um bloco colapsável que está atualmente no estado colapsado.
        '''
        return bool(self.component.IsLineCollapsed(line))

    def IsLineComment(self, line: int) -> bool:
        ''' Retorna True se a linha especificada em Line contiver comentários. Caso contrário, retorna False.
        '''
        return bool(self.component.IsLineComment(line))

    def IsLineModified(self, line: int) -> bool:
        ''' Retorna True se a linha foi modificada durante a sessão atual do editor.
        '''
        return bool(self.component.IsLineModified(line))

    def IsModified(self) -> bool:
        ''' Retorna True se alguma parte do documento atual foi modificada durante a sessão atual do editor.
        '''
        return bool(self.component.IsModified())

    def JoinSelectedLines(self) -> None:
        ''' Mescla as linhas de texto atualmente selecionadas em uma única linha de texto.
        '''
        self.component.JoinSelectedLines()

    def LowerCase(self) -> None:
        ''' Força o texto selecionado a ficar em letras minúsculas.
        '''
        self.component.LowerCase()

    def MoveCursorDocumentEnd(self) -> None:
        ''' Posiciona o cursor na última coluna da última linha do documento.
        '''
        self.component.MoveCursorDocumentEnd()

    def MoveCursorLineDown(self) -> None:
        ''' Move o cursor uma linha para baixo a partir de sua posição atual.
        '''
        self.component.MoveCursorLineDown()

    def MoveCursorLineEnd(self) -> None:
        ''' Posiciona o cursor na última coluna da linha atual.
        '''
        self.component.MoveCursorLineEnd()

    def MoveCursorLineHome(self) -> None:
        ''' Posiciona o cursor na primeira coluna da linha atual.
        '''
        self.component.MoveCursorLineHome()

    def MoveCursorLineUp(self) -> None:
        ''' Move o cursor uma linha para cima a partir de sua posição atual.
        '''
        self.component.MoveCursorLineUp()

    def MoveLineDown(self) -> None:
        ''' Move o conteúdo da linha em que o cursor está para a linha abaixo e move o conteúdo da linha abaixo do cursor para cima de uma linha.
        '''
        self.component.MoveLineDown()

    def MoveLineUp(self) -> None:
        ''' Move o conteúdo da linha em que o cursor está para a linha acima e move o conteúdo da linha acima do cursor para baixo de uma linha.
        '''
        self.component.MoveLineUp()

    def MoveWordLeft(self) -> None:
        ''' Move o cursor para a coluna que precede a próxima palavra encontrada à esquerda da posição atual do cursor.
        '''
        self.component.MoveWordLeft()

    def MoveWordRight(self) -> None:
        ''' Move o cursor para a coluna que precede a próxima palavra encontrada à direita da posição atual do cursor.
        '''
        self.component.MoveWordRight()

    def OverwriteModeEnabled(self) -> bool:
        ''' Retorna True se o modo de substituição estiver habilitado, False se estiver no modo de inserção.
        '''
        return bool(self.component.OverwriteModeEnabled())

    def RemoveAllBookmarks(self) -> None:
        ''' Remove todos os tipos de marcadores do documento. Tanto os marcadores numerados quanto os não numerados são removidos.
        '''
        self.component.RemoveAllBookmarks()

    def RemoveAllBreakpoints(self) -> None:
        ''' Remove todos os pontos de interrupção do documento atual.
        '''
        self.component.RemoveAllBreakpoints()

    def RemoveBookmarks(self, bookmarks: str) -> None:
        ''' Remove todos os marcadores especificados na string fornecida.
        '''
        self.component.RemoveBookmarks(bookmarks)

    def RemoveBreakpoint(self, line: int) -> None:
        ''' Remove o ponto de interrupção na linha especificada pelo parâmetro Line.
        '''
        self.component.RemoveBreakpoint(line)

    def ReplaceSelection(self, text: str) -> None:
        ''' Substitui o texto atualmente selecionado pelo texto contido no parâmetro Text.
        '''
        self.component.ReplaceSelection(text)

    def SaveToFile(self, file_path: str) -> None:
        ''' Salva o documento atual em um arquivo no caminho especificado em p1.
        '''
        self.component.SaveToFile(file_path)

    def ScrollToLine(self, line: int) -> None:
        ''' Rolamento para a linha especificada pelo parâmetro Line, se ainda não estiver visível na tela.
        '''
        self.component.ScrollToLine(line)

    def SelectAll(self) -> None:
        ''' Realça todo o texto no documento atual para seleção.
        '''
        self.component.SelectAll()

    def SelectBlockRange(self, line_start: int, column_start: int, line_end: int, column_end: int) -> None:
        ''' Realça uma região de texto no modo de bloco para seleção. Equivalente a pressionar a tecla ALT enquanto arrasta o mouse sobre o texto.
        LineStart especifica o número da linha a partir da qual a seleção deve começar.
        ColumnStart especifica o número da coluna a partir da qual a seleção deve começar.
        LineEnd especifica o número da linha onde a seleção terminará.
        ColumnEnd especifica o número da coluna onde a seleção terminará.
        '''
        self.component.SelectBlockRange(line_start, column_start, line_end, column_end)

    def SelectRange(self, line_start: int, column_start: int, line_end: int, column_end: int) -> None:
        ''' Realça uma região de texto para seleção.
        LineStart especifica o número da linha a partir da qual a seleção deve começar.
        ColumnStart especifica o número da coluna a partir da qual a seleção deve começar.
        LineEnd especifica o número da linha onde a seleção terminará.
        ColumnEnd especifica o número da coluna onde a seleção terminará.
        '''
        self.component.SelectRange(line_start, column_start, line_end, column_end)

    def SelectWordLeft(self) -> None:
        ''' Seleciona a palavra à esquerda da posição atual do cursor.
        '''
        self.component.SelectWordLeft()

    def SelectWordRight(self) -> None:
        ''' Seleciona a palavra à direita da posição atual do cursor.
        '''
        self.component.SelectWordRight()

    def Sentencize(self) -> None:
        ''' Torna maiúscula a primeira letra de cada sentença. As sentenças são delimitadas por caracteres ".". Todos os outros caracteres são transformados em minúsculas.
        '''
        self.component.Sentencize()

    def SetAutoBrace(self, status: bool) -> None:
        ''' Ativa ou desativa a funcionalidade de autocompletar colchetes.
        '''
        self.component.SetAutoBrace(status)

    def SetAutoCorrect(self, status: bool) -> None:
        ''' Ativa ou desativa a funcionalidade de autocorreção automática.
        '''
        self.component.SetAutoCorrect(status)

    def SetAutoIndent(self, status: bool) -> None:
        ''' Ativa ou desativa a funcionalidade de recuo automático.
        '''
        self.component.SetAutoIndent(status)

    def SetBookmarks(self, bookmarks: str) -> None:
        ''' Define marcadores.
        Aceita uma string no seguinte formato:
        <linha>[(<número>)][,<linha>] por exemplo, "10(1),22(2),33,42", <linha>={1,...,n}, <número>={1,...
        '''
        self.component.SetBookmarks(bookmarks)

    def SetBreakpoint(self, line: int) -> None:
        ''' Define um ponto de interrupção na linha especificada pelo parâmetro Line.
        '''
        self.component.SetBreakpoint(line)

    def SetCodeHints(self, status: bool) -> None:
        ''' Ativa ou desativa as dicas de código.
        '''
        self.component.SetCodeHints(status)

    def SetCorrectCaps(self, status: bool) -> None:
        ''' Ativa ou desativa a correção automática de maiúsculas.
        '''
        self.component.SetCorrectCaps(status)

    def SetLineFeedStyle(self, style: int) -> None:
        ''' Define o estilo de quebra de linha.
        '''
        self.component.SetLineFeedStyle(style)

    def SetOverwriteMode(self, status: bool) -> None:
        ''' Alterna entre os modos de Inserção e Sobrescrita. Se chamado com True, o modo de Sobrescrita é ativado. Caso contrário, o editor está no modo de Inserção.
        '''
        self.component.SetOverwriteMode(status)

    def SetSelectionPosInLine(self, linha: int, coluna: int) -> None:
        ''' Posiciona o cursor na linha <Linha> e coluna <Coluna>.
        '''
        self.component.SetSelectionPosInLine(linha, coluna)

    def SetSmartTab(self, status: bool) -> None:
        ''' Ativa ou desativa a funcionalidade de Smart Tab.
        '''
        self.component.SetSmartTab(status)

    def SetWordWrapMode(self, modo: int) -> None:
        ''' Define o modo de quebra de linha de acordo com o número fornecido em Modo:
        0 - Quebra de linha desativada.
        1 - Quebrar na borda da janela.
        2 - Quebrar na largura da página.
        3 - Quebrar na largura da página inserindo quebra rígida.
        '''
        self.component.SetWordWrapMode(modo)

    def SetWordWrapPosition(self, pos: int) -> None:
        ''' Pos especifica o número de colunas a serem exibidas antes da quebra de palavras ser aplicada.
        '''
        self.component.SetWordWrapPosition(pos)

    def SmartTabEnabled(self) -> bool:
        ''' Retorna True se a funcionalidade de Smart Tab estiver habilitada, False caso contrário.
        '''
        return bool(self.component.SmartTabEnabled())

    def SortSelectedLines(self) -> None:
        ''' Rearranja as linhas selecionadas em ordem alfanumérica.
        '''
        self.component.SortSelectedLines()

    def SwapCase(self) -> None:
        ''' Inverte a configuração de maiúsculas/minúsculas para o texto selecionado. Os caracteres maiúsculos são trocados por minúsculos e vice-versa.
        '''
        self.component.SwapCase()

    def ToggleCapsLock(self) -> None:
        ''' Ativa ou desativa a tecla Caps Lock.
        '''
        self.component.ToggleCapsLock()

    def ToggleNumberedBookmark(self, marcador: int, linha: int) -> None:
        ''' Alterna o estado do marcador numerado <Marcador> na linha <Linha>. Se já existir um marcador com o número <Marcador> na linha, ele será removido. Caso contrário, ele será adicionado.
        '''
        self.component.ToggleNumberedBookmark(marcador, linha)

    def ToggleStructureBlock(self, linha: int) -> None:
        ''' Se o número da linha especificado em <Linha> for a primeira linha de um bloco de código recolhível, este método alternará o status expandido/recolhido do bloco.
        '''
        self.component.ToggleStructureBlock(linha)

    def TransposeLine(self) -> None:
        ''' Troca o conteúdo da linha em que o cursor está atualmente com o conteúdo da linha acima da posição atual do cursor.
        '''
        self.component.TransposeLine()

    def UncommentSelectedLines(self) -> None:
        ''' Remove os comentários das linhas selecionadas.
        '''
        self.component.UncommentSelectedLines()

    def Undo(self, posicao_undo: int) -> None:
        ''' Realiza um undo ou redo, dependendo de PosicaoUndo. PosicaoUndo especifica uma posição baseada em zero no buffer de undo/redo. Se -1 for passado, um único passo de undo será executado.
        '''
        self.component.Undo(posicao_undo)

    def UnTab(self) -> None:
        ''' Remove uma TAB na posição atual do cursor. Equivalente a pressionar <SHIFT> + <TAB>.
        '''
        self.component.UnTab()

    def UpperCase(self) -> None:
        ''' Força o texto selecionado a ficar em maiúsculas.
        '''
        self.component.UpperCase()

class SapGuiSplitterContainer(SapGuiShell):
    ''' O GuiSplitterContainer representa o elemento divisor dynpro, que foi introduzido
    no Web Application Server ABAP no NetWeaver 7.1. O elemento divisor dynpro é semelhante
    ao controle divisor baseado em activeX, mas é um elemento dynpro simples.
    '''

    def IsVertical(self) -> bool:
        ''' Esta propriedade contém True se as células divisoras do GuiSplitterContainer estiverem alinhadas
        verticalmente e False se estiverem alinhadas horizontalmente.
        '''
        return self.component.IsVertical

    def SashPosition(self, position: int = None) -> int:
        ''' Contém a posição da divisória do divisor em caracteres.
        '''
        if position is not None:
            self.component.SashPosition = position
        return self.component.SashPosition

class SapGuiSplit(SapGuiShell):
    # TODO Criar descrição

    def GetColSize(self, Id: int) -> int:
        ''' Obtém o tamanho da coluna do divisor especificado.
        Id: O índice da coluna do divisor (começando com índice 1).
        Retorna o tamanho da coluna do divisor especificado em porcentagem.
        '''
        return self.component.GetColSize(Id)

    def GetRowSize(self, Id: int) -> int:
        ''' Obtém o tamanho da linha do divisor especificado.
        Id: O índice da linha do divisor (começando com índice 1).
        Retorna o tamanho da linha do divisor especificado em porcentagem.
        '''
        return self.component.GetRowSize(Id)

    def SetColSize(self, Id: int, Size: int):
        ''' Define o tamanho da coluna do divisor especificado.
        Id: O índice da coluna do divisor (começando com índice 1).
        Size: O tamanho desejado em porcentagem.
        '''
        self.component.SetColSize(Id, Size)

    def SetRowSize(self, Id: int, Size: int):
        ''' Define o tamanho da linha do divisor especificado.
        Id: O índice da linha do divisor (começando com índice 1).
        Size: O tamanho desejado em porcentagem.
        '''
        self.component.SetRowSize(Id, Size)

    def IsVertical(self) -> bool:
        ''' Esta propriedade contém True se as células divisoras do GuiSplit estiverem alinhadas verticalmente e False se estiverem alinhadas horizontalmente.
        '''
        return self.component.IsVertical

class SapGuiInputFieldControl(SapGuiShell):
    # TODO Criar descrição
    
    def Submit(self):
        ''' Submete a entrada para a aplicação.
        Esta função envia a entrada inserida para a aplicação.
        '''
        self.component.Submit()

    def ButtonTooltip(self) -> str:
        ''' Tooltip do botão de envio/consulta.
        '''
        return self.component.ButtonTooltip

    def FindButtonActivated(self) -> bool:
        ''' Esta propriedade é True quando o botão Find está ativo.
        '''
        return self.component.FindButtonActivated

    def HistoryOpened(self) -> bool:
        ''' Esta propriedade é True quando o histórico de entrada está aberto.
        '''
        return self.component.HistoryOpened

    def LabelText(self) -> str:
        ''' O texto do rótulo pertencente ao campo de entrada.
        '''
        return self.component.LabelText

    def Text(self, new_text: str = None) -> str:
        ''' Conteúdo de texto do campo de entrada em si.
        '''
        if new_text is not None:
            self.component.Text = new_text
        return self.component.Text

class SapGuiTextedit(SapGuiShell):
    ''' O controle TextEdit é um controle de edição multilinha que oferece vários benefícios possíveis.
    No que diz respeito aos scripts, a possibilidade de proteger partes do texto contra edição pelo usuário
    é especialmente útil. GuiTextedit estende o objeto GuiShell.
    '''

    def ContextMenu(self) -> None:
        ''' Chamar ContextMenu emula a solicitação de menu de contexto.
        '''
        self.component.ContextMenu()

    def DoubleClick(self) -> None:
        ''' Esta função emula um clique duplo do mouse.
        Para definir a seleção, a função setSelectionIndexes pode ser chamada antecipadamente.
        '''
        self.component.DoubleClick()

    def GetLineText(self, n_line: int) -> str:
        ''' Retorna o texto da linha especificada.
        '''
        return self.component.GetLineText(n_line)

    def GetUnprotectedTextPart(self, part: int) -> str:
        ''' Esta função recupera o conteúdo de uma parte de texto desprotegida usando o índice baseado em zero, part.
        '''
        return self.component.GetUnprotectedTextPart(part)

    def IsBreakpointLine(self, n_line: int) -> int:
        ''' Retorna VERDADEIRO se a linha especificada contiver um ponto de interrupção.
        '''
        return self.component.IsBreakpointLine(n_line)

    def IsCommentLine(self, n_line: int) -> int:
        ''' Retorna VERDADEIRO se a linha especificada for uma linha de comentário.
        '''
        return self.component.IsCommentLine(n_line)

    def IsHighlightedLine(self, n_line: int) -> int:
        ''' Retorna VERDADEIRO se a linha especificada estiver destacada.
        '''
        return self.component.IsHighlightedLine(n_line)

    def IsProtectedLine(self, n_line: int) -> int:
        ''' Retorna VERDADEIRO se a linha especificada estiver protegida.
        '''
        return self.component.IsProtectedLine(n_line)

    def IsSelectedLine(self, n_line: int) -> int:
        ''' Retorna VERDADEIRO se a linha especificada estiver selecionada.
        '''
        return self.component.IsSelectedLine(n_line)

    def ModifiedStatusChanged(self, status: int) -> None:
        ''' Esta função emula a alteração do status modificado.
        '''
        self.component.ModifiedStatusChanged(status)

    def MultipleFilesDropped(self, files: list) -> None:
        ''' Emula uma operação de arrastar e soltar, na qual vários arquivos são soltos no controle de texto.
        A lista contém, para cada arquivo, o nome completo do arquivo como uma string.
        '''
        self.component.MultipleFilesDropped(files)

    def PressF1(self) -> None:
        ''' Esta função emula a pressão da tecla F1 no teclado.
        '''
        self.component.PressF1()

    def PressF4(self) -> None:
        ''' Esta função emula a pressão da tecla F4 no teclado.
        '''
        self.component.PressF4()

    def SetSelectionIndexes(self, start: int, end: int) -> None:
        ''' Esta função define a faixa de texto visualmente selecionada. start e end são índices absolutos de caracteres baseados em zero.
        start corresponde à posição onde a seleção começa e end é a posição do primeiro caractere após a seleção. 
        Observe que definir start igual a end resulta na definição do cursor nessa posição.
        '''
        self.component.SetSelectionIndexes(start, end)

    def SetUnprotectedTextPart(self, part: int, text: str) -> int:
        ''' Esta função atribui o conteúdo do texto à parte de texto desprotegida com índice baseado em zero, part.
        A função retorna True se foi possível realizar a atribuição. Caso contrário, retorna False.
        '''
        return self.component.SetUnprotectedTextPart(part, text)

    def SingleFileDropped(self, filename: str) -> None:
        ''' Esta função emula a queda de um único arquivo com o caminho do diretório fileName.
        '''
        self.component.SingleFileDropped(filename)

    def CurrentColumn(self) -> int:
        ''' O número da coluna na qual o cursor de texto está atualmente posicionado.
        '''
        return self.component.CurrentColumn

    def CurrentLine(self) -> int:
        ''' O número da linha na qual o cursor de texto está atualmente posicionado.
        '''
        return self.component.CurrentLine

    def FirstVisibleLine(self, line_number: int = None) -> int:
        ''' A primeira linha visível é visualizada na borda superior do controle.
        '''
        if line_number is not None:
            self.component.FirstVisibleLine = line_number
        return self.component.FirstVisibleLine

    def LastVisibleLine(self) -> int:
        ''' O número da última linha que está atualmente visível.
        '''
        return self.component.LastVisibleLine

    def LineCount(self) -> int:
        ''' O número de todas as linhas no documento atual.
        '''
        return self.component.LineCount

    def NumberOfUnprotectedTextParts(self) -> int:
        ''' O número de partes de texto não protegidas, que estão contidas.
        '''
        return self.component.NumberOfUnprotectedTextParts

    def SelectedText(self) -> str:
        ''' O texto atualmente selecionado.
        '''
        return self.component.SelectedText

    def SelectionEndColumn(self) -> int:
        ''' O número da coluna na qual a seleção atual termina.
        '''
        return self.component.SelectionEndColumn

    def SelectionEndLine(self) -> int:
        ''' O número da linha na qual a seleção atual termina.
        '''
        return self.component.SelectionEndLine

    def SelectionIndexEnd(self) -> int:
        ''' Recupera o índice de caractere absoluto, baseado em zero, do ponto final da faixa de texto visualmente selecionada, ou seja, a posição onde a seleção termina.
        '''
        return self.component.SelectionIndexEnd

    def SelectionIndexStart(self) -> int:
        ''' Recupera o índice de caractere absoluto, baseado em zero, do ponto de partida da faixa de texto visualmente selecionada, ou seja, a posição onde a seleção começa.
        '''
        return self.component.SelectionIndexStart

    def SelectionStartColumn(self) -> int:
        ''' O número da coluna na qual a seleção atual começa.
        '''
        return self.component.SelectionStartColumn

    def SelectionStartLine(self) -> int:
        ''' O número da linha na qual a seleção atual começa.
        '''
        return self.component.SelectionStartLine

class SapGuiToolbarControl(SapGuiShell):
    # TODO Criar descrição
    
    def GetButtonChecked(self, button_pos: int) -> int:
        ''' Retorna se o botão na posição especificada está atualmente marcado (pressionado).
        '''
        return self.component.GetButtonChecked(button_pos)

    def GetButtonEnabled(self, button_pos: int) -> int:
        ''' Indica se o botão na posição especificada pode ser pressionado.
        '''
        return self.component.GetButtonEnabled(button_pos)

    def GetButtonIcon(self, button_pos: int) -> str:
        ''' Retorna o nome do ícone do botão de barra de ferramentas especificado.
        '''
        return self.component.GetButtonIcon(button_pos)

    def GetButtonId(self, button_pos: int) -> str:
        ''' Retorna o ID do botão de barra de ferramentas especificado.
        '''
        return self.component.GetButtonId(button_pos)

    def GetButtonText(self, button_pos: int) -> str:
        ''' Retorna o texto do botão de barra de ferramentas especificado.
        '''
        return self.component.GetButtonText(button_pos)

    def GetButtonTooltip(self, button_pos: int) -> str:
        ''' Retorna a dica de ferramenta do botão de barra de ferramentas especificado.
        '''
        return self.component.GetButtonTooltip(button_pos)

    def GetButtonType(self, button_pos: int) -> str:
        ''' Retorna o tipo do botão de barra de ferramentas especificado. Valores possíveis são: "Button", "ButtonAndMenu", "Menu", "Separator", "Group", "CheckBox".
        '''
        return self.component.GetButtonType(button_pos)

    def GetMenuItemIdFromPosition(self, pos: int) -> str:
        ''' Esta função retorna o identificador do item de menu com índice Position.
        '''
        return self.component.GetMenuItemIdFromPosition(pos)

    def PressButton(self, id: str) -> None:
        ''' Esta função emula o pressionamento do botão com o ID fornecido.
        '''
        self.component.PressButton(id)

    def PressContextButton(self, id: str) -> None:
        ''' Esta função emula o pressionamento do botão de contexto com o ID fornecido.
        '''
        self.component.PressContextButton(id)

    def SelectMenuItem(self, id: str) -> None:
        ''' Esta função emula a seleção do item de menu com o ID fornecido.
        '''
        self.component.SelectMenuItem(id)

    def SelectMenuItemByText(self, str_text: str) -> None:
        ''' Esta função emula a seleção do item de menu pelo texto do item de menu.
        '''
        self.component.SelectMenuItemByText(str_text)

    def ButtonCount(self) -> int:
        ''' O número de botões da barra de ferramentas, incluindo separadores.
        '''
        return self.component.ButtonCount

    def FocusedButton(self, focused_button_index: int = None) -> int:
        ''' O índice baseado em zero do botão que atualmente tem o foco.
        '''
        if focused_button_index is not None:
            self.component.FocusedButton = focused_button_index
        return self.component.FocusedButton

class SapGuiTree(SapGuiShell):
    ''' O Tree Control oferece suporte a três tipos de árvore.
    '''
    
    def ChangeCheckbox(self, node_key: str, item_name: str, checked: bool) -> None:
        ''' Emula a mudança de estado de uma caixa de seleção.
        '''
        self.component.ChangeCheckbox(node_key, item_name, checked)

    def ClickLink(self, node_key: str, item_name: str) -> None:
        ''' Emula a ativação de um link.
        '''
        self.component.ClickLink(node_key, item_name)

    def CollapseNode(self, node_key: str) -> None:
        ''' Fecha o nó com a chave de nó especificada.
        '''
        self.component.CollapseNode(node_key)

    def DefaultContextMenu(self) -> None:
        ''' Solicita um menu de contexto para todo o Controle de Árvore.
        '''
        self.component.DefaultContextMenu()

    def DoubleClickItem(self, node_key: str, item_name: str) -> None:
        ''' Emula o duplo clique em um item de texto.
        '''
        self.component.DoubleClickItem(node_key, item_name)

    def DoubleClickNode(self, node_key: str) -> None:
        ''' Emula o duplo clique em um nó.
        '''
        self.component.DoubleClickNode(node_key)

    def EnsureVisibleHorizontalItem(self, node_key: str, item_name: str) -> None:
        ''' Desloca a Árvore horizontalmente até que o item seja visível.
        '''
        self.component.EnsureVisibleHorizontalItem(node_key, item_name)

    def ExpandNode(self, node_key: str) -> None:
        ''' Expande o nó com a chave de nó especificada.
        '''
        self.component.ExpandNode(node_key)

    def FindNodeKeyByPath(self, path: str) -> str:
        ''' Encontra a chave de nó pelo seu caminho.
        '''
        return self.component.FindNodeKeyByPath(path)

    def GetAbapImage(self, key: str, name: str) -> str:
        ''' Recupera o código do ícone de uma imagem exibida no item especificado.
        '''
        return self.component.GetAbapImage(key, name)

    def GetAllNodeKeys(self):
        ''' Retorna uma coleção de todas as chaves de nó presentes no Controle de Árvore.
        '''
        return self.component.GetAllNodeKeys()

    def GetCheckBoxState(self, node_key: str, item_name: str) -> int:
        ''' Recupera o estado da caixa de seleção (1 = Marcado, 0 = Desmarcado).
        '''
        return self.component.GetCheckBoxState(node_key, item_name)

    def GetColumnCol(self, col_name: str):
        ''' Retorna as chaves de todos os itens na coluna especificada.
        '''
        return self.component.GetColumnCol(col_name)

    def GetColumnHeaders(self):
        ''' Retorna uma coleção de cabeçalhos de coluna.
        '''
        return self.component.GetColumnHeaders()

    def GetColumnIndexFromName(self, key: str) -> int:
        ''' Retorna o índice da coluna (começando em 1) da coluna especificada.
        '''
        return self.component.GetColumnIndexFromName(key)

    def GetColumnNames(self):
        ''' Retorna uma coleção de nomes de coluna.
        '''
        return self.component.GetColumnNames()

    def GetColumnTitleFromName(self, key: str) -> str:
        ''' Retorna o título da coluna especificada pelo parâmetro.
        '''
        return self.component.GetColumnTitleFromName(key)

    def GetColumnTitles(self):
        ''' Retorna uma coleção de títulos de coluna.
        '''
        return self.component.GetColumnTitles()

    def GetFocusedNodeKey(self) -> str:
        ''' Retorna a chave do nó que está com foco.
        '''
        return self.component.GetFocusedNodeKey()

    def GetHierarchyLevel(self, key: str) -> int:
        ''' Retorna o nível hierárquico da chave especificada, começando no nível 0.
        '''
        return self.component.GetHierarchyLevel(key)

    def GetHierarchyTitle(self) -> str:
        ''' Retorna o título hierárquico.
        '''
        return self.component.GetHierarchyTitle()

    def GetIsDisabled(self, node_key: str, item_name: str) -> int:
        ''' Retorna se o item especificado está desativado (1 = Desativado, 0 = Não desativado).
        '''
        return self.component.GetIsDisabled(node_key, item_name)

    def GetIsHighLighted(self, node_key: str, item_name: str) -> int:
        ''' Retorna se o item especificado está destacado (1 = Destacado, 0 = Não destacado).
        '''
        return self.component.GetIsHighLighted(node_key, item_name)

    def GetItemHeight(self, node_key: str, item_name: str) -> int:
        ''' Recupera a altura do item especificado em pixels.
        '''
        return self.component.GetItemHeight(node_key, item_name)

    def GetItemLeft(self, node_key: str, item_name: str) -> int:
        ''' Recupera a posição esquerda do item especificado em pixels.
        '''
        return self.component.GetItemLeft(node_key, item_name)

    def GetItemStyle(self, node_key: str, item_name: str) -> int:
        ''' Recupera o estilo do item especificado.
        '''
        return self.component.GetItemStyle(node_key, item_name)

    def GetItemText(self, key: str, name: str) -> str:
        ''' Retorna o texto do item especificado pelos parâmetros chave e nome.
        '''
        return self.component.GetItemText(key, name)

    def GetItemTextColor(self, key: str, name: str) -> int:
        ''' Recupera a cor da fonte do item especificado.
        '''
        return self.component.GetItemTextColor(key, name)

    def GetItemToolTip(self, key: str, name: str) -> str:
        ''' Recupera a dica do item especificado.
        '''
        return self.component.GetItemToolTip(key, name)

    def GetItemTop(self, node_key: str, item_name: str) -> int:
        ''' Recupera a posição superior do item especificado em pixels.
        '''
        return self.component.GetItemTop(node_key, item_name)

    def GetItemType(self, key: str, name: str) -> int:
        ''' Recupera o tipo de item da árvore de colunas:
        trvTreeStructureHierarchy = 0
        trvTreeStructureImage = 1
        trvTreeStructureText = 2
        trvTreeStructureBool = 3
        trvTreeStructureButton = 4
        trvTreeStructureLink = 5
        '''
        return self.component.GetItemType(key, name)

    def GetItemWidth(self, node_key: str, item_name: str) -> int:
        ''' Recupera a largura do item especificado em pixels.
        '''
        return self.component.GetItemWidth(node_key, item_name)

    def GetListTreeNodeItemCount(self, node_key: str) -> int:
        ''' Retorna o número de itens visíveis do nó especificado em uma árvore de lista.
        '''
        return self.component.GetListTreeNodeItemCount(node_key)

    def GetNextNodeKey(self, node_key: str) -> str:
        ''' Retorna a chave do próximo nó pertencente ao mesmo nó um nível acima.
        '''
        return self.component.GetNextNodeKey(node_key)

    def GetNodeAbapImage(self, key: str) -> str:
        ''' Recupera o código de ícone do nó especificado.
        '''
        return self.component.GetNodeAbapImage(key)

    def GetNodeChildrenCount(self, key: str) -> int:
        ''' Retorna o número de filhos diretos visíveis do nó especificado.
        '''
        return self.component.GetNodeChildrenCount(key)

    def GetNodeChildrenCountByPath(self, path: str) -> int:
        ''' Retorna o número de filhos visíveis do nó especificado pelo caminho.
        '''
        return self.component.GetNodeChildrenCountByPath(path)

    def GetNodeHeight(self, key: str) -> int:
        ''' Retorna a altura do nó especificado em pixels.
        '''
        return self.component.GetNodeHeight(key)

    def GetNodeIndex(self, key: str) -> int:
        ''' Retorna o índice da chave especificada dentro do seu nó.
        '''
        return self.component.GetNodeIndex(key)

    def GetNodeItemHeaders(self, node_key: str):
        ''' Retorna um objeto com os cabeçalhos de item do nó especificado.
        '''
        return self.component.GetNodeItemHeaders(node_key)

    def GetNodeKeyByPath(self, path: str) -> str:
        ''' Chave do nó especificado pelo caminho dado.
        '''
        return self.component.GetNodeKeyByPath(path)

    def GetNodeLeft(self, key: str) -> int:
        ''' Retorna a posição esquerda do nó especificado em pixels.
        '''
        return self.component.GetNodeLeft(key)

    def GetNodePathByKey(self, key: str) -> str:
        ''' Dado uma chave de nó, o caminho é recuperado (por exemplo, "2\1\2").
        '''
        return self.component.GetNodePathByKey(key)

    def GetNodesCol(self):
        ''' A coleção contém as chaves de todos os nós na árvore.
        '''
        return self.component.GetNodesCol()

    def GetNodeStyle(self, node_key: str) -> int:
        ''' Recupera o estilo do nó especificado.
        '''
        return self.component.GetNodeStyle(node_key)

    def GetNodeTextByKey(self, key: str) -> str:
        ''' Retorna o texto do nó especificado pela chave dada.
        '''
        return self.component.GetNodeTextByKey(key)

    def GetNodeTextByPath(self, path: str) -> str:
        ''' O texto de um nó definido pelo caminho dado é retornado.
        '''
        return self.component.GetNodeTextByPath(path)

    def GetNodeTextColor(self, key: str) -> int:
        ''' Retorna a cor da fonte do nó especificado.
        '''
        return self.component.GetNodeTextColor(key)

    def GetNodeToolTip(self, node_key: str) -> str:
        ''' Retorna a dica de ferramenta do nó especificado.
        '''
        return self.component.GetNodeToolTip(node_key)

    def GetNodeTop(self, key: str) -> int:
        ''' Retorna a posição superior do nó especificado em pixels.
        '''
        return self.component.GetNodeTop(key)

    def GetNodeWidth(self, key: str) -> int:
        ''' Retorna a largura do nó especificado em pixels.
        '''
        return self.component.GetNodeWidth(key)

    def GetParent(self, ckey: str) -> str:
        ''' Chave do nó pai do nó especificado pela chave dada.
        '''
        return self.component.GetParent(ckey)

    def GetPreviousNodeKey(self, node_key: str) -> str:
        ''' Retorna a chave do nó anterior pertencente ao mesmo nó um nível acima.
        '''
        return self.component.GetPreviousNodeKey(node_key)

    def GetSelectedNodes(self):
        ''' Retorna uma coleção de nós selecionados.
        '''
        return self.component.GetSelectedNodes()

    def GetSelectionMode(self) -> int:
        ''' Retorna o modo de seleção do Controle de Árvore:
        0: Seleção de Nó Único
        1: Seleção de Múltiplos Nós
        2: Seleção de Item Único
        3: Seleção de Múltiplos Itens
        '''
        return self.component.GetSelectionMode()

    def GetStyleDescription(self, n_style: int) -> str:
        ''' Retorna a descrição do estilo especificado.
        '''
        return self.component.GetStyleDescription(n_style)

    def GetSubNodesCol(self, path: str):
        ''' Retorna uma coleção de chaves de todos os subníveis do nó especificado pela chave dada.
        '''
        return self.component.GetSubNodesCol(path)

    def GetTreeType(self) -> int:
        ''' Retorna o tipo de árvore:
        0: Árvore Simples
        1: Árvore de Lista
        2: Árvore de Coluna
        '''
        return self.component.GetTreeType()

    def HeaderContextMenu(self, header_name: str) -> None:
        ''' Solicita um menu de contexto para um cabeçalho.
        '''
        self.component.HeaderContextMenu(header_name)

    def IsFolder(self, node_key: str) -> int:
        ''' Retorna True se o objeto especificado for um nó e não uma folha.
        '''
        return self.component.IsFolder(node_key)

    def IsFolderExpandable(self, node_key: str) -> int:
        ''' Retorna True se a pasta pertencente ao nó especificado pode ser expandida.
        '''
        return self.component.IsFolderExpandable(node_key)

    def IsFolderExpanded(self, node_key: str) -> int:
        ''' Retorna True se a pasta pertencente ao nó especificado estiver expandida.
        '''
        return self.component.IsFolderExpanded(node_key)

    def ItemContextMenu(self, node_key: str, item_name: str) -> None:
        ''' Solicita um menu de contexto para um item.
        '''
        self.component.ItemContextMenu(node_key, item_name)

    def NodeContextMenu(self, node_key: str) -> None:
        ''' Solicita um menu de contexto para um nó.
        '''
        self.component.NodeContextMenu(node_key)

    def PressButton(self, node_key: str, item_name: str) -> None:
        ''' Emula o pressionamento de um botão.
        '''
        self.component.PressButton(node_key, item_name)

    def PressHeader(self, header_name: str) -> None:
        ''' Emula o clique em um cabeçalho.
        '''
        self.component.PressHeader(header_name)

    def PressKey(self, key: str) -> None:
        ''' Emula o pressionamento de uma tecla.
        '''
        self.component.PressKey(key)

    def SelectColumn(self, column_name: str) -> None:
        ''' Adiciona uma coluna à seleção de colunas, removendo a seleção de nós ou itens.
        '''
        self.component.SelectColumn(column_name)

    def SelectedItemColumn(self) -> str:
        ''' Retorna o nome da coluna do item selecionado.
        '''
        return self.component.SelectedItemColumn()

    def SelectedItemNode(self) -> str:
        ''' Retorna a chave do nó do item selecionado.
        '''
        return self.component.SelectedItemNode()

    def SelectItem(self, node_key: str, item_name: str) -> None:
        ''' Emula a seleção de um item, removendo todas as outras seleções.
        '''
        self.component.SelectItem(node_key, item_name)

    def SelectNode(self, node_key: str) -> None:
        ''' Adiciona o nó com a chave especificada à seleção de nós.
        '''
        self.component.SelectNode(node_key)

    def SetCheckBoxState(self, node_key: str, item_name: str, state: int) -> None:
        ''' Marca ou desmarca a caixa de seleção na célula especificada do controle de árvore.
        Se o parâmetro "state" for igual a 0, a caixa de seleção é desmarcada; se o parâmetro for igual a 1, a caixa de seleção é marcada.
        '''
        self.component.SetCheckBoxState(node_key, item_name, state)

    def SetColumnWidth(self, column_name: str, width: int) -> None:
        ''' Define a largura de uma coluna em pixels.
        '''
        self.component.SetColumnWidth(column_name, width)

    def UnselectAll(self) -> None:
        ''' Remove todas as seleções.
        '''
        self.component.UnselectAll()

    def UnselectColumn(self, column_name: str) -> None:
        ''' Remove uma coluna da seleção de colunas.
        '''
        self.component.UnselectColumn(column_name)

    def UnselectNode(self, node_key: str) -> None:
        ''' Remove o nó com a chave especificada da seleção de nós.
        '''
        self.component.UnselectNode(node_key)

    def ColumnOrder(self, column_order: object = None) -> object:
        ''' A propriedade ColumnOrder é usada para trabalhar com a sequência de colunas.
            O nome de cada coluna na árvore de colunas deve ocorrer exatamente uma vez.
        '''
        if column_order is not None:
            self.component.ColumnOrder = column_order
        return self.component.ColumnOrder

    def HierarchyHeaderWidth(self, width: int = None) -> int:
        ''' A largura do Hierarchy Header em pixels.
        '''
        if width is not None:
            self.component.HierarchyHeaderWidth = width
        return self.component.HierarchyHeaderWidth

    def SelectedNode(self, node_key: str = None) -> str:
        ''' Esta propriedade representa a chave do nó atualmente selecionado.
            A seleção de um nó remove outras seleções (ou seja, seleção de coluna e seleção de item).
        '''
        if node_key is not None:
            self.component.SelectedNode = node_key
        return self.component.SelectedNode

    def TopNode(self, top_node_key: str = None) -> str:
        ''' Esta propriedade influencia a rolagem vertical do controle de árvore.
            TopNode contém a chave do nó que está localizado na borda superior do controle de árvore.
            A definição de um nó x como nó superior só é possível se houver nós visíveis suficientes abaixo de x para preencher a área de exibição do controle de árvore.
        '''
        if top_node_key is not None:
            self.component.TopNode = top_node_key
        return self.component.TopNode

class SapGuiChart(SapGuiShell):
    ''' O objeto GuiChart é de natureza muito técnica. Deve ser utilizado apenas para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    '''
    
    def ValueChange(self, series: int, point: int, x_value: str, y_value: str, data_change: bool, id: str, z_value: str, change_flag: int):
        '''
        Série: Número do conjunto de dados dentro da linha que deve ser alterado.
        point: Número do ponto de dados na linha que deve ser alterado.
        x_value: Novo valor de x.
        y_value: Novo valor de y.
        data_change: Definir este parâmetro como True significa que o valor não foi alterado interativamente no gráfico,
            mas sim inserindo o novo valor na página de propriedades do DataPoint.
        id: ID do contêiner de dados GFW do ponto alterado. Pode ser usado em vez do par série/ponto.
        z_value: Novo valor z.
        ChangeFlag: Notifica qual valor foi alterado ou se foi um valor de tempo.
            O valor é definido como uma matriz de bits, usando os 5 bits inferiores.
            1 x
            2 y
            4 x é o valor do tempo
            8 y é o valor do tempo
            16 z
            Se o novo valor for um momento específico, ele deverá ser definido usando uma string no formato mm/dd/aaaa hh:mm:ss.
        '''
        self.component.ValueChange(series, point, x_value, y_value, data_change, id, z_value, change_flag)

class SapGuiSapChart(SapGuiShell):
    # TODO Verificar classe
    pass

class SapGuiComboBoxControl(SapGuiShell):
    #TODO Criar uma descrição
    
    def FireSelected(self) -> None:
        ''' Envia evento "selecionado".
        '''
        self.component.FireSelected()
    
    def Entries(self) -> SapGuiCollection:
        ''' As entradas são novamente uma GuiCollection com: key(index=0), text(index=1) o texto de cada entrada que você pode obter por meio desta coleção.
        '''
        return self.component.Entries
    
    def LabelText(self) -> str:
        ''' Texto da etiqueta.
        '''
        return self.component.LabelText
    
    def Selected(self, select: str = None) -> str:
        ''' A chave da entrada atualmente selecionada da caixa de combinação.
        '''
        if select is not None: self.component.Selected = select
        return self.component.Selected
    
    def Text(self) -> str:
        ''' Texto atual da caixa de combinação.
        '''
        return self.component.Text

class SapGuiGridView(SapGuiShell):
    ''' A visualização em grade é semelhante ao controle de tabela dynpro, mas significativamente mais poderosa. '''
    
    def ClearSelection(self) -> None:
        ''' Chamar ClearSelection remove todas as seleções de linhas, colunas e células. '''
        self.component.ClearSelection()
    
    def Click(self, row: int, column: str) -> None:
        ''' Esta função emula um clique do mouse em uma determinada célula se os parâmetros forem válidos e gera uma exceção caso contrário. '''
        self.component.Click(row, column)
    
    def ClickCurrentCell(self) -> None:
        ''' Esta função emula um clique do mouse na célula atual. '''
        self.component.ClickCurrentCell()
    
    def ContextMenu(self) -> None:
        ''' Chamar ContextMenu emula a solicitação do menu de contexto. '''
        self.component.ContextMenu()
    
    def CurrentCellMoved(self) -> None:
        ''' Esta função notifica o servidor de que uma célula diferente se tornou a célula atual.
        Deve ser chamado sempre que a célula atual for alterada.
        '''
        self.component.CurrentCellMoved()
    
    def DeleteRows(self, rows: str) -> None:
        ''' As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices,por exemplo “3,5-8,14,15”.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        '''
        # TODO Funções auxiliares
        self.component.DeleteRows(rows)
    
    def DeselectColumn(self, column: str) -> None:
        ''' Esta função remove a coluna especificada da coleção de colunas selecionadas. '''
        self.component.DeselectColumn(column)
    
    def DoubleClick(self, row: int, column: str) -> None:
        ''' Esta função emula um clique duplo do mouse em uma determinada célula se os parâmetros forem válidos e gera uma exceção caso contrário. '''
        self.component.DoubleClick(row, column)
    
    def DoubleClickCurrentCell(self) -> None:
        ''' Esta função emula um clique duplo do mouse na célula atual. '''
        self.component.DoubleClickCurrentCell()
    
    def DuplicateRows(self, rows: str) -> None:
        ''' As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        Para qualquer índice único, uma cópia da linha será inserida no índice fornecido.
        Se um intervalo de índices for duplicado, todas as novas linhas serão inseridas como um bloco, antes das linhas antigas.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        '''
        # TODO Funções auxiliares
        self.component.DuplicateRows(rows)
    
    def GetCellChangeable(self, row: int, column: str) -> bool:
        ''' Esta função retorna True se a célula especificada puder ser alterada. '''
        self.component.GetCellChangeable(row, column)
    
    def GetCellCheckBoxChecked(self, row: int, column: str) -> bool:
        ''' Retorna True se a caixa de seleção na posição especificada estiver marcada.
        Lança uma exceção se não houver caixa de seleção na célula especificada. '''
        self.component.GetCellCheckBoxChecked(row, column)
    
    def GetCellColor(self, row: int, column: str) -> int:
        ''' Retorna um identificador para a cor da célula.
        Isso pode ser usado para recuperar as informações de cores usando GetColorInfo.
        '''
        self.component.GetCellColor(row, column)
    
    def GetCellHeight(self, row: int, column: str) -> int:
        ''' Retorna a altura da célula em pixels. '''
        self.component.GetCellHeight(row, column)
    
    def GetCellIcon(self, row: int, column: str) -> str:
        ''' Retorna a sequência de ícones da célula, se a célula contiver um ícone.
        A string tem o formato de ícone ABAP '@xy@', onde xy é um número ou caractere.
        '''
        self.component.GetCellIcon(row, column)
    
    def GetCellLeft(self, row: int, column: str) -> int:
        ''' Retorna a posição esquerda da célula nas coordenadas do cliente. '''
        self.component.GetCellLeft(row, column)
    
    def GetCellMaxLength(self, row: int, column: str) -> int:
        ''' Retorna o comprimento máximo da célula em número de bytes. '''
        self.component.GetCellMaxLength(row, column)
    
    def GetCellState(self, row: int, column: str) -> str:
        ''' Retorna o estado da célula. Os valores possíveis são:
        Normal
        Error
        Warning
        Info
        '''
        self.component.GetCellState(row, column)
    
    def GetCellTooltip(self, row: int, column: str) -> str:
        ''' Retorna a dica de ferramenta da célula.
        '''
        self.component.GetCellTooltip(row, column)
    
    def GetCellTop(self, row: int, column: str) -> int:
        ''' Retorna a posição superior da célula nas coordenadas do cliente. '''
        self.component.GetCellTop(row, column)
    
    def GetCellType(self, row: int, column: str) -> str:
        ''' Esta função retorna o tipo da célula especificada. Os valores possíveis são:
        Normal
        Button
        Checkbox
        ValueList
        RadioButton
        '''
        self.component.GetCellType(row, column)
    
    def GetCellValue(self, row: int, column: str) -> str:
        ''' Retorna o valor da célula como uma string.
        '''
        self.component.GetCellValue(row, column)
    
    def GetCellWidth(self, row: int, column: str) -> int:
        ''' Retorna a largura da célula em pixels. '''
        self.component.GetCellWidth(row, column)
    
    def GetColorInfo(self, color: int) -> str:
        ''' Retorna a descrição da cor da célula.
        '''
        self.component.GetColorInfo(color)
    
    def GetColumnDataType(self, column: str) -> str:
        ''' Retorna o tipo de dados da coluna de acordo com os 'tipos de dados integrados' do padrão de esquema XML.
        '''
        self.component.GetColumnDataType(column)
    
    def GetColumnPosition(self, column: str) -> int:
        ''' Retorna a posição da coluna conforme mostrado na tela, começando em 1.
        '''
        self.component.GetColumnPosition(column)
    
    def GetColumnSortType(self, column: str) -> str:
        ''' Retorna o tipo de classificação da coluna. Os valores possíveis são:
        None
        Ascending
        Descending
        '''
        self.component.GetColumnSortType(column)
    
    def GetColumnTitles(self, column: str) -> object:
        ''' Esta função retorna uma coleção de strings que são usadas para exibir o título de uma coluna.
        O controle escolhe o título apropriado de acordo com a largura da coluna.
        '''
        # TODO Verificar retorno
        self.component.GetColumnTitles(column)
    
    def GetColumnTooltip(self, column: str) -> str:
        ''' A dica de ferramenta de uma coluna contém um texto projetado para ajudar o usuário a compreender o significado da coluna.
        '''
        self.component.GetColumnTooltip(column)
    
    def GetColumnTotalType(self, column: str) -> str:
        ''' Retorna o tipo total da coluna. Os valores possíveis são:
        None
        Total
        Subtotal
        '''
        self.component.GetColumnTotalType(column)
    
    def GetDisplayedColumnTitle(self, column: str) -> str:
        ''' Esta função retorna o título da coluna exibida atualmente.
        Este texto é um dos valores da coleção retornada da função "getColumnTitles".
        '''
        self.component.GetDisplayedColumnTitle(column)
    
    def GetRowTotalLevel(self, row: int) -> int:
        ''' Retorna o nível da linha.
        '''
        self.component.GetRowTotalLevel(row)
    
    def GetSymbolInfo(self, symbol: str) -> str:
        ''' Retorna a descrição do símbolo na célula.
        '''
        self.component.GetSymbolInfo(symbol)
    
    def GetToolbarButtonChecked(self, button_pos: int) -> bool:
        ''' Retorna True se o botão estiver marcado (pressionado).
        '''
        self.component.GetToolbarButtonChecked(button_pos)
    
    def GetToolbarButtonEnabled(self, button_pos: int) -> bool:
        ''' Indica se o botão pode ser pressionado.
        '''
        self.component.GetToolbarButtonEnabled(button_pos)
    
    def GetToolbarButtonIcon(self, button_pos: int) -> str:
        ''' Retorna o nome do ícone do botão da barra de ferramentas especificado.
        '''
        self.component.GetToolbarButtonIcon(button_pos)
        
    def GetToolbarButtonId(self, button_pos: int) -> str:
        ''' Retorna o ID do botão da barra de ferramentas especificado, conforme definido no dicionário de dados ABAP.
        '''
        self.component.GetToolbarButtonId(button_pos)

    def GetToolbarButtonText(self, button_pos: int) -> str:
        ''' Retorna o texto do botão da barra de ferramentas especificado.
        '''
        self.component.GetToolbarButtonText(button_pos)

    def GetToolbarButtonTooltip(self, button_pos: int) -> str:
        ''' Retorna a dica de ferramentas do botão da barra de ferramentas especificado.
        '''
        self.component.GetToolbarButtonTooltip(button_pos)

    def GetToolbarButtonType(self, button_pos: int) -> str:
        ''' Retorna o tipo do botão da barra de ferramentas especificado. Os valores possíveis são:
        Button
        ButtonAndMenu
        Menu
        Separator
        Group
        CheckBox
        '''
        self.component.GetToolbarButtonType(button_pos)

    def GetToolbarFocusButton(self) -> int:
        ''' Retorna a posição do botão da barra de ferramentas que tem o foco. Se nenhum botão na barra de ferramentas tiver o foco, o método retorna -1.
        '''
        self.component.GetToolbarFocusButton()

    def HasCellF4Help(self, row: int, column: str) -> bool:
        ''' Retorna True se a célula tiver um valor de ajuda.
        '''
        self.component.HasCellF4Help(row, column)

    def HistoryCurEntry(self, row: int, column: str) -> str:
        ''' Retorna o texto da entrada selecionada atualmente da lista de histórico na célula especificada.
        '''
        self.component.HistoryCurEntry(row, column)

    def HistoryCurIndex(self, row: int, column: str) -> int:
        ''' Retorna o índice (base zero) da entrada selecionada atualmente na lista de histórico da célula especificada.
        '''
        self.component.HistoryCurIndex(row, column)

    def HistoryIsActive(self, row: int, column: str) -> bool:
        ''' Este método retorna True se a lista de histórico de entrada estiver aberta para a célula especificada.
        '''
        self.component.HistoryIsActive(row, column)

    def HistoryList(self, row: int, column: str) -> SapGuiCollection:
        ''' Este método recupera a lista de entradas de histórico de entrada da célula GuiGridView especificada como uma GuiCollection.
        Os valores da lista de histórico dependem do valor atual contido na célula.
        '''
        self.component.HistoryList(row, column)

    def InsertRows(self, rows: str) -> None:
        ''' As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        Para qualquer índice único, uma nova linha será adicionada no índice fornecido, movendo a linha antiga uma linha para baixo.
        Se um intervalo de índices for inserido, todas as novas linhas serão inseridas como um bloco, antes das linhas antigas.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        '''
        # TODO Funções auxiliares
        self.component.InsertRows(rows)

    def IsCellHotspot(self, row: int, column: str) -> bool:
        ''' Retorna True se a célula for um link.
        '''
        self.component.IsCellHotspot(row, column)

    def IsCellSymbol(self, row: int, column: str) -> bool:
        ''' Retorna True se o texto na célula for exibido na fonte de símbolo SAP.
        '''
        self.component.IsCellSymbol(row, column)

    def IsCellTotalExpander(self, row: int, column: str) -> bool:
        ''' Retorna True se a célula contiver um botão de expansão total.
        '''
        self.component.IsCellTotalExpander(row, column)

    def IsColumnFiltered(self, column: str) -> bool:
        ''' Retorna True se um filtro foi aplicado à coluna.
        '''
        self.component.IsColumnFiltered(column)

    def IsColumnKey(self, column: str) -> bool:
        ''' Retorna True se a coluna estiver marcada como uma coluna de chave.
        '''
        self.component.IsColumnKey(column)

    def IsTotalRowExpanded(self, row: int) -> bool:
        ''' Retorna True se a linha que contém um botão de expansão estiver atualmente expandida.
        '''
        self.component.IsTotalRowExpanded(row)

    def ModifyCell(self, row: int, column: str, value: str) -> None:
        ''' Se a linha e a coluna identificarem uma célula editável válida e o valor tiver um tipo válido para essa célula,
        o valor da célula será alterado. Caso contrário, uma exceção será gerada.
        '''
        self.component.ModifyCell(row, column, value)

    def ModifyCheckBox(self, row: int, column: str, checked: bool) -> None:
        ''' Se a linha e a coluna identificarem uma célula editável válida contendo uma caixa de seleção e o valor tiver um tipo válido para essa célula,
        o valor da célula será alterado. Caso contrário, uma exceção será gerada.
        '''
        self.component.ModifyCheckBox(row, column, checked)

    def MoveRows(self, from_row: int, to_row: int, dest_row: int) -> None:
        ''' As linhas com um índice maior ou igual a from_row até um índice menor ou igual a to_row são movidas para a posição de dest_row.
        Passar valores de índice inválidos como parâmetros gera uma exceção.
        '''
        self.component.MoveRows(from_row, to_row, dest_row)

    def PressButton(self, row: int, column: str) -> None:
        ''' Esta função emula o pressionamento de um botão colocado em uma célula específica.
        Ela gera uma exceção se a célula não contiver um botão ou se nem mesmo existir.
        '''
        self.component.PressButton(row, column)

    def PressButtonCurrentCell(self) -> None:
        ''' Esta função emula o pressionamento de um botão colocado na célula atual.
        Ela gera uma exceção se a célula não contiver um botão.
        '''
        self.component.PressButtonCurrentCell()

    def PressColumnHeader(self, column: str) -> None:
        ''' Esta função emula um clique do mouse no cabeçalho da coluna se o parâmetro identificar uma coluna válida.
        Caso contrário, gera uma exceção.
        '''
        self.component.PressColumnHeader(column)

    def PressEnter(self) -> None:
        ''' Esta função emula a pressão da tecla Enter.
        '''
        self.component.PressEnter()

    def PressF1(self) -> None:
        ''' Esta função emula a pressão da tecla F1 enquanto o foco está na visualização da grade.
        '''
        self.component.PressF1()

    def PressF4(self) -> None:
        ''' Esta função emula a pressão da tecla F4.
        '''
        self.component.PressF4()

    def PressToolbarButton(self, button_id: str) -> None:
        ''' Esta função emula o clique em um botão na barra de ferramentas da visualização da grade.
        '''
        self.component.PressToolbarButton(button_id)

    def PressToolbarContextButton(self, button_id: str) -> None:
        ''' Esta função emula a abertura do menu de contexto na barra de ferramentas da visualização da grade.
        '''
        self.component.PressToolbarContextButton(button_id)

    def PressTotalRow(self, row: int, column: str) -> None:
        ''' Esta função emula a pressão do botão da linha total, que expande ou condensa as linhas agrupadas.
        '''
        self.component.PressTotalRow(row, column)

    def PressTotalRowCurrentCell(self) -> None:
        ''' Esta função difere de PressTotalRow apenas no fato de tentar pressionar o botão de expansão na célula atual.
        '''
        self.component.PressTotalRowCurrentCell()

    def SelectAll(self) -> None:
        ''' Esta função seleciona todo o conteúdo da grade (ou seja, todas as linhas e todas as colunas).
        '''
        self.component.SelectAll()

    def SelectColumn(self, column: str) -> None:
        ''' Esta função adiciona a coluna especificada à coleção das colunas selecionadas.
        '''
        self.component.SelectColumn(column)

    def SelectionChanged(self) -> None:
        ''' Esta função notifica o servidor que a seleção foi alterada.
        '''
        self.component.SelectionChanged()

    def SelectToolbarMenuItem(self, item_id: str) -> None:
        ''' Esta função emula a seleção de um item no menu de contexto da barra de ferramentas da visualização da grade.
        '''
        self.component.SelectToolbarMenuItem(item_id)

    def SetColumnWidth(self, column: str, width: int) -> None:
        ''' Esta função define a largura de uma coluna em caracteres.
        '''
        self.component.SetColumnWidth(column, width)

    def SetCurrentCell(self, row: int, column: str) -> None:
        ''' Se a linha e a coluna identificarem uma célula válida, essa célula se tornará a célula atual.
        '''
        self.component.SetCurrentCell(row, column)

    def TriggerModified(self) -> None:
        ''' Notifica o servidor sobre várias alterações nas células.
        '''
        self.component.TriggerModified()

    def ColumnCount(self) -> int:
        ''' Esta propriedade representa o número de colunas no controle.
        '''
        return self.component.ColumnCount

    def ColumnOrder(self, order: object = None) -> object:
        ''' Esta coleção contém todos os identificadores de coluna na ordem em que estão atualmente exibidos.
        '''
        # TODO Verificar retorno
        if order is not None: self.component.ColumnOrder = order
        return self.component.ColumnOrder

    def CurrentCellColumn(self, column: str = None) -> str:
        ''' A string que identifica uma coluna é o nome do campo definido no dicionário de dados do SAP.
        '''
        if column is not None: self.component.CurrentCellColumn = column
        return self.component.CurrentCellColumn

    def CurrentCellRow(self, row: int = None) -> int:
        ''' O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        '''
        if row is not None: self.component.CurrentCellRow = row
        return self.component.CurrentCellRow

    def FirstVisibleColumn(self, column: str = None) -> str:
        ''' Esta propriedade representa a primeira coluna visível da área de rolagem da visualização da grade.
        '''
        if column is not None: self.component.FirstVisibleColumn = column
        return self.component.FirstVisibleColumn

    def FirstVisibleRow(self, row: int = None) -> int:
        ''' Este é o índice da primeira linha visível na grade.
        '''
        if row is not None: self.component.FirstVisibleRow = row
        return self.component.FirstVisibleRow

    def FrozenColumnCount(self) -> int:
        ''' Esta propriedade representa o número de colunas excluídas da rolagem horizontal.
        '''
        return self.component.FrozenColumnCount

    def RowCount(self) -> int:
        ''' Esta propriedade representa o número de linhas no controle.
        '''
        return self.component.RowCount

    def SelectedCells(self, cells: object = None) -> object:
        ''' A coleção de células selecionadas contém strings no formato "<índice da linha>,<identificador da coluna>", como "0,CARRID".
        '''
        # TODO Verificar retorno
        if cells is not None: self.component.SelectedCells = cells
        return self.component.SelectedCells

    def SelectedColumns(self, columns: object = None) -> object:
        ''' As colunas selecionadas estão disponíveis como uma coleção de strings, assim como a string CurrentCellColumn.
        '''
        # TODO Verificar retorno
        if columns is not None:
            self.component.SelectedColumns = columns
        return self.component.SelectedColumns

    def SelectedRows(self, rows: str = None) -> str:
        ''' A string é uma lista separada por vírgulas de números de índice de linha ou intervalos de índice, como "1,2,4-8,10".
        '''
        if rows is not None:
            self.component.SelectedRows = rows
        return self.component.SelectedRows

    def SelectionMode(self) -> str:
        ''' Retorna o modo de seleção atual da grade.
        '''
        return self.component.SelectionMode

    def Title(self) -> str:
        ''' Esta propriedade representa o título do controle da grade.
        '''
        return self.component.Title

    def ToolbarButtonCount(self) -> int:
        ''' O número de botões da barra de ferramentas, incluindo separadores.
        '''
        return self.component.ToolbarButtonCount

    def VisibleRowCount(self) -> int:
        ''' Recupera o número de linhas visíveis da grade.
        '''
        return self.component.VisibleRowCount

class SapGuiContainerShell(SapGuiShell):
    ''' Um GuiContainerShell é um wrapper para um conjunto de objetos GuiShell.
    GuiContainerShell estende o objeto GuiVContainer.
    O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    '''
    
    def DockerIsVertical(self) -> bool:
        ''' Será TRUE se o contêiner for um controle de janela de encaixe vertical.
        '''
        return self.component.DockerIsVertical
    
    def DockerPixelSize(self) -> int:
        ''' Retorna o tamanho do controle do Docker em pixels.
        '''
        return self.component.DockerPixelSize

class SapGuiTab(SapGuiVContainer):
    ''' Os objetos GuiTab são filhos de um objeto GuiTabStrip.
    O prefixo do tipo é tabp, o nome é o id do botão da aba retirado do dicionário de dados SAP.
    '''
    
    def ScrollToLeft(self) -> None:
        #TODO explicar melhor
        ''' ScrollToLeft desloca as guias para que uma determinada guia se torne a leftTab da faixa de guias.
        '''
        self.component.ScrollToLeft()
    
    def Select(self) -> None:
        ''' Esta função define a guia como a guia selecionada na faixa de guias.
        Alterar a guia selecionada de uma faixa de guias pode causar comunicação com o servidor.
        '''
        self.component.Select()

class SapGuiTabStrip(SapGuiVContainer):
    ''' Uma faixa de guias é um contêiner cujos filhos são do tipo GuiTab.
    O prefixo do tipo é tabulações, o nome é o nome do campo retirado do dicionário de dados SAP.
    Os filhos da faixa de guias são as guias. Embora todas as guias estejam disponíveis a qualquer momento, apenas os filhos da guia selecionada
    existem na hierarquia de objetos para faixas de guias controladas pelo servidor.
    '''
    
    def CharHeight(self) -> int:
        ''' Altura do GuiTabStrip em métrica de caracteres.
        '''
        return self.component.CharHeight
    
    def CharLeft(self) -> int:
        ''' Coordenada esquerda do GuiTabStrip na métrica de caracteres.
        '''
        return self.component.CharLeft
    
    def CharTop(self) -> int:
        ''' Coordenada superior do GuiTabStrip na métrica de caracteres.
        '''
        return self.component.CharTop
    
    def CharWidth(self) -> int:
        ''' Largura do GuiTabStrip na métrica de caracteres.
        '''
        return self.component.CharWidth
    
    def LeftTab(self) -> int:
        ''' Esta é a guia mais à esquerda cuja legenda está visível.
        A propriedade leftTab pode ser alterada chamando o método ScrollToLeft de um GuiTab diferente,
        conforme descrito na seção Objeto GuiTab.
        '''
        return self.component.LeftTab
    
    def SelectedTab(self) -> int:
        ''' A aba selecionada é aquela cujos descendentes estão visualizados no momento.
        A aba selecionada possui exatamente um filho, que é um GuiScrollContainer. Para selecionar uma guia, você chama o método 
        Select da respectiva página da guia. Veja também a seção Objeto GuiTab.
        '''
        return self.component.SelectedTab

class SapGuiScrollContainer(SapGuiVContainer):
    ''' Este contêiner representa subtelas roláveis. Uma subtela pode ser rolável sem realmente ter uma barra de rolagem,
    porque a existência de uma barra de rolagem depende da quantidade de dados exibidos e do tamanho da GuiUserArea.
    O prefixo do tipo é ssub, o nome é gerado a partir das configurações do dicionário de dados.
    '''
    
    def HorizontalScrollbar(self) -> SapGuiScrollbar:
        ''' A barra de rolagem horizontal do contêiner de rolagem.
        '''
        return SapGuiScrollbar(self.component.HorizontalScrollbar)
    
    def VerticalScrollbar(self) -> SapGuiScrollbar:
        ''' A barra de rolagem vertical do contêiner de rolagem.
        '''
        return SapGuiScrollbar(self.component.VerticalScrollbar)

class SapGuiFrameWindow(SapGuiVContainer):
    ''' Um GuiFrameWindow é um objeto visual de alto nível na hierarquia de tempo de execução.
    Pode ser a janela principal ou uma janela pop-up modal. Consulte as seções GuiMainWindow e GuiModalWindow para obter exemplos.
    O próprio GuiFrameWindow é uma interface abstrata. GuiFrameWindow estende o objeto GuiVContainer. O prefixo do tipo é wnd, o nome
    é wnd mais o número da janela entre colchetes.
    '''
    #TODO:
    
    def Close(self) -> None:
        ''' A função tenta fechar a janela. Tentar fechar a última janela principal de uma sessão não terá sucesso imediato
        a caixa de diálogo 'Você realmente deseja fazer logoff?' será exibida primeiro.
        '''
        # TODO: Colocar um parâmetro para ignorar a caixa de diálogo ao fecha a última janela
        self.component.Close()
    
    def CompBitmap(self, filename_1: str, filename_2: str) -> int:
        ''' Este método compara dois arquivos bitmap pixel por pixel.
        Tipo de retorno:
        O método retorna um dos seguintes valores:
        0: Os arquivos não diferem
        1: Os arquivos diferem em tamanho
        2: Os arquivos possuem conteúdo diferente
        3: Houve um erro
        '''
        return self.component.CompBitmap(filename_1, filename_2)
    
    def HardCopy(self, filename: str, image_type: int = 0, x_pos: int = None, y_pos: int = None, n_width: int = None, n_height: int = None) -> str:
        ''' Esta função despeja uma cópia impressa da janela como um arquivo bitmap no disco.
        O parâmetro é o nome do arquivo.
        Se a função for bem-sucedida, o valor de retorno será o caminho totalmente qualificado do arquivo.
        Se nenhuma informação de caminho for fornecida, o arquivo será gravado na pasta de documentos SAP GUI.
        Se os parâmetros opcionais xPos, yPos, nWidth e nHeight forem definidos, apenas o retângulo especificado da janela principal será capturado.
        image_type:
        0: BMP
        1: JPG
        2: PNG
        3: GIF
        4: TIFF
        '''
        return self.component.HardCopy(filename, image_type, x_pos, y_pos, n_width, n_height)
    
    def HardCopyToMemory(self, image_type: int = 0):
        # TODO Verificar retorno no python
        ''' Esta função retorna uma cópia impressa da janela como uma matriz segura de bytes.
        image_type:
        0: BMP
        1: JPG
        2: PNG
        3: GIF
        4: TIFF
        '''
        return self.component.HardCopyToMemory(image_type)
    
    def IsVKeyAllowed(self, v_key: int) -> bool:
        ''' Esta função retorna True se a chave virtual VKey estiver disponível no momento.
        As VKeys são definidas no pintor de menus.
        '''
        return self.component.IsVKeyAllowed(v_key)
    
    def Iconify(self) -> None:
        ''' Isso definirá uma janela para o estado iconificado.
        Não é possível iconificar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão iconificados.
        '''
        self.component.Iconify()
    
    def Minimize(self) -> None:
        ''' Isso definirá uma janela para o estado iconificado.
        Não é possível iconificar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão iconificados.
        '''
        self.Iconify()
    
    def Maximize(self) -> None:
        ''' Isso maximizará uma janela. Não é possível maximizar uma janela modal,
        é sempre a janela principal que será maximizada.
        '''
        self.component.Maximize()
    
    def Restore(self) -> None:
        ''' Isso restaurará uma janela de seu estado iconificado. 
        ão é possível restaurar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão restaurados.
        '''
        self.component.Restore()
    
    def SendVKey(self, v_key: int) -> None:
        ''' A chave virtual VKey é executada na janela. As VKeys são definidas no pintor de menus.
        '''
        return self.component.SendVKey(v_key)
    
    def ShowMessageBox(self, title: str, text: str, msg_icon: int, msg_type: int) -> int:
        ''' Mostra uma caixa de mensagem.
        O valor de retorno será uma das constantes GuiMessageBoxResult.
        title: Título da caixa de mensagem
        text: Texto da caixa de mensagem.
        msg_icon: MsgIcon define o ícone a ser usado para a caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxType.
        msg_type: MsgType define os botões disponíveis na caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxOption.
        '''
        return self.component.ShowMessageBox(title, text, msg_icon, msg_type)
    
    def JumpBackward(self) -> None:
        ''' Executa a tecla Ctrl+Shift+Tab na janela para retroceder um bloco.
        '''
        self.component.JumpBackward()
    
    def JumpForward(self) -> None:
        ''' Execute a tecla Ctrl+Tab na janela para avançar um bloco.
        '''
        self.component.JumpForward()
    
    def TabBackward(self) -> None:
        ''' Execute a tecla Shift+Tab na janela para retroceder um elemento.
        '''
        self.component.TabBackward()
    
    def TabForward(self) -> None:
        ''' Execute a tecla Tab na janela para avançar um elemento.
        '''
        self.component.TabForward()

    def ElementVisualizationMode(self, option: bool = None) -> bool:
        ''' Quando elementVisualizationMode está habilitado, um teste de acerto pode ser executado no
        SAP GUI movendo o cursor sobre a janela. O evento hit da sessão é disparado quando um componente é encontrado na posição do mouse.
        '''
        if option is not None: self.component.ElementVisualizationMode = option
        return self.component.ElementVisualizationMode
    
    def GuiFocus(self) -> SapGuiVComponent:
        # TODO
        ''' O SystemFocus suporta apenas elementos dynpro.
        Para receber informações sobre o controle ActiveX atualmente em foco você pode acessar a propriedade GuiFocus.
        '''
        return SapTypeInstance.GetInstance(self.component.GuiFocus)
    
    def Handle(self) -> int:
        ''' O identificador de janela do controle que está conectado ao GuiShell.
        Este é o identificador da janela subjacente no Microsoft Windows.
        '''
        return self.component.Handle
    
    def Iconic(self) -> bool:
        ''' Esta propriedade é True se a janela estiver iconificada.
        É possível executar comandos de script em uma janela iconificada, mas pode haver resultados indefinidos,
        especialmente quando controles estão envolvidos, pois estes podem ter configurações de tamanho inválidas.
        '''
        return self.component.Iconic
    
    def SystemFocus(self) -> SapGuiVComponent:
        # TODO
        ''' O SystemFocus especifica o componente que o sistema SAP está atualmente vendo como sendo focado.
        Este valor é válido apenas para elementos dynpro e pode, portanto, diferir do foco visto no frontend.
        '''
        return SapTypeInstance.GetInstance(self.component.SystemFocus)
    
    def WorkingPaneHeight(self) -> int:
        ''' Esta é a altura do painel de trabalho na métrica de caracteres.
        '''
        return self.component.WorkingPaneHeight
    
    def WorkingPaneWidth(self) -> int:
        ''' Esta é a largura do painel de trabalho na métrica de caracteres.
        O painel de trabalho é a área entre as barras de ferramentas na parte superior da janela e a barra de status na parte inferior da janela.
        '''
        return self.component.WorkingPaneWidth

class SapGuiModalWindow(SapGuiFrameWindow):
    ''' Uma GuiModalWindow é uma caixa de diálogo pop-up.
    '''
    
    def IsPopupDialog(self) -> bool:
        ''' Algumas janelas modais representam caixas de diálogo pop-up.
        Neste caso a propriedade IsPopupDialog é True.
        As caixas de diálogo pop-up são identificadas verificando o nome da fonte ABAP e o número do dynpro.
        '''
        return self.component.IsPopupDialog
    
    def PopupDialogText(self) -> str:
        ''' O texto dos campos de entrada da caixa de diálogo pop-up em formato concatenado.
        '''
        return self.component.PopupDialogText

class SapGuiTableControl(SapGuiVContainer):
    ''' O controle table é um elemento dynpro padrão, em contraste com o GuiCtrlGridView, que é semelhante.
    O prefixo do tipo é tbl, o nome é o nome do campo retirado do dicionário de dados SAP.
    '''
    #TODO  Funções adicionais
    
    def ConfigureLayout(self) -> SapGuiModalWindow:
        ''' Na caixa de diálogo de configuração o layout da tabela pode ser alterado. Esta caixa de diálogo é uma GuiModalWindow.
        '''
        return self.component.ConfigureLayout()
    
    def DeselectAllColumns(self) -> None:
        ''' Esta função pode ser usada para controles de tabela com um botão que permite desmarcar todas as colunas em uma única etapa.
        '''
        return self.component.DeselectAllColumns()
    
    def GetAbsoluteRow(self, index: int) -> SapGuiTableRow:
        ''' Ao contrário da coleção de linhas, a indexação suportada por esta função não redefine o índice após a rolagem,
        mas conta as linhas começando pela primeira linha em relação à primeira posição de rolagem.
        Se a linha selecionada não estiver visível no momento, uma exceção será gerada.
        '''
        return self.component.GetAbsoluteRow()
    
    def GetCell(self, row: int, column: int) -> SapGuiVComponent:
        ''' Este método retorna uma determinada célula da tabela.
        É mais eficiente do que acessar uma única célula usando coleções de linhas ou colunas.
        '''
        return self.component.GetCell(row, column)
    
    def ReorderTable(self, permutation: str) -> None:
        ''' A permutação de parâmetros descreve uma nova ordem das colunas.
        Por exemplo "1 3 2" moverá a coluna 3 para a segunda posição.
        '''
        # TODO Melhorar a função usando o nome das colunas
        return self.component.ReorderTable(permutation)
    
    def SelectAllColumns(self) -> None:
        ''' Esta função pode ser usada para controles de tabela com um botão que permite selecionar todas as colunas em uma única etapa.
        '''
        return self.component.SelectAllColumns()
    
    def CharHeight(self) -> int:
        ''' Altura do GuiTableControl na métrica de caracteres.
        '''
        return self.component.CharHeight
    
    def CharLeft(self) -> int:
        ''' Coordenada esquerda do GuiTableControl na métrica de caracteres.
        '''
        return self.component.CharLeft
    
    def CharTop(self) -> int:
        ''' Coordenada superior do GuiTableControl na métrica de caracteres.
        '''
        return self.component.CharTop
    
    def CharWidth(self) -> int:
        ''' Largura do GuiTableControl na métrica de caracteres.
        '''
        return self.component.CharWidth
    
    def ColSelectMode(self) -> int:
        ''' Existem três modos diferentes para selecionar colunas ou linhas, que são definidos no tipo de enumeração GuiTableSelectionType.
        '''
        return self.component.ColSelectMode
    
    def Columns(self) -> SapGuiCollection:
        ''' Os membros desta coleção são do tipo GuiTableColumn.
        Portanto, eles não suportam propriedades como id ou nome.
        '''
        return self.component.Columns
    
    def CurrentCol(self) -> int:
        ''' Índice baseado em zero da coluna atual.
        '''
        return self.component.CurrentCol
    
    def CurrentRow(self) -> int:
        ''' Índice baseado em zero da linha atual.
        '''
        return self.component.CurrentRow
    
    def HorizontalScrollbar(self) -> SapGuiScrollbar:
        ''' A barra de rolagem horizontal do controle de tabela.
        '''
        return self.component.HorizontalScrollbar
    
    def RowCount(self) -> int:
        ''' Número de linhas na tabela. Isso inclui linhas invisíveis. Para o número de linhas visíveis está disponível a propriedade VisibleRowCount.
        '''
        return self.component.RowCount
    
    def Rows(self) -> SapGuiCollection:
        ''' Os membros desta coleção são do tipo GuiTableRow.
        A indexação começa com 0 para a primeira linha visível, independente da posição atual da barra de rolagem horizontal.
        Após a rolagem, uma linha diferente terá o índice 0.
        '''
        return self.component.Rows
    
    def RowSelectMode(self) -> int:
        ''' Existem três modos diferentes para selecionar colunas ou linhas,
        que são definidos no tipo de enumeração GuiTableSelectionType.
        '''
        return self.component.RowSelectMode
    
    def TableFieldName(self) -> str:
        ''' A propriedade name do controle de tabela contém o nome do programa ABAP além do nome do campo simples.
        Esta propriedade contém apenas o nome do campo.
        '''
        return self.component.TableFieldName
    
    def VerticalScrollbar(self) -> SapGuiScrollbar:
        ''' A barra de rolagem vertical do controle de tabela.
        '''
        return self.component.VerticalScrollbar
    
    def VisibleRowCount(self) -> int:
        ''' Número de linhas visíveis na tabela. Para o número de todas as linhas a propriedade RowCount está disponível.
        '''
        return self.component.VisibleRowCount

class SapGuiSessionInfo():
    ''' GuiSessionInfo é membro de todos os objetos GuiSession.
    Disponibiliza informações técnicas sobre a sessão. Algumas de suas propriedades são exibidas na
    área de informações do sistema (na barra de status ou na área de título dependendo do tema SAP GUI utilizado).
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
    
    def ApplicationServer(self) -> str:
        ''' O nome do servidor de aplicação é definido somente se a sessão pertencer a uma conexão que
        foi iniciada sem balanceamento de carga, especificando um servidor de aplicação.
        '''
        return self.component.ApplicationServer
    
    def Client(self) -> str:
        ''' O cliente selecionado na tela de login.
        '''
        return self.component.Client
    
    def Codepage(self) -> int:
        ''' A página de códigos especificada no SAP Logon nas propriedades da conexão.
        '''
        return self.component.Codepage
    
    def Flushes(self) -> int:
        ''' A propriedade Flushes conta o número de liberações na fila de automação durante a comunicação do servidor.
        '''
        return self.component.Flushes
    
    def Group(self) -> str:
        ''' As informações do grupo de login estarão disponíveis somente se a sessão
        pertencer a uma conexão que foi iniciada usando balanceamento de carga.
        '''
        return self.component.Group
    
    def GuiCodepage(self) -> int:
        ''' Uma lista de codepages está disponível na tabela TCP00A do sistema SAP.
        Em um cliente executando Microsoft Windows com página de código 1252 (Latin I), a propriedade guiCodepage é 1160.
        '''
        return self.component.GuiCodepage
    
    def I18NMode(self) -> bool:
        ''' O modo I18N do SAP GUI é necessário para conjuntos de caracteres multibyte.
        '''
        return self.component.I18NMode
    
    def InterpretationTime(self) -> int:
        ''' O tempo de interpretação começa após a chegada dos dados do servidor.
        Compreende a análise dos dados e distribuição para os elementos SAP GUI. A unidade é milissegundos.
        '''
        return self.component.InterpretationTime
    
    def IsLowSpeedConnection(self) -> bool:
        ''' A propriedade é True se a conexão à qual pertence a sessão roda com flag de conexão de baixa velocidade.
        Esse sinalizador pode ser definido na página de propriedades de conexão avançadas da caixa de diálogo SAPLogon.
        O suporte ao SAP GUI Scripting é muito limitado para conexões de baixa velocidade, porque as informações necessárias
        para identificar objetos SAP GUI não estão sendo enviadas.
        '''
        return self.component.IsLowSpeedConnection
    
    def Language(self) -> str:
        ''' O idioma especificado na tela de login.
        '''
        return self.component.Language
    
    def MessageServer(self) -> str:
        ''' As informações do servidor de mensagens estarão disponíveis somente se a
        sessão pertencer a uma conexão que foi iniciada usando balanceamento de carga.
        '''
        return self.component.MessageServer
    
    def Program(self) -> str:
        ''' O nome do programa de origem que está sendo executado no momento.
        '''
        return self.component.Program
    
    def ResponseTime(self) -> int:
        ''' Este é o tempo gasto na comunicação da rede desde o momento em que os dados são
        enviados ao servidor até o momento em que chega a resposta do servidor. A unidade é milissegundos.
        '''
        return self.component.ResponseTime
    
    def RoundTrips(self) -> int:
        ''' Antes do SAP GUI enviar dados ao servidor, ele bloqueia a interface do usuário.
        Em muitos casos, ele não desbloqueará a interface quando os dados chegarem do servidor,
        mas enviará uma nova solicitação ao servidor imediatamente. Os controles, em particular,
        usam essa tecnologia para carregar os dados necessários para visualização.
        A contagem dessas alternâncias de token entre o SAP GUI e o servidor é a propriedade roundTrips.
        '''
        return self.component.RoundTrips
    
    def ScreenNumber(self) -> int:
        ''' O número da tela exibida atualmente.
        '''
        return self.component.ScreenNumber
    
    def ScriptingModeReadOnly(self) -> bool:
        ''' O modo somente leitura pode ser ativado usando um parâmetro de perfil do servidor de aplicativos.
        Neste modo o estado das aplicações SAP não pode ser alterado através da API de Scripting, o que significa:
        * As propriedades só podem ser lidas, mas não definidas
        * As funções só podem ser chamadas se não alterarem o estado do controle.
        Observações:
        Neste modo, os scripts podem ser gravados e as informações sobre o aplicativo podem ser lidas no SAP GUI,
        no entanto, uma transação não pode ser executada a partir de um script.
        '''
        return self.component.ScriptingModeReadOnly
    
    def ScriptingModeRecordingDisabled(self) -> bool:
        ''' O modo de gravação desabilitada pode ser habilitado usando um parâmetro de perfil do servidor de aplicativos.
        Neste modo, o SAP GUI Scripting não dispara nenhum evento. Isso implica que a interação do usuário não pode ser registrada.
        No entanto, os dados podem ser lidos no SAP GUI e os scripts podem ser usados para executar transações.
        '''
        return self.component.ScriptingModeRecordingDisabled
    
    def SessionNumber(self) -> int:
        ''' O número da sessão também é exibido no SAP GUI na barra de status.
        '''
        return self.component.SessionNumber
    
    def SystemName(self) -> str:
        ''' Este é o nome do sistema SAP.
        '''
        return self.component.SystemName
    
    def SystemNumber(self) -> int:
        ''' O número do sistema é definido somente se a sessão pertencer a uma
        conexão que foi iniciada sem balanceamento de carga, especificando um servidor de aplicação.
        '''
        return self.component.SystemNumber
    
    def SystemSessionId(self) -> str:
        ''' Todas as sessões SAP GUI da mesma conexão são representadas no servidor com o mesmo SystemSessionId.
        Usando SystemSessionId e SessionNumber, é possível encontrar uma sessão SAP GUI correspondente a partir de um aplicativo ABAP.
        '''
        return self.component.SystemSessionId
    
    def Transaction(self) -> str:
        ''' A transação que está sendo executada atualmente.
        '''
        return self.component.Transaction
    
    def UI_GUIDELINE(self) -> str:
        ''' Esta propriedade pode ser utilizada para identificar se a sessão SAP GUI está rodando com Fiori Visual Theme (Belize) ou não.
        O valor de retorno é
        1 se a sessão estiver sendo executada sem Fiori Visual Theme (Belize)
        2 se a sessão estiver rodando com Fiori Visual Theme (Belize)
        '''
        return self.component.UI_GUIDELINE
    
    def User(self) -> str:
        ''' O nome SAP do usuário conectado ao sistema.
        '''
        return self.component.User

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
