from __future__ import annotations

import time
from typing import Optional
import win32com.client

from .StdTCodes import SapFields, SapCommands


class GuiComponentType:
    GuiUnknown = -1  # Desconhecido: Um componente cujo tipo não é reconhecido ou não está definido.
    GuiComponent = 0  # Componente: O componente base que pode representar qualquer elemento na interface do SAP GUI.
    GuiVComponent = 1  # VComponent: Um tipo específico de componente visual.
    GuiVContainer = 2  # VContainer: Um tipo específico de contêiner visual.
    GuiApplication = 10  # Aplicação: Representa a aplicação SAP GUI em si, permitindo interagir com todo o ambiente SAP.
    GuiConnection = 11  # Conexão: Representa uma conexão com um servidor SAP, permitindo a seleção de diferentes sessões.
    GuiSession = 12  # Sessão: Representa uma sessão de comunicação com um servidor SAP.
    GuiFrameWindow = 20  # Janela de Quadro: Uma janela de quadro que pode conter outros elementos, como caixas de diálogo.
    GuiMainWindow = 21  # Janela Principal: A janela principal da aplicação SAP GUI, que contém a maioria dos elementos da interface.
    GuiModalWindow = 22  # Janela Modal: Uma janela que bloqueia a interação com outras partes da interface até ser fechada.
    GuiMessageWindow = 23  # Janela de Mensagem: Uma janela que exibe mensagens e notificações do sistema SAP.
    GuiLabel = 30  # Rótulo: Um rótulo de texto usado para exibir informações ou etiquetar outros componentes.
    GuiTextField = 31  # Campo de Texto: Um campo de entrada de texto para entrada de dados.
    GuiCTextField = 32  # Campo de Texto Curto: Um campo de entrada de texto para entrada de dados breve.
    GuiPasswordField = 33  # Campo de Senha: Um campo de entrada de senha usado para entrada segura de senhas.
    GuiComboBox = 34  # Caixa de Combinação: Uma caixa de texto com uma lista suspensa de opções que o usuário pode selecionar.
    GuiOkCodeField = 35  # Campo de Código OK: Um campo de entrada de código que pode ser usado para inserir comandos específicos.
    GuiButton = 40  # Botão: Um botão clicável que normalmente dispara ações ou comandos quando pressionado.
    GuiRadioButton = 41  # Botão de Opção: Uma opção que pode ser selecionada entre várias opções mutuamente exclusivas.
    GuiCheckBox = 42  # Caixa de Seleção: Uma caixa que pode ser marcada ou desmarcada para indicar uma escolha ou opção.
    GuiStatusPane = 43  # Painel de Status: Um painel dentro da barra de status que pode exibir informações adicionais.
    GuiCustomControl = 50  # Controle Personalizado: Um componente personalizado criado para atender a requisitos específicos.
    GuiContainerShell = 51  # Shell de Contêiner: Um shell que contém componentes em uma hierarquia de árvore.
    GuiBox = 62  # Caixa: Uma caixa de diálogo ou janela usada para exibir informações ou solicitar entrada do usuário.
    GuiContainer = 70  # Contêiner: Um elemento que pode conter outros componentes, como um grupo de botões ou campos.
    GuiSimpleContainer = 71  # Contêiner Simples: Um contêiner simples que contém outros componentes.
    GuiScrollContainer = 72  # Contêiner de Rolagem: Um contêiner que suporta rolagem de conteúdo.
    GuiListContainer = 73  # Contêiner de Lista: Um contêiner que exibe uma lista de itens, como uma lista de seleção.
    GuiUserArea = 74  # Área do Usuário: Uma área que pode conter componentes personalizados ou elementos específicos do usuário.
    GuiSplitterContainer = 75  # Contêiner de Divisão: Um contêiner que suporta divisão de áreas com barras divisórias.
    GuiTableControl = 80  # Controle de Tabela: Um controle que exibe dados tabulares em linhas e colunas.
    GuiTableColumn = 81  # Coluna de Tabela: Uma coluna em uma tabela que contém dados tabulares.
    GuiTableRow = 82  # Linha de Tabela: Uma linha em uma tabela que contém dados tabulares.
    GuiTabStrip = 90  # Tira de Guia: Uma tira de guias que permite alternar entre várias guias.
    GuiTab = 91  # Guia: Uma guia que permite alternar entre diferentes conjuntos de conteúdo.
    GuiScrollbar = 100  # Barra de Rolagem: Uma barra que permite rolar o conteúdo de uma área maior.
    GuiToolbar = 101  # Barra de Ferramentas: Uma barra que contém botões de ação e comandos frequentemente usados.
    GuiTitlebar = 102  # Barra de Título: A barra superior de uma janela que exibe o título e os botões de controle.
    GuiStatusbar = 103  # Barra de Status: Uma barra na parte inferior da interface que exibe informações de status.
    GuiMenu = 110  # Menu: Um menu suspenso que fornece acesso a várias opções e comandos.
    GuiMenubar = 111  # Barra de Menu: A barra de menu superior que contém menus e comandos.
    GuiCollection = 120  # Coleção: Representa uma coleção de elementos ou objetos SAP GUI, permitindo operações em massa.
    GuiSessionInfo = 121  # Informações de Sessão: Fornece informações sobre a sessão SAP atual.
    GuiShell = 122  # Shell: Uma janela de nível superior que pode conter outros componentes.
    GuiGOSShell = 123  # Shell de SOS: Um shell usado para exibir mensagens do sistema SAP e mensagens de erro.
    GuiSplitterShell = 124  # Shell de Divisão: Um shell que suporta divisão de áreas com barras divisórias.
    GuiDialogShell = 125  # Shell de Diálogo: Uma janela de diálogo que normalmente exibe informações detalhadas ou solicitações ao usuário.
    GuiDockShell = 126  # Shell de Ancoragem: Um shell de ancoragem usado para ancorar janelas em áreas específicas da interface.
    GuiContextMenu = 127  # Menu de Contexto: Um menu contextual que oferece opções específicas do contexto para um componente.
    GuiComponentCollection = 128  # Coleção de Componentes: Uma coleção de componentes SAP GUI, útil para gerenciar vários elementos.
    GuiVHViewSwitch = 129  # VHViewSwitch: Um tipo de interruptor de exibição usado em componentes visuais.


class GuiMessageBoxResult:
    MSG_RESULT_CANCEL = 0 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'Cancelar' é pressionado. (0)
    MSG_RESULT_OK = 1 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'OK' é pressionado. (1)
    MSG_RESULT_YES = 2 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'Sim' é pressionado. (2)
    MSG_RESULT_NO = 3 # Valor constante a ser usado como um valor de retorno pelo método showMessageBox. Esse valor é retornado quando o botão 'Não' é pressionado. (3)


class GuiMessageBoxOption:
    MSG_OPTION_OK = 0 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá apenas um botão 'OK'. (0)
    MSG_OPTION_YESNO = 1 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um botão 'Sim' e um botão 'Não'. (1)
    MSG_OPTION_OKCANCEL = 2 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um botão 'OK' e um botão 'Cancelar'. (2)


class GuiMessageBoxType:
    MSG_TYPE_INFORMATION = 0 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá a letra 'i' como ícone da caixa de mensagem. (0)
    MSG_TYPE_QUESTION = 1 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um ponto de interrogação como ícone da caixa de mensagem. (1)
    MSG_TYPE_WARNING = 2 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um ponto de exclamação como ícone da caixa de mensagem. (2)
    MSG_TYPE_ERROR = 3 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor exibirá um sinal de pare como ícone da caixa de mensagem. (3)
    MSG_TYPE_PLAIN = 4 # Valor constante a ser usado ao chamar o método showMessageBox. Usar este valor não exibirá nenhum ícone na caixa de mensagem. (4)


class GuiScrollbarType:
    GuiScrollbarTypeUnknown = 0
    GuiScrollbarTypeVertical = 1
    GuiScrollbarTypeHorizontal = 2


class GuiTableSelectionType:
    MULTIPLE_INTERVAL_SELECTION = 2 # Várias colunas/linhas podem ser selecionadas. (2)
    NO_SELECTION = 0 # Nenhuma seleção é possível. (0)
    SINGLE_SELECTION = 1 # Uma coluna/linha pode ser selecionada. (1)


class GuiEventType:
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


class GuiErrorType:
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


class GuiImageType:
    BMP = 0
    GIF = 2
    JPEG = 1
    PNG = 2


class GuiMagicDispIDs:
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


class SapKeys:

    ENTER = 0
    F1 = 1
    F2 = 2
    F3 = 3
    F4 = 4
    F5 = 5
    F6 = 6
    F7 = 7
    F8 = 8
    F9 = 9
    F10 = 10
    CTRL_S = 11
    F12 = 12
    SHIFT_F1 = 13
    SHIFT_F2 = 14
    SHIFT_F3 = 15
    SHIFT_F4 = 16
    SHIFT_F5 = 17
    SHIFT_F6 = 18
    SHIFT_F7 = 19
    SHIFT_F8 = 20
    SHIFT_F9 = 21
    SHIFT_CTRL_0 = 22
    SHIFT_F11 = 23
    SHIFT_F12 = 24
    CTRL_F1 = 25
    CTRL_F2 = 26
    CTRL_F3 = 27
    CTRL_F4 = 28
    CTRL_F5 = 29
    CTRL_F6 = 30
    CTRL_F7 = 31
    CTRL_F8 = 32
    CTRL_F9 = 33
    CTRL_F10 = 34
    CTRL_F11 = 35
    CTRL_F12 = 36
    CTRL_SHIFT_F1 = 37
    CTRL_SHIFT_F2 = 38
    CTRL_SHIFT_F3 = 39
    CTRL_SHIFT_F4 = 40
    CTRL_SHIFT_F5 = 41
    CTRL_SHIFT_F6 = 42
    CTRL_SHIFT_F7 = 43
    CTRL_SHIFT_F8 = 44
    CTRL_SHIFT_F9 = 45
    CTRL_SHIFT_F10 = 46
    CTRL_SHIFT_F11 = 47
    CTRL_SHIFT_F12 = 48
    CTRL_E = 70
    CTRL_F = 71
    CTRL_BAR = 72
    CTRL_BACKSLASH = 73
    CTRL_N = 74
    CTRL_O = 75
    CTRL_X = 76
    CTRL_C = 77
    CTRL_V = 78
    CTRL_Z = 79
    CTRL_PAGEUP = 80
    PAGEUP = 81
    PAGEDOWN = 82
    CTRL_PAGEDOWN = 83
    CTRL_G = 84
    CTRL_R = 85
    CTRL_P = 86


class SapKeySender:

    frame_window: GuiFrameWindow

    def __init__(self, frame_window: GuiFrameWindow):
        self.frame_window = frame_window

    def enter(self): self.frame_window.send_v_key(SapKeys.ENTER)
    def f1(self): self.frame_window.send_v_key(SapKeys.F1)
    def f2(self): self.frame_window.send_v_key(SapKeys.F2)
    def f3(self): self.frame_window.send_v_key(SapKeys.F3)
    def f4(self): self.frame_window.send_v_key(SapKeys.F4)
    def f5(self): self.frame_window.send_v_key(SapKeys.F5)
    def f6(self): self.frame_window.send_v_key(SapKeys.F6)
    def f7(self): self.frame_window.send_v_key(SapKeys.F7)
    def f8(self): self.frame_window.send_v_key(SapKeys.F8)
    def f9(self): self.frame_window.send_v_key(SapKeys.F9)
    def f10(self): self.frame_window.send_v_key(SapKeys.F10)
    def ctrl_s(self): self.frame_window.send_v_key(SapKeys.CTRL_S)
    def f12(self): self.frame_window.send_v_key(SapKeys.F12)
    def shift_f1(self): self.frame_window.send_v_key(SapKeys.SHIFT_F1)
    def shift_f2(self): self.frame_window.send_v_key(SapKeys.SHIFT_F2)
    def shift_f3(self): self.frame_window.send_v_key(SapKeys.SHIFT_F3)
    def shift_f4(self): self.frame_window.send_v_key(SapKeys.SHIFT_F4)
    def shift_f5(self): self.frame_window.send_v_key(SapKeys.SHIFT_F5)
    def shift_f6(self): self.frame_window.send_v_key(SapKeys.SHIFT_F6)
    def shift_f7(self): self.frame_window.send_v_key(SapKeys.SHIFT_F7)
    def shift_f8(self): self.frame_window.send_v_key(SapKeys.SHIFT_F8)
    def shift_f9(self): self.frame_window.send_v_key(SapKeys.SHIFT_F9)
    def shift_ctrl_0(self): self.frame_window.send_v_key(SapKeys.SHIFT_CTRL_0)
    def shift_f11(self): self.frame_window.send_v_key(SapKeys.SHIFT_F11)
    def shift_f12(self): self.frame_window.send_v_key(SapKeys.SHIFT_F12)
    def ctrl_f1(self): self.frame_window.send_v_key(SapKeys.CTRL_F1)
    def ctrl_f2(self): self.frame_window.send_v_key(SapKeys.CTRL_F2)
    def ctrl_f3(self): self.frame_window.send_v_key(SapKeys.CTRL_F3)
    def ctrl_f4(self): self.frame_window.send_v_key(SapKeys.CTRL_F4)
    def ctrl_f5(self): self.frame_window.send_v_key(SapKeys.CTRL_F5)
    def ctrl_f6(self): self.frame_window.send_v_key(SapKeys.CTRL_F6)
    def ctrl_f7(self): self.frame_window.send_v_key(SapKeys.CTRL_F7)
    def ctrl_f8(self): self.frame_window.send_v_key(SapKeys.CTRL_F8)
    def ctrl_f9(self): self.frame_window.send_v_key(SapKeys.CTRL_F9)
    def ctrl_f10(self): self.frame_window.send_v_key(SapKeys.CTRL_F10)
    def ctrl_f11(self): self.frame_window.send_v_key(SapKeys.CTRL_F11)
    def ctrl_f12(self): self.frame_window.send_v_key(SapKeys.CTRL_F12)
    def ctrl_shift_f1(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F1)
    def ctrl_shift_f2(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F2)
    def ctrl_shift_f3(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F3)
    def ctrl_shift_f4(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F4)
    def ctrl_shift_f5(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F5)
    def ctrl_shift_f6(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F6)
    def ctrl_shift_f7(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F7)
    def ctrl_shift_f8(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F8)
    def ctrl_shift_f9(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F9)
    def ctrl_shift_f10(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F10)
    def ctrl_shift_f11(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F11)
    def ctrl_shift_f12(self): self.frame_window.send_v_key(SapKeys.CTRL_SHIFT_F12)
    def ctrl_e(self): self.frame_window.send_v_key(SapKeys.CTRL_E)
    def ctrl_f(self): self.frame_window.send_v_key(SapKeys.CTRL_F)
    def ctrl_bar(self): self.frame_window.send_v_key(SapKeys.CTRL_BAR)
    def ctrl_backslash(self): self.frame_window.send_v_key(SapKeys.CTRL_BACKSLASH)
    def ctrl_n(self): self.frame_window.send_v_key(SapKeys.CTRL_N)
    def ctrl_o(self): self.frame_window.send_v_key(SapKeys.CTRL_O)
    def ctrl_x(self): self.frame_window.send_v_key(SapKeys.CTRL_X)
    def ctrl_c(self): self.frame_window.send_v_key(SapKeys.CTRL_C)
    def ctrl_v(self): self.frame_window.send_v_key(SapKeys.CTRL_V)
    def ctrl_z(self): self.frame_window.send_v_key(SapKeys.CTRL_Z)
    def ctrl_pageup(self): self.frame_window.send_v_key(SapKeys.CTRL_PAGEUP)
    def pageup(self): self.frame_window.send_v_key(SapKeys.PAGEUP)
    def pagedown(self): self.frame_window.send_v_key(SapKeys.PAGEDOWN)
    def ctrl_pagedown(self): self.frame_window.send_v_key(SapKeys.CTRL_PAGEDOWN)
    def ctrl_g(self): self.frame_window.send_v_key(SapKeys.CTRL_G)
    def ctrl_r(self): self.frame_window.send_v_key(SapKeys.CTRL_R)
    def ctrl_p(self): self.frame_window.send_v_key(SapKeys.CTRL_P)


# noinspection PyPep8Naming
class ComponentCast:

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch) -> None:
        self.component = component

    def GuiComponent(self) -> GuiComponent | None:
        if self.component is None: return None
        return GuiComponent(self.component)

    def GuiScrollbar(self) -> GuiScrollbar | None:
        if self.component is None: return None
        return GuiScrollbar(self.component)

    def GuiComponentCollection(self) -> GuiComponentCollection | None:
        if self.component is None: return None
        return GuiComponentCollection(self.component)

    def GuiTableColumn(self) -> GuiTableColumn | None:
        if self.component is None: return None
        return GuiTableColumn(self.component)

    def GuiTableRow(self) -> GuiTableRow | None:
        if self.component is None: return None
        return GuiTableRow(self.component)

    def GuiContainer(self) -> GuiContainer | None:
        if self.component is None: return None
        return GuiContainer(self.component)

    def GuiUtils(self) -> GuiUtils | None:
        if self.component is None: return None
        return GuiUtils(self.component)

    def GuiCollection(self) -> GuiCollection | None:
        if self.component is None: return None
        return GuiCollection(self.component)

    def GuiVComponent(self) -> GuiVComponent | None:
        if self.component is None: return None
        return GuiVComponent(self.component)

    def GuiVHViewSwitch(self) -> GuiVHViewSwitch | None:
        if self.component is None: return None
        return GuiVHViewSwitch(self.component)

    def GuiOkCodeField(self) -> GuiOkCodeField | None:
        if self.component is None: return None
        return GuiOkCodeField(self.component)

    def GuiMessageWindow(self) -> GuiMessageWindow | None:
        if self.component is None: return None
        return GuiMessageWindow(self.component)

    def GuiLabel(self) -> GuiLabel | None:
        if self.component is None: return None
        return GuiLabel(self.component)

    def GuiRadioButton(self) -> GuiRadioButton | None:
        if self.component is None: return None
        return GuiRadioButton(self.component)

    def GuiTextField(self) -> GuiTextField | None:
        if self.component is None: return None
        return GuiTextField(self.component)

    def GuiCTextField(self) -> GuiCTextField | None:
        if self.component is None: return None
        return GuiCTextField(self.component)

    def GuiPasswordField(self) -> GuiPasswordField | None:
        if self.component is None: return None
        return GuiPasswordField(self.component)

    def GuiStatusbar(self) -> GuiStatusbar | None:
        if self.component is None: return None
        return GuiStatusbar(self.component)

    def GuiStatusPane(self) -> GuiStatusPane | None:
        if self.component is None: return None
        return GuiStatusPane(self.component)

    def GuiComboBoxEntry(self) -> GuiComboBoxEntry | None:
        if self.component is None: return None
        return GuiComboBoxEntry(self.component)

    def GuiComboBox(self) -> GuiComboBox | None:
        if self.component is None: return None
        return GuiComboBox(self.component)

    def GuiCheckBox(self) -> GuiCheckBox | None:
        if self.component is None: return None
        return GuiCheckBox(self.component)

    def GuiButton(self) -> GuiButton | None:
        if self.component is None: return None
        return GuiButton(self.component)

    def GuiBox(self) -> GuiBox | None:
        if self.component is None: return None
        return GuiBox(self.component)

    def GuiMenu(self) -> GuiMenu | None:
        if self.component is None: return None
        return GuiMenu(self.component)

    def GuiContextMenu(self) -> GuiContextMenu | None:
        if self.component is None: return None
        return GuiContextMenu(self.component)

    def GuiVContainer(self) -> GuiVContainer | None:
        if self.component is None: return None
        return GuiVContainer(self.component)

    def GuiMenubar(self) -> GuiMenubar | None:
        if self.component is None: return None
        return GuiMenubar(self.component)

    def GuiGOSShell(self) -> GuiGOSShell | None:
        if self.component is None: return None
        return GuiGOSShell(self.component)

    def GuiDialogShell(self) -> GuiDialogShell | None:
        if self.component is None: return None
        return GuiDialogShell(self.component)

    def GuiSimpleContainer(self) -> GuiSimpleContainer | None:
        if self.component is None: return None
        return GuiSimpleContainer(self.component)

    def GuiCustomControl(self) -> GuiCustomControl | None:
        if self.component is None: return None
        return GuiCustomControl(self.component)

    def GuiToolbar(self) -> GuiToolbar | None:
        if self.component is None: return None
        return GuiToolbar(self.component)

    def GuiTitlebar(self) -> GuiTitlebar | None:
        if self.component is None: return None
        return GuiTitlebar(self.component)

    def GuiUserArea(self) -> GuiUserArea | None:
        if self.component is None: return None
        return GuiUserArea(self.component)

    def GuiShell(self) -> GuiShell | None:
        if self.component is None: return None
        return GuiShell(self.component)

    def GuiStage(self) -> GuiStage | None:
        if self.component is None: return None
        return GuiStage(self.component)

    def GuiPicture(self) -> GuiPicture | None:
        if self.component is None: return None
        return GuiPicture(self.component)

    def GuiOfficeIntegration(self) -> GuiOfficeIntegration | None:
        if self.component is None: return None
        return GuiOfficeIntegration(self.component)

    def GuiNetChart(self) -> GuiNetChart | None:
        if self.component is None: return None
        return GuiNetChart(self.component)

    def GuiMap(self) -> GuiMap | None:
        if self.component is None: return None
        return GuiMap(self.component)

    def GuiHTMLViewer(self) -> GuiHTMLViewer | None:
        if self.component is None: return None
        return GuiHTMLViewer(self.component)

    def GuiGraphAdapt(self) -> GuiGraphAdapt | None:
        if self.component is None: return None
        return GuiGraphAdapt(self.component)

    def GuiEAIViewer3D(self) -> GuiEAIViewer3D | None:
        if self.component is None: return None
        return GuiEAIViewer3D(self.component)

    def GuiEAIViewer2D(self) -> GuiEAIViewer2D | None:
        if self.component is None: return None
        return GuiEAIViewer2D(self.component)

    def GuiColorSelector(self) -> GuiColorSelector | None:
        if self.component is None: return None
        return GuiColorSelector(self.component)

    def GuiCalendar(self) -> GuiCalendar | None:
        if self.component is None: return None
        return GuiCalendar(self.component)

    def GuiBarChart(self) -> GuiBarChart | None:
        if self.component is None: return None
        return GuiBarChart(self.component)

    def GuiApoGrid(self) -> GuiApoGrid | None:
        if self.component is None: return None
        return GuiApoGrid(self.component)

    def GuiAbapEditor(self) -> GuiAbapEditor | None:
        if self.component is None: return None
        return GuiAbapEditor(self.component)

    def GuiSplitterContainer(self) -> GuiSplitterContainer | None:
        if self.component is None: return None
        return GuiSplitterContainer(self.component)

    def GuiSplit(self) -> GuiSplit | None:
        if self.component is None: return None
        return GuiSplit(self.component)

    def GuiInputFieldControl(self) -> GuiInputFieldControl | None:
        if self.component is None: return None
        return GuiInputFieldControl(self.component)

    def GuiTextedit(self) -> GuiTextedit | None:
        if self.component is None: return None
        return GuiTextedit(self.component)

    def GuiToolbarControl(self) -> GuiToolbarControl | None:
        if self.component is None: return None
        return GuiToolbarControl(self.component)

    def GuiTree(self) -> GuiTree | None:
        if self.component is None: return None
        return GuiTree(self.component)

    def GuiChart(self) -> GuiChart | None:
        if self.component is None: return None
        return GuiChart(self.component)

    def GuiSapChart(self) -> GuiSapChart | None:
        if self.component is None: return None
        return GuiSapChart(self.component)

    def GuiComboBoxControl(self) -> GuiComboBoxControl | None:
        if self.component is None: return None
        return GuiComboBoxControl(self.component)

    def GuiGridView(self) -> GuiGridView | None:
        if self.component is None: return None
        return GuiGridView(self.component)

    def GuiContainerShell(self) -> GuiContainerShell | None:
        if self.component is None: return None
        return GuiContainerShell(self.component)

    def GuiTab(self) -> GuiTab | None:
        if self.component is None: return None
        return GuiTab(self.component)

    def GuiTabStrip(self) -> GuiTabStrip | None:
        if self.component is None: return None
        return GuiTabStrip(self.component)

    def GuiScrollContainer(self) -> GuiScrollContainer | None:
        if self.component is None: return None
        return GuiScrollContainer(self.component)

    def GuiFrameWindow(self) -> GuiFrameWindow | None:
        if self.component is None: return None
        return GuiFrameWindow(self.component)

    def GuiMainWindow(self) -> GuiMainWindow | None:
        if self.component is None: return None
        return GuiMainWindow(self.component)

    def GuiModalWindow(self) -> GuiModalWindow | None:
        if self.component is None: return None
        return GuiModalWindow(self.component)

    def GuiTableControl(self) -> GuiTableControl | None:
        if self.component is None: return None
        return GuiTableControl(self.component)

    def GuiSessionInfo(self) -> GuiSessionInfo | None:
        if self.component is None: return None
        return GuiSessionInfo(self.component)

    def GuiSession(self) -> GuiSession | None:
        if self.component is None: return None
        return GuiSession(self.component)

    def GuiConnection(self) -> GuiConnection | None:
        if self.component is None: return None
        return GuiConnection(self.component)

    def GuiApplication(self) -> GuiApplication | None:
        if self.component is None: return None
        return GuiApplication(self.component)

    @staticmethod
    def get_instance(sap_component: win32com.client.CDispatch):
        if sap_component is None: return None
        # noinspection PyBroadException
        try: id_comp = sap_component.TypeAsNumber
        except: return None

        # TODO Verificar id do GuiStage, GuiPicture, GuiOfficeIntegration, GuiNetChart, GuiMap,
        # TODO GuiHTMLViewer, GuiGraphAdapt, GuiEAIViewer3D, GuiEAIViewer2D, GuiCalendar,
        # TODO GuiBarChart, GuiApoGrid, GuiAbapEditor, GuiSplit, GuiInputFieldControl,
        # TODO GuiTextedit, GuiToolbarControl, GuiTree, GuiChart, GuiSapChart, GuiComboBoxControl
        # TODO GuiGridView

        if id_comp == 0:
            return GuiComponent(sap_component)

        if id_comp == 1:
            return GuiVComponent(sap_component)

        if id_comp == 2:
            return GuiVContainer(sap_component)

        if id_comp == 10:
            return GuiApplication(sap_component)

        if id_comp == 11:
            return GuiConnection(sap_component)

        if id_comp == 12:
            return GuiSession(sap_component)

        if id_comp == 20:
            return GuiFrameWindow(sap_component)

        if id_comp == 21:
            return GuiMainWindow(sap_component)

        if id_comp == 22:
            return GuiModalWindow(sap_component)

        if id_comp == 23:
            return GuiMessageWindow(sap_component)

        if id_comp == 30:
            return GuiLabel(sap_component)

        if id_comp == 31:
            return GuiTextField(sap_component)

        if id_comp == 32:
            return GuiCTextField(sap_component)

        if id_comp == 33:
            return GuiPasswordField(sap_component)

        if id_comp == 34:
            return GuiComboBox(sap_component)

        if id_comp == 35:
            return GuiOkCodeField(sap_component)

        if id_comp == 40:
            return GuiButton(sap_component)

        if id_comp == 41:
            return GuiRadioButton(sap_component)

        if id_comp == 42:
            return GuiCheckBox(sap_component)

        if id_comp == 43:
            return GuiStatusPane(sap_component)

        if id_comp == 50:
            return GuiCustomControl(sap_component)

        if id_comp == 51:
            return GuiContainerShell(sap_component)

        if id_comp == 62:
            return GuiBox(sap_component)

        if id_comp == 70:
            return GuiContainer(sap_component)

        if id_comp == 71:
            return GuiSimpleContainer(sap_component)

        if id_comp == 72:
            return GuiScrollContainer(sap_component)

        # if id == 73: return GuiListContainer(sap_object)

        if id_comp == 74:
            return GuiUserArea(sap_component)

        if id_comp == 75:
            return GuiSplitterContainer(sap_component)

        if id_comp == 80:
            return GuiTableControl(sap_component)

        if id_comp == 81:
            return GuiTableColumn(sap_component)

        if id_comp == 82:
            return GuiTableRow(sap_component)

        if id_comp == 90:
            return GuiTabStrip(sap_component)

        if id_comp == 91:
            return GuiTab(sap_component)

        if id_comp == 100:
            return GuiScrollbar(sap_component)

        if id_comp == 101:
            return GuiToolbar(sap_component)

        if id_comp == 102:
            return GuiTitlebar(sap_component)

        if id_comp == 103:
            return GuiStatusbar(sap_component)

        if id_comp == 110:
            return GuiMenu(sap_component)

        if id_comp == 111:
            return GuiMenubar(sap_component)

        if id_comp == 120:
            return GuiCollection(sap_component)

        if id_comp == 121:
            return GuiSessionInfo(sap_component)

        if id_comp == 122:
            return GuiShell(sap_component)

        if id_comp == 123:
            return GuiGOSShell(sap_component)

        # if id == 124: return GuiSplitterShell(sap_object)

        if id_comp == 125:
            return GuiDialogShell(sap_component)

        #if id == 126: return GuiDockShell(sap_object)

        if id_comp == 127:
            return GuiContextMenu(sap_component)

        if id_comp == 128:
            return GuiComponentCollection(sap_component)

        if id_comp == 129:
            return GuiVHViewSwitch(sap_component)

        return GuiComponent(sap_component)


