Option Explicit
Option Private Module

' Author: Nathan Almeida
' Link: https://gist.github.com/Neitan96/179c29053f00e6cd4fdb166c8b314af0

' Dependências:
' VBAHelper: https://gist.github.com/Neitan96/5faf771139f8a5eaacf4838a1ec1417b

'========--------========
'     Configs da API
'========--------========

'!!!-> Parâmetros de execução do SAP

' Caminho do executavel do SAP.
Public Const sap_exe_path As String = "C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"

' Auto inicia o SAP ao usar a API InitSAP.
Public Const SAP_Auto_Start As Boolean = True

' Verifica se já tem uma conexão compatível aberta e abre uma nova janela para a macro.
Public Const SAP_Reuse_Connection As Boolean = True

' Habilita a reutilização de conexões abertas de outros usuários logados no SAP
Public Const SAP_Reuse_Login As Boolean = True

' Minimiza novas janelas abertas
Public Const SAP_Minimize_Windows As Boolean = True


'!!!-> Parâmetros de logon

' Force = Derruba o usuário caso já esteja logado em outro lugar.
' Exit = Finaliza a macro caso o usuário já esteja logado em outro lugar.
' Wait = Caso o usuário já esteja logado em outro lugar cancela o login
' e tenta novamente após um tempo definido.
Public Const SAP_Login_force_Method As String = "Force"

' O intervalo de tempo para tentar fazer login novamente caso
' o método de força de login for 'Wait'
Public Const SAP_Login_Wait_Seconds As Integer = 10

' Quantidade máxima de tentativas de login falhas,
' essa contagem não inclui o método de força de login 'Wait'
Public Const SAP_Login_Try_Max As Integer = 3

' Wait = Abre a tela de login e aguarda o usuário logar.
' InputBox = Abre uma caixa de mensagem de login e senha
'            e armazerna em uma variavel.
' FileTemp = Abre uma caixa de mensagem de login e senha
'            e armazerna em um arquivo na pasta pessoal.
Public Const SAP_Login_Method As String = "FileTemp"

' Caminho do arquivo de armazenamento do login e senha caso
' o método de login for 'FileTemp'
Public Const SAP_Login_Filepath As String = "/sapusercredentials.creds"

' Habilita o armazenamento de login por conexão
Public Const SAP_Login_Multi_Arm As Boolean = True

'========--------========
'   Variaveis globais
'========--------========

' Variaveis de armazenamento de credenciais
Global sap_creds_conns As New Collection
Global sap_creds_users As New Collection
Global sap_creds_passwords As New Collection

'========--------========
' Listagens de Transações, programas e conexões
'========--------========

' Nome das conexões disponiveis do SAP.
Public Const sap_conn_name_ecc As String = "1. ECC - Produção (DFP)"
Public Const sap_conn_name_ewm As String = "2. EWM - Produção (EWP)"

' Tela de login
Public Const TRANS_LOGIN As String = "S000"
Public Const PROG_LOGIN As String = "SAPMSYST"

' Menu principal
Public Const TRANS_MAIN_MENU As String = "SESSION_MANAGER"
Public Const PROG_MAIN_MENU As String = "SAPLSMTR_NAVIGATION"

' Monitor de WM
Public Const TRANS_EWM_MONITOR As String = "/SCWM/MON"

'========--------========
'    Listagens de IDS
'========--------========

Public Const ID_LOGIN_USERNAME As String = "wnd[0]/usr/txtRSYST-BNAME"
Public Const ID_LOGIN_PASSWORD As String = "wnd[0]/usr/pwdRSYST-BCODE"
Public Const ID_LOGIN_MANDT As String = "wnd[0]/usr/txtRSYST-MANDT"

Public Const ID_ALERTS_BAR As String = "wnd[0]/sbar/pane[0]"

'========--------========
'   Listagem de teclas
'========--------========

