from __future__ import annotations
from SapGuiApiWrapper import *
from SapTCodes import *

import os
import re
import time
import pymsgbox
import pywinauto
import configparser

class SavvyHelper():
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
    def InputBoxText(title: str, prompt: str, default_value: str = '') -> str:
        return pymsgbox.prompt(prompt, title, default_value)
    
    @staticmethod
    def InputBoxPassword(title: str, prompt: str) -> str:
        return pymsgbox.password(prompt, title)
    
    @staticmethod
    def InputBoxYesNo(title: str, prompt: str, buttons: list[str] = ['Sim', 'Não']) -> str:
        return pymsgbox.confirm(prompt, title, buttons=buttons) == buttons[0]

class SavvyLogger():
    ''' Classe para registro de execução da API
    '''
    # TODO Fazer um arquivo de registro.
    
    def Error(module: str, msg: str):
        print((('X► Módulo: ' + module + ' -> ') if SavvyHelper.CheckStrings(module) else '') + \
                'ERRO: ' + msg + ' !!!')
    
    def Warning(module: str, msg: str):
        print((('○ Módulo: ' + module + ' -> ') if SavvyHelper.CheckStrings(module) else '') + \
                'Atenção: ' + msg + ' !!!')
    
    def Debug(module: str, msg: str):
        print((('» Módulo: ' + module + ' -> ') if SavvyHelper.CheckStrings(module) else '') + \
                'Debug: ' + msg + ' !!!')

