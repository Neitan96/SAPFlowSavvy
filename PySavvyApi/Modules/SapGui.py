import win32com.client
import pywinauto
import time
import os

from PySavvyApi.SapGuiWrapper import GuiApplication

class SapGui:
    """ Classe feita para fazer manipulação no windows do programa do Sap Gui.

    Responsável por abrir, fechar e verificar, programa está aberto e manipular
    ambientes fora do SAP que está fora do controle no SAP Gui Scripting, como
    popups de erro e timeout.
    """

    WINDOW_TITLE_RE = 'SAP GUI for Windows .*'
    WINDOWS_TITLES = ['SAP GUI for Windows .*', 'Version Error']
    WINDOWS_BUTTONS = ['Não', 'No', 'OK']
    SAP_LOGON_PATH = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'

    @staticmethod
    def get_sap_gui_object(on_raise: bool = False) -> win32com.client.CDispatch | None:
        """ Obtém o objeto CDispatch do Sap Gui
        Args:
            on_raise: quando verdadeiro e o SAP Gui não está disponível ocasiona um erro
        Returns:
            GuiApplication: Objeto CDispatch do Sap Gui
        """
        if on_raise:
            return win32com.client.GetObject("SAPGUI")
        else:
            # noinspection PyBroadException
            try:
                return win32com.client.GetObject("SAPGUI")
            except: return None

    @staticmethod
    def get_sap_application() -> GuiApplication | None:
        """ Obtém a aplicação do Sap Gui
        Returns:
            GuiApplication: Aplicação do Sap Gui
        """
        obj = SapGui.get_sap_gui_object()
        if obj is None: return None
        return GuiApplication(obj.GetScriptingEngine)

    @staticmethod
    def sap_running() -> bool:
        """ Verifica se o SAP Logon está sendo executado
        """
        # noinspection PyBroadException
        try:
            sap_obj = SapGui.get_sap_gui_object()
            return type(sap_obj) == win32com.client.CDispatch
        except:
            pass
        return False

    @staticmethod
    def __filter_buttons_no(element):
        return (element.element_info.class_name == 'Button' and element.element_info.control_type == 'Button'
                and any(element.element_info.rich_text == button_title for button_title in SapGui.WINDOWS_BUTTONS))

    @staticmethod
    def __filter_windows_titles(window):
        return any(title in window.element_info.rich_text for title in SapGui.WINDOWS_TITLES)

    @staticmethod
    def close_all_popups(timeout: int = 3):
        """ Fecha popups de timeout e erros de conexão
        Args:
            timeout: Tempo máximo em segundos para procurar popups
        """
        # noinspection PyBroadException
        try:
            popup_app = (pywinauto.Application(backend='uia')
                         .connect(title_re=SapGui.WINDOW_TITLE_RE, found_index=0, timeout=timeout))
            windows_search = list(filter(SapGui.__filter_windows_titles, popup_app.windows()))

            for popup_window in windows_search:
                elements = list(filter(SapGui.__filter_buttons_no, popup_window.children()))
                for element in elements:
                    element.click()
                if len(elements) > 0:
                    time.sleep(2)
        except:
            pass

    @staticmethod
    def start_sap_logon(sap_logon_path: str | None = None, wait_secs_timeout: int = 30) -> bool:
        """ Inicia o SAP Logon

        Abre o executável do SAP Logon conforme o parâmetro sap_logon_path,
        caso já esteja aberto a função não é executada.

        Args:
            sap_logon_path (str): Caminho do executável do SAP Logon.
            wait_secs_timeout (int): Tempo máximo de espera para o SAP Logon abrir.
        """

        if SapGui.sap_running(): return True

        # noinspection PyBroadException
        try: os.startfile(sap_logon_path or SapGui.SAP_LOGON_PATH)
        except: return False

        while wait_secs_timeout > 0:
            wait_secs_timeout -= 1
            time.sleep(1)
            if SapGui.sap_running(): return True

        return SapGui.sap_running()

    @staticmethod
    def kill_process_sap_logon() -> None:
        """ Força a finalização do SAP. """
        os.system('taskkill -f -im saplogon.exe')