Public Const SAP_KEY_ENTER As Integer = 0
Public Const SAP_KEY_F1 As Integer = 1
Public Const SAP_KEY_F2 As Integer = 2
Public Const SAP_KEY_F3 As Integer = 3
Public Const SAP_KEY_F4 As Integer = 4
Public Const SAP_KEY_F5 As Integer = 5
Public Const SAP_KEY_F6 As Integer = 6
Public Const SAP_KEY_F7 As Integer = 7
Public Const SAP_KEY_F8 As Integer = 8
Public Const SAP_KEY_F9 As Integer = 9
Public Const SAP_KEY_F10 As Integer = 10
Public Const SAP_KEY_CTRL_S As Integer = 11
Public Const SAP_KEY_F12 As Integer = 12
Public Const SAP_KEY_SHIFT_F1 As Integer = 13
Public Const SAP_KEY_SHIFT_F2 As Integer = 14
Public Const SAP_KEY_SHIFT_F3 As Integer = 15
Public Const SAP_KEY_SHIFT_F4 As Integer = 16
Public Const SAP_KEY_SHIFT_F5 As Integer = 17
Public Const SAP_KEY_SHIFT_F6 As Integer = 18
Public Const SAP_KEY_SHIFT_F7 As Integer = 19
Public Const SAP_KEY_SHIFT_F8 As Integer = 20
Public Const SAP_KEY_SHIFT_F9 As Integer = 21
Public Const SAP_KEY_SHIFT_CTRL_0 As Integer = 22
Public Const SAP_KEY_SHIFT_F11 As Integer = 23
Public Const SAP_KEY_SHIFT_F12 As Integer = 24
Public Const SAP_KEY_CTRL_F1 As Integer = 25
Public Const SAP_KEY_CTRL_F2 As Integer = 26
Public Const SAP_KEY_CTRL_F3 As Integer = 27
Public Const SAP_KEY_CTRL_F4 As Integer = 28
Public Const SAP_KEY_CTRL_F5 As Integer = 29
Public Const SAP_KEY_CTRL_F6 As Integer = 30
Public Const SAP_KEY_CTRL_F7 As Integer = 31
Public Const SAP_KEY_CTRL_F8 As Integer = 32
Public Const SAP_KEY_CTRL_F9 As Integer = 33
Public Const SAP_KEY_CTRL_F10 As Integer = 34
Public Const SAP_KEY_CTRL_F11 As Integer = 35
Public Const SAP_KEY_CTRL_F12 As Integer = 36
Public Const SAP_KEY_CTRL_SHIFT_F1 As Integer = 37
Public Const SAP_KEY_CTRL_SHIFT_F2 As Integer = 38
Public Const SAP_KEY_CTRL_SHIFT_F3 As Integer = 39
Public Const SAP_KEY_CTRL_SHIFT_F4 As Integer = 40
Public Const SAP_KEY_CTRL_SHIFT_F5 As Integer = 41
Public Const SAP_KEY_CTRL_SHIFT_F6 As Integer = 42
Public Const SAP_KEY_CTRL_SHIFT_F7 As Integer = 43
Public Const SAP_KEY_CTRL_SHIFT_F8 As Integer = 44
Public Const SAP_KEY_CTRL_SHIFT_F9 As Integer = 45
Public Const SAP_KEY_CTRL_SHIFT_F10 As Integer = 46
Public Const SAP_KEY_CTRL_SHIFT_F11 As Integer = 47
Public Const SAP_KEY_CTRL_SHIFT_F12 As Integer = 48
Public Const SAP_KEY_CTRL_E As Integer = 70
Public Const SAP_KEY_CTRL_F As Integer = 71
Public Const SAP_KEY_CTRL_BAR As Integer = 72
Public Const SAP_KEY_CTRL_BACKSLASH As Integer = 73
Public Const SAP_KEY_CTRL_N As Integer = 74
Public Const SAP_KEY_CTRL_O As Integer = 75
Public Const SAP_KEY_CTRL_X As Integer = 76
Public Const SAP_KEY_CTRL_C As Integer = 77
Public Const SAP_KEY_CTRL_V As Integer = 78
Public Const SAP_KEY_CTRL_Z As Integer = 79
Public Const SAP_KEY_CTRL_PAGEUP As Integer = 80
Public Const SAP_KEY_PAGEUP As Integer = 81
Public Const SAP_KEY_PAGEDOWN As Integer = 82
Public Const SAP_KEY_CTRL_PAGEDOWN As Integer = 83
Public Const SAP_KEY_CTRL_G As Integer = 84
Public Const SAP_KEY_CTRL_R As Integer = 85
Public Const SAP_KEY_CTRL_P As Integer = 86

'========--------========
'        Módulos
'========--------========

'->!! Helper
' Prefixo: HelperSAP_
' Status: Finalizado
' Descrição:
' Módulo com funções de ajuda para toda a biblioteca.

'->!! Login Arm
' Prefixo: CredsSAP_
' Status: Finalizado
' TODOs: Não
' Escopo: Fazer a leitura e gravação de credenciais do usuário.
' # Descrição:
' Módulo para fazer o armazenamento de credenciais de login.

'->!! SAP Init
' Prefixo: InitSAP_
' Status: Finalizado
' TODOs: Sim
' Escopo: Inicialização do SAP até a tela de login.
' # Descrição:
' Faz a inicialização do SAP, desde o início do processo do SAP, criações de conexões e sessões.

'->!! SAP Login
' Prefixo: InitSAP_
' Status: Finalizado
' TODOs: Não
' Escopo: Somente a tela de login e verificação de login em sessões.
' # Descrição:
' Faz todo o processo de login no SAP, verificando senha incorretas, login já logado e etc.

