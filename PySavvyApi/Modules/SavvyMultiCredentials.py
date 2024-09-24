import os
import json
from typing import Callable


class SavvyMultiCredentials:
    """ Classe para armazenar e gerenciar múltiplas credenciais para a mesma conexão do SAP.

    Faz o armazenamento e gerenciamento de credenciais do SAP, podendo armazenar credenciais
    de diferentes usuários para a mesma conexão do SAP, possibilitando fazer o controle por
    ID da credencial, grupo, string de conexão, nome da conexão ou pela transação da credencial.

    Arquivo de exemplo: PySavvyApi/Modules/MultiCredentialsExample.json
    """

    _file_path: str  # Caminho do arquivo para salvar as credenciais do usuário
    _credentials: dict  # Cache de credenciais do usuário
    _password_generator: Callable[[str, str], str] | None  # Gerador de senhas caso o sap requisitar a troca de senha
    _credentials_user_input: Callable[[str, str], str] | None  # Função para obter as credenciais do usuário

    def __init__(self, credentials):
        self._file_path = os.path.expanduser('~\\sapmulticredentials.creds')
        self._credentials = {}
        self._new_password_generator = None
        self.load_file()

    @property
    def file_path_credentials(self) -> str:
        """ Caminho do arquivo para salvar as credenciais do usuário
        """
        return self._file_path

    @file_path_credentials.setter
    def file_path_credentials(self, file_path: str):
        self._file_path = file_path
        self.load_file()

    def load_file(self):
        """ Carrega as credenciais do arquivo
        """
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                self._credentials = json.load(file)

    def save_file(self):
        """ Salva as credenciais no arquivo
        """
        with open(self._file_path, 'w', encoding ='utf8') as file:
            json.dump(self._credentials, file, indent=4)

    def register_conn(self, conn_id: str, conn_description: str | None, conn_string: str | None, replace: bool = False):
        """ Registra uma conexão nomeada
        Registra uma conexão serve para garantir que a conexão exista no arquivo de credenciais,
        não irá substituir a conexão caso ela já exista, apenas se o parametro replace for True.

        É Obrigatório passar a descrição da conexão ou a string de conexão,
        caso não seja passado a descrição ou a string de conexão, a conexão não será registrada.

        Args:
            conn_id (str): Identificador da conexão, o nome pelo qual a conexão será chamada
            conn_description (str): Descrição da conexão
            conn_string (str): String de conexão
            replace (bool): Substituir a conexão caso ela já exista
        """
        if not replace and conn_id in self._credentials['Connections']:
            return
        if conn_description is None and conn_description != '':
            self._credentials['Connections']['conn_name'] = {'Description': conn_description}
            self.save_file()
        elif conn_string is None and conn_string != '':
            self._credentials['Connections']['conn_name'] = {'ConnectionString': conn_string}
            self.save_file()

    def register_cred(self, conn_name: str, username: str | None = None, password: str | None = None,
                      cred_id: str | None = None, transactions: list[str] = None, order: int | None = None,
                      replace_pass: bool = False):
        """ Faz o registro de uma credencial.
        Somente é necessário fazer o registro de uma credencial caso deseje fazer a busca por credenciais
        específicas durante a execução do programa ou queria registrar multiplas credenciais para a mesma conexão,
        possibilitando abrir sessões com usuários diferentes aumentando a quantidade de sessões simultâneas que
        podem ser abertas.

        A ordem de prioridade é utilizada para definir qual credencial será utilizada,
        para usar a conexão somente ao declarar explicitamente a credencial, user valores negativos,
        para definir explicitamente a credencial, é necessário passar o ID da credencial ou alguma transação
        que a credencial pode acessar.

        Args:
            conn_name (str): Nome da conexão registrada
            username (str): Nome do usuário
            password (str): Senha do usuário
            cred_id (str): Identificador da credencial
            transactions (list[str]): Lista de transações que a credencial pode acessar
            order (int): Ordem de prioridade da credencial
            replace_pass (bool): Substituir a senha caso ela já exista
        """
        # TODO Implementar a função register_cred
        pass
