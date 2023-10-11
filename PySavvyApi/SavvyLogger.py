from PySavvyApi.SavvyHelper import check_strings


class SavvyLogger:
    """ Classe para registro de execução da API
    """
    # TODO Fazer um arquivo de registro.

    @staticmethod
    def error(module: str, msg: str):
        print((('X► Módulo: ' + module + ' -> ') if check_strings(module) else '') + \
              'ERRO: ' + msg + ' !!!')

    @staticmethod
    def warning(module: str, msg: str):
        print((('○ Módulo: ' + module + ' -> ') if check_strings(module) else '') + \
              'Atenção: ' + msg + ' !!!')

    @staticmethod
    def debug(module: str, msg: str):
        print((('» Módulo: ' + module + ' -> ') if check_strings(module) else '') + \
              'Debug: ' + msg + ' !!!')