'->!! SAP Sessions
' Prefixo: SessionSAP_
' Status: Em progresso
' TODOs: -
' Escopo: Somente funções que envolva diretamente sessões.
' # Descrição:
' Funções para auxiliar o controle e gerenciamento de sessões.

'========--------========
'         Helper
'========--------========

' Verifica se objetos do SAP do tipo Collection são válidos.
Public Function HelperSAP_CheckCollection(ByVal colletion As Object, Optional check_count As Boolean = True)
    If Not CheckObject(colletion) Then
        HelperSAP_CheckCollection = False
        Exit Function
    End If
    
    On Error GoTo ErrorTryCheckCollEmp
    If check_count And colletion.Children.count < 1 Then
        GoTo ErrorTryCheckCollEmp
    End If
    
    HelperSAP_CheckCollection = True
    Exit Function
    
ErrorTryCheckCollEmp:
    HelperSAP_CheckCollection = False
End Function

' Retorna o nome sem espaços e caracteres especiais para sessões de arquivos de configurações
Public Function HelperSAP_NameToPathIniFile(name As String)
    HelperSAP_NameToPathIniFile = UCase(RegexReplace(name, "[^a-z|^A-Z]", ""))
End Function

'========--------========
'       Login Arm
'========--------========

' Retorna o caminho completo do arquivo de armazenamento de credenciais
Public Function CredsSAP_GetFullFilePath()
    CredsSAP_GetFullFilePath = SAP_Login_Filepath
    If Left(CredsSAP_GetFullFilePath, 1) = "/" Or Left(CredsSAP_GetFullFilePath, 1) = "\" Then _
        CredsSAP_GetFullFilePath = Environ(Environ_User_Folder) & CredsSAP_GetFullFilePath
End Function

' Retorna o nome da conexão caso o login por conexão esteja habilitado,
' ou retorna o nome padrão caso esteja desabilitado.
Public Function CredsSAP_GetConnNameKey(Optional conn_name As String = "Default")
    If SAP_Login_Multi_Arm Then
        CredsSAP_GetConnNameKey = conn_name
    Else
        CredsSAP_GetConnNameKey = "Default"
    End If
End Function

' Retorna o index das credenciais da conexão na variavel global
Public Function CredsSAP_GetConnNameIndex(Optional conn_name As String = "Default") As Integer
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    Dim index As Integer
    For index = 1 To sap_creds_conns.count
        If sap_creds_conns.Item(index) = conn_name Then
            CredsSAP_GetConnNameIndex = index
            Exit Function
        End If
    Next index
    CredsSAP_GetConnNameIndex = -1
End Function

' Obtém o nome de usuário SAP da conexão
Public Function CredsSAP_GetUserName(Optional conn_name As String = "Default")
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    Dim index As Integer
    index = CredsSAP_GetConnNameIndex(conn_name)
    If index > 0 Then _
        CredsSAP_GetUserName = sap_creds_users.Item(index)
End Function

' Obtém a senha de usuário SAP da conexão
Public Function CredsSAP_GetPassword(Optional conn_name As String = "Default")
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    Dim index As Integer
    index = CredsSAP_GetConnNameIndex(conn_name)
    If index > 0 Then _
        CredsSAP_GetPassword = sap_creds_passwords.Item(index)
End Function

' Define as credenciais de login na variavel global,
' essa função não afeta o arquivo de armazenamento
Public Function CredsSAP_SetCredsInGlobal(user_name As String, password As String, Optional conn_name As String = "Default")
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    Dim index_creds As Integer
    index_creds = CredsSAP_GetConnNameIndex(conn_name)
    
    If index_creds > 0 Then
        sap_creds_conns.Remove index_creds
        sap_creds_users.Remove index_creds
        sap_creds_passwords.Remove index_creds
    End If
    
    If CheckString(user_name) And CheckString(password) Then
        sap_creds_conns.Add conn_name
        sap_creds_users.Add user_name
        sap_creds_passwords.Add password
    End If
    
End Function

' Faz a leitura do login e senha do usuário SAP pelo método de armazenamento,
' caso o método de armazenamento de login for FileTemp e não tiver login e senha
' armazenados no arquivo ele fará a leitura do login e senha por meio de inputbox
' e salvar no arquivo e variaveis, caso o método de armazenamento de login for Wait,
' a função não fará nada.
Public Function CredsSAP_Read(Optional conn_name As String = "Default", Optional ForceRead As Boolean = False) As Boolean
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    If Not ForceRead Then
        If CheckString(CredsSAP_GetUserName(conn_name)) _
                And CheckString(CredsSAP_GetPassword(conn_name)) Then
            CredsSAP_Read = True
            Exit Function
        End If
    End If
    
    If SAP_Login_Method = "FileTemp" Then
        If Not CredsSAP_ReadFileLogin(conn_name) Then
            If CredsSAP_ReadInputLogin(conn_name) Then
                CredsSAP_WriteFileLogin conn_name
                CredsSAP_Read = True
            Else
                CredsSAP_ClearConn conn_name
                CredsSAP_Read = False
            End If
        Else
            CredsSAP_Read = True
        End If
    ElseIf SAP_Login_Method = "InputBox" Then
        CredsSAP_Read = CredsSAP_ReadInputLogin(conn_name)
    End If
    
