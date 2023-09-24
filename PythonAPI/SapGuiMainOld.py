

import os
import configparser
import re
import pymsgbox
import win32com.client
import time
from SapTCodes import *

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

class SapHelper():
    ''' Classe com funções básicas de ajudar
    '''
    
    @staticmethod
    def CheckStrings(*strings) -> bool:
        ''' Verificar se todos os parâmetros são strings e não estão vazias
        Parameters
        ----------
        *strings : str
            Strings para serem válidadas.
        '''
        for string in strings:
            if string is None or type(string) != str or string == '' or len(string) < 1:
                return False
        return True

    @staticmethod
    def PrintError(modulo: str, msg: str, on_adm: bool = True):
        ''' Imprime uma mensagem no formato de erro

        Parameters
        ----------
        modulo : str
            Módulo do erro.
        msg : str
            Mensagem do erro.
        on_adm : bool, optional
            Se deseja exibir uma mensagem para contatar o administrador do sistema.
        '''
        print((('Módulo: ' + modulo + ' -> ') if SapHelper.CheckStrings(modulo) else '') + \
                'ERRO: ' + msg + ' !!!' + \
                (' -> Contate o responsável pelo sistema!' if on_adm else ''))
    
    @staticmethod
    def PrintWaring(modulo: str, msg: str, on_adm: bool = True):
        ''' Imprime uma mensagem no formato de aviso

        Parameters
        ----------
        modulo : str
            Módulo do aviso.
        msg : str
            Mensagem do aviso.
        on_adm : bool, optional
            Se deseja exibir uma mensagem para contatar o administrador do sistema.
        '''
        print((('Módulo: ' + modulo + ' -> ') if SapHelper.CheckStrings(modulo) else '') + \
                'Atenção: ' + msg + ' !!!' + \
                (' -> Contate o responsável pelo sistema!' if on_adm else ''))

class InputBox():
    @staticmethod
    def Text(title: str, prompt: str, default_value: str = '') -> str:
        return pymsgbox.prompt(prompt, title, default_value)
    
    @staticmethod
    def Password(title: str, prompt: str) -> str:
        return pymsgbox.password(prompt, title)

class SapColletion(object):
    ''' Classe com funções de ajuda para objeto de listas do SAP

    Attributes
    ----------
    collection : object
        Objeto de lista do SAP
    '''

    def __init__(self, collection: object):
        '''
        Parameters
        ----------
        collection : object
            Objeto de lista do SAP
        '''
        if collection is None:
            Exception('Collection Object is None')
        self.collection = collection

    def __getattr__(self, n):
        return getattr(self.collection, n)

    def __setattr__(self, attr, n):
        if attr in self.__dict__ or attr == 'collection':
            super().__setattr__(attr, n)
        else:
            setattr(self.collection, attr, n)
    
    def CountItens(self) -> int:
        ''' Retorna a quantidade de itens da lista
        '''
        try: return self.collection.Children.Count
        except: return 0
    
    def GetAllItens(self) -> [object]:
        ''' Retorna uma array com todos os itens da lista
        '''
        try:
            itens = []
            for index in range(0, self.collection.Children.Count):
                itens.append(self.collection.Children(index))
            return itens
        except: return []

    def GetTypeDescription(self) -> str:
        ''' Retorna a descrição do tipo de itens da lista
        '''
        return self.collection.Type

    def GetTypeNumber(self) -> int:
        ''' Retorna o número do tipo de itens da lista
        '''
        return self.collection.TypeAsNumber
    
    def GetLastItem(self) -> object:
        ''' Retorna o último item da lista
        '''
        try: return self.collection.Children(self.CountItens()-1)
        except: return None