class GuiCollection:
    """ GuiCollection é semelhante à coleção GuiComponentCollection, mas seus membros não são necessariamente extensões do objeto GuiComponent.
    Pode ser usado para passar uma coleção como parâmetro para funções de objetos programáveis.
    Um objeto desta classe é criado chamando a função CreateGuiCollection do objeto GuiApplication.
    """

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    def add(self, item):
        """ Após a criação de uma GuiCollection, os itens podem ser adicionados chamando a função add.
        """
        self.component.Add(item)

    def element_at(self, index) -> object:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o index fornecido, uma exceção será gerada.
        """
        return self.component.ElementAt(index)

    def item(self, index) -> object:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Foi adicionado para compatibilidade com coleções do Microsoft Visual Basic.
        Se nenhum membro puder ser encontrado para o index fornecido, uma exceção será gerada.
        """
        return self.component.Item(index)

    @property
    def count(self) -> int:
        """ O número de elementos na coleção. Esta propriedade foi adicionada para compatibilidade com coleções do Microsoft Visual Basic.
        """
        return self.component.Count

    @property
    def length(self) -> int:
        """ O número de elementos na coleção.
        """
        return self.component.Length

    def to_list(self) -> list[object]:
        """ Retorna uma list com todos os itens da coleção.
        """
        itens = []
        for index in range(0, self.count):
            itens.append(self.item(index))
        return itens

    @property
    def type(self) -> str:
        """ As informações de tipo podem ser usadas para determinar quais propriedades e métodos um objeto suporta.
        O valor é o nome do tipo retirado desta documentação.
        O valor para GuiCollection é 'GuiCollection'.
        """
        return self.component.Type

    @property
    def type_as_number(self) -> int:
        """ Embora a propriedade Type seja um valor de string, a propriedade TypeAsNumber é um valor longo
        que pode ser usado alternativamente para identificar o tipo de um objeto.
        Foi adicionado para melhor desempenho em métodos como FindByIdEx.
        Os valores possíveis para esta propriedade são obtidos da enumeração GuiComponentType.
        """
        return self.component.TypeAsNumber


class GuiEnum:
    """ GuiEnum é a classe base para alguns enumeradores usados em scripts SAP GUI.
    """

    class_attrs: list[str]
    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        self.class_attrs = ['component']
        self.component = component

    def next(self, celt: int, rgvar, pcelt_fetched: int):
        return self.component.Next(celt, rgvar, pcelt_fetched)

    def reset(self):
        return self.component.Reset()

    def skip(self, celt: int):
        return self.component.Skip(celt)


class GuiComponent:
    """ GuiComponent é a classe base para a maioria das classes na API de script do SAP.
    """

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    @property
    def is_container_type(self) -> bool:
        """ Retorna True se o objeto é um container
        """
        return self.component.ContainerType

    @property
    def id(self) -> str:
        """ Um ID de objeto é um identificador textual exclusivo para o objeto.
        Isso é construído em uma formatação semelhante à URL, começando no GuiApplication
        e detalhando o respectivo objeto.
        """
        return self.component.Id

    @property
    def name(self) -> str:
        """ A propriedade name é especialmente útil ao trabalhar com scripts simples que acessam apenas campos de tela.
        Nesse caso um campo pode ser encontrado usando seu nome e informações de tipo,
        que é mais fácil de ler do que um ID possivelmente muito longo. No entanto,
        não há garantia de que não existam dois objetos com o mesmo nome.
        """
        return self.component.Name

    @property
    def parent(self) -> GuiComponent:
        """ O objeto pai acima na hierarquia de tempo de execução.
        Um objeto está sempre na coleção filhos de seu pai.
        """
        return ComponentCast.get_instance(self.component.Parent)

    @property
    def parent_cast(self) -> ComponentCast:
        """ Retorna o Parent pronto para fazer o Cast.
        """
        return ComponentCast(self.component.Parent)

    @property
    def type(self) -> str:
        """ Nome do tipo do objeto.
        As informações de tipo de GuiComponent podem ser usadas para determinar quais propriedades e métodos um objeto suporta.
        """
        return self.component.Type

    @property
    def type_as_number(self) -> int:
        """Embora a propriedade Type seja um valor de string,
        A propriedade TypeAsNumber é um valor numerico que pode ser usado alternativamente para identificar o tipo de um objeto.
        Foi adicionado para melhor desempenho em métodos como FindByIdEx.
        """
        return self.component.TypeAsNumber

    def cast_to(self) -> ComponentCast:
        """ Retorna a uma classe para fazer o cast do componente atual.
        """
        return ComponentCast(self.component)

    def connected_sap(self) -> bool:
        """ Verifica se o componente ainda está conectado ao SAP.
        """
        # noinspection PyBroadException
        try:
            # noinspection PyStatementEffect
            self.type_as_number
            return True
        except:
            return False


class GuiVComponent(GuiComponent):
    """ A interface GuiVComponent é exposta por todos os objetos visuais, como janelas, botões ou campos de texto.
    Assim como o GuiComponent, é uma interface abstrata. Qualquer objeto que suporte a interface GuiVComponent também expõe
    a interface GuiComponent.
    """

    def dump_state(self, inner_object: str) -> GuiCollection:
        """ Esta função despeja o estado do objeto. O parâmetro innerObject pode ser usado para especificar para qual
        objeto interno os dados devem ser despejados. Somente os componentes mais complexos, como o GuiCtrlGridView, suportam esse parâmetro.
        Todos os outros componentes sempre descartam seu estado completo. Todos os componentes que suportam este parâmetro têm em
        comum o fato de retornarem informações gerais sobre o estado do controle se o parâmetro “innerObject” contiver uma string vazia.
        Os valores disponíveis para o parâmetro innerObject são especificados como parte da descrição da classe dos componentes que o suportam.
        """
        return ComponentCast.get_instance(self.component.DumpState(inner_object))

    def set_focus(self) -> None:
        """ Esta função pode ser usada para definir o foco em um objeto. Se um usuário interagir com SAP GUI,
        ele moverá o foco sempre que a interação for com um novo objeto. Interagir com um objeto por meio do componente
        de script não altera o foco. Há alguns casos em que o aplicativo SAP verifica explicitamente o foco e
        se comporta de maneira diferente dependendo do objeto em foco.
        """
        self.component.SetFocus()

    def visualize(self, on: bool, inner_object: str) -> bool:
        """ Chamar este método de um componente exibirá uma moldura vermelha ao redor do componente especificado se o parâmetro on for verdadeiro.
        O quadro será removido se on for falso. Alguns componentes, como GuiCtrlGridView, suportam a exibição do quadro em torno de objetos internos,
        como células. O formato da string innerObject é o mesmo do método dumpState.
        """
        return self.component.Visualize(on, inner_object)

    @property
    def acc_label_collection(self) -> GuiComponentCollection:
        """ A coleção contém objetos do tipo GuiLabel que foram atribuídos a este controle no ABAP Screen Painter.
        """
        return ComponentCast.get_instance(self.component.AccLabelCollection)

    @property
    def acc_text(self) -> str:
        """ Um texto adicional para suporte de acessibilidade.
        """
        return self.component.AccText

    @property
    def acc_text_on_request(self) -> str:
        """ Um texto adicional para suporte de acessibilidade.
        """
        return self.component.AccTextOnRequest

    @property
    def acc_tooltip(self) -> str:
        """ Um texto de dica adicional para suporte de acessibilidade.
        """
        return self.component.AccTooltip

    @property
    def changeable(self) -> bool:
        """ Um objeto pode ser alterado se não estiver desabilitado nem somente leitura.
        """
        return self.component.Changeable

    @property
    def default_tooltip(self) -> str:
        """ Texto de dica de ferramenta gerado a partir do texto curto definido no
        dicionário de dados para determinado tipo de elemento de tela.
        """
        return self.component.DefaultTooltip

    @property
    def icon_name(self) -> str:
        """ Se ao objeto foi atribuído um ícone, então esta propriedade é o nome do ícone, caso contrário, é uma string vazia.
        """
        return self.component.IconName

    @property
    def is_symbol_font(self) -> bool:
        """ A propriedade é TRUE se o texto do componente for visualizado na fonte do símbolo SAP.
        """
        return self.component.IsSymbolFont

    @property
    def modified(self) -> bool:
        """ Um objeto é modificado se seu estado tiver sido alterado pelo usuário e essa alteração ainda não tiver sido enviada ao sistema SAP.
        """
        return self.component.Modified

    @property
    def parent_frame(self) -> GuiComponent:
        """ Se o controle estiver hospedado no objeto Frame, o valor da propriedade será esse quadro.
        """
        return ComponentCast.get_instance(self.component.ParentFrame)

    @property
    def text(self) -> str:
        """ O valor desta propriedade depende muito do tipo de objeto no qual ela é chamada.
        Isto é óbvio para campos de texto ou itens de menu. Por outro lado, esta propriedade está vazia para botões da
        barra de ferramentas e é o ID da classe para shells. Você pode ler a propriedade de texto de um rótulo, mas não
        pode alterá-la, enquanto só pode definir a propriedade de texto de um campo de senha, mas não lê-la.
        """
        return self.component.Text

    @text.setter
    def text(self, text: str = None) -> None:
        """ O valor desta propriedade depende muito do tipo de objeto no qual ela é chamada.
        Isto é óbvio para campos de texto ou itens de menu. Por outro lado, esta propriedade está vazia para botões da
        barra de ferramentas e é o ID da classe para shells. Você pode ler a propriedade de texto de um rótulo, mas não
        pode alterá-la, enquanto só pode definir a propriedade de texto de um campo de senha, mas não lê-la.
        """
        self.component.Text = text

    @property
    def tooltip(self) -> str:
        """ A dica de ferramenta contém um texto projetado para ajudar o usuário a entender o significado de um determinado campo de texto ou botão.
        """
        return self.component.Tooltip

    @property
    def screen_left(self) -> int:
        """ A posição y do componente nas coordenadas da tela.
        """
        return self.component.ScreenLeft

    @property
    def screen_top(self) -> int:
        """ A posição x do componente nas coordenadas da tela.
        """
        return self.component.ScreenTop

    @property
    def top(self) -> int:
        """ Coordenada superior do elemento nas coordenadas da tela.
        """
        return self.component.Top

    @property
    def left(self) -> int:
        """ Posição esquerda do elemento nas coordenadas da tela.
        """
        return self.component.Left

    @property
    def width(self) -> int:
        """ Largura do componente em pixels.
        """
        return self.component.Width

    @property
    def height(self) -> int:
        """ Altura do componente em pixels.
        """
        return self.component.Height


class GuiComponentCollection(GuiComponent):
    """ O GuiComponentCollection é usado para elementos de coleções, como a propriedade Children de contêineres.
    Cada elemento da coleção é uma extensão do GuiComponent.
    """

    def element_at(self, index: int, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.ElementAt(index))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.ElementAt(index))
            except:
                return None

    def item(self, index: int, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.Item(index))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.Item(index))
            except:
                return None

    def item_cast(self, index: int, on_raise: bool = False) -> Optional[ComponentCast]:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        O item será retornado em uma classe pronto para fazer o cast para o tipo do item desejado.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        """
        if on_raise:
            return ComponentCast(self.component.Item(index))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast(self.component.Item(index))
            except:
                return None

    @property
    def count(self) -> int:
        """ O número de elementos na coleção.
        """
        return self.component.Count

    @property
    def length(self) -> int:
        """ O número de elementos na coleção.
        """
        return self.component.Length

    def to_list(self) -> list[GuiComponent]:
        """ Retorna uma lista com todos os itens da coleção.
        """
        itens = []
        for index in range(0, self.count):
            itens.append(self.item(index))
        return itens

    def last_item(self) -> GuiComponent:
        """ Retona o útimo item da coleção.
        """
        return self.element_at(self.count - 1)

    def last_item_cast(self) -> ComponentCast:
        """ Retona o útimo item da coleção em uma classe pronta para fazer o cast para o tipo do item desejado.
        """
        return self.item_cast(self.count - 1)


class GuiContainer(GuiComponent):
    """ Um objeto herda a interface GuiContainer se ela puder ter filhos.
    Exemplos desta interface são janelas e subtelas, barras de ferramentas ou controles com filhos, como o controle divisor.
    """

    def find_by_id(self, id_element: str, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Pesquise nos descendentes do objeto um determinado objeto que corresponde ao ID.
        Se nenhum descendente com o ID fornecido puder ser encontrado, a função gera uma exceção,
        a menos que o parâmetro opcional on_raise seja definido como False.
        """
        result = self.component.findById(id_element, on_raise)
        if result is not None: return ComponentCast.get_instance(result)
        return None

    def find_by_id_cast(self, id_element: str, on_raise: bool = False) -> Optional[ComponentCast]:
        """ Pesquise nos descendentes do objeto um determinado objeto que corresponde ao ID.
        Se nenhum descendente com o ID fornecido puder ser encontrado, a função gera uma exceção,
        a menos que o parâmetro opcional on_raise seja definido como False.
        O Componente será retornado em uma classe de cast para fazer o hint no tipo desejado.
        """
        result = self.component.findById(id_element, on_raise)
        return ComponentCast(result)

    @property
    def children(self) -> GuiComponentCollection:
        """ Esta coleção contém todos os filhos diretos do objeto.
        """
        return GuiComponentCollection(self.component.Children)