End Function

' Limpar todos os armazenamentos de login e senha do usuário SAP
' Deleta o arquivo de armazenamento de login e limpa as variaveis
' de login e senha.
Public Function CredsSAP_ClearAll()
    On Error Resume Next
    
    While sap_creds_conns.count > 0
        sap_creds_conns.Remove 1
    Wend
    
    While sap_creds_users.count > 0
        sap_creds_users.Remove 1
    Wend
    
    While sap_creds_passwords.count > 0
        sap_creds_passwords.Remove 1
    Wend
    
    If FileExists(CredsSAP_GetFullFilePath) Then Kill CredsSAP_GetFullFilePath
End Function

' Limpar os armazenamentos de login e senha da conexão especificada.
Public Function CredsSAP_ClearConn(Optional conn_name As String = "Default")
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    On Error Resume Next
    
    CredsSAP_SetCredsInGlobal "", "", conn_name
    
    Dim Session_name As String
    Session_name = HelperSAP_NameToPathIniFile(conn_name)
    
    IniWriteParameter CredsSAP_GetFullFilePath, Session_name, vbNullString, vbNullString
    
End Function

' Faz a leitura do login e senha por meio de inputbox
' Exibe um inputbox para digitar o login e em seguida exibe
' outro inputbox para digitar a senha, a senha não é ocultada
' ao digitar.
Public Function CredsSAP_ReadInputLogin(Optional conn_name As String = "Default") As Boolean
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    On Error GoTo TryCredsSAP_ReadInputLogin
    
    Dim Login As Variant, password As Variant
    If conn_name = "Default" Then
        Login = Application.InputBox("Digite seu login:", "Login SAP", Type:=2)
        password = Application.InputBox("Digite sua senha:", "Login SAP", Type:=2)
    Else
        Login = Application.InputBox("Digite seu login para a conexão:" & vbCrLf & conn_name, "Login SAP", Type:=2)
        password = Application.InputBox("Digite sua senha para a conexão:" & vbCrLf & conn_name, "Login SAP", Type:=2)
    End If
    
    If TypeName(Login) = "Boolean" Or TypeName(password) = "Boolean" Or _
            Not CheckString(CStr(Login)) Or Not CheckString(CStr(password)) Then
            
        If MsgBoxYesNo("Login ou senha em branco, deseja inserir login novamente?") Then
            CredsSAP_ReadInputLogin = CredsSAP_ReadInputLogin(conn_name)
            Exit Function
        Else
            CredsSAP_SetCredsInGlobal "", "", conn_name
            CredsSAP_ReadInputLogin = False
        End If
        Exit Function
    End If
    
    CredsSAP_SetCredsInGlobal CStr(Login), CStr(password), conn_name
    CredsSAP_ReadInputLogin = True
    
    Exit Function
    
TryCredsSAP_ReadInputLogin:
    CredsSAP_ReadInputLogin = False
End Function

' Armazena o login e senha do usuário em arquivo de configurações
' é armazenado o login e senha de acordo com as variaveis de login e senha,
' caso o login ou a senha estiver em branco ele não armazenará.
Public Function CredsSAP_WriteFileLogin(Optional conn_name As String = "Default") As Boolean
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    On Error GoTo TryCredsSAP_WriteFileLogin
    
    Dim index_creds As Integer
    index_creds = CredsSAP_GetConnNameIndex(conn_name)
    
    If index_creds < 1 Or Not CheckString(sap_creds_users.Item(index_creds)) Or Not CheckString(sap_creds_passwords.Item(index_creds)) Then
        CredsSAP_ClearConn conn_name
        CredsSAP_WriteFileLogin = False
        Exit Function
    End If
    
    Dim Session_name As String
    Session_name = HelperSAP_NameToPathIniFile(conn_name)
    
    CredsSAP_WriteFileLogin = IniWriteParameter(CredsSAP_GetFullFilePath, Session_name, "username", sap_creds_users.Item(index_creds)) _
                            And IniWriteParameter(CredsSAP_GetFullFilePath, Session_name, "password", sap_creds_passwords.Item(index_creds))
    
    CredsSAP_WriteFileLogin = True
    Exit Function
    
TryCredsSAP_WriteFileLogin:
    CredsSAP_WriteFileLogin = False
End Function