class SapInit():
    ''' Classe para fazer a inicialização do SAP
    
    Faz toda a inicialização do SAP, abrindo o programa, obter o app e conexões ativas.

    Attributes
    ----------
    file_path : str
        Caminho do arquivo para armazenar credenciais.
    credentials : array
        Cache das credenciais lidas.
    '''
    
    def __init__(self, sap_logon_path: str = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe', \
                        auto_start: bool = True):
        '''
        Parameters
        ----------
        sap_logon_path : str, optional
            Caminho do arquivo do executavel do SAP Logon.
        auto_start : bool, optional
            Habilita a auto-inicialização do SAP caso não estiver aberto ao usar as funções dessa classe.
        '''
        self.sap_logon_path = sap_logon_path
        self.auto_start = auto_start
    
    def CheckRunning(self) -> bool:
        ''' Verifica se o SAP Logon está sendo executado
        '''
        try:
            SapObj = win32com.client.GetObject("SAPGUI")
            return type(SapObj) == win32com.client.CDispatch
        except: pass
            # SapHelper.PrintError('SAP Init', 'Erro ao verificar se o SAP está aberto')
        return False
    
    def StartProcess(self, step_check: int = 5, wait_seconds: int = 30) -> bool:
        ''' Inicia o SAP Logon

        Abre o executavel do SAP Logon de acordo com o argumento sap_logon_path,
        caso já esteja aberto a função não é executada.

        Parameters
        ----------
        step_check : int, optional
            Interval de tempo entre as verificações de abertura do SAP Logon
        wait_seconds : int, optional
            Tempo máximo de espera para o SAP Logon abrir.
        '''
        try:
            if self.CheckRunning(): return True
            
            os.startfile(self.sap_logon_path)
            while wait_seconds > 0:
                wait_seconds -= step_check
                time.sleep(step_check)
                if self.CheckRunning(): return True
                
            return self.CheckRunning()
        
        except:
            SapHelper.PrintError('SAP Init', 'Erro ao iniciar o programa do SAP')
        return False
    
    def KillProcess(self) -> None:
        os.system('taskkill -f -im saplogon.exe')
    
    def GetSapGui(self) -> object:
        ''' Obtém o objeto do SAP Gui

        Caso o SAP Logon não estiver aberto e o argumento auto_start for True,
        a função iniciará o SAP Logon.
        '''
        try:
            if self.auto_start and not self.CheckRunning():
                self.StartProcess()
            return win32com.client.GetObject("SAPGUI")
        except:
            SapHelper.PrintError('SAP Init', 'Erro ao obter o objeto do SAP Gui')
        return None

    def GetSapApp(self, sap_gui: object = None) -> object:
        ''' Obtém o objeto da aplicação do SAP Logon

        Caso o SAP Logon não estiver aberto e o argumento auto_start for True,
        a função iniciará o SAP Logon.

        Parameters
        ----------
        sap_gui : object, optional
            O objeto do SAP Gui para obter a aplicação do SAP Logon.
        '''
        try:
            if sap_gui is None: sap_gui = self.GetSapGui()
            return sap_gui.GetScriptingEngine
        except:
            SapHelper.PrintError('SAP Init', 'Erro ao obter a aplicação do SAP')
        return None

    def OpenConnection(self, conn_name: str, sap_app: object = None) -> 'SapConnection':
        ''' Abre uma conexão do SAP

        Caso o SAP Logon não estiver aberto e o argumento auto_start for True,
        a função iniciará o SAP Logon.

        Parameters
        ----------
        conn_name : str
            Nome da conexão SAP para ser aberta.
        sap_app : object, optional
            Aplicação do SAP para poder abrir a conexão.
        '''
        try:
            if sap_app is None: sap_app = self.GetSapApp()
            return SapConnection(sap_app.OpenConnection(conn_name, True))
        except:
            SapHelper.PrintError('SAP Init', 'Erro ao abrir uma nova conexão do SAP')
        return None

    def GetConnections(self, conn_name: str, sap_app: object = None) -> ['SapConnection']:
        ''' Procura uma conexão SAP pelo nome da conexão passada no parâmetro.

        * Caso o SAP Logon não estiver aberto e o argumento auto_start for True,
        a função iniciará o SAP Logon

        Parameters
        ----------
        conn_name : str
            Nome da conexão SAP para ser aberta.
        sap_app : object, optional
            Aplicação do SAP para poder procurar as conexões.
        '''
        try:
            if sap_app is None: sap_app = self.GetSapApp()
            connections = SapColletion(sap_app)
            connections = list(filter(lambda conn: conn.Description == conn_name, connections.GetAllItens()))
            return list(map(lambda conn: SapConnection(conn), connections))
                
        except:
          SapHelper.PrintError('SAP Init', 'Erro ao obter conexões do SAP')
        return None

    def GetSessionInMenuLogin(self, conn_name: str, sap_app: object = None) -> 'SapSession':
        ''' Procura uma conexão SAP que tenha uma sessão aberta no menu princiapal ou na tela login.

        * Caso o SAP Logon não estiver aberto e o argumento auto_start for True,
        a função iniciará o SAP Logon
        * Se não for encontrada nenhuma conexão aberta e o argumento auto_start for True,
        a função irá abrir uma conexão.
        * Se tiver conexão aberta e não encontrar nenhuma sessão no menu principal
        e o argumento auto_start for True a função irá abrir uma nova sessão na primeira 
        conexão aberta encontrada ou uma que esteja na tela de login.

        Parameters
        ----------
        conn_name : str
            Nome da conexão SAP para ser aberta.
        sap_app : object, optional
            Aplicação do SAP para poder procurar as conexões.
        '''
        try:
            connections = self.GetConnections(conn_name, sap_app)
            
            sessions = list(map(lambda conn: conn.GetSessionsInMenu(), connections))
            sessions = list(filter(lambda conns: len(conns) > 0, sessions))
            if len(sessions) > 0: return sessions[0][0]
            
            sessions = list(map(lambda conn: conn.GetSessionsInLogin(), connections))
            sessions = list(filter(lambda conns: len(conns) > 0, sessions))
            if len(sessions) > 0: return sessions[0][0]
            
            if self.auto_start:
                if len(connections) > 0:
                    return connections[0].OpenNewSession()
                else:
                    return self.OpenConnection(conn_name, sap_app).GetLastSession()
            
            return None
            
        except:
          SapHelper.PrintError('SAP Init', 'Erro ao obter sessão SAP no menu princiapal')
        return None

class SapConnection(object):
    ''' Classe com funções de ajuda para objetos de conexão SAP

    Attributes
    ----------
    connection : object
        Objeto da conexão SAP
    '''
    
    def __init__(self, connection: object):
        '''
        Parameters
        ----------
        connection : object
            Objeto da conexão SAP
        '''
        if connection is None:
            Exception('Connection Object is None')
        self.connection = SapColletion(connection)

    def __getattr__(self, n):
        return getattr(self.connection, n)

    def __setattr__(self, attr, n):
        if attr in self.__dict__ or attr == 'connection':
            super().__setattr__(attr, n)
        else:
            setattr(self.connection, attr, n)
    
    def GetName(self) -> str:
        ''' Obtém o nome da conexão
        '''
        return self.Description
    
    def GetAllSessions(self) -> ['SapSession']:
        ''' Obtém todas sessões abertas da conexão
        '''
        return list(map(lambda session: SapSession(session), self.connection.GetAllItens()))
    
    def GetSessionsInMenu(self) -> ['SapSession']:
        ''' Obtém todas sessões abertas no menu principal
        '''
        return list(filter(lambda session: session.info.CheckTransaction(SapTransactions.MAIN_MENU), self.GetAllSessions()))
    
    def GetSessionsInLogin(self) -> ['SapSession']:
        ''' Obtém todas sessões abertas no menu principal
        '''
        return list(filter(lambda session: session.info.CheckTransaction(SapTransactions.LOGIN), self.GetAllSessions()))
    
    def GetSessionsUser(self, user_name: str) -> ['SapSession']:
        ''' Obtém todas sessões abertas do usuário especificado no parâmetro
        '''
        return list(filter(lambda session: session.info.User() == user_name, self.GetAllSessions()))
    
    def GetLastSession(self) -> 'SapSession':
        ''' Obtém a última sessão aberta
        '''
        try:
            return SapSession(self.connection.GetLastItem())
        except:
            SapHelper.PrintError('Sap Connection', 'Não foi possivel obter a última sessão aberta')
        return None
    
    def OpenNewSession(self) -> 'SapSession':
        ''' Abre uma nova sessão na conexão
        '''
        return self.GetLastSession().OpenNewSession()

class SapSessionInfos(object):
    ''' Classe com funções dos atributos de informações da sessões

    Attributes
    ----------
    info : object
        informações da sessão SAP
    '''

    def __init__(self, info: object):
        if info is None:
            Exception('Session infos Object is None')
        self.info = info

    def __getattr__(self, n):
        return getattr(self.connection, n)

    def __setattr__(self, attr, n):
        if attr in self.__dict__ or attr == 'info':
            super().__setattr__(attr, n)
        else:
            setattr(self.connection, attr, n)
    
    def AppServer(self) -> str: return self.info.ApplicationServer
    def Client(self) -> str: return self.info.Client
    def Codepage(self) -> int: return self.info.Codepage
    def Flushes(self) -> int: return self.info.Flushes
    def Group(self) -> str: return self.info.Group
    def GuiCodepage(self) -> int: return self.info.GuiCodepage
    def I18NMode(self) -> bool: return self.info.I18NMode
    def InterpretationTime(self) -> int: return self.info.InterpretationTime
    def IsLowSpeedConnection(self) -> bool: return self.info.IsLowSpeedConnection
    def Language(self) -> str: return self.info.Language
    def MessageServer(self) -> str: return self.info.MessageServer
    def Program(self) -> str: return self.info.Program
    def ResponseTime(self) -> int: return self.info.ResponseTime
    def RoundTrips(self) -> int: return self.info.RoundTrips
    def ScreenNumber(self) -> int: return self.info.ScreenNumber
    def IsScriptModeReadOnly(self) -> bool: return self.info.ScriptingModeReadOnly
    def ScriptModeRecDisabled(self) -> bool: return self.info.ScriptingModeRecordingDisabled
    def SessionNumber(self) -> int: return self.info.SessionNumber
    def SystemName(self) -> str: return self.info.SystemName
    def SystemNumber(self) -> int: return self.info.SystemNumber
    def SystemSessionId(self) -> str: return self.info.SystemSessionId
    def Transaction(self) -> str: return self.info.Transaction
    def User(self) -> str: return self.info.User
    
    def CheckTransaction(self, transaction: str):
        return self.Transaction() == transaction
    
    def CheckProgram(self, program: str):
        return self.Program() == program
    
    def HasUser(self) -> bool:
        return SapHelper.CheckStrings(self.User())

class SapSession(object):
    ''' Classe com funções de ajuda para sessões do SAP

    Attributes
    ----------
    session : object
        Objeto da sessão SAP
    info : SapSessionInfos
        Informações da sessão
    auto_minimize : bool
        Auto minimiza as novas sessões abertas
    '''
    
    auto_minimize = True
    
    def __init__(self, session: object):
        if session is None:
            Exception('Session Object is None')
        self.session = SapColletion(session)
        self.info = SapSessionInfos(session.info)
        
        if SapSession.auto_minimize:
            self.Minimize()

    def __getattr__(self, n):
        return getattr(self.session, n)

    def __setattr__(self, attr, n):
        if attr in self.__dict__ or attr == 'session' or attr == 'info':
            super().__setattr__(attr, n)
        else:
            setattr(self.session, attr, n)
    
    def GetConnection(self) -> 'SapConnection':
        ''' Obtém conexão da sessão atual
        '''
        return SapConnection(self.Parent)
    
    def OpenNewSession(self) -> 'SapSession':
        ''' Abre uma nova sessão
        '''
        try:
            self.session.CreateSession()
            time.sleep(2)
            return self.GetConnection().GetLastSession()
        except:
            SapHelper.PrintError('Sap Session', 'Erro ao criar uma nova sessão do SAP')
        return None
    
    def findById(self, id: str, show_warning: bool = True) -> object:
        ''' Obtém um objeto pelo ID

        Parameters
        ----------
        id : str
            ID do objeto
        '''
        try: return self.session.findById(id)
        except:
            if show_warning: SapHelper.PrintWaring('Sap Session', f'Id ({id}) não encontrado na sessão')
        return None

    def GetAlertBarMsg(self) -> str:
        ''' Obtém a mensagem de aviso na barra inferior da SAP
        '''
        try: return self.findById(SapFields.ALERTS_BAR).Text
        except: SapHelper.PrintError('Sap Session', 'Erro ao obter mensagem de alerta da barra inferior')
        return None
    
    def InAlertBarMsg(self, search: str) -> bool:
        ''' Verifica se a string passada pelo parâmetro tem na mensagem de aviso do SAP

        Parameters
        ----------
        search : str
            string a ser procurada na mensagem de aviso.
        '''
        try: return self.GetAlertBarMsg().index(search) >= 0
        except: return False

    def SendKey(self, key: int) -> None:
        ''' Envia o pressionamento de uma tecla na sessão

        Parameters
        ----------
        key : int
            Tecla a ser enviada
        '''
        try: self.findById(f'wnd[{str(self.session.CountItens()-1)}]').sendVKey(key)
        except: SapHelper.PrintError('Sap Session', 'Erro enviar uma tecla para o SAP')
    
    def OpenTransaction(self, transaction: str) -> bool:
        ''' Inicia uma transação na sessão

        Parameters
        ----------
        transaction : str
            Transação para ser iniciada
        '''
        try:
            self.StartTransaction(transaction)
            return self.info.CheckTransaction(transaction)
        except: SapHelper.PrintError('Sap Session', 'Erro ao iniciar uma transação no SAP')
        return None
    
    def ExecuteCommand(self, command: str):
        ''' Envia um comando para a sessão

        Parameters
        ----------
        command : str
            Comando para ser enviado
        '''
        try: self.session.SendCommand(command)
        except: SapHelper.PrintError('Sap Session', f'Erro ao executar o comando {command} no SAP')

    def CloseSession(self):
        ''' Fecha a sessão atual
        '''
        self.ExecuteCommand('/i')
        try:
            popup_text = self.findById(SapFields.POPUP_LOGOFF_QUESTION).Text
            if 'logoff' in popup_text or 'log off' in popup_text:
                self.findById(SapFields.POPUP_LOGOFF_BNT_YES).Press()
        except: pass
        
    def BackToMenu(self) -> bool:
        ''' Volta ao menu principal
        '''
        if not self.info.CheckTransaction(SapTransactions.MAIN_MENU):
            self.OpenTransaction('/n')
        return self.info.CheckTransaction(SapTransactions.MAIN_MENU)

    def LockUser(self):
        ''' Bloqueia as interações do usuário na sessão atual
        '''
        try: self.LockSessionUI()
        except: SapHelper.PrintWaring('Sap Session', 'Erro ao bloquear o SAP para o usuário')

    def UnlockUser(self):
        ''' Desbloqueia as interações do usuário na sessão atual
        '''
        try: self.UnlockSessionUI()
        except: SapHelper.PrintWaring('Sap Session', 'Erro ao desbloquear o SAP para o usuário')
    
    def Minimize(self):
        ''' Minimiza a janela da sessão
        '''
        try: self.ActiveWindow.Iconify
        except: SapHelper.PrintWaring('Sap Session', f'Erro ao minimizar a janela do SAP')
    
    def Maximize(self):
        ''' Maximiza a janela da sessão
        '''
        try: self.ActiveWindow.Maximize
        except: SapHelper.PrintWaring('Sap Session', f'Erro ao maximizar a janela do SAP')
    
    def FocusWindows(self):
        ''' Faz o windows focar na janela da sessão
        '''
        self.Minimize()
        self.Maximize()
    
    def ResizeWindows(self, width: int, height: int):
        ''' Altera o tamanho da janela do SAP
        '''
        self.findById('wnd[0]').ResizeWorkingPane(width, height, False)
    
    def CheckInTimeout(self) -> bool:
        ''' Verifica se a sessão está em timeout, não funciona em sessão na tela de login
        '''
        try:
            ses_count = self.session.CountItens()
            new_session = self.OpenNewSession()
            if self.session.CountItens() > ses_count:
                new_session.CloseSession()
                return False
            return True
        except:
            SapHelper.PrintError('Sap Session', 'Erro ao verificar o timeout no SAP')
        return None

class SapGui():
    ''' Classe principal para gerenciamento dos objetos do SAP
    
    Parameters
    ----------
    credentials : 'SapCredentials'
        Instancia de gerencimento de credenciais
    sap_logon : 'SapInit'
        Instancia para inicialização e obtenção de objetos do SAP
    login_storage_method : str
        O tipo de armazenamento de login, sendo:
        * 'FileTemp' para armazenar em arquivo
        * 'InputBox' pede as credenciais por meio de inputbox e armazena apenas no cahe
        * 'Wait' Espera o usuário logar e continua o script
    login_force_method : str
        A tratativa para quando ao fazer login o usuário já estiver logado, sendo:
        * 'Force' para derrubar o usuário
        * 'Exit' finaliza o script
        * 'Wait' Espera o usuário deslogar da outra máquina
    login_wait_seconds : int
        O intervalo de tempo em segundos entre as checagens de liberação do login
        para o caso do login_force_method ser 'Wait'
    conns_names : SapConnNames
        Enum com os nome de conexões SAP
    transactions : SapTransactions
        Enum com a lista de transações do SAP
    programs : SapPrograms
        Enum com a lista de programas do SAP
    fields : SapFields
        Enum com a lista de ids de campos do SAP
    keys : SapKeys
        Enum com a lista de teclas para o SAP
    '''
    
    conns_names = SapConnNames()
    transactions = SapTransactions()
    programs = SapPrograms()
    fields = SapFields()
    keys = SapKeys()

    def __init__(self, auto_start: bool = True, login_storage_method: str = 'FileTemp', \
                    login_force_method = 'Force', login_wait_seconds = 10, \
                    sap_logon_path: str = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'):
        '''
        Parameters
        ----------
        auto_start : bool, optional
            Se deseja iniciar automaticamente o SAP caso esteja fechado
        login_storage_method : str, optional
            O tipo de armazenamento de login, sendo:
            * 'FileTemp' para armazenar em arquivo
            * 'InputBox' pede as credenciais por meio de inputbox e armazena apenas no cahe
            * 'Wait' Espera o usuário logar e continua o script
        login_force_method : str, optional
            A tratativa para quando ao fazer login o usuário já estiver logado, sendo:
            * 'Force' para derrubar o usuário
            * 'Exit' finaliza o script
            * 'Wait' Espera o usuário deslogar da outra máquina
        login_wait_seconds : int, optional
            O intervalo de tempo em segundos entre as checagens de liberação do login
            para o caso do login_force_method ser 'Wait'
        login_storage_method : str, optional
            O tipo de armazenamento de login, sendo:
            * 'FileTemp' para armazenar em arquivo
            * 'InputBox' pede as credenciais por meio de inputbox e armazena apenas no cahe
            * 'Wait' Espera o usuário logar e continua o script
        sap_logon_path : str, optional
            Caminho do arquivo do executavel do SAP Logon.
        '''
        
        if login_storage_method == 'Wait': self.credentials = None
        elif login_storage_method == 'InputBox': self.credentials = SapCredentials(None)
        else: self.credentials = SapCredentials()
        
        self.sap_logon = SapInit(auto_start=auto_start, sap_logon_path=sap_logon_path)
        self.login_force_method = login_force_method
        self.login_wait_seconds = login_wait_seconds
    
    def GetSessionLoged(self, conn_name: str) -> 'SapSession':
        ''' Obtém uma sessão logada
        
        Obtém uma sessão no menu principal, podendo ser uma que já esteja aberta,
        caso não tenha nenhuma aberta e o parâmetro auto_start do SapInit for True
        ele abrirá uma nova sessão.
        
        Parameters
        ----------
        conn_name : str
            Nome da conexão do SAP
        '''
        session = self.sap_logon.GetSessionInMenuLogin(conn_name)
        self.LoginSignIn(session)
        return session
    
    def LoginSignIn(self, session: 'SapSession', try_max: int = 3) -> 'SapSession':
        ''' Realiza o login no SAP
        
        Parameters
        ----------
        session : SapSession
            Sessão na tela de login
        try_max : int
            Máxima de tentativas falhas de login com credenciais inválidas
        '''
        try:
            if not session.info.CheckTransaction(SapTransactions.LOGIN):
                return session
            
            if self.credentials is None:
                session.FocusWindows()
                while session.info.CheckTransaction(SapTransactions.LOGIN):
                    time.sleep(1)
                if SapSession.auto_minimize:
                    session.Minimize()
                return session

            user_name, password = self.credentials.GetCredentials(session.GetConnection().GetName())
            if not SapHelper.CheckStrings(user_name, password): return False
            
            session.findById(SapFields.LOGIN_MANDT).Text = '300'
            session.findById(SapFields.LOGIN_USERNAME).Text = user_name
            session.findById(SapFields.LOGIN_PASSWORD).Text = password
            session.SendKey(SapKeys.ENTER)
            
            if session.InAlertBarMsg('logon)'):
                if try_max > 0:
                    return self.LoginSignIn(session, try_max - 1)
                return None
            
            force_sign_bnt = session.findById(SapFields.POPUP_MULTI_LOGIN_RAD_FORCE, False)
            
            if force_sign_bnt is not None:
                if self.login_force_method == 'Exit':
                    session.SendKey(SapKeys.F12)
                    return None
                
                if self.login_force_method == 'Force':
                    force_sign_bnt.Select
                    session.SendKey(SapKeys.ENTER)
                    
                if self.login_force_method == 'Wait':
                    conn_name = session.GetConnection().GetName()
                    session.SendKey(SapKeys.F12)
                    time.sleep(self.login_wait_seconds)
                    
                    new_session = self.sap_logon.OpenConnection(conn_name)
                    return self.LoginSignIn(new_session, try_max)
            
            field_count_fails = session.findById(SapFields.POP_UP_COUNT_FAILS_LABEL_LINE_1, False)
            if field_count_fails is not None: session.SendKey(SapKeys.ENTER)
            
            copy_r = session.findById('wnd[1]')
            if copy_r is not None and copy_r.Text == 'Copyright':
                session.SendKey(SapKeys.ENTER)
            
            session.BackToMenu()
            
            return session
            
        except: SapHelper.PrintError('Sap Session', 'Erro ao fazer login no SAP')
        return False