class SavvyCredentials():
    ''' Classe para gerenciamentos de credenciais do SAP
    
    Faz o armazenamento de credenciais do SAP em variavel e arquivo,
    tirando a necessidade do usúario ficar realizando login sempre que abrir
    uma nova conexão.

    Attributes
    ----------
    file_path : str
        Caminho do arquivo para armazenar credenciais.
    credentials : array
        Cache das credenciais lidas.
    '''
    
    def __init__(self, file_path = os.path.expanduser('~\\sapusercredentials.creds')):
        '''
        Parameters
        ----------
        file_path : str, optional
            Caminho do arquivo para armazenar credenciais,
            para desabilitar o armazenamento em arquivo passa esse parâmetro como None
        '''
        
        self.file_path = file_path
        self.credentials = {}
        self.ReadAllInFile()
    
    def GetCredentials(self, conn_name: str = 'Default', force_read: bool = False) -> (str, str):
        ''' Obtém a crendencial SAP do usuário

        Faz a leitura das credenciais e faz o tratamento caso não tenha credenciais armazenadas,
        se não tiver credenciais no cache e nem nos arquivos ele pede para o usuário fornecer e
        armazena as credenciais tanto no cache quanto no arquivo.

        Parameters
        ----------
        conn_name : str, optional
            Nome da conexão das credenciais.
        force_read : bool, optional
            Força a leitura das credenciais mesmo que ela já esteja em cache.
        '''
        
        if not force_read and conn_name in self.credentials:
            return (self.credentials[conn_name][0], self.credentials[conn_name][1])
        
        if self.file_path is not None:
            if self.ReadInFile(conn_name) or \
                (self.ReadInputBox(conn_name) and self.WriteInFile(conn_name)):
                return (self.credentials[conn_name][0], self.credentials[conn_name][1])

        else:
            if self.ReadInputBox(conn_name):
                return (self.credentials[conn_name][0], self.credentials[conn_name][1])

        return (None, None)


    def ClearAll(self) -> bool:
        ''' Limpa todos as credenciais tanto do cache quanto do arquivo
        '''
        try:
            self.credentials = {}
            os.remove(self.file_path)
            return True
        except:
            SavvyLogger.Error('Savvy Creds', 'Erro ao limpar todas as credenciais.')
        return False
    
    def ClearCredentials(self, conn_name: str = 'Default') -> bool:
        ''' Limpar as credenciais da conexão especificada

        Parameters
        ----------
        conn_name : str, optional
            Nome da conexão das credenciais.
        '''
        try:
            if conn_name in self.credentials: self.credentials.pop(conn_name)
            
            parse = configparser.ConfigParser()
            parse.read(self.file_path)
            conn_session = SavvyCredentials.__ConnNameToSession(conn_name)
            
            if parse.has_section(conn_session):
                parse.remove_section(conn_session)
                with open(self.file_path, 'w') as configfile:
                    parse.write(configfile)
                return True
            
        except:
            SavvyLogger.Error('Savvy Creds', f'Erro ao limpar as credenciais da conexão: {conn_name}')
        return False
    
    def ReadInputBox(self, conn_name: str = 'Default') -> bool:
        ''' Pede para o usuário fornecer as credenciais do SAP por meio de InputBox
        
        Essa função armazena a credencial fornecida pelo usuário apenas no cache,
        para armazenar no arquivo use a função WriteInFile.

        Parameters
        ----------
        conn_name : str, optional
            Nome da conexão das credenciais.
        '''
        try:
            desc_conn_user = 'Digite seu nome de usuário' + (':\t' if conn_name == 'Default' else ' da conexão:\n' + conn_name)
            desc_conn_pass = 'Digite sua senha' + (':\t\t' if conn_name == 'Default' else ' da conexão:\t\n' + conn_name)
            
            user_name = SavvyHelper.InputBoxText('Login SAP', desc_conn_user)
            password = SavvyHelper.InputBoxPassword('Login SAP', desc_conn_pass)
            
            if SavvyHelper.CheckStrings(user_name, password):
                self.credentials[conn_name] = [user_name, password]
                return True
            else:
                if SavvyHelper.InputBoxYesNo('Credenciais inválidas', 'As credenciais que você inseriu não são válidas\r\nDeseja inserir novamente?'):
                    return self.ReadInputBox(conn_name)
            
        except:
            SavvyLogger.Error('Savvy Creds', 'Erro ao ler as credenciais por meio de Inputbox')
        return False

    @staticmethod
    def __ConnNameToSession(conn_name: str = 'Default') -> str:
        ''' Faz o tratamento do nome da conexão para usar em sessões de arquivo de configurações
        
        Parameters
        ----------
        conn_name : str, optional
            Nome da conexão das credenciais.
        '''
        return re.sub('[^a-z|^A-Z]', '', conn_name).upper()
        
    def WriteInFile(self, conn_name: str = 'Default') -> bool:
        ''' Armazena as credenciais da conexão no cache no arquivo de credenciais

        Parameters
        ----------
        conn_name : str, optional
            Nome da conexão das credenciais.
        '''
        if self.file_path is None: return False
        
        parse = None
        try:
            parse = configparser.ConfigParser()
            parse.read(self.file_path)
        except:
            SavvyLogger.Error('Savvy Creds', 'Não foi possivel fazer a leitura do arquivo de credenciais')
            return False
        
        conn_session = SavvyCredentials.__ConnNameToSession(conn_name)
        
        user_name = self.credentials[conn_name][0]
        password = self.credentials[conn_name][1]
        
        if(SavvyHelper.CheckStrings(user_name, password)):
            try:
                if not parse.has_section(conn_session): parse.add_section(conn_session)
                parse.set(conn_session, 'username', user_name)
                parse.set(conn_session, 'password', password)
                parse.set(conn_session, 'connection', conn_name)
                with open(self.file_path, 'w') as configfile:
                    parse.write(configfile)
                return True
            except:
                SavvyLogger.Error('Savvy Creds', 'Não foi possivel gravar as credenciais no arquivo')
        
        return False
    
    def WriteAllInFile(self) -> bool:
        ''' Armazena todas as credenciais do cache no arquivo de credenciais
        '''
        if self.file_path is None: return False
        result = True
        for conn_name in self.credentials.keys():
            result = self.WriteInFile(conn_name) and result
        return result
    
    def ReadInFile(self, conn_name: str = 'Default') -> bool:
        ''' Faz a leitura das credenciais no arquivo e armazena no cache

        Parameters
        ----------
        conn_name : str, optional
            Nome da conexão das credenciais.
        '''
        if self.file_path is None: return False
        
        parse = None
        try:
            parse = configparser.ConfigParser()
            parse.read(self.file_path)
        except:
            SavvyLogger.Error('Savvy Creds', 'Não foi possivel fazer a leitura do arquivo de credenciais')
            return False
        
        conn_session = SavvyCredentials.__ConnNameToSession(conn_name)
        
        if not parse.has_section(conn_session): return False
        
        user_name = parse[conn_session]['username']
        password = parse[conn_session]['password']
        
        if(SavvyHelper.CheckStrings(user_name, password)):
            self.credentials[conn_name] = [user_name, password]
            return True

    def ReadAllInFile(self) -> bool:
        ''' Faz a leitura de todas as credenciais no arquivo e armazena no cache
        '''
        
        parse = None
        try:
            parse = configparser.ConfigParser()
            parse.read(self.file_path)
        except:
            SavvyLogger.Error('Savvy Creds', 'Não foi possivel fazer a leitura do arquivo de credenciais')
            return False
            
        for conn_session in parse.sections():
            user_name = parse[conn_session]['username']
            password = parse[conn_session]['password']
            conn_name = parse[conn_session]['connection']
            
            if SavvyHelper.CheckStrings(user_name, password, conn_name):
                self.credentials[conn_name] = [user_name, password]
        
        return True