' Faz a leitura do login e senha do usuário por meio do arquivo de configurações
' após a leitura o login e senha é armazenado nas variaveis de login e senha,
' caso tiver algum erro na leitura ou o login ou senha estiver em branco
' não será armazenado nenhuma das variaveis.
Public Function CredsSAP_ReadFileLogin(Optional conn_name As String = "Default") As Boolean
    conn_name = CredsSAP_GetConnNameKey(conn_name)
    
    On Error GoTo TryCredsSAP_ReadFileLogin
    
    Dim Session_name As String
    Session_name = HelperSAP_NameToPathIniFile(conn_name)
    
    Dim user_name_rd As String, password_rd As String
    user_name_rd = IniReadParameter(CredsSAP_GetFullFilePath, Session_name, "username")
    password_rd = IniReadParameter(CredsSAP_GetFullFilePath, Session_name, "password")
    
    CredsSAP_SetCredsInGlobal user_name_rd, password_rd, conn_name
    
    If Not CheckString(user_name_rd) Or Not CheckString(password_rd) Then
        CredsSAP_ClearConn conn_name
        CredsSAP_ReadFileLogin = False
        Exit Function
    End If
    
    CredsSAP_ReadFileLogin = True
    Exit Function
    
TryCredsSAP_ReadFileLogin:
    CredsSAP_ReadFileLogin = False
End Function

'========--------========
'        SAP Init
'========--------========

' Inicia o SAP Logon de acordo com o caminho definido no sap_path
Public Function InitSAP_StartProcess() As Boolean
    On Error GoTo TryInitSAPStartProcess
    
    Shell sap_exe_path, vbNormalFocus
    Dim WSHShell As Object
    Set WSHShell = CreateObject("WScript.Shell")
    Do Until WSHShell.AppActivate("SAP Logon ")
        WaitSeconds 2
    Loop
    Set WSHShell = Nothing

    InitSAP_StartProcess = True
    Exit Function
TryInitSAPStartProcess:
    InitSAP_StartProcess = False
End Function

' Força a finalização do programa do SAP
Public Function InitSAP_KillProcess()
    Shell "taskkill /f /im saplogon.exe", vbHide
End Function

' Verifica se o SAP Logon está aberto
Public Function InitSAP_CheckStarted() As Boolean
    On Error GoTo TryInitSAP_CheckStarted
    Dim sap_gui As Object
    Set sap_gui = GetObject("SAPGUI")
    InitSAP_CheckStarted = CheckObject(sap_gui)
    Exit Function
TryInitSAP_CheckStarted:
    InitSAP_CheckStarted = False
End Function

' Obtém o objeto do SAP Gui,
' Caso o SAP não estiver aberto e o parametro SAP_Auto_Start
' for verdadeiro ele iniciará automaticamente o SAP
Public Function InitSAP_GetSAPGui() As Object
    On Error Resume Next
    If SAP_Auto_Start And Not InitSAP_CheckStarted Then InitSAP_StartProcess
    Set InitSAP_GetSAPGui = GetObject("SAPGUI")
End Function

' Obtém o aplicativo do SAP,
' Caso o SAP não estiver aberto e o parametro SAP_Auto_Start
' for verdadeiro ele iniciará automaticamente o SAP
Public Function InitSAP_GetSAPApp(Optional ByVal sap_gui As Object) As Object
    On Error Resume Next
    If Not CheckObject(sap_gui) Then Set sap_gui = InitSAP_GetSAPGui
    Set InitSAP_GetSAPApp = sap_gui.GetScriptingEngine
End Function

' Abre uma nova conexão do SAP pelo nome,
' Caso o SAP não estiver aberto e o parametro SAP_Auto_Start
' for verdadeiro ele iniciará automaticamente o SAP
Public Function InitSAP_OpenConnection(ByVal conn_name As String, Optional ByVal sap_app As Object) As Object
    If Not CheckObject(sap_app) Then Set sap_app = InitSAP_GetSAPApp
    Set InitSAP_OpenConnection = sap_app.OpenConnection(conn_name, True)
    If SAP_Minimize_Windows Then SessionSAP_Minimize InitSAP_OpenConnection.Children(0)
End Function

' Obtém conexões do SAP de acordo com o nome da conexão, se o nome da conexão
' estiver em branco ele retorna a todas as conexões,
' caso não encontrar uma conexão com os criterios e o parametro SAP_Auto_Start
' for verdadeiro ele iniciará automaticamente uma nova conexão.
' O método de retorno é uma collection com as conexões.
Public Function InitSAP_GetConnection(Optional conn_name As String = "", Optional ByVal sap_app As Object) As Collection
    If Not CheckObject(sap_app) Then Set sap_app = InitSAP_GetSAPApp
    
    Set InitSAP_GetConnection = New Collection

    Dim connections, conn As Object
    If CheckObject(sap_app) Then Set connections = sap_app.connections()
    
    If CheckObject(connections) Then
        Dim i As Long
        For i = 0 To connections.count() - 1
            Set conn = sap_app.Children(CLng(i))
            If CheckObject(conn) Then
            
                If Not CheckString(conn_name) Or conn.Description = conn_name Then
                    InitSAP_GetConnection.Add conn
                End If
                
            End If
        Next
    End If
    
    ' Verifica se foi achada alguma conexão, se não foi achada ele abre uma nova conexão
    If SAP_Auto_Start And InitSAP_GetConnection.count < 1 Then
        Set conn = InitSAP_OpenConnection(conn_name, sap_app)
        If CheckObject(conn) Then InitSAP_GetConnection.Add conn
    End If
    
