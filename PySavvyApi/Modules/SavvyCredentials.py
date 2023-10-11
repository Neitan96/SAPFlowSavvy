import configparser
import re
import os

from PySavvyApi.SavvyLogger import SavvyLogger
from PySavvyApi.SavvyHelper import inputbox_text, inputbox_password, inputbox_yes_no, check_strings


class SavvyCredentials:
    """ Classe para gerenciamentos de credenciais do SAP

    Faz o armazenamento de credenciais do SAP em variavel e arquivo,
    tirando a necessidade do usúario ficar realizando login sempre que abrir
    uma nova conexão.
    """

    _file_path: str
    _credentials: dict[str, list[str]]

    def __init__(self):
        self._file_path = os.path.expanduser('~\\sapusercredentials.creds')
        self._credentials = {}
        self.read_all_in_file()

    @property
    def file_path_credentials(self) -> str:
        """ Caminho do arquivo para salvar as credenciais do usuário
        """
        return self._file_path

    @file_path_credentials.setter
    def file_path_credentials(self, file_path: str):
        self._file_path = file_path

    @property
    def credentiails(self):
        return self._credentials

    def get_credentials(self, conn_name: str = 'Default', force_read: bool = False, save_in_file: bool = True) -> (str, str):
        """ Obtém a crendencial SAP do usuário

        Faz a leitura das credenciais e faz o tratamento caso não tenha credenciais armazenadas,
        se não tiver credenciais no cache e nem nos arquivos ele pede para o usuário fornecer e
        armazena as credenciais tanto no cache quanto no arquivo.

        Args:
            save_in_file: Se deseja salvar as credenciais no arquivo na pasta pessoal do usuário
            conn_name (str): nome da conexão das credenciais.
            force_read (bool): força a leitura das credenciais mesmo que ela já esteja em cache.
        """

        if not force_read and conn_name in self._credentials:
            return self._credentials[conn_name][0], self._credentials[conn_name][1]

        if self._file_path is not None:
            if self.read_in_file(conn_name) or \
                    (self.read_input_box(conn_name) and (not save_in_file or self.write_in_file(conn_name))):
                return self._credentials[conn_name][0], self._credentials[conn_name][1]

        else:
            if self.read_input_box(conn_name):
                return self._credentials[conn_name][0], self._credentials[conn_name][1]

        return None, None


    def clear_all(self) -> bool:
        """ Limpa todos as credenciais tanto do cache quanto do arquivo
        """
        # noinspection PyBroadException
        try:
            self._credentials = {}
            os.remove(self._file_path)
            return True
        except:
            SavvyLogger.error('Savvy Creds', 'Erro ao limpar todas as credenciais.')
        return False

    def clear_credentials(self, conn_name: str = 'Default') -> bool:
        """ Limpar as credenciais da conexão especificada

        Args:
            conn_name (str): Nome da conexão das credenciais.
        """
        # noinspection PyBroadException
        try:
            if conn_name in self._credentials: self._credentials.pop(conn_name)

            parse = configparser.ConfigParser()
            parse.read(self._file_path)
            conn_session = SavvyCredentials.__conn_name_to_session(conn_name)

            if parse.has_section(conn_session):
                parse.remove_section(conn_session)
                with open(self._file_path, 'w') as configfile:
                    parse.write(configfile)
                return True

        except:
            SavvyLogger.error('Savvy Creds', f'Erro ao limpar as credenciais da conexão: {conn_name}')
        return False

    def read_input_box(self, conn_name: str = 'Default') -> bool:
        """ Pede para o usuário fornecer as credenciais do SAP por meio de InputBox

        Essa função armazena a credencial fornecida pelo usuário apenas no cache,
        para armazenar no arquivo use a função WriteInFile.

        Args:
            conn_name (str): Nome da conexão das credenciais.
        """

        # noinspection PyBroadException
        try:
            desc_conn_user = 'Digite seu nome de usuário' + \
                (':\t' if conn_name == 'Default' else ' da conexão:\n' + conn_name)
            desc_conn_pass = 'Digite sua senha' + (
                ':\t\t' if conn_name == 'Default' else ' da conexão:\t\n' + conn_name)

            user_name = inputbox_text('Login SAP', desc_conn_user)
            password = inputbox_password('Login SAP', desc_conn_pass)

            if check_strings(user_name, password):
                self._credentials[conn_name] = [user_name, password]
                return True
            else:
                if inputbox_yes_no('Credenciais inválidas',
                                             'As credenciais que você inseriu não são válidas\r\nDeseja inserir novamente?'):
                    return self.read_input_box(conn_name)

        except:
            SavvyLogger.error('Savvy Creds', 'Erro ao ler as credenciais por meio de Inputbox')
        return False

    @staticmethod
    def __conn_name_to_session(conn_name: str = 'Default') -> str:
        """ Faz o tratamento do nome da conexão para usar em sessões de arquivo de configurações

        Args:
            conn_name (str): Nome da conexão das credenciais.
        """
        return re.sub('[^a-z|^A-Z]', '', conn_name).upper()

    def write_in_file(self, conn_name: str = 'Default') -> bool:
        """ Armazena as credenciais da conexão no cache no arquivo de credenciais

        Args:
            conn_name (str): Nome da conexão das credenciais.
        """
        if self._file_path is None: return False

        parse: configparser.ConfigParser
        # noinspection PyBroadException
        try:
            parse = configparser.ConfigParser()
            parse.read(self._file_path)
        except:
            SavvyLogger.error('Savvy Creds', 'Não foi possivel fazer a leitura do arquivo de credenciais')
            return False

        conn_session = SavvyCredentials.__conn_name_to_session(conn_name)

        user_name = self._credentials[conn_name][0]
        password = self._credentials[conn_name][1]

        if check_strings(user_name, password):
            # noinspection PyBroadException
            try:
                if not parse.has_section(conn_session): parse.add_section(conn_session)
                parse.set(conn_session, 'username', user_name)
                parse.set(conn_session, 'password', password)
                parse.set(conn_session, 'connection', conn_name)
                with open(self._file_path, 'w') as configfile:
                    parse.write(configfile)
                return True
            except:
                SavvyLogger.error('Savvy Creds', 'Não foi possivel gravar as credenciais no arquivo')

        return False

    def write_all_in_file(self) -> bool:
        """ Armazena todas as credenciais do cache no arquivo de credenciais
        """
        if self._file_path is None: return False
        result = True
        for conn_name in self._credentials.keys():
            result = self.write_in_file(conn_name) and result
        return result

    def read_in_file(self, conn_name: str = 'Default') -> bool:
        """ Faz a leitura das credenciais no arquivo e armazena no cache

        Args:
            conn_name (str): Nome da conexão das credenciais.
        """
        if self._file_path is None: return False

        parse: configparser.ConfigParser
        # noinspection PyBroadException
        try:
            parse = configparser.ConfigParser()
            parse.read(self._file_path)
        except:
            SavvyLogger.error('Savvy Creds', 'Não foi possivel fazer a leitura do arquivo de credenciais')
            return False

        conn_session = SavvyCredentials.__conn_name_to_session(conn_name)

        if not parse.has_section(conn_session): return False

        user_name = parse[conn_session]['username']
        password = parse[conn_session]['password']

        if check_strings(user_name, password):
            self._credentials[conn_name] = [user_name, password]
            return True

    def read_all_in_file(self) -> bool:
        """ Faz a leitura de todas as credenciais no arquivo e armazena no cache
        """

        parse: configparser.ConfigParser
        # noinspection PyBroadException
        try:
            parse = configparser.ConfigParser()
            parse.read(self._file_path)
        except:
            SavvyLogger.error('Savvy Creds', 'Não foi possivel fazer a leitura do arquivo de credenciais')
            return False

        for conn_session in parse.sections():
            user_name = parse[conn_session]['username']
            password = parse[conn_session]['password']
            conn_name = parse[conn_session]['connection']

            if check_strings(user_name, password, conn_name):
                self._credentials[conn_name] = [user_name, password]

        return True