class GuiVContainer(GuiVComponent, GuiContainer):
    """ Um objeto expõe a interface GuiVContainer se ela estiver visível e puder ter filhos.
    Exemplos dessa interface são janelas e subtelas, barras de ferramentas ou controles com filhos, como o controle divisor.
    GuiVContainer estende o objeto GuiContainer e o objeto GuiVComponent.
    """

    # Criar mais funções de localização de componentes

    def find_all_by_name(self, name: str, type_component: str, on_raise: bool = True) -> Optional[GuiComponentCollection]:
        """ Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção quando FindAllByName ou FindAllByNameEx forem usados.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindAllByName(name, type_component))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.FindAllByName(name, type_component))
            except:
                pass

        return None

    def find_all_by_name_ex(self, name: str, type_component: int, on_raise: bool = True) -> Optional[GuiComponentCollection]:
        """ Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção quando FindAllByName ou FindAllByNameEx forem usados.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindAllByNameEx(name, type_component))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.FindAllByNameEx(name, type_component))
            except:
                pass

        return None

    def find_by_name(self, name: str, type_component: str, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Ao contrário de FindById, esta função não garante um resultado único.
        Ele simplesmente retornará o primeiro descendente que corresponda aos parâmetros de nome e tipo.
        Esta é uma descrição mais natural do objeto do que o ID complexo, mas só faz sentido em objetos dynpro,
        pois a maioria dos outros objetos não tem um nome significativo. Se nenhum descendente com nome
        e tipo correspondentes for encontrado, a função gera uma exceção.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindByName(name, type_component))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.FindByName(name, type_component))
            except:
                pass

        return None

    def find_by_name_ex(self, name: str, type_component: int, on_raise: bool = True) -> Optional[GuiComponentCollection]:
        """ Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção
        quando FindAllByName ou FindAllByNameEx forem usados.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindByNameEx(name, type_component))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.FindByNameEx(name, type_component))
            except:
                pass

        return None


class GuiFrameWindow(GuiVContainer):
    """ Um GuiFrameWindow é um objeto visual de alto nível na hierarquia de tempo de execução.
    Pode ser a janela principal ou uma janela pop-up modal. Consulte as seções GuiMainWindow e GuiModalWindow para obter exemplos.
    O próprio GuiFrameWindow é uma interface abstrata. GuiFrameWindow estende o objeto GuiVContainer. O prefixo do tipo é wnd, o nome
    é wnd mais o número da janela entre colchetes.
    """

    def close(self) -> None:
        """ A função tenta fechar a janela. Tentar fechar a última janela principal de uma sessão não terá sucesso imediato
        a caixa de diálogo 'Você realmente deseja fazer logoff?' será exibida primeiro.
        """
        self.component.Close()

    def comp_bitmap(self, filename_1: str, filename_2: str) -> int:
        """ Este método compara dois arquivos bitmap píxel por píxel.
        Tipo de retorno:
        O método retorna um dos seguintes valores:
        0: Os arquivos não diferem
        1: Os arquivos diferem em tamanho
        2: Os arquivos possuem conteúdo diferente
        3: Houve um erro
        """
        return self.component.CompBitmap(filename_1, filename_2)

    def hard_copy(self, filename: str, image_type: int = 0, x_pos: int = None, y_pos: int = None, n_width: int = None, n_height: int = None) -> str:
        """ Esta função despeja uma cópia impressa da janela como um arquivo bitmap no disco.
        O parâmetro é o nome do arquivo.
        Se a função for bem-sucedida, o valor de retorno será o caminho totalmente qualificado do arquivo.
        Se nenhuma informação de caminho for fornecida, o arquivo será gravado na pasta de documentos SAP GUI.
        Caso os parâmetros opcionais xPos, yPos, nWidth e nHeight forem definidos, apenas o retângulo especificado da janela principal será capturado.
        image_type:
        0: BMP
        1: JPG
        2: PNG
        3: GIF
        4: TIFF
        """
        return self.component.HardCopy(filename, image_type, x_pos, y_pos, n_width, n_height)

    def hard_copy_to_memory(self, image_type: int = 0):
        """ Esta função retorna uma cópia impressa da janela como uma matriz segura de bytes.
        image_type:
        0: BMP
        1: JPG
        2: PNG
        3: GIF
        4: TIFF
        """
        # TODO Verificar retorno no python
        return self.component.HardCopyToMemory(image_type)

    def is_v_key_allowed(self, v_key: int) -> bool:
        """ Esta função retorna True se a chave virtual VKey estiver disponível no momento.
        As VKeys são definidas no pintor de menus.
        """
        return self.component.IsVKeyAllowed(v_key)

    def iconify(self) -> None:
        """ Isso definirá uma janela para o estado iconificado.
        Não é possível iconificar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão iconificados.
        """
        self.component.Iconify()

    def minimize(self) -> None:
        """ Isso definirá uma janela para o estado iconificado.
        Não é possível iconificar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão iconificados.
        """
        self.iconify()

    def maximize(self) -> None:
        """ Isso maximizará uma janela. Não é possível maximizar uma janela modal,
        é sempre a janela principal que será maximizada.
        """
        self.component.Maximize()

    def restore(self) -> None:
        """ Isso restaurará uma janela de seu estado iconificado.
        não é possível restaurar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão restaurados.
        """
        self.component.Restore()

    def set_focus_windows(self) -> None:
        """ Isso faz o windows focar na janela indepedente do estado atual do mesmo.
        """
        self.minimize()
        self.maximize()

    def send_v_key(self, v_key: int) -> None:
        """ A chave virtual VKey é executada na janela. As VKeys são definidas no pintor de menus.
        """
        return self.component.SendVKey(v_key)

    def send_key(self) -> SapKeySender:
        """ Retorna um objeto com funções de teclas para serem enviadas
        """
        return SapKeySender(self)

    def show_message_box(self, title: str, text: str, msg_icon: int, msg_type: int) -> int:
        """ Mostra uma caixa de mensagem.
        O valor de retorno será uma das constantes GuiMessageBoxResult.
        title: Título da caixa de mensagem
        text: texto da caixa de mensagem.
        msg_icon: MsgIcon define o ícone a ser usado para a caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxType.
        msg_type: MsgType define os botões disponíveis na caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxOption.
        """
        return self.component.ShowMessageBox(title, text, msg_icon, msg_type)

    def jump_backward(self) -> None:
        """ Executa a tecla Ctrl+Shift+Tab na janela para retroceder um bloco.
        """
        self.component.JumpBackward()

    def jump_forward(self) -> None:
        """ Execute a tecla Ctrl+Tab na janela para avançar um bloco.
        """
        self.component.JumpForward()

    def tab_backward(self) -> None:
        """ Execute a tecla Shift+Tab na janela para retroceder um elemento.
        """
        self.component.TabBackward()

    def tab_forward(self) -> None:
        """ Execute a tecla Tab na janela para avançar um elemento.
        """
        self.component.TabForward()

    @property
    def element_visualization_mode(self) -> bool:
        """ Quando elementVisualizationMode está habilitado, um teste de acerto pode ser executado no
        SAP GUI movendo o cursor sobre a janela. O evento hit da sessão é disparado quando um componente é encontrado na posição do mouse.
        """
        return self.component.ElementVisualizationMode

    @element_visualization_mode.setter
    def element_visualization_mode(self, option: bool = None) -> None:
        """ Quando elementVisualizationMode está habilitado, um teste de acerto pode ser executado no
        SAP GUI movendo o cursor sobre a janela. O evento hit da sessão é disparado quando um componente é encontrado na posição do mouse.
        """
        self.component.ElementVisualizationMode = option

    @property
    def gui_focus(self) -> GuiVComponent:
        """ O SystemFocus suporta apenas elementos dynpro.
        Para receber informações sobre o controle ActiveX atualmente em foco você pode acessar a propriedade GuiFocus.
        """
        # TODO Retorna ao component cast
        return GuiVComponent(self.component.GuiFocus)

    @property
    def handle(self) -> int:
        """ O identificador de janela do controle que está conectado ao GuiShell.
        Este é o identificador da janela subjacente no Microsoft Windows.
        """
        return self.component.Handle

    @property
    def iconic(self) -> bool:
        """ Esta propriedade é True se a janela estiver iconificada.
        É possível executar comandos de script em uma janela iconificada, mas pode haver resultados indefinidos,
        especialmente quando controles estão envolvidos, pois estes podem ter configurações de tamanho inválidas.
        """
        return self.component.Iconic

    @property
    def system_focus(self) -> GuiVComponent:
        """ O SystemFocus especifica o componente que o sistema SAP está atualmente vendo como sendo focado.
        Este valor é válido apenas para elementos dynpro e pode, portanto, diferir do foco visto no frontend.
        """
        # TODO Retorna ao component cast
        return GuiVComponent(self.component.SystemFocus)

    @property
    def working_pane_height(self) -> int:
        """ Esta é a altura do painel de trabalho na métrica de caracteres.
        """
        return self.component.WorkingPaneHeight

    @property
    def working_pane_width(self) -> int:
        """ Esta é a largura do painel de trabalho na métrica de caracteres.
        O painel de trabalho é a área entre as barras de ferramentas na parte superior da janela e a barra de status na parte inferior da janela.
        """
        return self.component.WorkingPaneWidth


class GuiStatusPane(GuiVComponent):
    """ O pai dos objetos GuiStatusPane é a barra de status (veja também Objeto GuiStatusbar).
    Os objetos GuiStatusPane refletem as áreas individuais da barra de status, por exemplo, "pane[0]"
    refere-se à seção da barra de status onde as mensagens são exibidas. Veja também Objeto GuiStatusbar.
    """

    def has_in_text(self, text: str) -> bool:
        """ Verifica se tem um texto específico dentro do texto do painel.
        """
        return self.text is not None and text in self.text


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


class GuiSession(GuiContainer):
    """ A GuiSession fornece o contexto no qual um usuário executa uma determinada tarefa, como trabalhar com uma transação.
    É, portanto, o ponto de acesso para aplicações, que gravam as ações de um usuário em relação a uma tarefa específica ou reproduzem essas ações.
    """

    @property
    def user_area(self) -> GuiUserArea:
        return self.find_by_id_cast('wnd[0]/usr').GuiUserArea()

    def send_v_key(self, v_key: int) -> None:
        """ A chave virtual v_key é executada na janela ativa da sessão.
        As VKeys são definidas no pintor de menus.
        """
        self.active_window.send_v_key(v_key=v_key)

    def send_key(self) -> SapKeySender:
        """ Retorna um objeto com funções de teclas para serem enviadas
        """
        return SapKeySender(self.active_window)

    def get_alert_status_pane(self) -> GuiStatusPane:
        """ Obtém a barra de alerta principal.
        """
        # noinspection PyTypeChecker
        return self.find_by_id(SapFields.ALERT_STATUS_PANE, False)

    def as_std_number_format(self, number: str) -> str:
        """ Dependendo do formato numérico do sistema, o sinal de menos dos números pode ser colocado à direita do número.
        Usando esta função, o sinal de menos é movido para a esquerda.
        """
        return self.component.AsStdNumberFormat(number)

    def clear_error_list(self) -> None:
        """ Este método limpa a lista de erros que podem ser criados quando controles ActiveX são encontrados em uma tela que não suporta scripts SAP GUI.
        Caso contrário, a lista será limpa após um evento de erro ser gerado. Isso acontece no final de uma viagem de ida e volta.
        """
        return self.component.ClearErrorList()

    def create_session(self) -> Optional[GuiSession]:
        """ Esta função abre uma nova sessão, que é então visualizada por uma nova janela principal.
        Isso se assemelha ao comando "/o" que pode ser executado no campo de comando.
        """
        conn = self.parent_cast.GuiConnection()
        sessions_id = list(map(lambda comp: comp.id, conn.sessions_list))
        self.component.CreateSession()
        seconds = 5.0
        while seconds > 0 :
            seconds -= 0.25
            time.sleep(0.25)
            for session in conn.sessions_list:
                if session.id not in sessions_id:
                    return session

        return None

    def close_session(self, ignore_popup_logoff: bool = False) -> None:
        if ignore_popup_logoff and self.parent_cast.GuiConnection().sessions.count <= 1:
            self.send_command(SapCommands.CLOSE_ALL_SESSIONS)
        else:
            self.send_command(SapCommands.CLOSE_SESSION)

    def enable_jaws_events(self) -> None:
        """ Habilite o envio de eventos para o leitor de tela Freedom Scientific JAWS,
        que se comunica com SAP GUI para Windows através da API de Scripting.
        Por padrão o envio de eventos está ativado.
        """
        return self.component.EnableJawsEvents()

    def end_transaction(self) -> None:
        """ Chamar esta função tem o mesmo efeito que SendCommand("/n").
        """
        return self.component.EndTransaction()

    def find_by_position(self, x: int, y: int, on_raise: bool = True) -> GuiCollection:
        """ Este método pode ser usado para fazer um hittest em uma sessão SAP GUI.
        Os parâmetros x e y devem ser fornecidos em coordenadas de tela.
        Se nenhum componente for encontrado, uma exceção será gerada, a menos que raise seja definido como False.
        Nesse caso, um objeto None é retornado.
        """
        return GuiCollection(self.component.FindByPosition(x, y, on_raise))

    def get_icon_resource_name(self, text: str) -> str:
        """ No SAP GUI, os ícones são frequentemente descritos como texto no formato @nn@, onde nn é um número.
        A função getIconResourceName traduz a notação @nn@ no nome do recurso em sapbtmp.dll.
        """
        return self.component.GetIconResourceName(text)

    def get_v_key_description(self, v_key: int) -> str:
        """ Quando um script é gravado, ele geralmente contém chamadas sendVKey(n), onde n é um número.
        O método getVKeyDescription traduz esses números em um texto legível. Por exemplo, o número 0 é traduzido no texto “Enter”.
        """
        return self.component.GetVKeyDescription(v_key)

    def lock_session_ui(self) -> None:
        """ Este método bloqueia a sessão para que nenhuma interação do usuário seja
        possível até que a sessão seja desbloqueada usando UnlockSessionUI.
        """
        return self.component.LockSessionUI()

    def unlock_session_ui(self) -> None:
        """ Este método desbloqueia a sessão após ela ter sido bloqueada usando LockSessionUI.
        """
        return self.component.UnlockSessionUI()

    def send_command(self, command: str) -> None:
        """ Usando esta função você pode executar qualquer string de comando,
        que de outra forma poderia ser inserida na caixa de combinação do campo de comando.
        """
        return self.component.SendCommand(command)

    def start_transaction(self, transaction: str) -> bool:
        """ Chamar esta função com o parâmetro "xyz" tem o mesmo efeito que SendCommand("/nxyz").
        """
        if transaction.startswith('/o') or transaction.startswith('/o'):
            transaction = transaction[2:]
        if transaction.startswith('/'):
            transaction = transaction[1:]
        self.component.StartTransaction(transaction)
        return self.info.transaction == transaction

    @property
    def acc_enhanced_tab_chain(self) -> bool:
        """ Esta propriedade será True se a respectiva opção "Incluir elementos somente leitura e desabilitados na cadeia de guias"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        return self.component.AccEnhancedTabChain

    @acc_enhanced_tab_chain.setter
    def acc_enhanced_tab_chain(self, option: bool = None) -> None:
        """ Esta propriedade será True se a respectiva opção "Incluir elementos somente leitura e desabilitados na cadeia de guias"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        self.component.AccEnhancedTabChain = option

    @property
    def acc_symbol_replacement(self) -> bool:
        """ Esta propriedade é True se a respectiva opção "Exibir símbolos em listas como letras"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        return self.component.AccSymbolReplacement

    @acc_symbol_replacement.setter
    def acc_symbol_replacement(self, option: bool = None) -> None:
        """ Esta propriedade é True se a respectiva opção "Exibir símbolos em listas como letras"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        self.component.AccSymbolReplacement = option

    @property
    def active_window(self) -> GuiFrameWindow:
        """ Todas as janelas podem ser encontradas na coleção Children do GuiSession.
        No entanto, na maioria das vezes, um aplicativo acessará a janela da sessão atualmente ativada,
        pois essa é a janela com a qual o usuário provavelmente irá interagir. Esta propriedade pretende ser um atalho para esta janela.
        """
        return GuiFrameWindow(self.component.ActiveWindow)

    @property
    def busy(self) -> bool:
        """ Enquanto o SAP GUI aguarda dados do servidor, nenhuma chamada de script será retornada,
        bloqueando o thread em execução. Isto pode não ser aceitável para aplicações avançadas.
        Uma forma de evitar isso é verificar a propriedade Busy da sessão.
        Se esta propriedade for True, então uma chamada de Scripting subsequente aguardará o término da comunicação com o servidor.
        """
        return self.component.Busy

    @busy.setter
    def busy(self, option: bool = None) -> None:
        """ Enquanto o SAP GUI aguarda dados do servidor, nenhuma chamada de script será retornada,
        bloqueando o thread em execução. Isto pode não ser aceitável para aplicações avançadas.
        Uma forma de evitar isso é verificar a propriedade Busy da sessão.
        Se esta propriedade for True, então uma chamada de Scripting subsequente aguardará o término da comunicação com o servidor.
        """
        self.component.Busy = option

    @property
    def error_list(self) -> GuiCollection:
        return GuiCollection(self.component.ErrorList)

    @error_list.setter
    def error_list(self, errors: GuiCollection = None) -> None:
        self.component.ErrorList = errors.component

    @property
    def info(self) -> GuiSessionInfo:
        """ As informações são do tipo GuiSessionInfo.
        Ele contém informações técnicas sobre a conexão atual, os dados de login, o aplicativo SAP em execução e muito mais.
        """
        return GuiSessionInfo(self.component.Info)

    @property
    def is_active(self) -> bool:
        """ TRUE se a janela da sessão estiver ativa.
        """
        return self.component.IsActive

    @is_active.setter
    def is_active(self, option: bool = None) -> None:
        """ TRUE se a janela da sessão estiver ativa.
        """
        self.component.IsActive = option

    @property
    def is_list_box_active(self) -> bool:
        """ Esta propriedade é True se uma caixa de listagem estiver aberta no momento (para um GuiComboBox).
        """
        return self.component.IsListBoxActive

    @property
    def list_box_curr_entry(self) -> int:
        """ O índice da entrada da caixa de listagem atualmente selecionada.
        """
        return self.component.ListBoxCurrEntry

    @property
    def list_box_curr_entry_height(self) -> int:
        """ A altura da entrada atual da caixa de listagem em píxeis.
        """
        return self.component.ListBoxCurrEntryHeight

    @property
    def list_box_curr_entry_left(self) -> int:
        """ A posição esquerda da entrada atual da caixa de listagem em píxeis.
        """
        return self.component.ListBoxCurrEntryLeft

    @property
    def list_box_curr_entry_top(self) -> int:
        """ A posição superior da entrada atual da caixa de listagem em píxeis.
        """
        return self.component.ListBoxCurrEntryTop

    @property
    def list_box_curr_entry_width(self) -> int:
        """ A largura da entrada atual da caixa de listagem em pixels.
        """
        return self.component.ListBoxCurrEntryWidth

    @property
    def list_box_height(self) -> int:
        """ A altura da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxHeight

    @property
    def list_box_left(self) -> int:
        """ A posição esquerda da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxLeft

    @property
    def list_box_top(self) -> int:
        """ A posição superior da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxTop

    @property
    def list_box_width(self) -> int:
        """ A largura da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxWidth

    @property
    def passport_pre_system_id(self) -> str:
        """ O ID do pré-sistema. Parte das informações do passaporte.
        """
        return self.component.PassportPreSystemId

    @passport_pre_system_id.setter
    def passport_pre_system_id(self, option: str = None) -> None:
        """ O ID do pré-sistema. Parte das informações do passaporte.
        """
        self.component.PassportPreSystemId = option

    @property
    def passport_system_id(self) -> str:
        """ O ID do sistema. Parte das informações do passaporte.
        """
        return self.component.PassportSystemId

    @passport_system_id.setter
    def passport_system_id(self, option: str = None) -> None:
        """ O ID do sistema. Parte das informações do passaporte.
        """
        self.component.PassportSystemId = option

    @property
    def passport_transaction_id(self) -> str:
        """ O ID exclusivo da transação. Parte das informações do passaporte.
        """
        return self.component.PassportTransactionId

    @passport_transaction_id.setter
    def passport_transaction_id(self, option: str = None) -> None:
        """ O ID exclusivo da transação. Parte das informações do passaporte.
        """
        self.component.PassportTransactionId = option

    @property
    def progress_percent(self) -> int:
        """ A porcentagem exibida pelo indicador de progresso do SAP GUI.
        """
        return self.component.ProgressPercent

    @property
    def progress_text(self) -> str:
        """ O texto exibido pelo indicador de progresso.
        """
        return self.component.ProgressText

    @property
    def record(self) -> bool:
        """ Definir esta propriedade como True habilita o modo de gravação da sessão.
        Neste modo, as alterações nos elementos da interface do usuário são registradas no SAP GUI e enviadas
        para um aplicativo de gravação usando o evento Change descrito posteriormente.
        Observações:
        Alguns elementos da interface do usuário podem se comportar de maneira diferente no modo de gravação e durante a reprodução ou interação manual.
        * A caixa de diálogo de ajuda F4 é sempre exibida como uma janela modal.
        * Arrastar e soltar está desativado.
        """
        return self.component.Record

    @record.setter
    def record(self, option: bool = None) -> None:
        """ Definir esta propriedade como True habilita o modo de gravação da sessão.
        Neste modo, as alterações nos elementos da interface do usuário são registradas no SAP GUI e enviadas
        para um aplicativo de gravação usando o evento Change descrito posteriormente.
        Observações:
        Alguns elementos da interface do usuário podem se comportar de maneira diferente no modo de gravação e durante a reprodução ou interação manual.
        * A caixa de diálogo de ajuda F4 é sempre exibida como uma janela modal.
        * Arrastar e soltar está desativado.
        """
        self.component.Record = option

    @property
    def record_file(self) -> str:
        """ Uma maneira simples de gravar um script é definir a propriedade recordFile com um nome de arquivo válido e,
        em seguida, ativar a propriedade record. Um arquivo Visual Basic Script com o nome fornecido será criado na
        pasta SAP GUI Scripts no PC cliente.
        Observações: Esta propriedade aceita apenas nomes de arquivos simples sem informações de caminho.
        """
        return self.component.RecordFile

    @record_file.setter
    def record_file(self, option: str = None) -> None:
        """ Uma maneira simples de gravar um script é definir a propriedade recordFile com um nome de arquivo válido e,
        em seguida, ativar a propriedade record. Um arquivo Visual Basic Script com o nome fornecido será criado na
        pasta SAP GUI Scripts no PC cliente.
        Observações: Esta propriedade aceita apenas nomes de arquivos simples sem informações de caminho.
        """
        self.component.RecordFile = option

    @property
    def save_as_unicode(self) -> bool:
        """ Se esta propriedade estiver configurada como TRUE, os scripts gravados serão salvos na codificação UNICODE.
        Overwise é a página de código do sistema atual.
        """
        return self.component.SaveAsUnicode

    @save_as_unicode.setter
    def save_as_unicode(self, option: bool = None) -> None:
        """ Se esta propriedade estiver configurada como TRUE, os scripts gravados serão salvos na codificação UNICODE.
        Overwise é a página de código do sistema atual.
        """
        self.component.SaveAsUnicode = option

    @property
    def show_dropdown_keys(self) -> bool:
        """ Se esta propriedade for TRUE, os menus suspensos mostrarão não apenas o texto das entradas suspensas, mas também as chaves.
        """
        return self.component.ShowDropdownKeys

    @show_dropdown_keys.setter
    def show_dropdown_keys(self, option: bool = None) -> None:
        """ Se esta propriedade for TRUE, os menus suspensos mostrarão não apenas o texto das entradas suspensas, mas também as chaves.
        """
        self.component.ShowDropdownKeys = option

    @property
    def suppress_backend_popups(self) -> bool:
        return self.component.SuppressBackendPopups

    @suppress_backend_popups.setter
    def suppress_backend_popups(self, option: bool = None) -> None:
        self.component.SuppressBackendPopups = option

    @property
    def test_tool_mode(self) -> int:
        """ Durante os testes internos, alguns aspectos da interface do usuário mostraram-se difíceis de lidar com
        ferramentas de teste que usam a API de script para automatizar o SAP GUI. Por esta razão foi adicionado um
        modo especial no qual as seguintes alterações são administradas.

        * Embora as mensagens de sucesso (S), aviso (W) e erro (E) sejam sempre exibidas na barra de status,
            as mensagens de informação (I) e de aborto (A) são exibidas como janelas pop-up, a menos que testToolMode esteja definido.
        * O modo de atualização do servidor de aplicativos é alterado para modo imediato para a conexão.
        * As mensagens do sistema são ignoradas para não interromper a gravação ou reprodução de scripts.

        0: Desativar TestToolMode
        1: Habilite TestToolMode
        """
        return self.component.TestToolMode

    @test_tool_mode.setter
    def test_tool_mode(self, option: int = None) -> None:
        """ Durante os testes internos, alguns aspectos da interface do usuário mostraram-se difíceis de lidar com
        ferramentas de teste que usam a API de script para automatizar o SAP GUI. Por esta razão foi adicionado um
        modo especial no qual as seguintes alterações são administradas.

        * Embora as mensagens de sucesso (S), aviso (W) e erro (E) sejam sempre exibidas na barra de status,
            as mensagens de informação (I) e de aborto (A) são exibidas como janelas pop-up, a menos que testToolMode esteja definido.
        * O modo de atualização do servidor de aplicativos é alterado para modo imediato para a conexão.
        * As mensagens do sistema são ignoradas para não interromper a gravação ou reprodução de scripts.

        0: Desativar TestToolMode
        1: Habilite TestToolMode
        """
        self.component.TestToolMode = option


class GuiConnection(GuiContainer):
    """ Um GuiConnection representa a conexão entre o SAP GUI e um servidor de aplicativos.
    As conexões podem ser abertas a partir do SAP Logon ou dos métodos openConnection e openConnectionByConnectionString do GuiApplication.
    """

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
        return self.sessions.last_item_cast().GuiSession().create_session()

    def sessions_user(self, user_name: str) -> list[GuiSession]:
        """ Obtém todas as sessões do usuário.
        """
        return list(filter(lambda session: session.info.user == user_name, self.sessions_list))

    def sessions_in_transaction(self, *transactions: str) -> list[GuiSession]:
        """ Obtém todas as sessões que está na transação.
        """
        return list(filter(lambda session: session.info.transaction in transactions, self.sessions_list))


class GuiUtils:

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    def close_file(self, file: int) -> None:
        """ Esta função fecha um arquivo que foi aberto usando OpenFile.
        """
        self.component.CloseFile(file)

    def open_file(self, name: str) -> int:
        """ O arquivo será criado na pasta de documentos SAP GUI.
        O valor de retorno é um identificador para o arquivo.
        name: Nome do arquivo de texto a ser criado. Por motivos de segurança, este nome não deve conter nenhuma informação de caminho.
        """
        return self.component.OpenFile(name)

    def show_message_box(self, title: str, text: str, msg_icon: int, msg_type: int) -> int:
        """ Mostra uma caixa de mensagem.
        O valor de retorno será uma das constantes GuiMessageBoxResult.
        title: título da caixa de mensagem
        text: texto da caixa de mensagem.
        msg_icon: msg_icon define o ícone a ser usado para a caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxType.
        msg_type: msg_type define os botões disponíveis na caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxOption.
        """
        return self.component.ShowMessageBox(title, text, msg_icon, msg_type)

    def write(self, file: int, text: str) -> None:
        """ Escreva texto em um arquivo aberto sem uma nova linha no final.
        """
        return self.component.Write(file, text)

    def write_line(self, file: int, text: str) -> None:
        """ Escreva o texto em um arquivo aberto com uma nova linha no final.
        """
        return self.component.WriteLine(file, text)


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


class GuiScrollbar:
    """ A classe GuiScrollbar é uma classe utilitária usada, por exemplo, em GuiScrollContainer ou GuiTableControl.
    """

    # TODO Fazer mais funções de auxilio

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    @property
    def maximum(self) -> int:
        """ Esta é a posição máxima da barra de rolagem.
        """
        return self.component.Maximum

    @property
    def minimum(self) -> int:
        """ Esta é a posição mínima da barra de rolagem.
        """
        return self.component.Minimum

    @property
    def page_size(self) -> int:
        """ Quando o usuário rola uma página para baixo, a posição será aumentada pelo valor de pageSize.
        """
        return self.component.PageSize

    @property
    def position(self) -> int:
        """ A posição do polegar da barra de rolagem pode ser definida em valores do mínimo ao máximo.
        """
        return self.component.Position

    @position.setter
    def position(self, position: int):
        """ A posição do polegar da barra de rolagem pode ser definida em valores do mínimo ao máximo.
        """
        self.component.Position = position

    def load_all(self) -> None:
        """ Faz o carregamento completo do componente, rolando do começo até o fim do scroll.
        """
        self.position = self.minimum
        while self.position < self.maximum:
            new_pos = min(self.maximum, self.position+self.page_size)
            self.position = new_pos


class GuiMenu(GuiVComponent):
    """ Um GuiMenu pode ter outros objetos GuiMenu como filhos.
    O prefixo do tipo é menu, o nome é o texto do item de menu.
    Caso o item não possua texto, como o caso dos separadores, então o nome é a última parte do id, menu[n].
    """

    def select(self) -> None:
        """ Selecione o menu.
        """
        self.component.Select()


class GuiContextMenu(GuiMenu):
    """ Um GuiContextMenu pode ter outros objetos GuiContextMenu como filhos.
    O tipo é mnu, o nome é o código de função enviado ao sistema quando o item de menu é selecionado.
    """

    pass


class GuiUserArea(GuiVContainer):
    """ A GuiUserArea compreende a área entre a barra de ferramentas e a barra de status para janelas do
    tipo GuiMainWindow e a área entre a barra de título e a barra de ferramentas para janelas modais,
    podendo também ser limitada por controles docker. Os elementos dynpro padrão podem ser encontrados apenas
    nesta área, com exceção dos botões, que também são encontrados nas barras de ferramentas.
    """

    def find_by_label(self, text: str, type_component: str, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Um método muito simples para encontrar um objeto é pesquisar especificando o texto do respectivo rótulo.
        """
        if on_raise: return ComponentCast.get_instance(self.component.FindByLabel(text, type_component))
        else:
            # noinspection PyBroadException
            try: return ComponentCast.get_instance(self.component.FindByLabel(text, type_component))
            except: pass

        return None

    @property
    def current_context_menu(self) -> GuiContextMenu:
        """ Esta propriedade só é definida quando um menu de contexto está disponível no objeto shell.
        """
        return ComponentCast.get_instance(self.component.CurrentContextMenu)

    @property
    def horizontal_scrollbar(self) -> GuiScrollbar:
        """ A área do usuário é definida para ser rolável mesmo que as barras de rolagem nem sempre estejam visíveis.
        """
        return ComponentCast.get_instance(self.component.HorizontalScrollbar)

    @property
    def vertical_scrollbar(self) -> GuiScrollbar:
        """ A área do usuário é definida para ser rolável mesmo que as barras de rolagem nem sempre estejam visíveis.
        """
        return ComponentCast.get_instance(self.component.VerticalScrollbar)

    @property
    def is_otf_preview(self) -> bool:
        """ Esta propriedade é TRUE, caso seja exibido um Controle de Preview SAPScript na área do usuário.
        """
        return self.component.IsOTFPreview


class GuiStatusbar(GuiVComponent):
    """ GuiStatusbar representa a mensagem que exibe parte da barra de status na parte inferior da janela SAP GUI.
    Ele não inclui as informações do sistema e de login exibidas na área mais à direita da barra de status,
    pois estão disponíveis no objeto GuiSessionInfo. GuiStatusbar estende o objeto GuiVComponent. O prefixo do tipo é sbar.
    """

    def double_click(self) -> None:
        self.component.DoubleClick()

    @property
    def handle(self) -> int:
        """ O identificador de janela do controle que está conectado ao GuiShell.
        """
        return self.component.Handle

    @property
    def message_as_popup(self) -> bool:
        """ Algumas mensagens podem ser exibidas não apenas na barra de status, mas também como uma janela pop-up.
        Nesses casos, esta propriedade é definida como True para que um script saiba que precisa fechar um pop-up para continuar.
        """
        return self.component.MessageAsPopup

    @property
    def message_id(self) -> str:
        """ Este é o nome da classe de mensagem usada na chamada de mensagem ABAP.
        """
        return self.component.MessageId

    @property
    def message_number(self) -> str:
        """ Este é o nome do número da mensagem usado na chamada de mensagem ABAP.
        Geralmente será um número, mas isso não é imposto pelo sistema.
        """
        return self.component.MessageNumber

    @property
    def message_parameter(self) -> str:
        """ Estes são os valores dos parâmetros usados para expandir os espaços reservados na definição do texto da mensagem no dicionário de dados.
        A propriedade text do GuiStatusbar já contém o texto expandido da mensagem. Um máximo de 8 valores de parâmetros podem
        ser fornecidos na codificação ABAP, portanto o índice deve estar na faixa de 0 a 7.
        """
        return self.component.MessageParameter

    @property
    def message_type(self) -> str:
        """ Esta propriedade pode ter qualquer um dos seguintes valores:
        S - Success
        W - Warning
        E - Error
        A - Abort
        I - Information
        """
        return self.component.MessageType


class GuiToolbar(GuiVContainer):
    """ Cada GuiFrameWindow possui uma GuiToolbar.
    O GuiMainWindow possui duas barras de ferramentas, a menos que a segunda tenha sido desativada pela aplicação ABAP.
    A barra de ferramentas superior é a barra de ferramentas do sistema, enquanto a segunda barra de ferramentas é a barra de ferramentas do aplicativo.
    Os filhos de uma GuiToolbar são botões. Os índices dos botões da barra de ferramentas são determinados pelos valores de chave virtual definidos para o botão.
    """

    pass


class GuiTitlebar(GuiVContainer):
    """ A barra de título só é exibida e exposta como um objeto separado no modo Novo Design Visual.
    O prefixo do tipo e o nome do GuiTitlebar são titl.
    Em algumas transações a barra de título pode conter objetos do tipo GuiGosShell.
    """

    pass


class GuiTab(GuiVContainer):
    """ Os objetos GuiTab são filhos de um objeto GuiTabStrip.
    O prefixo do tipo é tabp, o nome é o id do botão da aba retirado do dicionário de dados SAP.
    """

    def scroll_to_left(self) -> None:
        #TODO explicar melhor
        """ ScrollToLeft desloca as guias para que uma determinada guia se torne a leftTab da faixa de guias.
        """
        self.component.ScrollToLeft()

    def select(self) -> None:
        """ Esta função define a guia como a guia selecionada na faixa de guias.
        Alterar a guia selecionada de uma faixa de guias pode causar comunicação com o servidor.
        """
        self.component.Select()