End Function

'========--------========
'   SAP Init - Sessions
'========--------========

' Obtém um sessão do SAP a partir do objeto de uma conexão
' Param get_session_no_user: Habilita a obtenção de sessões sem usuários logados.
Public Function InitSAP_GetSessionByConn(ByVal sap_conn As Object, Optional get_session_no_user As Boolean = True) As Object
    If Not CheckObject(sap_conn) Then Exit Function

    Dim sessions, sess, infos As Object
    Set sessions = sap_conn.sessions()
    
    Dim i As Long
    For i = 0 To sessions.count() - 1
        Set sess = sap_conn.Children(CLng(i))
        If HelperSAP_CheckCollection(sess) Then
            
            ' Verifica a reutilização de login
            If SAP_Reuse_Login Then
                Set InitSAP_GetSessionByConn = sess
                Exit Function
            End If
            
            Set infos = sess.info()
            If CheckObject(infos) Then
                ' Verificando o login ativo da sessão
                Dim user_name As String
                
                CredsSAP_Read sap_conn.Description
                user_name = CredsSAP_GetUserName(sap_conn.Description)
                
                If (get_session_no_user And Not CheckString(infos.user)) Or _
                    (CheckString(user_name) And infos.user = user_name) Then
                    Set InitSAP_GetSessionByConn = sess
                    Exit Function
                End If
            End If
            
        End If
    Next
    
End Function

' Obtém uma sessão do SAP a partir do nome da conexão, fazendo a procura por sessões
' validas em todas as conexões com o nome passado pelo parâmetro.
' Param conn_name: Nome da conexão para fazer a busca de sessões.
Public Function InitSAP_GetSessionByNameConn(ByVal conn_name As String) As Object
    Dim connections As Collection
    Set connections = InitSAP_GetConnection(conn_name:=conn_name)
    
    Dim conn, Session As Object
    For Each conn In connections
        Set Session = InitSAP_GetSessionByConn(conn, True)
        If HelperSAP_CheckCollection(Session) Then
            Set InitSAP_GetSessionByNameConn = Session
            Exit Function
        End If
    Next
    
End Function

' Abre uma nova sessão do SAP a partir do nome da conexão.
' Param conn_name: Nome da conexão para iniciar a nova sessão.
' Param sap_app: Aplicativo do SAP para fazer a busca das conexões.
Public Function InitSAP_OpenSession(Optional conn_name As String = "", Optional ByVal sap_app As Object) As Object
    Set InitSAP_OpenSession = InitSAP_GetSessionByConn(InitSAP_OpenConnection(conn_name, sap_app))
End Function

'========--------========
'      SAP Login
'========--------========

' Verifica se a sessão tem login ativo ou um login específico.
' Param sap_session: Sessão para fazer a validação do login.
' Param user_name: Login de checagem da sessão.
Public Function InitSAP_CheckLoged(ByVal sap_session As Object, Optional user_name As String = "") As Boolean
    On Error GoTo TryInitSAP_CheckLoged
    
    Dim infos As Object
    Set infos = sap_session.info()
    
    If infos.user = "" Then GoTo TryInitSAP_CheckLoged
    If user_name <> "" And infos.user <> user_name Then GoTo TryInitSAP_CheckLoged
    
    InitSAP_CheckLoged = True
    Exit Function
    
TryInitSAP_CheckLoged:
    InitSAP_CheckLoged = False
End Function

