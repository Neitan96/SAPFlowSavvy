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

Priority:
	- GuiCTextField
	- GuiCustomControl
	- GuiInputFieldControl
	- GuiLabel
	- GuiPasswordField
	- GuiRadioButton
	- GuiTextedit
	- GuiTextField
	- GuiToolbarControl
	- GuiTree

* Objects:
	- GuiAbapEditor - N/a
	- GuiApoGrid
	- GuiBarChart
	- GuiCalendar
	- GuiColorSelector
	- GuiDialogShell
	- GuiEAIViewer2D
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
	- GuiSimpleContainer
	- GuiSplit
	- GuiSplitterContainer
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