class GuiTabStrip(GuiVContainer):
    """ Uma faixa de guias é um contêiner cujos filhos são do tipo GuiTab.
    O prefixo do tipo é tabulações, o nome é o nome do campo retirado do dicionário de dados SAP.
    Os filhos da faixa de guias são as guias. Embora todas as guias estejam disponíveis a qualquer momento, apenas os filhos da guia selecionada
    existem na hierarquia de objetos para faixas de guias controladas pelo servidor.
    """

    @property
    def char_height(self) -> int:
        """ Altura do GuiTabStrip em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiTabStrip na métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiTabStrip na métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiTabStrip na métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def left_tab(self) -> int:
        """ Esta é a guia mais à esquerda cuja legenda está visível.
        A propriedade leftTab pode ser alterada chamando o método ScrollToLeft de um GuiTab diferente,
        conforme descrito na seção Objeto GuiTab.
        """
        return self.component.LeftTab

    @property
    def selected_tab(self) -> int:
        """ A aba selecionada é aquela cujos descendentes estão visualizados no momento.
        A aba selecionada possui exatamente um filho, que é um GuiScrollContainer. Para selecionar uma guia, você chama o método
        Select da respectiva página da guia. Veja também a seção Objeto GuiTab.
        """
        return self.component.SelectedTab


class GuiShell(GuiVContainer):
    """ GuiShell é um objeto abstrato cuja interface é suportada por todos os controles.
    GuiShell estende o objeto GuiVContainer. O prefixo do tipo é shell, o nome é a última parte do id, shell[n].
    """

    def select_context_menu_item(self, function_code: str) -> None:
        """ Selecione um item no menu de contexto do controle.
        """
        return self.component.SelectContextMenuItem(function_code)

    def select_context_menu_item_by_position(self, position_desc: str) -> None:
        """ Este método permite selecionar um item do menu de contexto usando a posição do item.
        Portanto, é independente do texto do item de menu.
        """
        return self.component.SelectContextMenuItemByPosition(position_desc)

    def select_context_menu_item_by_text(self, text: str) -> None:
        """ Selecione um item de menu de um menu de contexto usando o texto do item e possíveis menus de nível superior.
        """
        return self.component.SelectContextMenuItemByText(text)

    @property
    def acc_description(self) -> str:
        """ Descrição de acessibilidade do shell. Esta descrição pode ser usada para shells que não possuem um elemento de título.
        """
        return self.component.AccDescription

    @property
    def current_context_menu(self) -> GuiContextMenu:
        """ Esta propriedade só é definida quando um menu de contexto está disponível no objeto shell.
        """
        return GuiContextMenu(self.component.CurrentContextMenu)

    @property
    def drag_drop_supported(self) -> bool:
        """ Esta propriedade é True se o shell permitir operações de arrastar e soltar.
        """
        return self.component.DragDropSupported

    @property
    def handle(self) -> int:
        """ O identificador de janela do controle que está conectado ao GuiShell.
        """
        return self.component.Handle

    @property
    def ocx_events(self) -> GuiCollection:
        """ Retorna uma coleção contendo os IDs de eventos do controle ActiveX. Estes são os eventos que o controle pode enviar ao servidor.
        """
        return GuiCollection(self.component.OcxEvents)

    @property
    def sub_type(self) -> str:
        """ Informações adicionais de tipo para identificar o controle representado pelo shell, por exemplo, Picture, TextEdit, GridView…
        """
        return self.component.SubType


class GuiGridView(GuiShell):
    """ A visualização em grade é semelhante ao controle de tabela dynpro, mas significativamente mais poderosa.
    """

    def clear_selection(self) -> None:
        """ Chamar ClearSelection remove todas as seleções de linhas, colunas e células.
        """
        self.component.ClearSelection()

    def click(self, row: int, column: str) -> None:
        """ Esta função emula um clique do mouse em uma determinada célula se os parâmetros forem válidos e gera uma exceção caso contrário.
        """
        self.component.Click(row, column)

    def click_current_cell(self) -> None:
        """ Esta função emula um clique do mouse na célula atual.
        """
        self.component.ClickCurrentCell()

    def context_menu(self) -> None:
        """ Chamar ContextMenu emula a solicitação do menu de contexto.
        """
        self.component.ContextMenu()

    def current_cell_moved(self) -> None:
        """ Esta função notifica o servidor de que uma célula diferente se tornou a célula atual.
        Deve ser chamado sempre que a célula atual for alterada.
        """
        self.component.CurrentCellMoved()

    def delete_rows(self, rows: str) -> None:
        """ As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        """
        # TODO Funções auxiliares
        self.component.DeleteRows(rows)

    def deselect_column(self, column: str) -> None:
        """ Esta função remove a coluna especificada da coleção de colunas selecionadas.
        """
        self.component.DeselectColumn(column)

    def double_click(self, row: int, column: str) -> None:
        """ Esta função emula um clique duplo do mouse em uma determinada célula se os parâmetros forem válidos e gera uma exceção caso contrário.
        """
        self.component.DoubleClick(row, column)

    def double_click_current_cell(self) -> None:
        """ Esta função emula um clique duplo do mouse na célula atual.
        """
        self.component.DoubleClickCurrentCell()

    def duplicate_rows(self, rows: str) -> None:
        """ As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        Para qualquer índice único, uma cópia da linha será inserida no índice fornecido.
        Se um intervalo de índices for duplicado, todas as novas linhas serão inseridas como um bloco, antes das linhas antigas.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        """
        # TODO Funções auxiliares
        self.component.DuplicateRows(rows)

    def get_cell_changeable(self, row: int, column: str) -> bool:
        """ Esta função retorna True se a célula especificada puder ser alterada.
        """
        return self.component.GetCellChangeable(row, column)

    def get_cell_check_box_checked(self, row: int, column: str) -> bool:
        """ Retorna True se a caixa de seleção na posição especificada estiver marcada.
        Lança uma exceção se não houver caixa de seleção na célula especificada.
        """
        return self.component.GetCellCheckBoxChecked(row, column)

    def get_cell_color(self, row: int, column: str) -> int:
        """ Retorna um identificador para a cor da célula.
        Isso pode ser usado para recuperar as informações de cores usando GetColorInfo.
        """
        return self.component.GetCellColor(row, column)

    def get_cell_height(self, row: int, column: str) -> int:
        """ Retorna a altura da célula em pixels.
		"""
        return self.component.GetCellHeight(row, column)

    def get_cell_icon(self, row: int, column: str) -> str:
        """ Retorna a sequência de ícones da célula, se a célula contiver um ícone.
        A string tem o formato de ícone ABAP '@xy@', onde xy é um número ou caractere.
        """
        return self.component.GetCellIcon(row, column)

    def get_cell_left(self, row: int, column: str) -> int:
        """ Retorna a posição esquerda da célula nas coordenadas do cliente.
		"""
        return self.component.GetCellLeft(row, column)

    def get_cell_max_length(self, row: int, column: str) -> int:
        """ Retorna o comprimento máximo da célula em número de bytes.
	    """
        return self.component.GetCellMaxLength(row, column)

    def get_cell_state(self, row: int, column: str) -> str:
        """ Retorna o estado da célula. Os valores possíveis são:
        Normal
        Error
        Warning
        Info
        """
        return self.component.GetCellState(row, column)

    def get_cell_tooltip(self, row: int, column: str) -> str:
        """ Retorna a dica de ferramenta da célula.
        """
        return self.component.GetCellTooltip(row, column)

    def get_cell_top(self, row: int, column: str) -> int:
        """ Retorna a posição superior da célula nas coordenadas do cliente.
		"""
        return self.component.GetCellTop(row, column)

    def get_cell_type(self, row: int, column: str) -> str:
        """ Esta função retorna o tipo da célula especificada. Os valores possíveis são:
        Normal
        Button
        Checkbox
        ValueList
        RadioButton
        """
        return self.component.GetCellType(row, column)

    def get_cell_value(self, row: int, column: str) -> str:
        """ Retorna o valor da célula como uma string.
        """
        return self.component.GetCellValue(row, column)

    def get_cell_width(self, row: int, column: str) -> int:
        """ Retorna a largura da célula em pixels.
        """
        return self.component.GetCellWidth(row, column)

    def get_color_info(self, color: int) -> str:
        """ Retorna a descrição da cor da célula.
        """
        return self.component.GetColorInfo(color)

    def get_column_data_type(self, column: str) -> str:
        """ Retorna o tipo de dados da coluna conforme os 'tipos de dados integrados' do padrão de esquema XML.
        """
        return self.component.GetColumnDataType(column)

    def get_column_position(self, column: str) -> int:
        """ Retorna a posição da coluna conforme mostrado na tela, começando em 1.
        """
        return self.component.GetColumnPosition(column)

    def get_column_sort_type(self, column: str) -> str:
        """ Retorna o tipo de classificação da coluna. Os valores possíveis são:
        None
        Ascending
        Descending
        """
        return self.component.GetColumnSortType(column)

    def get_column_titles(self, column: str) -> object:
        """ Esta função retorna uma coleção de strings usadas para exibir o título de uma coluna.
        O controle escolhe o título apropriado conforme a largura da coluna.
        """
        # TODO Verificar retorno
        return self.component.GetColumnTitles(column)

    def get_column_tooltip(self, column: str) -> str:
        """ A dica de ferramenta de uma coluna contém um texto projetado para ajudar o usuário a compreender o significado da coluna.
        """
        return self.component.GetColumnTooltip(column)

    def get_column_total_type(self, column: str) -> str:
        """ Retorna o tipo total da coluna. Os valores possíveis são:
        None
        Total
        Subtotal
        """
        return self.component.GetColumnTotalType(column)

    def get_displayed_column_title(self, column: str) -> str:
        """ Esta função retorna o título da coluna exibida atualmente.
        Este texto é um dos valores da coleção retornada da função "getColumnTitles".
        """
        return self.component.GetDisplayedColumnTitle(column)

    def get_row_total_level(self, row: int) -> int:
        """ Retorna o nível da linha.
        """
        return self.component.GetRowTotalLevel(row)

    def get_symbol_info(self, symbol: str) -> str:
        """ Retorna a descrição do símbolo na célula.
        """
        return self.component.GetSymbolInfo(symbol)

    def get_toolbar_button_checked(self, button_pos: int) -> bool:
        """ Retorna True se o botão estiver marcado (pressionado).
        """
        return self.component.GetToolbarButtonChecked(button_pos)

    def get_toolbar_button_enabled(self, button_pos: int) -> bool:
        """ Indica se o botão pode ser pressionado.
        """
        return self.component.GetToolbarButtonEnabled(button_pos)

    def get_toolbar_button_icon(self, button_pos: int) -> str:
        """ Retorna o nome do ícone do botão da barra de ferramentas especificado.
        """
        return self.component.GetToolbarButtonIcon(button_pos)

    def get_toolbar_button_id(self, button_pos: int) -> str:
        """ Retorna o ID do botão da barra de ferramentas especificado, conforme definido no dicionário de dados ABAP.
        """
        return self.component.GetToolbarButtonId(button_pos)

    def get_toolbar_button_text(self, button_pos: int) -> str:
        """ Retorna o texto do botão da barra de ferramentas especificado.
        """
        return self.component.GetToolbarButtonText(button_pos)

    def get_toolbar_button_tooltip(self, button_pos: int) -> str:
        """ Retorna a dica de ferramentas do botão da barra de ferramentas especificado.
        """
        return self.component.GetToolbarButtonTooltip(button_pos)

    def get_toolbar_button_type(self, button_pos: int) -> str:
        """ Retorna o tipo do botão da barra de ferramentas especificado. Os valores possíveis são:
        Button
        ButtonAndMenu
        Menu
        Separator
        Group
        CheckBox
        """
        return self.component.GetToolbarButtonType(button_pos)

    def get_toolbar_focus_button(self) -> int:
        """ Retorna a posição do botão da barra de ferramentas com o foco. Se nenhum botão na barra de ferramentas tiver o foco, o método retorna -1.
        """
        return self.component.GetToolbarFocusButton()

    def has_cell_f4_help(self, row: int, column: str) -> bool:
        """ Retorna True se a célula tiver um valor de ajuda.
        """
        return self.component.HasCellF4Help(row, column)

    def history_cur_entry(self, row: int, column: str) -> str:
        """ Retorna o texto da entrada selecionada atualmente da lista de histórico na célula especificada.
        """
        return self.component.HistoryCurEntry(row, column)

    def history_cur_index(self, row: int, column: str) -> int:
        """ Retorna o índice (base zero) da entrada selecionada atualmente na lista de histórico da célula especificada.
        """
        return self.component.HistoryCurIndex(row, column)

    def history_is_active(self, row: int, column: str) -> bool:
        """ Este método retorna True se a lista de histórico de entrada estiver aberta para a célula especificada.
        """
        return self.component.HistoryIsActive(row, column)

    def history_list(self, row: int, column: str) -> GuiCollection:
        """ Este método recupera a lista de entradas de histórico de entrada da célula GuiGridView especificada como uma GuiCollection.
        Os valores da lista de histórico dependem do valor atual contido na célula.
        """
        return GuiCollection(self.component.HistoryList(row, column))

    def insert_rows(self, rows: str) -> None:
        """ As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        Para qualquer índice único, uma nova linha será adicionada no índice fornecido, movendo a linha antiga uma linha para baixo.
        Se um intervalo de índices for inserido, todas as novas linhas serão inseridas como um bloco, antes das linhas antigas.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        """
        # TODO Funções auxiliares
        self.component.InsertRows(rows)

    def is_cell_hotspot(self, row: int, column: str) -> bool:
        """ Retorna True se a célula for um link.
        """
        return self.component.IsCellHotspot(row, column)

    def is_cell_symbol(self, row: int, column: str) -> bool:
        """ Retorna True se o texto na célula for exibido na fonte de símbolo SAP.
        """
        return self.component.IsCellSymbol(row, column)

    def is_cell_total_expander(self, row: int, column: str) -> bool:
        """ Retorna True se a célula contiver um botão de expansão total.
        """
        return self.component.IsCellTotalExpander(row, column)

    def is_column_filtered(self, column: str) -> bool:
        """ Retorna True se um filtro foi aplicado à coluna.
        """
        return self.component.IsColumnFiltered(column)

    def is_column_key(self, column: str) -> bool:
        """ Retorna True se a coluna estiver marcada como uma coluna de chave.
        """
        return self.component.IsColumnKey(column)

    def is_total_row_expanded(self, row: int) -> bool:
        """ Retorna True se a linha que contém um botão de expansão estiver atualmente expandida.
        """
        return self.component.IsTotalRowExpanded(row)

    def modify_cell(self, row: int, column: str, value: str) -> None:
        """ Se a linha e a coluna identificarem uma célula editável válida e o valor tiver um tipo válido para essa célula,
        o valor da célula será alterado. Caso contrário, uma exceção será gerada.
        """
        self.component.ModifyCell(row, column, value)

    def modify_check_box(self, row: int, column: str, checked: bool) -> None:
        """ Se a linha e a coluna identificarem uma célula editável válida contendo uma caixa de seleção e o valor tiver um tipo válido para essa célula,
        o valor da célula será alterado. Caso contrário, uma exceção será gerada.
        """
        self.component.ModifyCheckBox(row, column, checked)

    def move_rows(self, from_row: int, to_row: int, dest_row: int) -> None:
        """ As linhas com um índice maior ou igual a from_row até um índice menor, ou igual a to_row são movidas para a posição de dest_row.
        Passar valores de índice inválidos como parâmetros gera uma exceção.
        """
        self.component.MoveRows(from_row, to_row, dest_row)

    def press_button(self, row: int, column: str) -> None:
        """ Esta função emula o pressionamento de um botão colocado em uma célula específica.
        Ela gera uma exceção se a célula não contiver um botão ou se nem mesmo existir.
        """
        self.component.PressButton(row, column)

    def press_button_current_cell(self) -> None:
        """ Esta função emula o pressionamento de um botão colocado na célula atual.
        Ela gera uma exceção se a célula não contiver um botão.
        """
        self.component.PressButtonCurrentCell()

    def press_column_header(self, column: str) -> None:
        """ Esta função emula um clique do mouse no cabeçalho da coluna se o parâmetro identificar uma coluna válida.
        Caso contrário, gera uma exceção.
        """
        self.component.PressColumnHeader(column)

    def press_enter(self) -> None:
        """ Esta função emula a pressão da tecla Enter.
        """
        self.component.PressEnter()

    def press_f1(self) -> None:
        """ Esta função emula a pressão da tecla F1 enquanto o foco está na visualização da grade.
        """
        self.component.PressF1()

    def press_f4(self) -> None:
        """ Esta função emula a pressão da tecla F4.
        """
        self.component.PressF4()

    def press_toolbar_button(self, button_id: str) -> None:
        """ Esta função emula o clique em um botão na barra de ferramentas da visualização da grade.
        """
        self.component.PressToolbarButton(button_id)

    def press_toolbar_context_button(self, button_id: str) -> None:
        """ Esta função emula a abertura do menu de contexto na barra de ferramentas da visualização da grade.
        """
        self.component.PressToolbarContextButton(button_id)

    def press_total_row(self, row: int, column: str) -> None:
        """ Esta função emula a pressão do botão da linha total, que expande ou condensa as linhas agrupadas.
        """
        self.component.PressTotalRow(row, column)

    def press_total_row_current_cell(self) -> None:
        """ Esta função difere de PressTotalRow apenas no fato de tentar pressionar o botão de expansão na célula atual.
        """
        self.component.PressTotalRowCurrentCell()

    def select_all(self) -> None:
        """ Esta função seleciona todo o conteúdo da grade (ou seja, todas as linhas e todas as colunas).
        """
        self.component.SelectAll()

    def select_column(self, column: str) -> None:
        """ Esta função adiciona a coluna especificada à coleção das colunas selecionadas.
        """
        self.component.SelectColumn(column)

    def selection_changed(self) -> None:
        """ Esta função notifica o servidor que a seleção foi alterada.
        """
        self.component.SelectionChanged()

    def select_toolbar_menu_item(self, item_id: str) -> None:
        """ Esta função emula a seleção de um item no menu de contexto da barra de ferramentas da visualização da grade.
        """
        self.component.SelectToolbarMenuItem(item_id)

    def set_column_width(self, column: str, width: int) -> None:
        """ Esta função define a largura de uma coluna em caracteres.
        """
        self.component.SetColumnWidth(column, width)

    def set_current_cell(self, row: int, column: str) -> None:
        """ Se a linha e a coluna identificarem uma célula válida, essa célula se tornará a célula atual.
        """
        self.component.SetCurrentCell(row, column)

    def trigger_modified(self) -> None:
        """ Notifica o servidor sobre várias alterações nas células.
        """
        self.component.TriggerModified()

    @property
    def column_count(self) -> int:
        """ Esta propriedade representa o número de colunas no controle.
        """
        return self.component.ColumnCount

    @property
    def column_order(self) -> object:
        """ Esta coleção contém todos os identificadores de coluna na ordem em que estão atualmente exibidos.
        """
        # TODO Verificar retorno
        return self.component.ColumnOrder

    @column_order.setter
    def column_order(self, order: object = None) -> None:
        """ Esta coleção contém todos os identificadores de coluna na ordem em que estão atualmente exibidos.
        """
        # TODO Verificar retorno
        self.component.ColumnOrder = order

    @property
    def current_cell_column(self) -> str:
        """ A string que identifica uma coluna é o nome do campo definido no dicionário de dados do SAP.
        """
        return self.component.CurrentCellColumn

    @current_cell_column.setter
    def current_cell_column(self, column: str = None) -> None:
        """ A string que identifica uma coluna é o nome do campo definido no dicionário de dados do SAP.
        """
        self.component.CurrentCellColumn = column

    @property
    def current_cell_row(self) -> int:
        """ O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        """
        return self.component.CurrentCellRow

    @current_cell_row.setter
    def current_cell_row(self, row: int = None) -> None:
        """ O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        """
        self.component.CurrentCellRow = row

    @property
    def first_visible_column(self) -> str:
        """ Esta propriedade representa a primeira coluna visível da área de rolagem da visualização da grade.
        """
        return self.component.FirstVisibleColumn

    @first_visible_column.setter
    def first_visible_column(self, column: str = None) -> None:
        """ Esta propriedade representa a primeira coluna visível da área de rolagem da visualização da grade.
        """
        self.component.FirstVisibleColumn = column

    @property
    def first_visible_row(self) -> int:
        """ Este é o índice da primeira linha visível na grade.
        """
        return self.component.FirstVisibleRow

    @first_visible_row.setter
    def first_visible_row(self, row: int = None) -> None:
        """ Este é o índice da primeira linha visível na grade.
        """
        self.component.FirstVisibleRow = row

    @property
    def frozen_column_count(self) -> int:
        """ Esta propriedade representa o número de colunas excluídas da rolagem horizontal.
        """
        return self.component.FrozenColumnCount

    @property
    def row_count(self) -> int:
        """ Esta propriedade representa o número de linhas no controle.
        """
        return self.component.RowCount

    @property
    def selected_cells(self) -> object:
        """ A coleção de células selecionadas contém strings no formato "<índice da linha>,<identificador da coluna>", como "0,CARRID".
        """
        # TODO Verificar retorno
        return self.component.SelectedCells

    @selected_cells.setter
    def selected_cells(self, cells: object = None) -> None:
        """ A coleção de células selecionadas contém strings no formato "<índice da linha>,<identificador da coluna>", como "0,CARRID".
        """
        # TODO Verificar retorno
        self.component.SelectedCells = cells

    @property
    def selected_columns(self) -> object:
        """ As colunas selecionadas estão disponíveis como uma coleção de strings, assim como a string CurrentCellColumn.
        """
        # TODO Verificar retorno
        return self.component.SelectedColumns

    @selected_columns.setter
    def selected_columns(self, columns: object = None) -> None:
        """ As colunas selecionadas estão disponíveis como uma coleção de strings, assim como a string CurrentCellColumn.
        """
        # TODO Verificar retorno
        self.component.SelectedColumns = columns

    @property
    def selected_rows(self) -> str:
        """ A string é uma lista separada por vírgulas de números de índice de linha ou intervalos de índice, como "1,2,4-8,10".
        """
        return self.component.SelectedRows

    @selected_rows.setter
    def selected_rows(self, rows: str = None) -> None:
        """ A string é uma lista separada por vírgulas de números de índice de linha ou intervalos de índice, como "1,2,4-8,10".
        """
        self.component.SelectedRows = rows

    @property
    def selection_mode(self) -> str:
        """ Retorna o modo de seleção atual da grade.
        """
        return self.component.SelectionMode

    @property
    def title(self) -> str:
        """ Esta propriedade representa o título do controle da grade.
        """
        return self.component.Title

    @property
    def toolbar_button_count(self) -> int:
        """ O número de botões da barra de ferramentas, incluindo separadores.
        """
        return self.component.ToolbarButtonCount

    @property
    def visible_row_count(self) -> int:
        """ Recupera o número de linhas visíveis da grade.
        """
        return self.component.VisibleRowCount


class GuiSimpleContainer(GuiVContainer):
    """ Este contêiner representa subtelas não roláveis. Ele não possui nenhuma funcionalidade
    além das interfaces herdadas.
    O prefixo do tipo é sub, o nome é gerado a partir das configurações do dicionário de dados.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Obtém uma propriedade da lista.
        property: A propriedade que você deseja obter. Consulte a documentação do objeto GuiLabel para obter mais informações.
        Retorna o valor da propriedade especificada.
        """
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Obtém uma propriedade da lista sem considerar propriedades de elementos pais.
        property: A propriedade que você deseja obter. Consulte a documentação do objeto GuiLabel para obter mais informações.
        Retorna o valor da propriedade especificada, ignorando propriedades de elementos pais.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_step_loop(self) -> bool:
        """ Esta propriedade é True se o contêiner for um contêiner de loop de etapa.
        """
        return self.component.IsStepLoop

    @property
    def loop_col_count(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de colunas no loop de etapa.
        """
        return self.component.LoopColCount

    @property
    def loop_current_col(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número atual da linha no loop de etapa.
        """
        return self.component.LoopCurrentCol

    @property
    def loop_current_col_count(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de colunas na linha atual do loop de etapa.
        """
        return self.component.LoopCurrentColCount

    @property
    def loop_current_row(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número atual da coluna no loop de etapa.
        """
        return self.component.LoopCurrentRow

    @property
    def loop_row_count(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de linhas no loop de etapa.
        """
        return self.component.LoopRowCount


class GuiToolbarControl(GuiShell):
    # TODO Criar descrição

    def get_button_checked(self, button_pos: int) -> int:
        """ Retorna se o botão na posição especificada está atualmente marcado (pressionado).
        """
        return self.component.GetButtonChecked(button_pos)

    def get_button_enabled(self, button_pos: int) -> int:
        """ Indica se o botão na posição especificada pode ser pressionado.
        """
        return self.component.GetButtonEnabled(button_pos)

    def get_button_icon(self, button_pos: int) -> str:
        """ Retorna o nome do ícone do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonIcon(button_pos)

    def get_button_id(self, button_pos: int) -> str:
        """ Retorna o ID do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonId(button_pos)

    def get_button_text(self, button_pos: int) -> str:
        """ Retorna o texto do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonText(button_pos)

    def get_button_tooltip(self, button_pos: int) -> str:
        """ Retorna a dica de ferramenta do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonTooltip(button_pos)

    def get_button_type(self, button_pos: int) -> str:
        """ Retorna o tipo do botão de barra de ferramentas especificado. Valores possíveis são: "Button", "ButtonAndMenu", "Menu", "Separator", "Group", "CheckBox".
        """
        return self.component.GetButtonType(button_pos)

    def get_menu_item_id_from_position(self, pos: int) -> str:
        """ Esta função retorna o identificador do item de menu com índice Position.
        """
        return self.component.GetMenuItemIdFromPosition(pos)

    def press_button(self, id_button: str) -> None:
        """ Esta função emula o pressionamento do botão com o ID fornecido.
        """
        self.component.PressButton(id_button)

    def press_context_button(self, id_button: str) -> None:
        """ Esta função emula o pressionamento do botão de contexto com o ID fornecido.
        """
        self.component.PressContextButton(id_button)

    def select_menu_item(self, id_item: str) -> None:
        """ Esta função emula a seleção do item de menu com o ID fornecido.
        """
        self.component.SelectMenuItem(id_item)

    def select_menu_item_by_text(self, str_text: str) -> None:
        """ Esta função emula a seleção do item de menu pelo texto do item de menu.
        """
        self.component.SelectMenuItemByText(str_text)

    @property
    def button_count(self) -> int:
        """ O número de botões da barra de ferramentas, incluindo separadores.
        """
        return self.component.ButtonCount

    @property
    def focused_button(self) -> int:
        """ O índice baseado em zero do botão que atualmente tem o foco.
        """
        return self.component.FocusedButton

    @focused_button.setter
    def focused_button(self, focused_button_index: int = None) -> None:
        """ O índice baseado em zero do botão que atualmente tem o foco.
        """
        self.component.FocusedButton = focused_button_index


class GuiTextField(GuiVComponent):
    """ GuiTextField estende o objeto GuiVComponent. O prefixo do tipo é txt, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Retorna uma propriedade de lista específica.
        Para mais informações, consulte a documentação sobre o método GetListProperty no objeto GuiLabel.
        """
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Este método retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Consulte GuiLabel::GetListProperty para uma descrição dos atributos disponíveis.
        Ao contrário do método GetListProperty, o GetListPropertyNonRec retornará apenas informações definidas para o elemento
        específico e ignorará propriedades de lista definidas para elementos pais.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def caret_position(self) -> int:
        """ A posição do cursor dentro de um campo de texto.
        """
        return self.component.CaretPosition

    @caret_position.setter
    def caret_position(self, caret_position: int = None) -> None:
        """ A posição do cursor dentro de um campo de texto.
        """
        self.component.CaretPosition = caret_position

    @property
    def displayed_text(self) -> str:
        """ Esta propriedade contém o texto conforme exibido na tela, incluindo espaços em branco precedentes ou subsequentes.
            Esses espaços em branco são removidos da propriedade de texto.
        """
        return self.component.DisplayedText

    @property
    def highlighted(self) -> bool:
        """ Esta propriedade é True se a flag Highlighted estiver definida no screen painter para o elemento dynpro.
        """
        return self.component.Highlighted

    @property
    def history_cur_entry(self) -> str:
        """ Texto da entrada atualmente focada na lista de histórico.
        """
        return self.component.HistoryCurEntry

    @property
    def history_cur_index(self) -> int:
        """ Índice atualmente focado na lista suspensa de histórico.
        """
        return self.component.HistoryCurIndex

    @property
    def history_is_active(self) -> bool:
        """ Esta propriedade é True se o histórico local do campo de entrada estiver atualmente aberto.
        """
        return self.component.HistoryIsActive

    @property
    def history_list(self) -> object:
        """ Lista de entradas na caixa de histórico local.
        """
        return self.component.HistoryList

    @property
    def is_hotspot(self) -> bool:
        """ Elementos dynpro, como rótulos, podem ser configurados para causar uma ida e volta quando clicados. Nesse caso, o cursor do mouse muda para a forma de mão. Isso é chamado de hot spot.
        """
        return self.component.IsHotspot

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign left'.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_o_field(self) -> bool:
        """ OField é um elemento especial de dynpro ABAP, o Output Field. Esses campos podem ser definidos programaticamente com um valor em tempo de execução. Nesse aspecto, eles diferem dos rótulos. No entanto, eles não podem ser usados para inserir dados, portanto, não são campos de entrada.
        """
        return self.component.IsOField

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def left_label(self) -> GuiLabel:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo esquerdo do controle.
        """
        return GuiLabel(self.component.LeftLabel)

    @property
    def max_length(self) -> int:
        """ O comprimento máximo do texto que pode ser escrito em um campo de texto é contado em unidades de código. Em clientes não Unicode, essas unidades são equivalentes a bytes.
        """
        return self.component.MaxLength

    @property
    def numerical(self) -> bool:
        """ Se esta flag estiver definida, apenas números e caracteres especiais podem ser escritos no campo de texto.
        """
        return self.component.Numerical

    @property
    def required(self) -> bool:
        """ Esta propriedade é True se o componente for um valor obrigatório para a tela.
        """
        return self.component.Required

    @property
    def right_label(self) -> GuiLabel:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo direito do controle.
        """
        return GuiLabel(self.component.RightLabel)


class GuiCTextField(GuiTextField):
    """ Se o cursor estiver definido em um campo de texto do tipo GuiCTextField,
    um botão de caixa de combinação será exibido à direita do campo de texto.
    Pressionar este botão equivale a pressionar a tecla F4. O botão não é representado no
    modelo de objeto de script como um objeto separado; é considerado parte do campo de texto.
    Não há outras diferenças entre GuiTextField e GuiCTextField. GuiCTextField estende o GuiTextField.
    O prefixo do tipo é ctxt, o nome é o Fieldname retirado do dicionário de dados SAP.
    """

    # TODO Adicionar funções auxiliares

    pass


class GuiOkCodeField(GuiVComponent):
    """ O GuiOkCodeField é colocado na barra de ferramentas superior da janela principal.
    É uma caixa de combinação na qual comandos podem ser inseridos. Definir o texto de GuiOkCodeField
    não executará o comando até que a comunicação do servidor seja iniciada, por exemplo, emulando a tecla Enter (VKey 0).
    O prefixo do tipo é okcd, o nome está vazio.
    """

    def press_f1(self) -> None:
        """ Emule pressionando a tecla F1 enquanto o foco está no GuiOkCodeField.
        """
        self.component.PressF1()

    @property
    def opened(self) -> bool:
        """ Em designs SAP GUI mais recentes que o design Clássico, o GuiOkCodeField pode ser recolhido usando
        o botão de seta à direita dele. No SAP GUI para Windows, o GuiOkCodeField também pode ser recolhido por
        meio de uma configuração no registro do Windows.
        Esta propriedade contém False se o GuiOkCodeField estiver recolhido.
        """
        return self.component.Opened


class GuiInputFieldControl(GuiShell):
    """ GuiInputFieldControl oferece um campo de entrada que pode ser usado dentro de
    contêineres de controle (ao contrário do elemento Dynpro representado por GuiTextField)
    """

    def submit(self):
        """ Submete a entrada para a aplicação.
        Esta função envia a entrada inserida para a aplicação.
        """
        self.component.Submit()

    @property
    def button_tooltip(self) -> str:
        """ Tooltip do botão de envio/consulta.
        """
        return self.component.ButtonTooltip

    @property
    def find_button_activated(self) -> bool:
        """ Esta propriedade é True quando o botão Find está ativo.
        """
        return self.component.FindButtonActivated

    @property
    def history_opened(self) -> bool:
        """ Esta propriedade é True quando o histórico de entrada está aberto.
        """
        return self.component.HistoryOpened

    @property
    def label_text(self) -> str:
        """ O texto do rótulo pertencente ao campo de entrada.
        """
        return self.component.LabelText

    @property
    def text(self) -> str:
        """ Conteúdo de texto do campo de entrada em si.
        """
        return self.component.Text

    @text.setter
    def text(self, new_text: str = None) -> None:
        """ Conteúdo de texto do campo de entrada em si.
        """
        self.component.Text = new_text


class GuiPasswordField(GuiTextField):
    """ A única diferença entre GuiTextField e GuiPasswordField é que a propriedade Text não pode ser lida para um campo de senha.
    O texto retornado está sempre vazio. Durante a gravação a senha também não é salva no script gravado. GuiPasswordField
    estende o GuiTextField. O prefixo do tipo é pwd, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    pass


class GuiSplit(GuiShell):
    # TODO Criar descrição

    def get_col_size(self, id_column: int) -> int:
        """ Obtém o tamanho da coluna do divisor especificado.
        Id: O índice da coluna do divisor (começando com índice 1).
        Retorna o tamanho da coluna do divisor especificado em porcentagem.
        """
        return self.component.GetColSize(id_column)

    def get_row_size(self, id_row: int) -> int:
        """ Obtém o tamanho da linha do divisor especificado.
        Id: O índice da linha do divisor (começando com índice 1).
        Retorna o tamanho da linha do divisor especificado em porcentagem.
        """
        return self.component.GetRowSize(id_row)

    def set_col_size(self, id_column: int, size: int):
        """ Define o tamanho da coluna do divisor especificado.
        Id: O índice da coluna do divisor (começando com índice 1).
        Size: O tamanho desejado em porcentagem.
        """
        self.component.SetColSize(id_column, size)

    def set_row_size(self, id_row: int, size: int):
        """ Define o tamanho da linha do divisor especificado.
        Id: O índice da linha do divisor (começando com índice 1).
        Size: O tamanho desejado em porcentagem.
        """
        self.component.SetRowSize(id_row, size)

    @property
    def is_vertical(self) -> bool:
        """ Esta propriedade contém True se as células divisoras do GuiSplit estiverem alinhadas verticalmente e False se estiverem alinhadas horizontalmente.
        """
        return self.component.IsVertical


class GuiMenubar(GuiVContainer):
    """ Apenas a janela principal possui uma barra de menu.
    Os filhos da barra de menu são menus. GuiMenubar estende o objeto GuiVContainer.
    O prefixo e o nome do tipo são mbar.
    """

    pass


class GuiLabel(GuiVComponent):
    """ GuiLabel representa uma etiqueta de texto.
    O prefixo do tipo é lbl, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Retorna propriedades de contêineres em geral.
        property: A propriedade que você deseja obter. Consulte a documentação para opções disponíveis.
        Retorna o valor da propriedade especificada.
        """
        # TODO Verificar documentação novamente e fazer funções auxiliares
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Veja GuiLabel::GetListProperty para uma descrição dos atributos disponíveis.
        Ao contrário do método GetListProperty, GetListPropertyNonRec só retornará informações definidas para o elemento específico
        e ignorará as propriedades definidas para elementos pais.
        property: A propriedade que você deseja obter. Consulte a documentação para opções disponíveis.
        Retorna o valor da propriedade especificada.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def caret_position(self) -> int:
        """ Definir a posição do cursor dentro de um rótulo é possível, mesmo que não seja visualizada como um cursor pelo SAP GUI.
        No entanto, a posição é transmitida para o servidor, para que a lógica da aplicação ABAP possa depender dessa posição.
        """
        return self.component.CaretPosition

    @caret_position.setter
    def caret_position(self, caret_position: int = None) -> None:
        """ Definir a posição do cursor dentro de um rótulo é possível, mesmo que não seja visualizada como um cursor pelo SAP GUI.
        No entanto, a posição é transmitida para o servidor, para que a lógica da aplicação ABAP possa depender dessa posição.
        """
        self.component.CaretPosition = caret_position

    @property
    def color_index(self) -> int:
        """ Este número define o índice da cor da lista deste elemento.
        """
        return self.component.ColorIndex

    @property
    def color_intensified(self) -> bool:
        """ Esta propriedade é True se a flag Intensified estiver definida no screen painter para este elemento dynpro.
        """
        return self.component.ColorIntensified

    @property
    def color_inverse(self) -> bool:
        """ Esta propriedade é True se o estilo de cor inversa estiver definido no screen painter para o elemento.
        """
        return self.component.ColorInverse

    @property
    def displayed_text(self) -> str:
        """ Esta propriedade contém o texto conforme exibido na tela, incluindo espaços em branco precedentes ou subsequentes.
        Esses espaços em branco são removidos da propriedade de texto.
        """
        return self.component.DisplayedText

    @property
    def highlighted(self) -> bool:
        """ Esta propriedade é True se a flag Highlighted estiver definida no screen painter para o elemento dynpro.
        """
        return self.component.Highlighted

    @property
    def is_hotspot(self) -> bool:
        """ Elementos dynpro, como rótulos, podem ser configurados para causar uma viagem de ida e volta quando clicados.
        Nesse caso, o cursor do mouse muda para a forma de mão. Isso é chamado de ponto de acesso.
        """
        return self.component.IsHotspot

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é definida se o rótulo foi atribuído como rótulo esquerdo de outro controle.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é definida se o rótulo foi atribuído como rótulo direito de outro controle.
        """
        return self.component.IsRightLabel

    @property
    def max_length(self) -> int:
        """ O comprimento máximo do texto de um rótulo é contado em unidades de código. Em clientes não Unicode, essas unidades são equivalentes a bytes.
        """
        return self.component.MaxLength

    @property
    def numerical(self) -> bool:
        """ Esta bandeira é True se o rótulo só puder conter números.
        """
        return self.component.Numerical

    @property
    def row_text(self) -> str:
        """ Esta propriedade está disponível apenas em telas de lista ABAP. Ela retorna o texto da linha inteira que contém o componente atual.
        """
        return self.component.RowText


class GuiCheckBox(GuiVComponent):
    """ GuiCheckBox representa uma CheckBox no SAP.
    O prefixo do tipo é chk, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Para mais informações consulte a documentação sobre o método GetListProperty dentro do GuiLabel Object.
        """
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Este método retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Consulte GuiLabel::GetListProperty para obter uma descrição dos atributos disponíveis.
        Em contraste com o método GetListProperty, GetListPropertyNonRec retornará apenas informações definidas para o elemento específico e
        ignorará as propriedades da lista definidas para elementos pais.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def color_index(self) -> int:
        """ Este número define o índice da cor da lista deste elemento.
        """
        return self.component.ColorIndex

    @property
    def color_intensified(self) -> bool:
        """ Esta propriedade será True se o sinalizador Intensificado estiver definido no Screen Painter para este elemento dynpro.
        """
        return self.component.ColorIntensified

    @property
    def color_inverse(self) -> bool:
        """ Esta propriedade será True se o estilo de cor inverso estiver definido no Screen Painter para o elemento.
        """
        return self.component.ColorInverse

    @property
    def flushing(self) -> bool:
        """ Alguns componentes, como botões de opção ou caixas de seleção, podem causar uma viagem de ida e
        volta quando seu valor for alterado. Se for esse o caso, a propriedade Flushing é True.
        """
        return self.component.Flushing

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver o sinalizador 'atribuir à esquerda'.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP e não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver o sinalizador 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def left_label(self) -> bool:
        """ Etiqueta esquerda do componente. O rótulo é atribuído no Screen Painter, usando o sinalizador 'assign left'.
        """
        return self.component.LeftLabel

    @property
    def right_label(self) -> bool:
        """ Etiqueta direita do componente.
        Esta propriedade é definida no Screen Painter usando o sinalizador 'assign right'.
        """
        return self.component.RightLabel

    @property
    def row_text(self) -> bool:
        """ Esta propriedade só está disponível em telas de lista ABAP.
        Ele retorna o texto da linha while que contém o componente atual.
        """
        return self.component.RowText

    @property
    def selected(self) -> bool:
        """ Assim como os botões de opção, marcar uma caixa de seleção pode
        causar comunicação com o servidor, dependendo da definição do ABAP Screen Painter.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, option: bool) -> None:
        """ Assim como os botões de opção, marcar uma caixa de seleção pode
        causar comunicação com o servidor, dependendo da definição do ABAP Screen Painter.
        """
        self.component.Selected = option


class GuiBox(GuiVComponent):
    """ Uma GuiBox é um quadro simples com um nome (também chamado de "Group Box").
    Os itens dentro da moldura não são filhos da caixa. O prefixo do tipo é "caixa".
    """

    @property
    def char_height(self) -> int:
        """ Altura do GuiBox em caracteres métricos.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiBox em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiBox em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiBox em métrica de caracteres.
        """
        return self.component.CharWidth


class GuiTextedit(GuiShell):
    """ O controle TextEdit é um controle de edição multilinha que oferece vários benefícios possíveis.
    No que diz respeito aos scripts, a possibilidade de proteger partes do texto contra edição pelo usuário
    é especialmente útil. GuiTextedit estende o objeto GuiShell.
    """

    def context_menu(self) -> None:
        """ Chamar ContextMenu emula a solicitação de menu de contexto.
        """
        self.component.ContextMenu()

    def double_click(self) -> None:
        """ Esta função emula um clique duplo do mouse.
        Para definir a seleção, a função setSelectionIndexes pode ser chamada antecipadamente.
        """
        self.component.DoubleClick()

    def get_line_text(self, n_line: int) -> str:
        """ Retorna o texto da linha especificada.
        """
        return self.component.GetLineText(n_line)

    def get_unprotected_text_part(self, part: int) -> str:
        """ Esta função recupera o conteúdo de uma parte de texto desprotegida usando o índice baseado em zero, part.
        """
        return self.component.GetUnprotectedTextPart(part)

    def is_breakpoint_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada contiver um ponto de interrupção.
        """
        return self.component.IsBreakpointLine(n_line)

    def is_comment_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada for uma linha de comentário.
        """
        return self.component.IsCommentLine(n_line)

    def is_highlighted_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada estiver destacada.
        """
        return self.component.IsHighlightedLine(n_line)

    def is_protected_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada estiver protegida.
        """
        return self.component.IsProtectedLine(n_line)

    def is_selected_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada estiver selecionada.
        """
        return self.component.IsSelectedLine(n_line)

    def modified_status_changed(self, status: int) -> None:
        """ Esta função emula a alteração do status modificado.
        """
        self.component.ModifiedStatusChanged(status)

    def multiple_files_dropped(self, files: list) -> None:
        """ Emula uma operação de arrastar e soltar, na qual vários arquivos são soltos no controle de texto.
        A lista contém, para cada arquivo, o nome completo do arquivo como uma string.
        """
        self.component.MultipleFilesDropped(files)

    def press_f1(self) -> None:
        """ Esta função emula a pressão da tecla F1 no teclado.
        """
        self.component.PressF1()

    def press_f4(self) -> None:
        """ Esta função emula a pressão da tecla F4 no teclado.
        """
        self.component.PressF4()

    def set_selection_indexes(self, start: int, end: int) -> None:
        """ Esta função define a faixa de texto visualmente selecionada. start e end são índices absolutos de caracteres baseados em zero.
        start corresponde à posição onde a seleção começa e end é a posição do primeiro caractere após a seleção.
        Observe que definir start igual a end resulta na definição do cursor nessa posição.
        """
        self.component.SetSelectionIndexes(start, end)

    def set_unprotected_text_part(self, part: int, text: str) -> int:
        """ Esta função atribui o conteúdo do texto à parte de texto desprotegida com índice baseado em zero, part.
        A função retorna True se foi possível realizar a atribuição. Caso contrário, retorna False.
        """
        return self.component.SetUnprotectedTextPart(part, text)

    def single_file_dropped(self, filename: str) -> None:
        """ Esta função emula a queda de um único arquivo com o caminho do diretório fileName.
        """
        self.component.SingleFileDropped(filename)

    @property
    def current_column(self) -> int:
        """ O número da coluna na qual o cursor de texto está atualmente posicionado.
        """
        return self.component.CurrentColumn

    @property
    def current_line(self) -> int:
        """ O número da linha na qual o cursor de texto está atualmente posicionado.
        """
        return self.component.CurrentLine

    @property
    def first_visible_line(self) -> int:
        """ A primeira linha visível é visualizada na borda superior do controle.
        """
        return self.component.FirstVisibleLine

    @first_visible_line.setter
    def first_visible_line(self, line_number: int = None) -> None:
        """ A primeira linha visível é visualizada na borda superior do controle.
        """
        self.component.FirstVisibleLine = line_number

    @property
    def last_visible_line(self) -> int:
        """ O número da última linha que está atualmente visível.
        """
        return self.component.LastVisibleLine

    @property
    def line_count(self) -> int:
        """ O número de todas as linhas no documento atual.
        """
        return self.component.LineCount

    @property
    def number_of_unprotected_text_parts(self) -> int:
        """ O número de partes de texto não protegidas, que estão contidas.
        """
        return self.component.NumberOfUnprotectedTextParts

    @property
    def selected_text(self) -> str:
        """ O texto atualmente selecionado.
        """
        return self.component.SelectedText

    @property
    def selection_end_column(self) -> int:
        """ O número da coluna na qual a seleção atual termina.
        """
        return self.component.SelectionEndColumn

    @property
    def selection_end_line(self) -> int:
        """ O número da linha na qual a seleção atual termina.
        """
        return self.component.SelectionEndLine

    @property
    def selection_index_end(self) -> int:
        """ Recupera o índice de caractere absoluto, baseado em zero, do ponto final da faixa de texto visualmente selecionada, ou seja, a posição onde a seleção termina.
        """
        return self.component.SelectionIndexEnd

    @property
    def selection_index_start(self) -> int:
        """ Recupera o índice de caractere absoluto, baseado em zero, do ponto de partida da faixa de texto visualmente selecionada, ou seja, a posição onde a seleção começa.
        """
        return self.component.SelectionIndexStart

    @property
    def selection_start_column(self) -> int:
        """ O número da coluna na qual a seleção atual começa.
        """
        return self.component.SelectionStartColumn

    @property
    def selection_start_line(self) -> int:
        """ O número da linha na qual a seleção atual começa.
        """
        return self.component.SelectionStartLine


class GuiComboBoxEntry:

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    @property
    def key(self) -> str:
        """ Valor-chave da entrada da caixa de combinação.
        """
        return self.component.Key

    @property
    def pos(self) -> int:
        """ Posição da entrada da caixa de combinação. O intervalo vai de 1 ao número de entradas na caixa de combinação.
        """
        return self.component.Pos

    @property
    def value(self) -> str:
        """ Value of the combo box entry.
        """
        return self.component.Value


class GuiComboBox(GuiVComponent):
    """ O GuiComboBox é um pouco semelhante ao GuiCTextField, mas tem uma implementação completamente diferente.
    Enquanto pressionar o botão da caixa de combinação de um GuiCTextField abrirá um novo dynpro ou controle no qual uma
    seleção pode ser feita, o GuiComboBox recupera todas as opções possíveis na inicialização do servidor, para que a
    seleção seja feita exclusivamente no cliente. GuiComboBox estende o objeto GuiVComponent. O prefixo do tipo é cmb,
    o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def set_key_space(self) -> None:
        """ Esta função define a propriedade key da caixa de combinação para o caractere de espaço. Foi introduzido para eCATT.
        """
        self.component.SetKeySpace()

    @property
    def char_height(self) -> int:
        """ Altura do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def cur_list_box_entry(self) -> GuiComboBoxEntry:
        """ A entrada atualmente focada na lista suspensa.
        """
        return GuiComboBoxEntry(self.component.CurListBoxEntry)

    @property
    def entries(self) -> GuiCollection:
        """ Todos os membros desta coleção são do tipo GuiComboBoxEntry e têm apenas duas propriedades,
        chave e valor, ambas do tipo String. O key data pode ser exibido no SAP GUI configurando as
        opções 'Show keys... ' no diálogo de opções do SAP GUI.
        """
        return GuiCollection(self.component.Entries)

    @property
    def flushing(self) -> bool:
        """ Alguns componentes, como botões de rádio, caixas de seleção ou caixas de combinação,
        podem causar uma round trip quando seu valor é alterado. Se for o caso, a propriedade Flushing é Verdadeira.
        """
        return self.component.Flushing

    @property
    def highlighted(self) -> bool:
        """ Esta propriedade é Verdadeira se a flag Highlighted estiver definida no Screen Painter para a caixa de combinação.
        """
        return self.component.Highlighted

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é Verdadeira se a caixa de combinação tiver a flag 'assign left'.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_box_active(self) -> bool:
        """ Esta propriedade é Verdadeira se a lista suspensa da caixa de combinação estiver atualmente aberta.
        """
        return self.component.IsListBoxActive

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é Verdadeira se a caixa de combinação tiver a flag 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def key(self) -> str:
        """ Esta é a chave do item atualmente selecionado. Você pode alterar este item definindo a propriedade Key para um novo valor.
        """
        return self.component.Key

    @key.setter
    def key(self, key: str = None) -> None:
        """ Esta é a chave do item atualmente selecionado. Você pode alterar este item definindo a propriedade Key para um novo valor.
        """
        self.component.Key = key

    @property
    def left_label(self) -> str:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo esquerdo da caixa de combinação.
        """
        return self.component.LeftLabel

    @property
    def required(self) -> bool:
        """ Se a flag Required estiver definida para uma caixa de combinação, a entrada vazia não poderá ser selecionada na lista.
        """
        return self.component.Required

    @property
    def right_label(self) -> GuiVComponent:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo direito da caixa de combinação.
        """
        return GuiVComponent(self.component.RightLabel)

    @property
    def show_key(self) -> bool:
        """ Esta propriedade é Verdadeira se a caixa de combinação mostrar tanto as chaves
        quanto os valores (isso pode ser configurado definindo as opções 'Show keys... '
        no diálogo de opções do SAP GUI).
        """
        return self.component.ShowKey

    @property
    def value(self) -> str:
        """ Este é o valor do item atualmente selecionado. Você pode alterar este item definindo a propriedade Value para um novo valor.
        """
        return self.component.Value

    @value.setter
    def value(self, value: str = None) -> None:
        """ Este é o valor do item atualmente selecionado. Você pode alterar este item definindo a propriedade Value para um novo valor.
        """
        self.component.Value = value


class GuiComboBoxControl(GuiShell):
    # TODO Criar uma descrição

    def fire_selected(self) -> None:
        """ Envia evento "selecionado".
        """
        self.component.FireSelected()

    @property
    def entries(self) -> GuiCollection:
        """ As entradas são novamente uma GuiCollection com: key(index=0), text(index=1) o texto de cada entrada que você pode obter por meio desta coleção.
        """
        return GuiCollection(self.component.Entries)

    @property
    def label_text(self) -> str:
        """ Texto da etiqueta.
        """
        return self.component.LabelText

    @property
    def selected(self) -> str:
        """ A chave da entrada atualmente selecionada da caixa de combinação.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, select: str = None) -> None:
        """ A chave da entrada atualmente selecionada da caixa de combinação.
        """
        self.component.Selected = select

    @property
    def text(self) -> str:
        """ Texto atual da caixa de combinação.
        """
        return self.component.Text


class GuiRadioButton(GuiVComponent):
    """ O prefixo do tipo é rad, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def select(self) -> None:
        """ Selecionar um botão de opção automaticamente desmarca todos os outros botões dentro do mesmo grupo.
        Isso pode causar uma viagem de ida e volta ao servidor, dependendo da definição do botão no screen painter.
        """
        self.component.Select()

    @property
    def char_height(self) -> int:
        """ Altura do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def flushing(self) -> bool:
        """ Alguns componentes, como botões de rádio ou caixas de seleção, podem causar uma viagem de ida e volta quando seu valor é alterado. Se for o caso, a propriedade Flushing é True.
        """
        return self.component.Flushing

    @property
    def group_count(self) -> int:
        """ O número de botões de rádio no mesmo grupo ao qual o objeto atual pertence.
        """
        return self.component.GroupCount

    @property
    def group_members(self) -> object:
        """ A coleção de objetos GuiRadioButton pertencentes ao mesmo grupo de botões de rádio.
        """
        return self.component.GroupMembers

    @property
    def group_pos(self) -> int:
        """ A posição do botão de rádio no respectivo grupo de botões de rádio (vária de 1 a GroupCount).
        """
        return self.component.GroupPos

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign left'.
        """
        return self.component.IsLeftLabel

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def left_label(self) -> object:
        """ Rótulo esquerdo do GuiRadioButton. O rótulo é atribuído no Screen Painter, usando a flag 'assign left'.
        """
        return self.component.LeftLabel

    @property
    def right_label(self) -> object:
        """ Rótulo direito do GuiRadioButton. Esta propriedade é definida no Screen Painter usando a flag 'assign right'.
        """
        return self.component.RightLabel


class GuiButton(GuiVComponent):
    """ GuiButton representa todos os botões que estão no dynpros, na barra de ferramentas ou nos controles da tabela.
    O prefixo do tipo é btn, a propriedade name é o nome do campo obtido do dicionário de dados SAP.
    Há uma exceção: para botões de tabstrip, é o ID do botão definido no pintor de tela obtido do dicionário de dados SAP.
    """

    def press(self) -> None:
        """ Isso emula o pressionamento manual de um botão.
        Pressionar um botão sempre fará com que a comunicação do servidor ocorra,
        tornando inválidas todas as referências a elementos abaixo do nível da janela.
        """
        self.component.Press()

    @property
    def emphasized(self) -> bool:
        """ Esta propriedade é True se o botão for exibido enfatizado
        (no Fiori Visual Themes: O botão mais à esquerda no rodapé e botões configurados como "Fiori Usage D Display<->Change").
        """
        return self.component.Emphasized

    @property
    def left_label(self) -> GuiVComponent:
        """ Rótulo esquerdo do GuiButton. O rótulo é atribuído no Screen Painter, usando o sinalizador 'assign left'.
        """
        return GuiVComponent(self.component.LeftLabel)

    @property
    def right_label(self) -> GuiVComponent:
        """ Rótulo direito do GuiButton. Esta propriedade é definida no Screen Painter usando o sinalizador 'assign right'.
        """
        return GuiVComponent(self.component.RightLabel)


class GuiColorSelector(GuiShell):
    """ GuiColorSelector exibe um conjunto de cores para seleção.
    """

    def change_selection(self, i: int) -> None:
        """ Esta função emula a seleção da cor pelo usuário na posição de índice especificada.
        """
        self.component.ChangeSelection(i)


class GuiCustomControl(GuiVContainer):
    """ O GuiCustomControl é um objeto wrapper usado para colocar controles ActiveX em telas dynpro.
    Embora GuiCustomControl seja um elemento dynpro, seus filhos são do tipo GuiContainerShell, que é um contêiner
    para controles. GuiCustomControl estende o objeto GuiVContainer. O prefixo do tipo é cntl, o nome é o
    nome do campo retirado do dicionário de dados SAP.
    """

    @property
    def char_height(self) -> int:
        """ Altura do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharWidth


class GuiGOSShell(GuiVContainer):
    """ O GuiGosShell está disponível apenas no modo Novo Design Visual.
    O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    """

    pass


class GuiPicture(GuiShell):
    """ O controle de imagem exibe uma imagem em uma tela SAP GUI.
    """

    def click(self) -> None:
        """ Emula um clique único em uma imagem.
        """
        self.component.Click()

    def click_control_area(self, x: int, y: int) -> None:
        """ Emula um clique em uma posição específica. As coordenadas devem ser fornecidas em píxeis em relação ao controle da imagem conforme exibido na tela.
        """
        self.component.ClickControlArea(x, y)

    def click_picture_area(self, x: int, y: int) -> None:
        """ Emula um clique em uma posição específica. As coordenadas devem ser fornecidas em píxeis em relação ao arquivo de imagem original. Elas podem diferir das coordenadas em píxeis da imagem exibida devido ao dimensionamento.
        """
        self.component.ClickPictureArea(x, y)

    def context_menu(self, x: int, y: int) -> None:
        """ Abre um menu de contexto na posição especificada. As coordenadas devem ser fornecidas em píxeis em relação ao controle da imagem conforme exibido na tela.
        """
        self.component.ContextMenu(x, y)

    def double_click(self) -> None:
        """ Emula um clique duplo em uma imagem.
        """
        self.component.DoubleClick()

    def double_click_control_area(self, x: int, y: int) -> None:
        """ Emula um clique duplo em uma posição específica. As coordenadas devem ser fornecidas em píxeis
        em relação ao controle da imagem conforme exibido na tela.
        """
        self.component.DoubleClickControlArea(x, y)

    def double_click_picture_area(self, x: int, y: int) -> None:
        """ Emula um clique duplo em uma posição específica. As coordenadas devem ser fornecidas em píxeis em
        relação ao arquivo de imagem original. Elas podem diferir das coordenadas em píxeis da imagem exibida devido ao dimensionamento.
        """
        self.component.DoubleClickPictureArea(x, y)

    @property
    def alt_text(self) -> str:
        """ Esta propriedade contém o texto alternativo que pode ser atribuído a uma imagem (por exemplo, usado
        para pessoas com deficiência visual quando um leitor de tela é usado) (somente leitura).
        """
        return self.component.AltText

    @property
    def display_mode(self) -> str:
        """ Modo de exibição da imagem (somente leitura).
        Valores possíveis desta propriedade são:
        - "Normal": A imagem é mostrada em seu tamanho original. Se o tamanho da imagem for maior do que o tamanho do controle,
        o controle fornece barras de rolagem. Se o tamanho da imagem for menor do que o tamanho do controle, a imagem é mostrada
        no canto superior esquerdo do controle.
        - "Stretch": A imagem é redimensionada de forma que sempre ocupe a área completa do controle.
        - "Fit": A imagem é redimensionada de forma que ela se ajusta à área de controle sem a necessidade de mostrar barras de rolagem.
        Ao contrário de "Stretch", o modo "Fit" preserva a proporção de largura e altura da imagem.
        - "NormalCenter": semelhante a "Normal", exceto que a imagem não é mostrada no canto superior esquerdo, mas no centro do controle.
        - "FitCenter": semelhante a "Fit", exceto que a imagem não é mostrada no canto superior esquerdo, mas no centro do controle.
        """
        return self.component.DisplayMode

    @property
    def icon(self) -> str:
        """ Retorna o código de ícone SAPGUI (por exemplo, "@01@") do ícone exibido. Se nenhum ícone for exibido, a propriedade contém
        uma string vazia (somente leitura).
        """
        return self.component.Icon

    @property
    def url(self) -> str:
        """ Retorna a URL da imagem exibida. Se um ícone estiver sendo exibido (consulte a propriedade "icon"), a propriedade contém uma
        string vazia. Dependendo da aplicação que utiliza o controle, a URL pode conter partes temporárias da URL (por exemplo, UUIDs) (somente leitura).
        """
        return self.component.Url


class GuiSapChart(GuiShell):
    # TODO Verificar classe
    pass


class GuiNetChart(GuiShell):
    """ O GuiNetChart é uma ferramenta poderosa para exibir e modificar diagramas de relacionamento entre entidades.
    É de natureza muito técnica e só deve ser utilizado para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    """

    def get_link_content(self, link_id: int, text_id: int) -> str:
        """ Retorna o conteúdo do link.
        link_id: índice do link.
        text_id: valor interno a ser determinado durante a gravação.
        """
        return self.component.GetLinkContent(link_id, text_id)

    def get_node_content(self, node_id: int, text_id: int) -> str:
        """ Retorna o conteúdo do nó.
        node_id: índice do nó.
        text_id: valor interno a ser determinado durante a gravação.
        """
        return self.component.GetNodeContent(node_id, text_id)

    def send_data(self, data: str) -> None:
        """ Emula a saída de cada ação acionada no lado do controle. O resultado da ação é enviado para o servidor.
        Atualmente, não é possível selecionar ou desselecionar objetos individuais no lado do cliente e reproduzir/criptografar essas ações "locais".
        """
        self.component.SendData(data)

    @property
    def link_count(self) -> int:
        """ Número de links na rede (somente leitura).
        """
        return self.component.LinkCount

    @property
    def node_count(self) -> int:
        """ Número de nós na rede (somente leitura).
        """
        return self.component.NodeCount


class GuiMap(GuiShell):
    """ Para o controle do mapa, apenas membros básicos do GuiShell estão disponíveis.
    A gravação e a reprodução não são possíveis.
    """

    pass


class GuiScrollContainer(GuiVContainer):
    """ Este contêiner representa subtelas roláveis. Uma subtela pode ser rolável sem realmente ter uma barra de rolagem,
    porque a existência de uma barra de rolagem depende da quantidade de dados exibidos e do tamanho da GuiUserArea.
    O prefixo do tipo é ssub, o nome é gerado a partir das configurações do dicionário de dados.
    """

    @property
    def horizontal_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem horizontal do contêiner de rolagem.
        """
        return GuiScrollbar(self.component.HorizontalScrollbar)

    @property
    def vertical_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem vertical do contêiner de rolagem.
        """
        return GuiScrollbar(self.component.VerticalScrollbar)


class GuiSplitterContainer(GuiShell):
    """ O GuiSplitterContainer representa o elemento divisor dynpro, que foi introduzido
    no Web Application Server ABAP no NetWeaver 7.1. O elemento divisor dynpro é semelhante
    ao controle divisor baseado em activeX, mas é um elemento dynpro simples.
    """

    @property
    def is_vertical(self) -> bool:
        """ Esta propriedade contém True se as células divisoras do GuiSplitterContainer estiverem alinhadas
        verticalmente e False se estiverem alinhadas horizontalmente.
        """
        return self.component.IsVertical

    @property
    def sash_position(self) -> int:
        """ Contém a posição da divisória do divisor em caracteres.
        """
        return self.component.SashPosition

    @sash_position.setter
    def sash_position(self, position: int = None) -> None:
        """ Contém a posição da divisória do divisor em caracteres.
        """
        self.component.SashPosition = position


class GuiContainerShell(GuiShell):
    """ Um GuiContainerShell é um wrapper para um conjunto de objetos GuiShell.
    GuiContainerShell estende o objeto GuiVContainer.
    O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    """

    @property
    def docker_is_vertical(self) -> bool:
        """ Será TRUE se o contêiner for um controle de janela de encaixe vertical.
        """
        return self.component.DockerIsVertical

    @property
    def docker_pixel_size(self) -> int:
        """ Retorna o tamanho do controle do Docker em píxeis.
        """
        return self.component.DockerPixelSize


class GuiDialogShell(GuiVContainer):
    """ O GuiDialogShell é uma janela externa usada como contêiner para outros shells, por exemplo,
    uma barra de ferramentas. O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    """

    def close(self):
        """ Este método fecha a janela externa.
        """
        self.component.Close()

    @property
    def title(self) -> str:
        """ Título do diálogo.
        """
        return self.component.Title


class GuiMainWindow(GuiFrameWindow):
    """ Esta janela representa a janela principal de uma sessão SAP GUI.
    """

    def resize_working_pane(self, width: int, height: int, throw_on_fail: bool) -> None:
        """ Redimensiona a janela para que a área de trabalho disponível tenha a largura e altura fornecidas em métrica de caracteres.
        throw_on_fail: O parâmetro throw_on_fail foi adicionado para uso no SAP GUI for Java, pois alguns gerenciadores de janelas podem não suportar um redimensionamento de janela controlado pelo programa.
        """
        self.component.ResizeWorkingPane(width, height, throw_on_fail)

    def resize_working_pane_ex(self, width: int, height: int, throw_on_fail: bool) -> None:
        """ Redimensiona a janela para que a área de trabalho disponível tenha a largura e altura fornecidas em píxeis.
        """
        self.component.ResizeWorkingPaneEx(width, height, throw_on_fail)

    @property
    def buttonbar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de botões da aplicação, a barra de ferramentas inferior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de botões da aplicação.
        """
        return self.component.ButtonbarVisible

    @buttonbar_visible.setter
    def buttonbar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de botões da aplicação, a barra de ferramentas inferior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de botões da aplicação.
        """
        self.component.ButtonbarVisible = visible

    @property
    def statusbar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de status na parte inferior da janela SAP GUI estiver visível.
        Configurar esta propriedade como False ocultará a barra de status.
        Quando a barra de status está oculta, as mensagens serão exibidas em uma janela pop-up.
        """
        return self.component.StatusbarVisible

    @statusbar_visible.setter
    def statusbar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de status na parte inferior da janela SAP GUI estiver visível.
        Configurar esta propriedade como False ocultará a barra de status.
        Quando a barra de status está oculta, as mensagens serão exibidas em uma janela pop-up.
        """
        self.component.StatusbarVisible = visible

    @property
    def titlebar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de título estiver visível.
        Configurar esta propriedade como False ocultará a barra de título.
        """
        return self.component.TitlebarVisible

    @titlebar_visible.setter
    def titlebar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de título estiver visível.
        Configurar esta propriedade como False ocultará a barra de título.
        """
        self.component.TitlebarVisible = visible

    @property
    def toolbar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de ferramentas do sistema, a barra de ferramentas superior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de ferramentas do sistema.
        """
        return self.component.ToolbarVisible

    @toolbar_visible.setter
    def toolbar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de ferramentas do sistema, a barra de ferramentas superior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de ferramentas do sistema.
        """
        self.component.ToolbarVisible = visible


class GuiModalWindow(GuiFrameWindow):
    """ Uma GuiModalWindow é uma caixa de diálogo pop-up.
    """

    @property
    def is_popup_dialog(self) -> bool:
        """ Algumas janelas modais representam caixas de diálogo pop-up.
        Neste caso a propriedade IsPopupDialog é True.
        As caixas de diálogo pop-up são identificadas verificando o nome da fonte ABAP e o número do dynpro.
        """
        return self.component.IsPopupDialog

    @property
    def popup_dialog_text(self) -> str:
        """ O texto dos campos de entrada da caixa de diálogo pop-up em formato concatenado.
        """
        return self.component.PopupDialogText


class GuiTableColumn(GuiComponentCollection):
    """ GuiTableColumn representa uma coluna em um controle de tabela.
    """

    @property
    def default_tooltip(self) -> str:
        """ Texto de dica de ferramenta gerado a partir do texto curto definido no dicionário de dados para determinado tipo de elemento de tela.
        """
        return self.component.DefaultTooltip

    @property
    def fixed(self) -> bool:
        """ Algumas colunas podem ser fixas, o que significa que não serão roladas com o restante das colunas.
        """
        return self.component.Fixed

    @property
    def icon_name(self) -> str:
        """ Se ao objeto foi atribuído um ícone, então esta propriedade é o nome do ícone, caso contrário, é uma string vazia.
        """
        return self.component.IconName

    @property
    def selected(self) -> bool:
        """ Esta propriedade é verdadeira se a coluna estiver selecionada.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, option: bool) -> None:
        """ Esta propriedade é verdadeira se a coluna estiver selecionada.
        """
        self.component.Selected = option

    @property
    def title(self) -> str:
        """ Esta é a legenda da coluna.
        """
        return self.component.Title

    @property
    def tooltip(self) -> str:
        """ A dica de ferramenta contém um texto projetado para ajudar o usuário a entender o significado de um determinado campo de texto ou botão.
        """
        return self.component.Tooltip


class GuiTableRow(GuiComponentCollection):
    """ GuiTableRow representa uma linha em um controle de tabela.
    """

    # TODO Funções de auxilio

    @property
    def selectable(self) -> bool:
        """ Esta propriedade será True se a linha puder ser selecionada.
        """
        return self.component.Selectable

    @property
    def selected(self) -> bool:
        """ Esta propriedade é verdadeira se a linha estiver selecionada.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, option: bool) -> None:
        """ Esta propriedade é verdadeira se a linha estiver selecionada.
        """
        self.component.Selected = option


class GuiTableControl(GuiVContainer):
    """ O controle table é um elemento dynpro padrão, em contraste com o GuiCtrlGridView, que é semelhante.
    O prefixo do tipo é tbl, o nome é o nome do campo retirado do dicionário de dados SAP.
    """
    # TODO Funções adicionais

    def configure_layout(self) -> GuiModalWindow:
        """ Na caixa de diálogo de configuração o layout da tabela pode ser alterado. Esta caixa de diálogo é uma GuiModalWindow.
        """
        return GuiModalWindow(self.component.ConfigureLayout())

    def deselect_all_columns(self) -> None:
        """ Esta função pode ser usada para controles de tabela com um botão que permite desmarcar todas as colunas em uma única etapa.
        """
        return self.component.DeselectAllColumns()

    def get_absolute_row(self, index: int) -> GuiTableRow:
        """ Ao contrário da coleção de linhas, a indexação suportada por esta função não redefine o índice após a rolagem,
        mas conta as linhas começando pela primeira linha em relação à primeira posição de rolagem.
        Se a linha selecionada não estiver visível no momento, uma exceção será gerada.
        """
        return GuiTableRow(self.component.GetAbsoluteRow(index))

    def get_cell(self, row: int, column: int) -> GuiVComponent:
        """ Este método retorna uma determinada célula da tabela.
        É mais eficiente do que acessar uma única célula usando coleções de linhas ou colunas.
        """
        return GuiVComponent(self.component.GetCell(row, column))

    def reorder_table(self, permutation: str) -> None:
        """ A permutação de parâmetros descreve uma nova ordem das colunas.
        Por exemplo, "1 3 2" moverá a coluna 3 para a segunda posição.
        """
        # TODO Melhorar a função usando o nome das colunas
        self.component.ReorderTable(permutation)

    def select_all_columns(self) -> None:
        """ Esta função pode ser usada para controles de tabela com um botão que permite selecionar todas as colunas em uma única etapa.
        """
        self.component.SelectAllColumns()

    @property
    def char_height(self) -> int:
        """ Altura do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def col_select_mode(self) -> int:
        """ Existem três modos diferentes para selecionar colunas ou linhas, definidos no tipo de enumeração GuiTableSelectionType.
        """
        return self.component.ColSelectMode

    @property
    def columns(self) -> GuiCollection:
        """ Os membros desta coleção são do tipo GuiTableColumn.
        Portanto, eles não suportam propriedades como id ou nome.
        """
        return GuiCollection(self.component.Columns)

    @property
    def current_col(self) -> int:
        """ Índice baseado em zero da coluna atual.
        """
        return self.component.CurrentCol

    @property
    def current_row(self) -> int:
        """ Índice baseado em zero da linha atual.
        """
        return self.component.CurrentRow

    @property
    def horizontal_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem horizontal do controle de tabela.
        """
        return GuiScrollbar(self.component.HorizontalScrollbar)

    @property
    def row_count(self) -> int:
        """ Número de linhas na tabela. Isso inclui linhas invisíveis. Para o número de linhas visíveis está disponível a propriedade VisibleRowCount.
        """
        return self.component.RowCount

    @property
    def rows(self) -> GuiCollection:
        """ Os membros desta coleção são do tipo GuiTableRow.
        A indexação começa com 0 para a primeira linha visível, independente da posição atual da barra de rolagem horizontal.
        Após a rolagem, uma linha diferente terá o índice 0.
        """
        return GuiCollection(self.component.Rows)

    @property
    def row_select_mode(self) -> int:
        """ Existem três modos diferentes para selecionar colunas ou linhas,
        definidos no tipo de enumeração GuiTableSelectionType.
        """
        return self.component.RowSelectMode

    @property
    def table_field_name(self) -> str:
        """ A propriedade name do controle de tabela contém o nome do programa ABAP além do nome do campo simples.
        Esta propriedade contém apenas o nome do campo.
        """
        return self.component.TableFieldName

    @property
    def vertical_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem vertical do controle de tabela.
        """
        return GuiScrollbar(self.component.VerticalScrollbar)

    @property
    def visible_row_count(self) -> int:
        """ Número de linhas visíveis na tabela. Para o número de todas as linhas a propriedade RowCount está disponível.
        """
        return self.component.VisibleRowCount


class GuiMessageWindow(GuiVComponent):
    """ GuiMessageWindow é uma caixa de mensagem exibida pela mensagem showMessageBox do GuiUtils.
    """

    @property
    def focused_button(self) -> int:
        """ Índice baseado em zero do botão que atualmente tem foco (somente leitura).
        """
        return self.component.FocusedButton

    @property
    def help_button_help_text(self) -> str:
        """ Texto de ajuda do botão de ajuda (leitura/escrita).
        """
        return self.component.HelpButtonHelpText

    @help_button_help_text.setter
    def help_button_help_text(self, help_text: str = None) -> None:
        """ Texto de ajuda do botão de ajuda (leitura/escrita).
        """
        self.component.HelpButtonHelpText = help_text

    @property
    def help_button_text(self) -> str:
        """ Texto do botão de ajuda (leitura/escrita).
        """
        return self.component.HelpButtonText

    @help_button_text.setter
    def help_button_text(self, text: str = None) -> None:
        """ Texto do botão de ajuda (leitura/escrita).
        """
        self.component.HelpButtonText = text

    @property
    def message_text(self) -> str:
        """ Texto da mensagem (leitura/escrita).
        """
        return self.component.MessageText

    @message_text.setter
    def message_text(self, text: str = None) -> None:
        """ Texto da mensagem (leitura/escrita).
        """
        self.component.MessageText = text

    @property
    def message_type(self) -> int:
        """ Tipo de mensagem (leitura/escrita).
        """
        return self.component.MessageType

    @message_type.setter
    def message_type(self, message_type: int = None) -> None:
        """ Tipo de mensagem (leitura/escrita).
        """
        self.component.MessageType = message_type

    @property
    def ok_button_help_text(self) -> str:
        """ Texto de ajuda do botão OK (leitura/escrita).
        """
        return self.component.OKButtonHelpText

    @ok_button_help_text.setter
    def ok_button_help_text(self, help_text: str = None) -> None:
        """ Texto de ajuda do botão OK (leitura/escrita).
        """
        self.component.OKButtonHelpText = help_text

    @property
    def ok_button_text(self) -> str:
        """ Texto do botão OK (leitura/escrita).
        """
        return self.component.OKButtonText

    @ok_button_text.setter
    def ok_button_text(self, text: str = None) -> None:
        """ Texto do botão OK (leitura/escrita).
        """
        self.component.OKButtonText = text

    @property
    def visible(self) -> bool:
        """ Esta propriedade é True se o controle é visível, e False se estiver oculto (leitura/escrita).
        """
        return self.component.Visible

    @visible.setter
    def visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se o controle é visível, e False se estiver oculto (leitura/escrita).
        """
        self.component.Visible = visible


class GuiTree(GuiShell):
    """ O Tree Control oferece suporte a três tipos de árvore.
    """

    def change_checkbox(self, node_key: str, item_name: str, checked: bool) -> None:
        """ Emula a mudança de estado de uma caixa de seleção.
        """
        self.component.ChangeCheckbox(node_key, item_name, checked)

    def click_link(self, node_key: str, item_name: str) -> None:
        """ Emula a ativação de um link.
        """
        self.component.ClickLink(node_key, item_name)

    def collapse_node(self, node_key: str) -> None:
        """ Fecha o nó com a chave de nó especificada.
        """
        self.component.CollapseNode(node_key)

    def default_context_menu(self) -> None:
        """ Solicita um menu de contexto para todo o Controle de Árvore.
        """
        self.component.DefaultContextMenu()

    def double_click_item(self, node_key: str, item_name: str) -> None:
        """ Emula o duplo clique em um item de texto.
        """
        self.component.DoubleClickItem(node_key, item_name)

    def double_click_node(self, node_key: str) -> None:
        """ Emula o duplo clique em um nó.
        """
        self.component.DoubleClickNode(node_key)

    def ensure_visible_horizontal_item(self, node_key: str, item_name: str) -> None:
        """ Desloca a Árvore horizontalmente até que o item seja visível.
        """
        self.component.EnsureVisibleHorizontalItem(node_key, item_name)

    def expand_node(self, node_key: str) -> None:
        """ Expande o nó com a chave de nó especificada.
        """
        self.component.ExpandNode(node_key)

    def find_node_key_by_path(self, path: str) -> str:
        """ Encontra a chave de nó pelo seu caminho.
        """
        return self.component.FindNodeKeyByPath(path)

    def get_abap_image(self, key: str, name: str) -> str:
        """ Recupera o código do ícone de uma imagem exibida no item especificado.
        """
        return self.component.GetAbapImage(key, name)

    def get_all_node_keys(self):
        """ Retorna uma coleção de todas as chaves de nó presentes no Controle de Árvore.
        """
        return self.component.GetAllNodeKeys()

    def get_check_box_state(self, node_key: str, item_name: str) -> int:
        """ Recupera o estado da caixa de seleção (1 = Marcado, 0 = Desmarcado).
        """
        return self.component.GetCheckBoxState(node_key, item_name)

    def get_column_col(self, col_name: str):
        """ Retorna as chaves de todos os itens na coluna especificada.
        """
        return self.component.GetColumnCol(col_name)

    def get_column_headers(self):
        """ Retorna uma coleção de cabeçalhos de coluna.
        """
        return self.component.GetColumnHeaders()

    def get_column_index_from_name(self, key: str) -> int:
        """ Retorna o índice da coluna (começando em 1) da coluna especificada.
        """
        return self.component.GetColumnIndexFromName(key)

    def get_column_names(self):
        """ Retorna uma coleção de nomes de coluna.
        """
        return self.component.GetColumnNames()

    def get_column_title_from_name(self, key: str) -> str:
        """ Retorna o título da coluna especificada pelo parâmetro.
        """
        return self.component.GetColumnTitleFromName(key)

    def get_column_titles(self):
        """ Retorna uma coleção de títulos de coluna.
        """
        return self.component.GetColumnTitles()

    def get_focused_node_key(self) -> str:
        """ Retorna a chave do nó que está com foco.
        """
        return self.component.GetFocusedNodeKey()

    def get_hierarchy_level(self, key: str) -> int:
        """ Retorna o nível hierárquico da chave especificada, começando no nível 0.
        """
        return self.component.GetHierarchyLevel(key)

    def get_hierarchy_title(self) -> str:
        """ Retorna o título hierárquico.
        """
        return self.component.GetHierarchyTitle()

    def get_is_disabled(self, node_key: str, item_name: str) -> int:
        """ Retorna se o item especificado está desativado (1 = Desativado, 0 = Não desativado).
        """
        return self.component.GetIsDisabled(node_key, item_name)

    def get_is_high_lighted(self, node_key: str, item_name: str) -> int:
        """ Retorna se o item especificado está destacado (1 = Destacado, 0 = Não destacado).
        """
        return self.component.GetIsHighLighted(node_key, item_name)

    def get_item_height(self, node_key: str, item_name: str) -> int:
        """ Recupera a altura do item especificado em píxeis.
        """
        return self.component.GetItemHeight(node_key, item_name)

    def get_item_left(self, node_key: str, item_name: str) -> int:
        """ Recupera a posição esquerda do item especificado em píxeis.
        """
        return self.component.GetItemLeft(node_key, item_name)

    def get_item_style(self, node_key: str, item_name: str) -> int:
        """ Recupera o estilo do item especificado.
        """
        return self.component.GetItemStyle(node_key, item_name)

    def get_item_text(self, key: str, name: str) -> str:
        """ Retorna o texto do item especificado pelos parâmetros-chave e nome.
        """
        return self.component.GetItemText(key, name)

    def get_item_text_color(self, key: str, name: str) -> int:
        """ Recupera a cor da fonte do item especificado.
        """
        return self.component.GetItemTextColor(key, name)

    def get_item_tool_tip(self, key: str, name: str) -> str:
        """ Recupera a dica do item especificado.
        """
        return self.component.GetItemToolTip(key, name)

    def get_item_top(self, node_key: str, item_name: str) -> int:
        """ Recupera a posição superior do item especificado em píxeis.
        """
        return self.component.GetItemTop(node_key, item_name)

    def get_item_type(self, key: str, name: str) -> int:
        """ Recupera o tipo de item da árvore de colunas:
        trvTreeStructureHierarchy = 0
        trvTreeStructureImage = 1
        trvTreeStructureText = 2
        trvTreeStructureBool = 3
        trvTreeStructureButton = 4
        trvTreeStructureLink = 5
        """
        return self.component.GetItemType(key, name)

    def get_item_width(self, node_key: str, item_name: str) -> int:
        """ Recupera a largura do item especificado em pixels.
        """
        return self.component.GetItemWidth(node_key, item_name)

    def get_list_tree_node_item_count(self, node_key: str) -> int:
        """ Retorna o número de itens visíveis do nó especificado em uma árvore de lista.
        """
        return self.component.GetListTreeNodeItemCount(node_key)

    def get_next_node_key(self, node_key: str) -> str:
        """ Retorna a chave do próximo nó pertencente ao mesmo nó um nível acima.
        """
        return self.component.GetNextNodeKey(node_key)

    def get_node_abap_image(self, key: str) -> str:
        """ Recupera o código de ícone do nó especificado.
        """
        return self.component.GetNodeAbapImage(key)

    def get_node_children_count(self, key: str) -> int:
        """ Retorna o número de filhos diretos visíveis do nó especificado.
        """
        return self.component.GetNodeChildrenCount(key)

    def get_node_children_count_by_path(self, path: str) -> int:
        """ Retorna o número de filhos visíveis do nó especificado pelo caminho.
        """
        return self.component.GetNodeChildrenCountByPath(path)

    def get_node_height(self, key: str) -> int:
        """ Retorna a altura do nó especificado em pixels.
        """
        return self.component.GetNodeHeight(key)

    def get_node_index(self, key: str) -> int:
        """ Retorna o índice da chave especificada dentro do seu nó.
        """
        return self.component.GetNodeIndex(key)

    def get_node_item_headers(self, node_key: str):
        """ Retorna um objeto com os cabeçalhos de item do nó especificado.
        """
        return self.component.GetNodeItemHeaders(node_key)

    def get_node_key_by_path(self, path: str) -> str:
        """ Chave do nó especificado pelo caminho dado.
        """
        return self.component.GetNodeKeyByPath(path)

    def get_node_left(self, key: str) -> int:
        """ Retorna a posição esquerda do nó especificado em píxeis.
        """
        return self.component.GetNodeLeft(key)

    def get_node_path_by_key(self, key: str) -> str:
        """ Dado uma chave de nó, o caminho é recuperado (por exemplo, "2\1\2").
        """
        return self.component.GetNodePathByKey(key)

    def get_nodes_col(self):
        """ A coleção contém as chaves de todos os nós na árvore.
        """
        return self.component.GetNodesCol()

    def get_node_style(self, node_key: str) -> int:
        """ Recupera o estilo do nó especificado.
        """
        return self.component.GetNodeStyle(node_key)

    def get_node_text_by_key(self, key: str) -> str:
        """ Retorna o texto do nó especificado pela chave dada.
        """
        return self.component.GetNodeTextByKey(key)

    def get_node_text_by_path(self, path: str) -> str:
        """ O texto de um nó definido pelo caminho dado é retornado.
        """
        return self.component.GetNodeTextByPath(path)

    def get_node_text_color(self, key: str) -> int:
        """ Retorna a cor da fonte do nó especificado.
        """
        return self.component.GetNodeTextColor(key)

    def get_node_tool_tip(self, node_key: str) -> str:
        """ Retorna a dica de ferramenta do nó especificado.
        """
        return self.component.GetNodeToolTip(node_key)

    def get_node_top(self, key: str) -> int:
        """ Retorna a posição superior do nó especificado em píxeis.
        """
        return self.component.GetNodeTop(key)

    def get_node_width(self, key: str) -> int:
        """ Retorna a largura do nó especificado em pixels.
        """
        return self.component.GetNodeWidth(key)

    def get_parent(self, ckey: str) -> str:
        """ Chave do nó pai do nó especificado pela chave dada.
        """
        return self.component.GetParent(ckey)

    def get_previous_node_key(self, node_key: str) -> str:
        """ Retorna a chave do nó anterior pertencente ao mesmo nó um nível acima.
        """
        return self.component.GetPreviousNodeKey(node_key)

    def get_selected_nodes(self):
        """ Retorna uma coleção de nós selecionados.
        """
        return self.component.GetSelectedNodes()

    def get_selection_mode(self) -> int:
        """ Retorna o modo de seleção do Controle de Árvore:
        0: Seleção de Nó Único
        1: Seleção de Múltiplos Nós
        2: Seleção de Item Único
        3: Seleção de Múltiplos Itens
        """
        return self.component.GetSelectionMode()

    def get_style_description(self, n_style: int) -> str:
        """ Retorna a descrição do estilo especificado.
        """
        return self.component.GetStyleDescription(n_style)

    def get_sub_nodes_col(self, path: str):
        """ Retorna uma coleção de chaves de todos os subníveis do nó especificado pela chave dada.
        """
        return self.component.GetSubNodesCol(path)

    def get_tree_type(self) -> int:
        """ Retorna o tipo de árvore:
        0: Árvore Simples
        1: Árvore de Lista
        2: Árvore de Coluna
        """
        return self.component.GetTreeType()

    def header_context_menu(self, header_name: str) -> None:
        """ Solicita um menu de contexto para um cabeçalho.
        """
        self.component.HeaderContextMenu(header_name)

    def is_folder(self, node_key: str) -> int:
        """ Retorna True se o objeto especificado for um nó e não uma folha.
        """
        return self.component.IsFolder(node_key)

    def is_folder_expandable(self, node_key: str) -> int:
        """ Retorna True se a pasta pertencente ao nó especificado pode ser expandida.
        """
        return self.component.IsFolderExpandable(node_key)

    def is_folder_expanded(self, node_key: str) -> int:
        """ Retorna True se a pasta pertencente ao nó especificado estiver expandida.
        """
        return self.component.IsFolderExpanded(node_key)

    def item_context_menu(self, node_key: str, item_name: str) -> None:
        """ Solicita um menu de contexto para um item.
        """
        self.component.ItemContextMenu(node_key, item_name)

    def node_context_menu(self, node_key: str) -> None:
        """ Solicita um menu de contexto para um nó.
        """
        self.component.NodeContextMenu(node_key)

    def press_button(self, node_key: str, item_name: str) -> None:
        """ Emula o pressionamento de um botão.
        """
        self.component.PressButton(node_key, item_name)

    def press_header(self, header_name: str) -> None:
        """ Emula o clique em um cabeçalho.
        """
        self.component.PressHeader(header_name)

    def press_key(self, key: str) -> None:
        """ Emula o pressionamento de uma tecla.
        """
        self.component.PressKey(key)

    def select_column(self, column_name: str) -> None:
        """ Adiciona uma coluna à seleção de colunas, removendo a seleção de nós ou itens.
        """
        self.component.SelectColumn(column_name)

    def selected_item_column(self) -> str:
        """ Retorna o nome da coluna do item selecionado.
        """
        return self.component.SelectedItemColumn()

    def selected_item_node(self) -> str:
        """ Retorna a chave do nó do item selecionado.
        """
        return self.component.SelectedItemNode()

    def select_item(self, node_key: str, item_name: str) -> None:
        """ Emula a seleção de um item, removendo todas as outras seleções.
        """
        self.component.SelectItem(node_key, item_name)

    def select_node(self, node_key: str) -> None:
        """ Adiciona o nó com a chave especificada à seleção de nós.
        """
        self.component.SelectNode(node_key)

    def set_check_box_state(self, node_key: str, item_name: str, state: int) -> None:
        """ Marca ou desmarca a caixa de seleção na célula especificada do controle de árvore.
        Se o parâmetro "state" for igual a 0, a caixa de seleção é desmarcada; se o parâmetro for igual a 1, a caixa de seleção é marcada.
        """
        self.component.SetCheckBoxState(node_key, item_name, state)

    def set_column_width(self, column_name: str, width: int) -> None:
        """ Define a largura de uma coluna em pixels.
        """
        self.component.SetColumnWidth(column_name, width)

    def unselect_all(self) -> None:
        """ Remove todas as seleções.
        """
        self.component.UnselectAll()

    def unselect_column(self, column_name: str) -> None:
        """ Remove uma coluna da seleção de colunas.
        """
        self.component.UnselectColumn(column_name)

    def unselect_node(self, node_key: str) -> None:
        """ Remove o nó com a chave especificada da seleção de nós.
        """
        self.component.UnselectNode(node_key)

    @property
    def column_order(self) -> object:
        """ A propriedade ColumnOrder é usada para trabalhar com a sequência de colunas.
            O nome de cada coluna na árvore de colunas deve ocorrer exatamente uma vez.
        """
        return self.component.ColumnOrder

    @column_order.setter
    def column_order(self, column_order: object = None) -> None:
        """ A propriedade ColumnOrder é usada para trabalhar com a sequência de colunas.
            O nome de cada coluna na árvore de colunas deve ocorrer exatamente uma vez.
        """
        self.component.ColumnOrder = column_order

    @property
    def hierarchy_header_width(self) -> int:
        """ A largura do Hierarchy Header em pixels.
        """
        return self.component.HierarchyHeaderWidth

    @hierarchy_header_width.setter
    def hierarchy_header_width(self, width: int = None) -> None:
        """ A largura do Hierarchy Header em pixels.
        """
        self.component.HierarchyHeaderWidth = width

    @property
    def selected_node(self) -> str:
        """ Esta propriedade representa a chave do nó atualmente selecionado.
            A seleção de um nó remove outras seleções (ou seja, seleção de coluna e seleção de item).
        """
        return self.component.SelectedNode

    @selected_node.setter
    def selected_node(self, node_key: str = None) -> None:
        """ Esta propriedade representa a chave do nó atualmente selecionado.
            A seleção de um nó remove outras seleções (ou seja, seleção de coluna e seleção de item).
        """
        self.component.SelectedNode = node_key

    @property
    def top_node(self) -> str:
        """ Esta propriedade influencia a rolagem vertical do controle de árvore.
            TopNode contém a chave do nó que está localizado na borda superior do controle de árvore.
            A definição de um nó x como nó superior só é possível se houver nós visíveis suficientes abaixo de x para preencher a área de exibição do controle de árvore.
        """
        return self.component.TopNode

    @top_node.setter
    def top_node(self, top_node_key: str = None) -> None:
        """ Esta propriedade influencia a rolagem vertical do controle de árvore.
            TopNode contém a chave do nó que está localizado na borda superior do controle de árvore.
            A definição de um nó x como nó superior só é possível se houver nós visíveis suficientes abaixo de x para preencher a área de exibição do controle de árvore.
        """
        self.component.TopNode = top_node_key


class GuiStage(GuiShell):
    """ Para o controle de palco apenas estão disponíveis membros básicos do GuiShell.
    A gravação e a reprodução não são possíveis.
    """

    def context_menu(self, str_id: str) -> None:
        """ Chamar esta função abre um menu de contexto.
        str_id: ID do menu de contexto.
        """
        self.component.ContextMenu(str_id)

    def double_click(self, str_id: str) -> None:
        """ Esta função emula um clique duplo do mouse.
        str_id: ID do elemento no qual ocorrerá o clique duplo.
        """
        self.component.DoubleClick(str_id)

    def select_items(self, str_items: str) -> None:
        """ Seleciona os itens especificados pelo parâmetro str_items.
        str_items: uma string contendo os itens a serem selecionados.
        """
        self.component.SelectItems(str_items)


class GuiChart(GuiShell):
    """ O objeto GuiChart é de natureza muito técnica. Deve ser utilizado apenas para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    """

    def value_change(self, series: int, point: int, x_value: str, y_value: str, data_change: bool, id_container: str, z_value: str, change_flag: int):
        """
        Série: Número do conjunto de dados dentro da linha que deve ser alterado.
        point: Número do ponto de dados na linha que deve ser alterado.
        x_value: novo valor de x.
        y_value: novo valor de y.
        data_change: definir este parâmetro como True significa que o valor não foi alterado interativamente no gráfico,
            mas sim inserindo o novo valor na página de propriedades do DataPoint.
        id_container: ID do contêiner de dados GFW do ponto alterado. Pode ser usado em vez do par série/ponto.
        z_value: novo valor z.
        ChangeFlag: Notifica qual valor foi alterado ou se foi um valor de tempo.
            O valor é definido como uma matriz de bits, usando os 5 bits inferiores.
            1 x
            2 y
            4 x é o valor do tempo
            8 y é o valor do tempo
            16 z
            Se o novo valor for um momento específico, ele deverá ser definido usando uma string no formato mm/dd/aaaa hh:mm:ss.
        """
        self.component.ValueChange(series, point, x_value, y_value, data_change, id_container, z_value, change_flag)


class GuiBarChart(GuiShell):
    """ O GuiBarChart é uma ferramenta poderosa para exibir e modificar diagramas de escala de tempo.
    O objeto é de natureza muito técnica. Deve ser utilizado apenas para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    """

    def bar_count(self, chart_id: int) -> int:
        """ Retorna o número de barras no gráfico especificado.
        """
        return self.component.BarCount(chart_id)

    def get_bar_content(self, chart_id: int, bar_id: int, text_id: int) -> str:
        """ Retorna o conteúdo da barra especificada.
        """
        return self.component.GetBarContent(chart_id, bar_id, text_id)

    def get_grid_line_content(self, chart_id: int, grid_line_id: int, text_id: int) -> str:
        """ Retorna o conteúdo da linha de grade especificada.
        """
        return self.component.GetGridLineContent(chart_id, grid_line_id, text_id)

    def grid_count(self, chart_id: int) -> int:
        """ Retorna o número de grades dentro do gráfico especificado.
        """
        return self.component.GridCount(chart_id)

    def link_count(self, chart_id: int) -> int:
        """ Retorna o número de links dentro do gráfico especificado.
        """
        return self.component.LinkCount(chart_id)

    def send_data(self, dados: str) -> None:
        """ Envia dados para o servidor.
        """
        self.component.SendData(dados)

    @property
    def chart_count(self) -> int:
        """ Número de gráficos.
        """
        return self.component.ChartCount


class GuiCalendar(GuiShell):
    """ O controle de calendário pode ser usado para selecionar datas ou períodos únicos.
    """

    def context_menu(self, ctx_menu_id: int, ctx_menu_cell_row: int, ctx_menu_cell_col: int, date_begin: str, date_end: str) -> None:
        """ Chama esta função para abrir um menu de contexto.

        O parâmetro CtxMenuId indica o tipo de célula na qual o menu de contexto foi aberto:
        Valor   Tipo de Célula  Descrição
        0       Data            Invocação em uma célula com uma única data
        1       Dia da Semana   Invocação em um botão para um determinado dia da semana
        2       Semana          Invocação em um botão para uma semana específica
        """
        self.component.ContextMenu(ctx_menu_id, ctx_menu_cell_row, ctx_menu_cell_col, date_begin, date_end)

    def create_date(self, day: int, month: int, year: int) -> str:
        """ Cria uma data no formato "YYYYMMDD" a partir dos parâmetros de dia, mês e ano.
        """
        return self.component.CreateDate(day, month, year)

    def get_color(self, from_color: str) -> int:
        """ Retorna a cor associada a partir do valor de cor especificado.
        """
        return self.component.GetColor(from_color)

    def get_color_info(self, color: int) -> str:
        """ Retorna a explicação definida pela aplicação para cores semânticas usadas no GuiCalendar (começando com índice 0).
        """
        return self.component.GetColorInfo(color)

    def get_date_tooltip(self, date: str) -> str:
        """ Retorna o texto de dica de ferramenta da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetDateTooltip(date)

    def get_day(self, date: str) -> int:
        """ Retorna o dia da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetDay(date)

    def get_month(self, date: str) -> int:
        """ Retorna o mês da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetMonth(date)

    def get_weekday(self, date: str) -> str:
        """ Retorna o dia da semana da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetWeekday(date)

    def get_week_number(self, date: str) -> int:
        """ Retorna o número da semana da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetWeekNumber(date)

    def get_year(self, date: str) -> int:
        """ Retorna o ano da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetYear(date)

    def is_weekend(self, date: str) -> int:
        """ Retorna True se a data especificada pelo parâmetro estiver em um fim de semana.
        """
        return self.component.IsWeekend(date)

    def select_month(self, month: int, year: int) -> None:
        """ Seleciona o mês especificado pelos parâmetros (começando com índice 1).
        """
        self.component.SelectMonth(month, year)

    def select_range(self, from_date: str, to_date: str) -> None:
        """ Seleciona o intervalo especificado pelos parâmetros (no formato "YYYYMMDD").
        """
        self.component.SelectRange(from_date, to_date)

    def select_week(self, week: int, year: int) -> None:
        """ Seleciona a semana especificada pelos parâmetros (começando com índice 0).
        """
        self.component.SelectWeek(week, year)

    @property
    def end_selection(self) -> str:
        """ O último dia do intervalo de datas selecionado (no formato "YYYYMMDD").
        """
        return self.component.EndSelection

    @property
    def first_visible_date(self) -> str:
        """ Esta é a data mais antiga visível no controle de calendário.
        """
        return self.component.FirstVisibleDate

    @first_visible_date.setter
    def first_visible_date(self, date: str = None) -> None:
        """ Esta é a data mais antiga visível no controle de calendário.
        """
        self.component.FirstVisibleDate = date

    @property
    def focus_date(self) -> str:
        """ A data atualmente focada (identificada pela borda de foco) no controle de calendário está disponível no formato "YYYYMMDD".
        """
        return self.component.FocusDate

    @focus_date.setter
    def focus_date(self, date: str = None) -> None:
        """ A data atualmente focada (identificada pela borda de foco) no controle de calendário está disponível no formato "YYYYMMDD".
        """
        self.component.FocusDate = date

    @property
    def focused_element(self) -> int:
        """ Esta propriedade indica qual parte de um controle GuiCalendar composto atualmente tem o foco.
        Os valores possíveis são:
        0 - "InputField": O campo de entrada (seletor) para inserir manualmente uma data atualmente tem foco
        1 - "Button": O botão de pressão para abrir o painel de navegação atualmente tem foco
        2 - "Navigator": O painel de navegação pop-up está aberto e atualmente tem foco
        """
        return self.component.FocusedElement

    @property
    def horizontal(self) -> bool:
        """ Esta propriedade contém True se o GuiCalendar tiver orientação horizontal, caso contrário, contém False.
        """
        return self.component.Horizontal

    @property
    def last_visible_date(self) -> str:
        """ A última data que está atualmente sendo exibida pelo GuiCalendar (no formato "YYYYMMDD").
        """
        return self.component.LastVisibleDate

    @last_visible_date.setter
    def last_visible_date(self, date: str = None) -> None:
        """ A última data que está atualmente sendo exibida pelo GuiCalendar (no formato "YYYYMMDD").
        """
        self.component.LastVisibleDate = date

    @property
    def selection_interval(self) -> str:
        """ O intervalo é representado por duas strings de data concatenadas separadas por uma vírgula.
        """
        return self.component.SelectionInterval

    @selection_interval.setter
    def selection_interval(self, interval: str = None) -> None:
        """ O intervalo é representado por duas strings de data concatenadas separadas por uma vírgula.
        """
        self.component.SelectionInterval = interval

    @property
    def start_selection(self) -> str:
        """ O primeiro dia do intervalo de datas selecionado (no formato "YYYYMMDD").
        """
        return self.component.StartSelection

    @property
    def today(self) -> str:
        """ O dia atual (no formato "YYYYMMDD").
        """
        return self.component.Today


class GuiOfficeIntegration(GuiShell):
    """ O objeto GuiOfficeIntegration (Desktop Office Integration) oferece um contêiner para hospedar
    diversos tipos de aplicativos Office (Microsoft Word, Microsoft Excel, Microsoft Powerpoint).
    """

    def append_row(self, name: str, row: str) -> None:
        """ Adiciona uma nova linha a uma tabela especificada pelo parâmetro "name" na coleção de tabelas.
        O parâmetro "row" é a representação em base64 da linha binária.
        """
        self.component.AppendRow(name, row)

    def close_document(self, cookie: int, ever_changed: int, changed_after_save: int) -> None:
        """ Envia o evento de fechamento do documento especificado pelo parâmetro "cookie" para o servidor.
        O parâmetro "ever_changed" é do tipo Byte e indica se o documento foi alterado permanentemente.
        O parâmetro "changed_after_save" é do tipo Byte e indica se o documento foi alterado após o salvamento.
        """
        self.component.CloseDocument(cookie, ever_changed, changed_after_save)

    def custom_event(self, cookie: int, event_name: str, param_count: int, *params) -> None:
        """ Envia o evento personalizado "eventName" para o servidor.
        O documento especificado pelo parâmetro "cookie" é a fonte do evento.
        Os parâmetros adicionais, "par1" a "par12", são opcionais e podem ser usados para enviar até 12 parâmetros para o evento personalizado.
        """
        self.component.CustomEvent(cookie, event_name, param_count, *params)

    def remove_content(self, name: str) -> None:
        """ Remove o conteúdo de uma tabela na coleção de tabelas.
        O parâmetro "name" é o nome da tabela a ser removida.
        """
        self.component.RemoveContent(name)

    def save_document(self, cookie: int, changed: int) -> None:
        """ Envia o evento de salvamento do documento especificado pelo parâmetro "cookie" para o servidor.
        O parâmetro "changed" é do tipo Byte e indica se o documento foi alterado.
        """
        self.component.SaveDocument(cookie, changed)

    def set_document(self, index: int, document: str) -> None:
        """ Substitui ou adiciona um novo documento com o índice especificado.
        O parâmetro "document" é a representação em base64 do documento binário.
        """
        self.component.SetDocument(index, document)

    @property
    def document(self) -> object:
        """ O documento hospedado dentro do objeto GuiOfficeIntegration (somente leitura).
        """
        return self.component.Document

    @property
    def hosted_application(self) -> int:
        """ Este índice identifica a aplicação hospedada no objeto GuiOfficeIntegration (somente leitura).
        Valores possíveis são:
        1 - Microsoft Word
        2 - Microsoft Excel
        3 - Microsoft PowerPoint
        """
        return self.component.HostedApplication


class GuiVHViewSwitch(GuiVComponent):
    """ GuiVHViewSwitch representa o objeto “View Switch” que foi introduzido com o tema Belize no SAP GUI.
    O View Switch é colocado na área de cabeçalho da janela principal do SAP GUI e pode ser usado para selecionar diferentes visualizações
    dentro de um aplicativo.
    Muitas telas podem ser exibidas de diferentes maneiras (por exemplo, como uma árvore ou uma lista).
    Para mudar de uma visualização para outra de forma confortável, essas telas podem fazer uso do View Switch.
    """

    pass


class GuiHTMLViewer(GuiShell):
    """ O GuiHTMLViewer é usado para exibir um documento HTML dentro do SAP GUI.
    """

    def context_menu(self):
        """ Chamar contextMenu simula a solicitação do menu de contexto.
        Observe que essa função se aplica apenas a menus de contexto fornecidos pelo backend,
        não ao menu de contexto local, gerado pelo controle HTML.
        """
        self.component.ContextMenu()

    def sap_event(self, frame_name: str, post_data: str, url: str):
        """ Esta função envia um formulário HTML para o backend.

        Observações:

        Se o formulário deve ser enviado usando o método GET, os dados são anexados ao nome do evento
        no formato usual de URL HTTP, por exemplo:

        Exemplo de código:
        sapEvent("Frame1", "", "sapevent:SUBMIT_FORM_AS_GET_METHOD?FirstName=John&LastName=Smith")

        Neste caso, PostData é sempre uma string vazia.

        Se o formulário deve ser enviado usando o método POST, os dados são transportados no parâmetro PostData:

        Exemplo de código:
        sapEvent("Frame1", "FirstName=John&LastName=Smith", "sapevent:SUBMIT_FORM_AS_POST_METHOD")

        FrameName: Este é o nome do quadro no qual o formulário HTML que foi enviado está localizado.
        PostData: Contém os dados do formulário quando um envio é feito usando o método POST.
        Url: Este é o URL enviado para o backend. O nome do protocolo para a string de URL é "sapevent:"
            Isso é seguido pelo nome do evento conforme definido na Propriedade de Ação do formulário HTML
            que está sendo chamado.
        """
        self.component.SapEvent(frame_name, post_data, url)

    @property
    def browser_handle(self) -> object:
        return self.component.BrowserHandle

    @property
    def document_complete(self) -> int:
        return self.component.DocumentComplete


class GuiGraphAdapt(GuiShell):
    """ Para o controle do adaptador gráfico, apenas membros básicos do GuiShell estão disponíveis. A gravação e a reprodução não são possíveis.
    Observações
    Além dos novos controles baseados em ActiveX, o SAP GUI também vem com um conjunto de executáveis gráficos externos,
    por exemplo, para exibir um gráfico GANTT. Esses executáveis não são suportados pela API.
    Se durante a execução de um script um desses executáveis for iniciado, o script será bloqueado.
    Se você precisar automatizar um processo durante o qual um executável gráfico é exibido, você precisará de uma ferramenta
    de automação que permita manipular o SAP GUI usando a API de script e outros aplicativos do Windows usando métodos nativos.
    """

    pass


class GuiEAIViewer3D(GuiShell):
    """ O controle GuiEAIViewer3D é utilizado para visualizar imagens gráficas tridimensionais no sistema SAP.
    """

    pass


class GuiEAIViewer2D(GuiShell):
    """ O controle GuiEAIViewer2D é utilizado para visualizar imagens gráficas bidimensionais no sistema SAP.
    O usuário pode realizar redlining sobre a imagem carregada. o wrapper de script para esse controle registra
    todas as ações do usuário durante o processo de redlining e reproduz as mesmas ações quando o script gravado é reproduzido.
    """

    def annotation_text_request(self, text: str) -> None:
        # TODO Criar descrição
        return self.component.annotationTextRequest(text)

    @property
    def annotation_enabled(self) -> int:
        """ O valor desta propriedade é definido como 1 quando a marcação está ativada.
        O controle wrapper começa a gravar as ações do usuário assim que esta propriedade é definida como valor 1.
        """
        return self.component.AnnotationEnabled

    @annotation_enabled.setter
    def annotation_enabled(self, enabled: int = None) -> None:
        """ O valor desta propriedade é definido como 1 quando a marcação está ativada.
        O controle wrapper começa a gravar as ações do usuário assim que esta propriedade é definida como valor 1.
        """
        self.component.AnnotationEnabled = enabled

    @property
    def annotation_mode(self) -> int:
        """ Durante a marcação, o modo de marcação selecionado é armazenado nesta propriedade.
        """
        return self.component.AnnotationMode

    @annotation_mode.setter
    def annotation_mode(self, mode: int = None) -> None:
        """ Durante a marcação, o modo de marcação selecionado é armazenado nesta propriedade.
        """
        self.component.AnnotationMode = mode

    @property
    def redlining_stream(self) -> str:
        """ Esta propriedade armazena a camada de marcação como um objeto BLOB (Binary Large Data Object).
        Durante a gravação, todo o BLOB é copiado para o script gerado.
        """
        return self.component.RedliningStream

    @redlining_stream.setter
    def redlining_stream(self, stream: str = None) -> None:
        """ Esta propriedade armazena a camada de marcação como um objeto BLOB (Binary Large Data Object).
        Durante a gravação, todo o BLOB é copiado para o script gerado.
        """
        self.component.RedliningStream = stream


class GuiApoGrid(GuiShell):
    """ Observações
    O GuiApoGrid é um objeto criado especificamente para aplicações SAP SCM.
    Ele implementa um quadro de planejamento, semelhante a um controle GuiGridView.

    As colunas e linhas são identificadas pela sua posição começando em zero:
    0 <= linha <Contagem de linhas
    0 <= coluna <Contagem de colunas
    Após uma busca detalhada, as linhas são renumeradas para que o número de qualquer linha possa mudar. A rolagem horizontal não afeta o número de uma coluna.
    """

    def cancel_cut(self) -> None:
        """ Aborta a operação de corte.
        """
        self.component.CancelCut()

    def clear_selection(self) -> None:
        """ Chamar clearSelection remove todas as seleções de linhas, colunas e células.
        """
        self.component.ClearSelection()

    def context_menu(self, coluna: int, linha: int) -> None:
        """ Chamar contextMenu emula a solicitação de menu de contexto.
        """
        self.component.ContextMenu(coluna, linha)

    def cut(self) -> None:
        """ Corta as células selecionadas.
        """
        self.component.Cut()

    def deselect_cell(self, coluna: int, linha: int) -> None:
        """ Deseleciona as células especificadas. Esta função remove as células especificadas da coleção de células selecionadas.
        """
        self.component.DeselectCell(coluna, linha)

    def deselect_column(self, coluna: int) -> None:
        """ Esta função remove a coluna especificada da coleção de colunas selecionadas.
        """
        self.component.DeselectColumn(coluna)

    def deselect_row(self, linha: int) -> None:
        """ Esta função remove a linha especificada da coleção de linhas selecionadas.
        """
        self.component.DeselectRow(linha)

    def double_click_cell(self, coluna: int, linha: int) -> None:
        """ Esta função emula um duplo clique do mouse em uma célula específica se os parâmetros forem válidos e gera uma exceção caso contrário.
        """
        self.component.DoubleClickCell(coluna, linha)

    def get_bgd_color_info(self, linha: int, coluna: int) -> str:
        """ Esta função retorna a cor de fundo da célula especificada.
        """
        return self.component.GetBgdColorInfo(linha, coluna)

    def get_cell_changeable(self, coluna: int, linha: int) -> bool:
        """ Esta função retorna True se a célula especificada for editável.
        """
        return self.component.GetCellChangeable(coluna, linha)

    def get_cell_format(self, coluna: int, linha: int) -> str:
        """ Retorna o formato da célula especificada.
        """
        return self.component.GetCellFormat(coluna, linha)

    def get_cell_tooltip(self, coluna: int, linha: int) -> str:
        """ Esta função retorna a dica de ferramenta da célula especificada.
        """
        return self.component.GetCellTooltip(coluna, linha)

    def get_cell_value(self, coluna: int, linha: int) -> str:
        """ Esta função retorna o valor da célula especificada como uma string.
        """
        return self.component.GetCellValue(coluna, linha)

    def get_fgd_color_info(self, linha: int, coluna: int) -> str:
        """ Esta função retorna a cor da fonte da célula especificada.
        """
        return self.component.GetFgdColorInfo(linha, coluna)

    def get_icon_info(self, linha: int, coluna: int) -> str:
        """ Retorna informações do ícone da célula especificada.
        """
        return self.component.GetIconInfo(linha, coluna)

    def is_cell_selected(self, coluna: int, linha: int) -> bool:
        """ Retorna True se a célula especificada estiver selecionada.
        """
        return self.component.IsCellSelected(coluna, linha)

    def is_col_selected(self, coluna: int) -> bool:
        """ Retorna True se a coluna especificada estiver selecionada.
        """
        return bool(self.component.IsColSelected(coluna))

    def is_row_selected(self, linha: int) -> bool:
        """ Retorna True se a linha especificada estiver selecionada.
        """
        return bool(self.component.IsRowSelected(linha))

    def paste(self, valores_celula: object, num_colunas: int) -> int:
        """ Aciona uma operação de colar.
        """
        return self.component.Paste(valores_celula, num_colunas)

    def press_enter(self) -> None:
        """ Emula a pressão da tecla Enter.
        """
        self.component.PressEnter()

    def select_all(self) -> None:
        """ Esta função seleciona todo o conteúdo da grade (ou seja, todas as linhas e colunas).
        """
        self.component.SelectAll()

    def select_cell(self, coluna: int, linha: int) -> None:
        """ Seleciona a célula especificada.
        """
        self.component.SelectCell(coluna, linha)

    def select_column(self, coluna: int) -> None:
        """ Seleciona a coluna especificada.
        """
        self.component.SelectColumn(coluna)

    def select_row(self, linha: int) -> None:
        """ Seleciona a linha especificada.
        """
        self.component.SelectRow(linha)

    def set_cell_value(self, coluna: int, linha: int, valor: str) -> str:
        """ Esta função insere o valor especificado na célula especificada.
        """
        return self.component.SetCellValue(coluna, linha, valor)

    @property
    def column_count(self) -> int:
        """ Esta propriedade representa o número de colunas no controle.
        """
        return self.component.ColumnCount

    @property
    def current_cell_column(self) -> int:
        """ O índice da coluna que contém a célula atual.
        """
        return self.component.CurrentCellColumn

    @property
    def current_cell_row(self) -> int:
        """ O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        """
        return self.component.CurrentCellRow

    @property
    def first_visible_column(self) -> int:
        """ Esta propriedade representa a primeira coluna visível da área rolável do controle APOGrid.
        """
        return self.component.FirstVisibleColumn

    @property
    def first_visible_row(self) -> int:
        """ Este é o índice da primeira linha visível na grade. Definir esta propriedade para um índice de linha inválido gerará uma exceção.
        """
        return self.component.FirstVisibleRow

    @property
    def fixed_columns_left(self) -> int:
        """ O número de colunas fixas no lado esquerdo da grade.
        """
        return self.component.FixedColumnsLeft

    @property
    def fixed_columns_right(self) -> int:
        """ O número de colunas fixas no lado direito da grade.
        """
        return self.component.FixedColumnsRight

    @property
    def fixed_rows_bottom(self) -> int:
        """ O número de linhas fixas na parte inferior da grade.
        """
        return self.component.FixedRowsBottom

    @property
    def fixed_rows_top(self) -> int:
        """ O número de linhas fixas na parte superior da grade.
        """
        return self.component.FixedRowsTop

    @property
    def row_count(self) -> int:
        """ Esta propriedade representa o número de linhas no controle.
        """
        return self.component.RowCount

    @property
    def selected_cells(self) -> object:
        """ A coleção de células selecionadas. Tentar definir esta propriedade como um valor inválido gerará uma exceção.
        """
        return self.component.SelectedCells

    @property
    def selected_columns(self) -> str:
        """ As colunas selecionadas estão disponíveis como uma coleção. Configurar esta propriedade pode gerar uma exceção se a nova coleção contiver uma coluna inválida.
        """
        return self.component.SelectedColumns

    @property
    def selected_columns_object(self) -> object:
        """ Retorna a coleção de colunas selecionadas como um objeto.
        """
        return self.component.SelectedColumnsObject

    @property
    def selected_rows(self) -> str:
        """ As linhas selecionadas estão disponíveis como uma coleção. Configurar esta propriedade pode gerar uma exceção se a nova coleção contiver uma linha inválida.
        """
        return self.component.SelectedRows

    @property
    def selected_rows_object(self) -> object:
        """ Retorna a coleção de linhas selecionadas como um objeto.
        """
        return self.component.SelectedRowsObject

    @property
    def visible_column_count(self) -> int:
        """ Recupera o número de colunas visíveis da grade.
        """
        return self.component.VisibleColumnCount

    @property
    def visible_row_count(self) -> int:
        """ Recupera o número de linhas visíveis da grade.
        """
        return self.component.VisibleRowCount


class GuiAbapEditor(GuiShell):
    """ O objeto GuiAbapEditor representa o novo controle do editor ABAP disponível a partir do SAP_BASIS release 6.20 (ver também SAP Note 930742).
    GuiAbapEditor estende GuiShell.
    """

    def auto_brace_enabled(self) -> bool:
        """ Retorna True se a função de autocolchetes estiver atualmente ativada. """
        return self.component.AutoBraceEnabled()

    def auto_complete(self):
        """ Invoca a caixa de lista de auto-completar. """
        self.component.AutoComplete()

    def auto_correct_enabled(self) -> bool:
        """ Retorna True se a função de correção automática estiver atualmente ativada. """
        return self.component.AutoCorrectEnabled()

    def auto_expand(self):
        """ Ativa o mecanismo de autoexpansão de modelos de código. """
        self.component.AutoExpand()

    def auto_indent_enabled(self) -> bool:
        """ Retorna True se a função de autoindentação estiver atualmente ativada. """
        return self.component.AutoIndentEnabled()

    def capitalize(self):
        """ Torna maiúscula a primeira letra alfabética de cada palavra no texto selecionado. Todas as outras letras são transformadas em minúsculas. """
        self.component.Capitalize()

    def clipboard_copy(self):
        """ Realiza uma operação de cópia para a área de transferência no texto atualmente selecionado. """
        self.component.ClipboardCopy()

    def clipboard_cut(self):
        """ Realiza uma operação de corte para a área de transferência no texto atualmente selecionado. """
        self.component.ClipboardCut()

    def clipboard_paste(self):
        """ Cole o conteúdo atual da área de transferência a partir da posição atual do cursor. """
        self.component.ClipboardPaste()

    def clipboard_ring_paste(self, index: int):
        """ Cole uma entrada do anel da área de transferência do editor no editor.
        Index: Índice com base em 1 da entrada da área de transferência conforme aparece no menu de contexto do editor ABAP.
        """
        self.component.ClipboardRingPaste(index)

    def code_hints_enabled(self) -> bool:
        """ Retorna True se as dicas de código estiverem atualmente ativadas. """
        return self.component.CodeHintsEnabled()

    def comment_selected_lines(self):
        """ Coloca as linhas selecionadas entre comentários. """
        self.component.CommentSelectedLines()

    def correct_caps_enabled(self) -> bool:
        """ Retorna True se a função de correção de maiúsculas estiver atualmente ativada. """
        return self.component.CorrectCapsEnabled()

    def delete(self):
        """ Exclui o caractere que segue a posição atual do cursor. Equivalente a pressionar a tecla <DEL>. """
        self.component.Delete()

    def delete_back(self):
        """ Move o cursor para a coluna anterior, excluindo o caractere atualmente presente lá. Equivalente a pressionar a tecla de retrocesso. """
        self.component.DeleteBack()

    def delete_range(self, line_start: int, column_start: int, line_end: int, column_end: int):
        """ Define uma região de texto para exclusão.
        LineStart: Especifica o número da linha a partir da qual a exclusão deve começar.
        ColumnStart: Especifica o número da coluna a partir da qual a exclusão deve começar.
        LineEnd: Especifica o número da linha onde a exclusão terminará.
        ColumnEnd: Especifica o número da coluna onde a exclusão terminará.
        """
        self.component.DeleteRange(line_start, column_start, line_end, column_end)

    def delete_selection(self) -> None:
        """ Exclui o texto atualmente selecionado.
        """
        self.component.DeleteSelection()

    def delete_word(self) -> None:
        """ Exclui a palavra que precede a posição atual do cursor.
        """
        self.component.DeleteWord()

    def delete_word_back(self) -> None:
        """ Exclui a palavra que precede a posição atual do cursor.
        """
        self.component.DeleteWordBack()

    def duplicate_line(self) -> None:
        """ Duplica o conteúdo da linha na qual o cursor está atualmente e insere uma cópia do conteúdo da linha abaixo do cursor.
        """
        self.component.DuplicateLine()

    def format_selected_lines(self) -> None:
        """ Formata as linhas selecionadas conforme as configurações de "Pretty Printer" e "Formatting", como Auto Indent e Smart Tab.
        """
        self.component.FormatSelectedLines()

    def get_auto_complete_entry_count(self) -> int:
        """ Retorna o número de entradas disponíveis exibidas na caixa de lista de auto-completar.
        """
        return self.component.GetAutoCompleteEntryCount()

    def get_auto_complete_entry_text(self, index: int) -> str:
        """ Retorna uma string representando a entrada na caixa de lista de autocompletar correspondente ao índice fornecido como parâmetro.
        """
        return self.component.GetAutoCompleteEntryText(index)

    def get_auto_complete_icon_type(self, index: int) -> int:
        """ Retorna o índice da imagem associada à entrada de autocompletar especificada no índice. Retorna -1 se nenhuma imagem estiver associada.
        """
        return self.component.GetAutoCompleteIconType(index)

    def get_auto_complete_sub_icon_type(self, index: int) -> int:
        """ Retorna o índice da subimagem associada à entrada de autocompletar especificada no índice. Retorna -1 se nenhuma subimagem estiver associada.
        """
        return self.component.GetAutoCompleteSubIconType(index)

    def get_auto_complete_toolbar_button_tool_tip(self, index: int) -> str:
        """ Retorna o texto de dica de ferramenta exibido pelo botão de barra de ferramentas de autocompletar especificado no índice.
        """
        return self.component.GetAutoCompleteToolbarButtonToolTip(index)

    def get_auto_complete_tool_tip_delay(self) -> int:
        """ Retorna o número de milissegundos que passam entre a realçar uma entrada na lista de autocompletar e a exibição da dica de ferramenta correspondente.
        """
        return self.component.GetAutoCompleteToolTipDelay()

    def get_current_tool_tip_text(self) -> str:
        """ Recupera o texto na dica de ferramenta atualmente exibida para dica de código ou lista de auto-completar. Múltiplas linhas são separadas por caracteres \n.
        """
        return self.component.GetCurrentToolTipText()

    def get_cursor_column_position(self) -> int:
        """ Retorna o número da coluna em que o cursor atualmente reside.
        """
        return self.component.GetCursorColumnPosition()

    def get_cursor_line_position(self) -> int:
        """ Retorna o número da linha em que o cursor atualmente reside.
        """
        return self.component.GetCursorLinePosition()

    def get_first_visible_line(self) -> int:
        """ Retorna o número da linha superior visível na sessão atual do editor.
        """
        return self.component.GetFirstVisibleLine()

    def get_html_clipboard_contents(self) -> str:
        """ Retorna uma string contendo o conteúdo atual da área de transferência no formato HTML. Retorna uma string vazia se a área de transferência não contiver nada no formato HTML.
        """
        return self.component.GetHTMLClipboardContents()

    def get_last_visible_line(self) -> int:
        """ Retorna o número da linha inferior visível na sessão atual do editor.
        """
        return self.component.GetLastVisibleLine()

    def get_line_count(self) -> int:
        """ Retorna o número total de linhas contidas no documento na sessão atual.
        """
        return self.component.GetLineCount()

    def get_line_text(self, line: int) -> str:
        """ Retorna uma string contendo o conteúdo da linha especificada pelo parâmetro Line.
        """
        return self.component.GetLineText(line)

    def get_numbered_bookmarks(self, line: int) -> object:
        """ Retorna uma coleção de números de marcadores atribuídos à linha especificada pelo parâmetro Line. O número do marcador pode variar de 0 a 9. Se nenhum marcador numerado estiver atribuído, a coleção estará vazia.
        """
        return self.component.GetNumberedBookmarks(line)

    def get_rtf_clipboard_contents(self) -> str:
        """ Retorna uma string contendo o conteúdo atual da área de transferência no formato Rich Text. Retorna uma string vazia se a área de transferência não contiver nada no formato Rich Text.
        """
        return self.component.GetRTFClipboardContents()

    def get_selected_auto_complete(self) -> int:
        """ Retorna o índice base zero da entrada atualmente selecionada na caixa de lista de autocompletar. O método retornará -1 se nenhuma entrada estiver selecionada.
        """
        return self.component.GetSelectedAutoComplete()

    def get_selected_text(self) -> str:
        """ Retorna uma string contendo o texto atualmente destacado ou selecionado na sessão do editor. Se o texto selecionado abranger mais de uma linha, quaisquer caracteres de terminador de linha serão incluídos na string retornada por este método.
        """
        return self.component.GetSelectedText()

    def get_structure_block_end_line(self, line: int) -> int:
        """ Retorna a linha final do bloco de estrutura relevante para a linha especificada pelo parâmetro Line. Se a linha não estiver dentro de um bloco de estrutura, o método retorna -1.
        """
        return self.component.GetStructureBlockEndLine(line)

    def get_structure_block_start_line(self, line: int) -> int:
        """ Retorna a linha inicial do bloco de estrutura relevante para a linha especificada pelo parâmetro Line. Se a linha estiver dentro de um bloco de estrutura aninhado, a linha inicial do bloco mais interno será retornada. Se a linha não estiver dentro de um bloco de estrutura, o método retorna -1.
        """
        return self.component.GetStructureBlockStartLine(line)

    def get_undo_position(self) -> int:
        """ Retorna a posição atual do documento no buffer de desfazer/refazer.
        """
        return self.component.GetUndoPosition()

    def get_word_wrap_mode(self) -> int:
        """ Retorna um número inteiro correspondente ao modo atual de quebra de linha:
        0 - Quebra de linha desativada.
        1 - Quebra na borda da janela.
        2 - Quebra pela largura da página.
        3 - Quebra pela largura da página inserindo quebra rígida.
        """
        return self.component.GetWordWrapMode()

    def get_word_wrap_position(self) -> int:
        """ Retorna a largura da página atualmente atribuída à quebra de linha. O número retornado é o número de colunas após o qual a quebra de linha será aplicada.
        """
        return self.component.GetWordWrapPosition()

    def go_next_book_mark(self) -> None:
        """ Navega até a linha onde o próximo marcador não numerado está definido.
        """
        self.component.GoNextBookMark()

    def go_numbered_bookmark(self, mark: int) -> None:
        """ Navega até a linha onde o marcador numerado Mark está localizado.
        """
        self.component.GoNumberedBookmark(mark)

    def go_previous_book_mark(self) -> None:
        """ Navega até a linha onde o marcador não numerado anterior está definido.
        """
        self.component.GoPreviousBookMark()

    def insert_tab(self) -> None:
        """ Insere uma TAB na posição atual do cursor. Equivalente a pressionar a tecla TAB.
        """
        self.component.InsertTab()

    def insert_text(self, text: str, line: int, column: int) -> None:
        """ Insere o texto especificado em Text na posição especificada em Line e Column como se o texto tivesse sido digitado no editor a partir do teclado.
        """
        self.component.InsertText(text, line, column)

    def is_auto_complete_entry_bold(self, index: int) -> bool:
        """ Retorna True se a entrada de auto-completar especificada no índice estiver em negrito.
        """
        return bool(self.component.IsAutoCompleteEntryBold(index))

    def is_auto_complete_open(self) -> bool:
        """ Retorna True se a caixa de lista de autocompletar estiver atualmente aberta.
        """
        return bool(self.component.IsAutoCompleteOpen())

    def is_auto_complete_toolbar_button_pressed(self, index: int) -> bool:
        """ Retorna True se o botão da barra de ferramentas de autocompletar especificado no índice estiver atualmente pressionado. Caso contrário, retorna False.
        """
        return bool(self.component.IsAutoCompleteToolbarButtonPressed(index))

    def is_auto_complete_tool_tip_visible(self) -> bool:
        """ Retorna True se a dica de ferramenta correspondente a uma entrada na caixa de lista de autocompletar estiver atualmente visível.
        """
        return bool(self.component.IsAutoCompleteToolTipVisible())

    def is_bookmark(self, line: int) -> bool:
        """ Retorna True se a linha estiver marcada com um marcador padrão que não é numerado. O método não fornece informações sobre se a linha está marcada com um marcador numerado.
        """
        return bool(self.component.IsBookmark(line))

    def is_breakpoint_set(self, line: int) -> bool:
        """ Retorna True se um ponto de interrupção estiver definido na linha especificada pelo parâmetro Line.
        """
        return bool(self.component.IsBreakpointSet(line))

    def is_line_collapsed(self, line: int) -> bool:
        """ Retorna True se o número da linha passado corresponder a uma linha que marca o início de um bloco colapsável que está atualmente no estado colapsado.
        """
        return bool(self.component.IsLineCollapsed(line))

    def is_line_comment(self, line: int) -> bool:
        """ Retorna True se a linha especificada em Line contiver comentários. Caso contrário, retorna False.
        """
        return bool(self.component.IsLineComment(line))

    def is_line_modified(self, line: int) -> bool:
        """ Retorna True se a linha foi modificada durante a sessão atual do editor.
        """
        return bool(self.component.IsLineModified(line))

    def is_modified(self) -> bool:
        """ Retorna True se alguma parte do documento atual foi modificada durante a sessão atual do editor.
        """
        return bool(self.component.IsModified())

    def join_selected_lines(self) -> None:
        """ Mescla as linhas de texto atualmente selecionadas em uma única linha de texto.
        """
        self.component.JoinSelectedLines()

    def lower_case(self) -> None:
        """ Força o texto selecionado a ficar em letras minúsculas.
        """
        self.component.LowerCase()

    def move_cursor_document_end(self) -> None:
        """ Posiciona o cursor na última coluna da última linha do documento.
        """
        self.component.MoveCursorDocumentEnd()

    def move_cursor_line_down(self) -> None:
        """ Move o cursor uma linha para baixo a partir de sua posição atual.
        """
        self.component.MoveCursorLineDown()

    def move_cursor_line_end(self) -> None:
        """ Posiciona o cursor na última coluna da linha atual.
        """
        self.component.MoveCursorLineEnd()

    def move_cursor_line_home(self) -> None:
        """ Posiciona o cursor na primeira coluna da linha atual.
        """
        self.component.MoveCursorLineHome()

    def move_cursor_line_up(self) -> None:
        """ Move o cursor uma linha para cima a partir de sua posição atual.
        """
        self.component.MoveCursorLineUp()

    def move_line_down(self) -> None:
        """ Move o conteúdo da linha em que o cursor está para a linha abaixo e move o conteúdo da linha abaixo do cursor para cima de uma linha.
        """
        self.component.MoveLineDown()

    def move_line_up(self) -> None:
        """ Move o conteúdo da linha em que o cursor está para a linha acima e move o conteúdo da linha acima do cursor para baixo de uma linha.
        """
        self.component.MoveLineUp()

    def move_word_left(self) -> None:
        """ Move o cursor para a coluna que precede a próxima palavra encontrada à esquerda da posição atual do cursor.
        """
        self.component.MoveWordLeft()

    def move_word_right(self) -> None:
        """ Move o cursor para a coluna que precede a próxima palavra encontrada à direita da posição atual do cursor.
        """
        self.component.MoveWordRight()

    def overwrite_mode_enabled(self) -> bool:
        """ Retorna True se o modo de substituição estiver habilitado, false se estiver no modo de inserção.
        """
        return bool(self.component.OverwriteModeEnabled())

    def remove_all_bookmarks(self) -> None:
        """ Remove todos os tipos de marcadores do documento. Tanto os marcadores numerados quanto os não numerados são removidos.
        """
        self.component.RemoveAllBookmarks()

    def remove_all_breakpoints(self) -> None:
        """ Remove todos os pontos de interrupção do documento atual.
        """
        self.component.RemoveAllBreakpoints()

    def remove_bookmarks(self, bookmarks: str) -> None:
        """ Remove todos os marcadores especificados na string fornecida.
        """
        self.component.RemoveBookmarks(bookmarks)

    def remove_breakpoint(self, line: int) -> None:
        """ Remove o ponto de interrupção na linha especificada pelo parâmetro Line.
        """
        self.component.RemoveBreakpoint(line)

    def replace_selection(self, text: str) -> None:
        """ Substitui o texto atualmente selecionado pelo texto contido no parâmetro Text.
        """
        self.component.ReplaceSelection(text)

    def save_to_file(self, file_path: str) -> None:
        """ Salva o documento atual em um arquivo no caminho especificado em p1.
        """
        self.component.SaveToFile(file_path)

    def scroll_to_line(self, line: int) -> None:
        """ Rolamento para a linha especificada pelo parâmetro Line, se ainda não estiver visível na tela.
        """
        self.component.ScrollToLine(line)

    def select_all(self) -> None:
        """ Realça todo o texto no documento atual para seleção.
        """
        self.component.SelectAll()

    def select_block_range(self, line_start: int, column_start: int, line_end: int, column_end: int) -> None:
        """ Realça uma região de texto no modo de bloco para seleção. Equivalente a pressionar a tecla ALT enquanto arrasta o mouse sobre o texto.
        LineStart especifica o número da linha a partir da qual a seleção deve começar.
        ColumnStart especifica o número da coluna a partir da qual a seleção deve começar.
        LineEnd especifica o número da linha onde a seleção terminará.
        ColumnEnd especifica o número da coluna onde a seleção terminará.
        """
        self.component.SelectBlockRange(line_start, column_start, line_end, column_end)

    def select_range(self, line_start: int, column_start: int, line_end: int, column_end: int) -> None:
        """ Realça uma região de texto para seleção.
        LineStart especifica o número da linha a partir da qual a seleção deve começar.
        ColumnStart especifica o número da coluna a partir da qual a seleção deve começar.
        LineEnd especifica o número da linha onde a seleção terminará.
        ColumnEnd especifica o número da coluna onde a seleção terminará.
        """
        self.component.SelectRange(line_start, column_start, line_end, column_end)

    def select_word_left(self) -> None:
        """ Seleciona a palavra à esquerda da posição atual do cursor.
        """
        self.component.SelectWordLeft()

    def select_word_right(self) -> None:
        """ Seleciona a palavra à direita da posição atual do cursor.
        """
        self.component.SelectWordRight()

    def sentencize(self) -> None:
        """ Torna maiúscula a primeira letra de cada sentença. As sentenças são delimitadas por caracteres ".". Todos os outros caracteres são transformados em minúsculas.
        """
        self.component.Sentencize()

    def set_auto_brace(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de autocompletar colchetes.
        """
        self.component.SetAutoBrace(status)

    def set_auto_correct(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de autocorreção automática.
        """
        self.component.SetAutoCorrect(status)

    def set_auto_indent(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de recuo automático.
        """
        self.component.SetAutoIndent(status)

    def set_bookmarks(self, bookmarks: str) -> None:
        """ Define marcadores.
        Aceita uma string no seguinte formato:
        <linha>[(<número>)][,<linha>] por exemplo, "10(1),22(2),33,42", <linha>={1,...,n}, <número>={1,...
        """
        self.component.SetBookmarks(bookmarks)

    def set_breakpoint(self, line: int) -> None:
        """ Define um ponto de interrupção na linha especificada pelo parâmetro Line.
        """
        self.component.SetBreakpoint(line)

    def set_code_hints(self, status: bool) -> None:
        """ Ativa ou desativa as dicas de código.
        """
        self.component.SetCodeHints(status)

    def set_correct_caps(self, status: bool) -> None:
        """ Ativa ou desativa a correção automática de maiúsculas.
        """
        self.component.SetCorrectCaps(status)

    def set_line_feed_style(self, style: int) -> None:
        """ Define o estilo de quebra de linha.
        """
        self.component.SetLineFeedStyle(style)

    def set_overwrite_mode(self, status: bool) -> None:
        """ Alterna entre os modos de Inserção e Sobrescrita. Se chamado com True, o modo de Sobrescrita é ativado. Caso contrário, o editor está no modo de Inserção.
        """
        self.component.SetOverwriteMode(status)

    def set_selection_pos_in_line(self, linha: int, coluna: int) -> None:
        """ Posiciona o cursor na linha <Linha> e coluna <Coluna>.
        """
        self.component.SetSelectionPosInLine(linha, coluna)

    def set_smart_tab(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de Smart Tab.
        """
        self.component.SetSmartTab(status)

    def set_word_wrap_mode(self, modo: int) -> None:
        """ Define o modo de quebra de linha conforme o número fornecido em Modo:
        0 - Quebra de linha desativada.
        1 - Quebrar na borda da janela.
        2 - Quebrar na largura da página.
        3 - Quebrar na largura da página inserindo quebra rígida.
        """
        self.component.SetWordWrapMode(modo)

    def set_word_wrap_position(self, pos: int) -> None:
        """ Pos especifica o número de colunas a serem exibidas antes da quebra de palavras ser aplicada.
        """
        self.component.SetWordWrapPosition(pos)

    def smart_tab_enabled(self) -> bool:
        """ Retorna True se a funcionalidade de Smart Tab estiver habilitada, false caso contrário.
        """
        return bool(self.component.SmartTabEnabled())

    def sort_selected_lines(self) -> None:
        """ Rearranja as linhas selecionadas em ordem alfanumérica.
        """
        self.component.SortSelectedLines()

    def swap_case(self) -> None:
        """ Inverte a configuração de maiúsculas/minúsculas para o texto selecionado. Os caracteres maiúsculos são trocados por minúsculos e vice-versa.
        """
        self.component.SwapCase()

    def toggle_caps_lock(self) -> None:
        """ Ativa ou desativa a tecla Caps Lock.
        """
        self.component.ToggleCapsLock()

    def toggle_numbered_bookmark(self, marcador: int, linha: int) -> None:
        """ Alterna o estado do marcador numerado <Marcador> na linha <Linha>. Se já existir um marcador com o número <Marcador> na linha, ele será removido. Caso contrário, ele será adicionado.
        """
        self.component.ToggleNumberedBookmark(marcador, linha)

    def toggle_structure_block(self, linha: int) -> None:
        """ Se o número da linha especificado em <Linha> for a primeira linha de um bloco de código recolhível, este método alternará o status expandido/recolhido do bloco.
        """
        self.component.ToggleStructureBlock(linha)

    def transpose_line(self) -> None:
        """ Troca o conteúdo da linha em que o cursor está atualmente com o conteúdo da linha acima da posição atual do cursor.
        """
        self.component.TransposeLine()

    def uncomment_selected_lines(self) -> None:
        """ Remove os comentários das linhas selecionadas.
        """
        self.component.UncommentSelectedLines()

    def undo(self, posicao_undo: int) -> None:
        """ Realiza um undo ou redo, dependendo de PosicaoUndo. PosicaoUndo especifica uma posição baseada em zero no buffer de undo/redo. Se -1 for passado, um único passo de undo será executado.
        """
        self.component.Undo(posicao_undo)

    def un_tab(self) -> None:
        """ Remove uma TAB na posição atual do cursor. Equivalente a pressionar <SHIFT> + <TAB>.
        """
        self.component.UnTab()

    def upper_case(self) -> None:
        """ Força o texto selecionado a ficar em maiúsculas.
        """
        self.component.UpperCase()