' Faz o login do SAP de acordo com os parâmetros configurados na biblioteca.
' Param sap_session: Sessão para fazer o login.
Public Function InitSAP_Login(sap_session As Object, Optional try_count As Integer = 1) As Boolean
    On Error GoTo TryInitSAP_Login
    If Not HelperSAP_CheckCollection(sap_session) Then Exit Function
    If InitSAP_CheckLoged(sap_session) Then Exit Function
    If SessionSAP_GetTransaction(sap_session) <> TRANS_LOGIN Then Exit Function
    
    ' Verificando se o metodo de login é manual
    If SAP_Login_Method = "Wait" Then
        ' Aguardando o usuário fazer login
        While HelperSAP_CheckCollection(sap_session) And Not InitSAP_CheckLoged(sap_session)
            WaitSeconds 2
        Wend
    Else
    
        If CredsSAP_Read(sap_session.Parent.Description) Then
            Dim user_name As String, password As String
            user_name = CredsSAP_GetUserName(sap_session.Parent.Description)
            password = CredsSAP_GetPassword(sap_session.Parent.Description)
            
            ' Verificando e realizando login com as credenciais lidas
            If CheckString(user_name) And CheckString(password) Then
                SessionSAP_FindID(sap_session, ID_LOGIN_MANDT).Text = "300"
                SessionSAP_FindID(sap_session, ID_LOGIN_USERNAME).Text = user_name
                SessionSAP_FindID(sap_session, ID_LOGIN_PASSWORD).Text = password
                SessionSAP_SendKey sap_session, SAP_KEY_ENTER
            End If
            
        Else
            InitSAP_Login = False
            Exit Function
        End If
    
    End If
    
    ' Verificando se o login ou a senha estava errada
    Dim AlertCheck As String
    If SessionSAP_InAlertBarMsg(sap_session, "logon)") Then
        ' Limpando as informações de login inválidas e fazendo nova tentativa de login
        CredsSAP_ClearAll
        If try_count < SAP_Login_Try_Max Then
            InitSAP_Login sap_session, try_count + 1
            Exit Function
        End If
    End If
    
    Dim radio_bnt_force As Variant
    Set radio_bnt_force = SessionSAP_FindID(sap_session, "wnd[1]/usr/radMULTI_LOGON_OPT1")
    
    ' Verificando tela múltiplo login foi aberta
    If CheckObject(radio_bnt_force) Then
        ' Verificando método de forçamento de login e executando a tratativa
        If SAP_Login_force_Method = "Exit" Then
            SessionSAP_SendKey sap_session, SAP_KEY_F12
            InitSAP_Login = False
            Exit Function
            
        ElseIf SAP_Login_force_Method = "Force" Then
            radio_bnt_force.Select
            SessionSAP_SendKey sap_session, SAP_KEY_ENTER
            
        ElseIf SAP_Login_force_Method = "Wait" Then
            Dim conn_name As String
            conn_name = sap_session.Parent.Description
            ' Fechando a sessão atual e aguardando o tempo para a nova tentativa
            SessionSAP_SendKey sap_session, SAP_KEY_F12
            WaitSeconds SAP_Login_Wait_Seconds
            
            ' Abrindo uma nova sessão e fazendo a nova tentativa
            Dim new_session As Object
            Set new_session = InitSAP_OpenSession(conn_name)
            If HelperSAP_CheckCollection(new_session) Then
                InitSAP_Login = InitSAP_Login(new_session, try_count)
                Exit Function
            Else
                InitSAP_Login = False
                Exit Function
            End If
        End If
    End If
    
    Dim filed_text_fails As Variant
    Set filed_text_fails = SessionSAP_FindID(sap_session, "wnd[1]/usr/txtMESSTXT1")
    ' Verificando tela número de tentativas falhadas
    If CheckObject(filed_text_fails) Then
        SessionSAP_SendKey sap_session, SAP_KEY_ENTER
    End If
    
    
TryInitSAP_Login:
    InitSAP_Login = HelperSAP_CheckCollection(sap_session) And InitSAP_CheckLoged(sap_session)
End Function

' Obtém uma sessão do SAP de acordo com os parâmetros da biblioteca.
' Param conn_name: Nome da conexão que será usada.
Public Function InitSAP_GetNewSession(conn_name As String) As Object
    Dim Session As Object
    Set Session = InitSAP_GetSessionByNameConn(conn_name)
    
    If Not InitSAP_CheckLoged(Session) Then
        If Not InitSAP_Login(Session) Then
            Exit Function
        End If
    End If
    
    Set InitSAP_GetNewSession = Session
End Function

'========--------========
'      SAP Sessions
'========--------========

' Obtém o nome da transação atual da sessão
Public Function SessionSAP_GetTransaction(Session As Object) As String
    If HelperSAP_CheckCollection(Session) Then
        SessionSAP_GetTransaction = Session.info().Transaction
    End If
End Function

' Abre uma transação na sessão
Public Function SessionSAP_StartTransaction(Session As Object, Transaction As String, Optional CreateSession As Boolean = False) As Object
    If HelperSAP_CheckCollection(Session) Then
        Dim CloseIfFail As Boolean
        CloseIfFail = False
        If CreateSession Then
            Session = SessionSAP_OpenNewSession(Session)
            CloseIfFail = True
        End If
        Session.StartTransaction Transaction
        If SessionSAP_CheckTransaction(Session, Transaction) Then
            Set SessionSAP_StartTransaction = Session
        Else
            If CloseIfFail Then SessionSAP_Close Session
        End If
    End If
End Function

