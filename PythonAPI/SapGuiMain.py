from __future__ import annotations
from SapGuiApiWrapper import *
from SapTCodes import *

import os
import re
import pymsgbox
import configparser

class SavvyParameters():
    pass #TODO

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