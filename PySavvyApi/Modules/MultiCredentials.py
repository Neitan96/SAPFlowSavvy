import os
import json
import datetime
from random import randint
from typing import Callable, Literal


class MultiCredentials:
    """ Classe para armazenar e gerenciar múltiplas credenciais para a mesma conexão do SAP.

    Faz o armazenamento e gerenciamento de credenciais do SAP, podendo armazenar credenciais
    de diferentes usuários para a mesma conexão do SAP, possibilitando fazer o controle por
    ID da credencial, grupo, string de conexão, nome da conexão ou pela transação da credencial.

    Exemplo de uso:
    ```python
    from PySavvyApi.Modules.MultiCredentials import MultiCredentials

    # Cria uma instância da classe MultiCredentials
    multi_cred = MultiCredentials()

    # Registra uma conexão
    multi_cred.conn_register('ECC', '1. ECC - Produção (DFP)', 'SAP - 100 - 00 - 00 - 00')

    # Registra uma credencial
    multi_cred.creds_register(conn_name='ECC',
                                username='user1',
                                password='password1',
                                cred_id='user1',
                                transactions=['VA03', 'MB52'],
                                order=0)

    # Registra outra credencial
    multi_cred.creds_register(conn_name='ECC',
                                username='user2',
                                password='password2',
                                cred_id='user2',
                                transactions=['MM01', 'MM02'],
                                order=1)

    # Lista as credenciais registradas
    print(multi_cred.creds_list())

    # Habilita o gerador de senha padrão
    multi_cred.pass_gen_set_default_gen()

    # Gera uma nova senha para a credencial
    multi_cred.creds_gen_new_pass('user1')

    # Busca as credenciais registradas
    print(multi_cred.creds_find(conn_name='ECC', transactions=['S000']))

    # Deleta uma credencial registrada
    multi_cred.creds_delete('user1')

    # Deleta todas as credenciais registradas
    multi_cred.creds_delete_all()
    ```

    Arquivo de exemplo: PySavvyApi/Modules/MultiCredentialsExample.json
    """

    _file_path: str  # Caminho do arquivo para salvar as credenciais do usuário
    _credentials: dict  # Cache de credenciais do usuário
    _password_gen: Callable[[str, str, str], str] | None  # Gerador de senhas caso o sap requisitar a troca de senha
    _credentials_user_input: Callable[[str, str], str] | None  # Função para obter as credenciais do usuário

    def __init__(self, file_path: str = None):
        file_path = file_path or os.path.expanduser('~\\sapmulticredentials.creds')
        self._file_path = file_path
        self._credentials = {}
        self._password_gen = None
        self.load_creds_file()

    # noinspection PyUnusedLocal
    @staticmethod
    def default_password_gen(username: str, conn_name: str, password_now: str) -> str:
        """ Gerador de senha padrão
        Gera uma senha padrão baseada no nome do usuário data e número aleatório.

        Args:
            username (str): Nome do usuário
            conn_name (str): Nome da conexão
            password_now (str): Senha de atual

        Returns:
            str: Senha gerada
        """
        new_password = f'{username[:5]}@{datetime.datetime.now().strftime("%Y%m")}'
        if new_password == password_now:
            new_password += str(randint(1000,9999))
        return new_password

    def pass_gen_set_default_gen(self):
        """ Define o gerador de senha padrão

        Define o gerador de senha padrão, caso o sap requisitar a troca de senha,
        será gerado uma senha baseada no nome do usuário, data e número aleatório.
        """
        self._password_gen = self.default_password_gen

    @property
    def pass_gen(self) -> Callable[[str, str], str] | None:
        """ Gerador de senha

        Returns:
            Callable[[str, str], str]: Função geradora de senha
        """
        return self._password_gen

    @pass_gen.setter
    def pass_gen(self, generator: Callable[[str, str, str], str]):
        """ Define o gerador de senha
        Define o gerador de senha, caso o sap requisitar a troca de senha,

        Args:
            generator (Callable[[str, str], str]): Função geradora de senha
        """
        self._password_gen = generator

    @property
    def file_path_credentials(self) -> str:
        """ Caminho do arquivo para salvar as credenciais do usuário
        """
        return self._file_path

    @file_path_credentials.setter
    def file_path_credentials(self, file_path: str):
        self._file_path = file_path
        self.load_creds_file()

    def load_creds_file(self):
        """ Carrega as credenciais do arquivo
        """
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                self._credentials = json.load(file)

    def save_creds_file(self):
        """ Salva as credenciais no arquivo
        """
        with open(self._file_path, 'w', encoding ='utf8') as file:
            # noinspection PyTypeChecker
            json.dump(self._credentials, file, indent=4)

    def conn_register(self, conn_id: str, conn_description: str | None, conn_string: str | None, replace: bool = False):
        """ Registra uma conexão nomeada
        Registra uma conexão serve para garantir que a conexão exista no arquivo de credenciais,
        não irá substituir a conexão caso ela já exista, apenas se o parâmetro replace for True.

        É Obrigatório passar a descrição da conexão ou a string de conexão,
        caso não seja passado a descrição ou a string de conexão, a conexão não será registrada.

        Args:
            conn_id (str): Identificador da conexão, o nome pelo qual a conexão será chamada
            conn_description (str): Descrição da conexão
            conn_string (str): String de conexão
            replace (bool): Substituir a conexão caso ela já exista
        """
        conn_id = conn_id.lower()
        if not replace and conn_id in self._credentials['Connections']:
            return
        if conn_description is None and conn_description != '':
            self._credentials['Connections'][conn_id] = {'Description': conn_description}
            self.save_creds_file()
        elif conn_string is None and conn_string != '':
            self._credentials['Connections'][conn_id] = {'ConnectionString': conn_string}
            self.save_creds_file()

    def conn_list_ids(self) -> list:
        """ Lista as conexões registradas
        Retorna uma lista com os identificadores das conexões registradas.

        Returns:
            list: Lista com os identificadores das conexões registradas
        """
        if 'Connections' not in self._credentials:
            return []
        return list(self._credentials['Connections'].keys())

    def conn(self, conn_id: str) -> (Literal['ConnectionString', 'Description'] | None, str | None):
        """ Retorna as informações da conexão
        Retorna a descrição ou a string de conexão da conexão registrada.

        Args:
            conn_id (str): Identificador da conexão

        Returns:
            Literal['ConnectionString', 'Description']: Tipo de conexão, pode ser a descrição ou a string de conexão
            str: Informação da conexão, descrição ou string de conexão
        """
        if 'Connections' not in self._credentials or conn_id.lower() not in self._credentials['Connections']:
            return None, None

        creds: dict = self._credentials['Connections'][conn_id.lower()]
        type_conn = next(iter(creds.keys()))
        return type_conn, creds[type_conn]

    def conn_find_desc(self, conn_description: str) -> str | None:
        """ Retorna o identificador da conexão
        Retorna o identificador da conexão baseado na descrição da conexão.

        Args:
            conn_description (str): Descrição da conexão

        Returns:
            str: Identificador da conexão
        """
        if 'Connections' not in self._credentials:
            return None

        for conn_id, conn in self._credentials['Connections'].items():
            if conn['Description'] == conn_description:
                return conn_id
        return None

    def conn_find_conn_string(self, conn_string: str) -> str | None:
        """ Retorna o identificador da conexão
        Retorna o identificador da conexão baseado na string de conexão.

        Args:
            conn_string (str): String de conexão

        Returns:
            str: Identificador da conexão
        """
        if 'Connections' not in self._credentials:
            return None

        for conn_id, conn in self._credentials['Connections'].items():
            if conn['ConnectionString'] == conn_string:
                return conn_id
        return None

    def conn_delete(self, conn_id: str):
        """ Deleta uma conexão registrada
        Deleta uma conexão registrada, caso a conexão não exista, não faz nada.

        Args:
            conn_id (str): Identificador da conexão
        """
        conn_id = conn_id.lower()
        if conn_id in self._credentials['Connections']:
            del self._credentials['Connections'][conn_id]
            self.save_creds_file()

    def conn_delete_all(self):
        """ Deleta todas as conexões registradas
        """
        self._credentials['Connections'] = {}
        self.save_creds_file()

    def creds_register(self, conn_name: str, username: str | None = None, password: str | None = None,
                       cred_id: str | None = None, transactions: list[str] = None, order: int | None = None,
                       replace_pass: bool = False) -> str:
        """ Faz o registro de uma credencial.
        Somente é necessário fazer o registro de uma credencial caso deseje fazer a busca por credenciais
        específicas durante a execução do programa ou queria registrar multiplas credenciais para a mesma conexão,
        possibilitando abrir sessões com usuários diferentes aumentando a quantidade de sessões simultâneas que
        podem ser abertas.

        A ordem de prioridade é utilizada para definir qual credencial será utilizada,
        para usar a credencial somente ao declarar explicitamente, use valores negativos,
        para definir explicitamente a credencial, é necessário passar o ID da credencial ou alguma transação
        que a credencial pode acessar.

        Caso não for declarado o cred_id, será gerado um ID baseado no nome da conexão e do usuário.

        Args:
            conn_name (str): Nome da conexão registrada
            username (str): Nome do usuário
            password (str): Senha do usuário
            cred_id (str): Identificador da credencial
            transactions (list[str]): Lista de transações que a credencial pode acessar
            order (int): Ordem de prioridade da credencial
            replace_pass (bool): Substituir a senha caso ela já exista

        Returns:
            str: Identificador da credencial
        """
        if not cred_id:
            cred_id = f"{conn_name}_{username}"

        if cred_id in self._credentials and not replace_pass:
            return cred_id

        if 'Credentials' not in self._credentials:
            self._credentials['Credentials'] = {}

        self._credentials['Credentials'][cred_id] = {
            'ConnectionName': conn_name,
            'Order': order or 0,
            'Username': username,
            'Password': password,
            'Transactions': transactions or []
        }

        self.save_creds_file()

    def creds_list(self) -> list:
        """ Lista as credenciais registradas
        Retorna uma lista com os identificadores das credenciais registradas.

        Returns:
            list: Lista com os identificadores das credenciais registradas
        """
        if 'Credentials' not in self._credentials:
            return []
        return list(self._credentials['Credentials'].keys())

    def creds_find(self, conn_name: str = None, transactions: list[str] = None, username: str = None,
                   order_min: int | None = 0, order_max: int | None = None) -> dict[str, dict]:
        """ Busca as credenciais registradas pelos parâmetros fornecidos.
        Ao passar algum parâmetro None, ele não será considerado na busca.

        Args:
            conn_name (str): Nome da conexão
            transactions (list[str]): Lista de transações que a credencial pode acessar
            username (str): Nome do usuário
            order_min (int): Ordem mínima da credencial
            order_max (int): Ordem máxima da credencial

        Returns:
            dict: Dicionário com as credenciais encontradas
        """
        if 'Credentials' not in self._credentials:
            return {}

        creds = {}
        for cred_id, cred in self._credentials['Credentials'].items():
            if conn_name and conn_name != cred['ConnectionName']:
                continue
            if username and creds.get('Username') == username:
                continue
            if transactions and('Transactions' not in creds
                                or any(t not in cred['Transactions'] for t in transactions)):
                continue
            if order_min and ('Order' not in creds or cred['Order'] < order_min):
                continue
            if order_max and ('Order' not in creds or cred['Order'] > order_max):
                continue
            creds[cred_id] = cred
        return creds

    def creds(self, cred_id: str) -> dict | None:
        """ Retorna as informações da credencial
        Retorna as informações da credencial registrada.

        Args:
            cred_id (str): Identificador da credencial

        Returns:
            dict: Informações da credencial
        """
        if 'Credentials' not in self._credentials or cred_id not in self._credentials['Credentials']:
            return None
        return self._credentials['Credentials'][cred_id]

    def creds_set_password(self, cred_id: str, password: str | None):
        """ Define a senha da credencial
        Define a senha da credencial registrada.

        Passe None para o parâmetro password para remover a senha da credencial.

        Args:
            cred_id (str): Identificador da credencial
            password (str): Senha da credencial
        """
        if 'Credentials' not in self._credentials or cred_id not in self._credentials['Credentials']:
            return
        if password:
            self._credentials['Credentials'][cred_id]['Password'] = password
        else:
            del self._credentials['Credentials'][cred_id]['Password']
        self.save_creds_file()

    def creds_invalidate_pass(self, cred_id: str):
        """ Invalida a senha da credencial
        Invalida a senha da credencial registrada, removendo a senha da credencial.

        Args:
            cred_id (str): Identificador da credencial
        """
        self.creds_set_password(cred_id, None)

    def creds_gen_new_pass(self, cred_id: str) -> str | None:
        """ Gera uma nova senha para a credencial
        Gera uma nova senha para a credencial, caso o gerador de senha não esteja definido,
        não será gerada uma nova senha.

        Ao gerar uma nova senha, a senha antiga será substituída pela nova senha gerada,
        e a nova senha será salva no arquivo de credenciais.

        Args:
            cred_id (str): Identificador da credencial

        Returns:
            str: Nova senha gerada
        """
        if (self._password_gen is None or 'Credentials' not in self._credentials
                or cred_id not in self._credentials['Credentials']):
            return None

        cred_infos = self._credentials['Credentials'][cred_id]
        password_now = None
        if 'Password' in cred_infos:
            password_now = cred_infos['Password']
        new_password = self._password_gen(cred_infos['Username'], cred_infos['ConnectionName'], password_now)
        if new_password is None:
            return None

        self._credentials['Credentials'][cred_id]['Password'] = new_password
        self.save_creds_file()


    def creds_delete(self, cred_id: str):
        """ Deleta uma credencial registrada
        Deleta uma credencial registrada, caso a credencial não exista, não faz nada.

        Args:
            cred_id (str): Identificador da credencial
        """
        if 'Credentials' not in self._credentials or cred_id not in self._credentials['Credentials']:
            return
        del self._credentials['Credentials'][cred_id]
        self.save_creds_file()

    def creds_delete_all(self):
        """ Deleta todas as credenciais registradas
        """
        self._credentials['Credentials'] = {}
        self.save_creds_file()