' Valida se a sessão está na transação especificada
Public Function SessionSAP_CheckTransaction(Session As Object, Transaction As String) As Boolean
    SessionSAP_CheckTransaction = SessionSAP_GetTransaction(Session) = Transaction
End Function


' Obtém o nome do programa atual da sessão
Public Function SessionSAP_GetProgram(Session As Object) As String
    If HelperSAP_CheckCollection(Session) Then
        SessionSAP_GetProgram = Session.info().Program
    End If
End Function

' Valida se a sessão está no programa especificado
Public Function SessionSAP_CheckProgram(Session As Object, Program As String) As Boolean
    SessionSAP_CheckProgram = SessionSAP_GetProgram(Session) = Program
End Function


' Executa um comando na sessão
Public Function SessionSAP_ExecuteCmd(Session As Object, Command As String)
    If HelperSAP_CheckCollection(Session) Then
        Session.SendCommand Command
    End If
End Function

' Faz a sessão voltar ao menu principal
Public Function SessionSAP_BackToMenu(Session As Object)
    SessionSAP_ExecuteCmd Session, "/n"
End Function

' Faz a sessão voltar ao menu principal
Public Function SessionSAP_Close(Session As Object)
    SessionSAP_ExecuteCmd Session, "/i"
End Function

' Faz a sessão voltar ao menu principal
Public Function SessionSAP_CloseAll(Session As Object)
    SessionSAP_ExecuteCmd Session, "/nex"
End Function

' Faz a sessão voltar ao menu principal
Public Function SessionSAP_Minimize(Session As Object)
    Session.ActiveWindow.Iconify
End Function

' Verifica se a sessão foi finalizada por inatividade
Public Function SessionSAP_CheckInTimeout(Session As Object)
    If Not HelperSAP_CheckCollection(Session) Then Exit Function
    
    Dim session_count As Integer
    session_count = Session.Parent.sessions.count
    
    Dim new_session As Object
    Set new_session = SessionSAP_OpenNewSession(Session)
    
    If Session.Parent.sessions.count > session_count Then
        SessionSAP_CheckInTimeout = False
        SessionSAP_Close new_session
    Else
        SessionSAP_CheckInTimeout = True
    End If
End Function

' Bloqueia as iterações do usuário no SAP
Public Function SessionSAP_BlockUser(Session As Object)
    If Not HelperSAP_CheckCollection(Session) Then Exit Function
    Session.LockSessionUI
End Function

' Bloqueia as iterações do usuário no SAP
Public Function SessionSAP_UnblockUser(Session As Object)
    If Not HelperSAP_CheckCollection(Session) Then Exit Function
    Session.UnlockSessionUI
End Function

' Faz a busca de um objeto pelo ID com tratamento de erro
Public Function SessionSAP_FindID(Session As Object, id As String, Optional on_error As Boolean = False) As Object
    If Not on_error Then
        On Error Resume Next
    End If
    If HelperSAP_CheckCollection(Session) Then
        Set SessionSAP_FindID = Session.findById(id)
    End If
End Function

' Faz a simulação do pressionamento de uma tecla
Public Function SessionSAP_SendKey(Session As Object, Key As Integer)
    If HelperSAP_CheckCollection(Session) Then
        Session.findById("wnd[" & CStr(Session.Children.count - 1) & "]").sendVKey Key
    End If
End Function


' Ontém a última sessão aberta da conexão
Public Function SessionSAP_GetLast(ByVal sap_conn As Object) As Object
    If Not CheckObject(sap_conn) Then Exit Function

    Dim sessions As Object
    Set sessions = sap_conn.sessions()
    Set SessionSAP_GetLast = sap_conn.Children(CLng(sessions.count() - 1))
End Function

' Abre uma nova janela na conexão da sessão
Public Function SessionSAP_OpenNewSession(ByVal Session As Object) As Object
    If Not HelperSAP_CheckCollection(Session) Then Exit Function
    Session.CreateSession
    WaitSeconds 2
    Set SessionSAP_OpenNewSession = SessionSAP_GetLast(Session.Parent)
    If SAP_Minimize_Windows Then SessionSAP_Minimize SessionSAP_OpenNewSession
End Function


' Obtém a mensagem que aparece no rodapé do SAP
Public Function SessionSAP_GetAlertBarMsg(Session As Object) As String
    SessionSAP_GetAlertBarMsg = SessionSAP_FindID(Session, ID_ALERTS_BAR).Text
End Function

' Verifica se alguma palavra apareceu na mensagem do rodapé do SAP
Public Function SessionSAP_InAlertBarMsg(Session As Object, search_str As String) As Boolean
    Dim AlertMsg As String
    AlertMsg = SessionSAP_GetAlertBarMsg(Session)
    SessionSAP_InAlertBarMsg = CheckString(AlertMsg) And InStr(AlertMsg, search_str) > 0
End Function