class SapInit():
    ''' Classe para inicialização do SAP, vai desde iniciar o programa até fazer login
    '''
    
    def __init__(self, login_storage_method: str = 'FileTemp', \
                    login_force_method = 'Force', login_wait_seconds = 10, \
                    login_mandt = '300', login_language = 'PT', \
                    login_file_storage = os.path.expanduser('~\\sapusercredentials.creds'), \
                    sap_logon_path: str = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe') -> None:
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
        elif login_storage_method == 'InputBox': self.credentials = SavvyCredentials(file_path=None)
        else: self.credentials = SavvyCredentials(file_path=login_file_storage)
        
        self.login_force_method = login_force_method
        self.login_wait_seconds = login_wait_seconds
        self.login_mandt = login_mandt
        self.login_language = login_language
        self.sap_logon_path = sap_logon_path
        
        self.regex_timeout_tile = 'SAP GUI for Windows .*'
    
    def __filter_buttons_no(self, element):
        return element.element_info.class_name == 'Button' \
            and element.element_info.control_type == 'Button' \
            and (element.element_info.rich_text == 'Não' \
                    or element.element_info.rich_text == 'No')
            
    def __filter_windows_titles(self, window):
        return 'SAP GUI for Windows' in window.element_info.rich_text
    
    def CloseAllTimeOutPopups(self):
        try:
            popup_app = pywinauto.Application(backend='uia').connect(title_re='SAP GUI for Windows .*', found_index=0)
            windows_search = list(filter(self.__filter_windows_titles, popup_app.windows()))

            for popup_window in windows_search:
                elements = list(filter(self.__filter_buttons_no, popup_window.children()))
                for element in elements:
                    element.click()
        except: pass
    
    
    def SapRunning(self) -> bool:
        ''' Verifica se o SAP Logon está sendo executado
        '''
        try:
            SapObj = SapGuiAuto.GetSapGuiObject()
            return type(SapObj) == win32com.client.CDispatch
        except: pass
        return False
    
    def StartProcess(self, step_check: int = 5, wait_seconds: int = 30) -> bool:
        ''' Inicia o SAP Logon

        Abre o executável do SAP Logon de acordo com o argumento sap_logon_path,
        caso já esteja aberto a função não é executada.

        Parameters
        ----------
        step_check : int, optional
            Interval de tempo entre as verificações de abertura do SAP Logon
        wait_seconds : int, optional
            Tempo máximo de espera para o SAP Logon abrir.
        '''
        
        if self.SapRunning(): return True
            
        try:
            os.startfile(self.sap_logon_path)
        except:
            SavvyLogger.Error('SAP Init', 'Erro ao iniciar o programa do SAP')
            return False
    
        while wait_seconds > 0:
            wait_seconds -= step_check
            time.sleep(step_check)
            if self.SapRunning(): return True
            
        return self.SapRunning()
        
    
    def KillProcess(self) -> None:
        ''' Força a finalização do SAP. '''
        os.system('taskkill -f -im saplogon.exe')
        
    def LoginAfterSignIn(self, session: SapGuiSession) -> SapGuiSession:
        
        field_count_fails = session.FindById(SapFields.POP_UP_COUNT_FAILS_LABEL_LINE_1, False)
        if field_count_fails is not None: session.SendKey(SapKeys.ENTER)
        
        copy_r = session.FindById('wnd[1]', False)
        if copy_r is not None and copy_r.Text == 'Copyright':
            session.SendKey(SapKeys.ENTER)
        
        if not session.Info().Transaction() == SapTransactions.LOGIN:
            session.SendCommand(SapCommands.RETURN_MENU)
        
        return session

    def LoginSignIn(self, session: SapGuiSession, try_max: int = 3) -> SapGuiSession:
        ''' Realiza o login no SAP
        
        Parameters
        ----------
        session : SapSession
            Sessão na tela de login
        try_max : int
            Máxima de tentativas falhas de login com credenciais inválidas
        '''
        if session is None or session.component is None or not session.ConnectedSap():
            return None
        
        session = self.LoginAfterSignIn(session)
        
        if not session.Info().Transaction() == SapTransactions.LOGIN:
            return session
        
        if self.credentials is None:
            session.ActiveWindow().SetFocusWindows()
            while session.info.CheckTransaction(SapTransactions.LOGIN):
                time.sleep(1)
            return session

        conn_name = session.Parent().Description()
        user_name, password = self.credentials.GetCredentials(conn_name)
        if not SavvyHelper.CheckStrings(user_name, password): return False
        
        try:
            session.FindById(SapFields.LOGIN_MANDT).Text(self.login_mandt)
            session.FindById(SapFields.LOGIN_LANGUAGE).Text(self.login_language)
            session.FindById(SapFields.LOGIN_USERNAME).Text(user_name)
            session.FindById(SapFields.LOGIN_PASSWORD).Text(password)
            session.SendKey(SapKeys.ENTER)
        except:
            SavvyLogger.Error('SAP Init', 'Erro ao preencher as credenciais de login')
            return False
        
        if not session.ConnectedSap():
            self.credentials.ClearCredentials(conn_name)
            return None
        
        if session.GetAlertStatusPane().HasInText('logon)'):
            self.credentials.ClearCredentials(conn_name)
            if try_max > 0:
                return self.LoginSignIn(session, try_max - 1)
            return None
        
        force_sign_bnt = session.FindById(SapFields.POPUP_MULTI_LOGIN_RAD_FORCE, False)
        force_sign_bnt: SapGuiRadioButton
        
        if force_sign_bnt is not None:
            if self.login_force_method == 'Exit':
                session.ActiveWindow().SendKey(SapKeys.F12)
                return None
            
            if self.login_force_method == 'Force':
                force_sign_bnt.Select()
                session.ActiveWindow().SendKey(SapKeys.ENTER)
                
            if self.login_force_method == 'Wait':
                conn_name = session.Parent().Description()
                sap_app = session.Parent().Parent()
                session.ActiveWindow().SendKey(SapKeys.F12)
                time.sleep(self.login_wait_seconds)
                
                new_session = sap_app.OpenConnection(conn_name, True).Sessions().LastItem()
                return self.LoginSignIn(new_session, try_max)
        
        return self.LoginAfterSignIn(session)

    def GetSessionLoged(self, conn_name: str, reuse_conn:bool = True, reuse_sessions:bool = True) -> SapGuiSession:
        self.CloseAllTimeOutPopups()
        if not self.StartProcess(): return None
        sap_app = SapGuiAuto.GetSapApplication()
        if sap_app is None: return None
        
        connections = []
        if reuse_conn: connections = sap_app.ConnectionsList(conn_name)
        
        if len(connections) <= 0:
            conn = sap_app.OpenConnection(conn_name, True)
            if conn is None: return None
            connections = [conn]
        
        if reuse_sessions:
            for conn in connections:
                sessions = conn.SessionsInTransaction(SapTransactions.MAIN_MENU)
                if len(sessions) > 0: return sessions[0]
                
        for conn in connections:
            sessions = conn.SessionsInTransaction(SapTransactions.LOGIN)
            if len(sessions) > 0: return self.LoginSignIn(sessions[0])
        
        return None