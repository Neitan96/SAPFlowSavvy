
class SapConnNames:
    ECC = '1. ECC - Produção (DFP)'
    EWM = '2. EWM - Produção (EWP)'


class SapTransactions:
    LOGIN = 'S000'  # Tela de login
    MAIN_MENU = 'SESSION_MANAGER'  # Menu principal
    TRANS_EWM_MONITOR = '/SCWM/MON'  # Monitor de WM


class SapPrograms:
    LOGIN = 'SAPMSYST'  # Tela de login
    MAIN_MENU = 'SAPLSMTR_NAVIGATION'  # Menu principal


class SapCommands:
    CLOSE_SESSION = '/i'
    CLOSE_ALL_SESSIONS = '/nex'
    DEBUG = '/h'
    RETURN_MENU = '/n'
    POPUP_SESSIONS = '/o'


class SapFields:
    # Geral
    ALERT_STATUS_PANE = 'wnd[0]/sbar/pane[0]'

    # Tela de login
    LOGIN_USERNAME = 'wnd[0]/usr/txtRSYST-BNAME'
    LOGIN_PASSWORD = 'wnd[0]/usr/pwdRSYST-BCODE'
    LOGIN_MANDT = 'wnd[0]/usr/txtRSYST-MANDT'
    LOGIN_LANGUAGE = 'wnd[0]/usr/txtRSYST-LANGU'

    # Pop-up número de tentativas falhadas
    POP_UP_COUNT_FAILS_ICON = 'wnd[1]/usr/txtIK1'
    POP_UP_COUNT_FAILS_LABEL_LINE_1 = 'wnd[1]/usr/txtMESSTXT1'
    POP_UP_COUNT_FAILS_LABEL_LINE_2 = 'wnd[1]/usr/txtMESSTXT2'
    POP_UP_COUNT_FAILS_BNT_OK = 'wnd[1]/tbar[0]/btn[0]'
    POP_UP_COUNT_FAILS_BNT_HELP = 'wnd[1]/tbar[0]/btn[1]'

    # Pop-up logon múltiplo
    POPUP_MULTI_LOGIN_LABEL_LINE_1 = 'wnd[1]/usr/txtMULTI_LOGON_TEXT'
    POPUP_MULTI_LOGIN_LABEL_LINE_2 = 'wnd[1]/usr/txtMULTI_LOGON_TEXT2'
    POPUP_MULTI_LOGIN_LABEL_LINE_3 = 'wnd[1]/usr/lbl%#AUTOTEXT001'
    POPUP_MULTI_LOGIN_LABEL_LINE_4 = 'wnd[1]/usr/lbl%#AUTOTEXT002'
    POPUP_MULTI_LOGIN_LABEL_LINE_5 = 'wnd[1]/usr/lbl%#AUTOTEXT003'
    POPUP_MULTI_LOGIN_RAD_FORCE = 'wnd[1]/usr/radMULTI_LOGON_OPT1'
    POPUP_MULTI_LOGIN_RAD_CANCEL = 'wnd[1]/usr/radMULTI_LOGON_OPT3'

    # Pop-up confirmação de logoff
    POPUP_LOGOFF_WARNING = 'wnd[1]/usr/txtSPOP-TEXTLINE1'
    POPUP_LOGOFF_QUESTION = 'wnd[1]/usr/txtSPOP-TEXTLINE2'
    POPUP_LOGOFF_BNT_YES = 'wnd[1]/usr/btnSPOP-OPTION1'
    POPUP_LOGOFF_BNT_NO = 'wnd[1]/usr/btnSPOP-OPTION2'
