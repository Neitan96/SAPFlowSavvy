import time

import pywinauto
import win32com.client
import os

from ..SapGuiWrapper import GuiApplication

class SapGui:

    @staticmethod
    def get_sap_gui_object():
        return win32com.client.GetObject("SAPGUI")

    @staticmethod
    def get_sap_application() -> GuiApplication:
        return GuiApplication(SapGui.get_sap_gui_object().GetScriptingEngine)

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
        return (element.element_info.class_name == 'Button'
                and element.element_info.control_type == 'Button'
                and (element.element_info.rich_text == 'Não' or element.element_info.rich_text == 'No')
                )

    @staticmethod
    def __filter_windows_titles(window):
        return 'SAP GUI for Windows' in window.element_info.rich_text

    @staticmethod
    def close_all_time_out_popups():
        # noinspection PyBroadException
        try:
            popup_app = pywinauto.Application(backend='uia').connect(title_re='SAP GUI for Windows .*', found_index=0)
            windows_search = list(filter(SapGui.__filter_windows_titles, popup_app.windows()))

            for popup_window in windows_search:
                elements = list(filter(SapGui.__filter_buttons_no, popup_window.children()))
                for element in elements:
                    element.click()
        except:
            pass

    @staticmethod
    def start_sap_logon(sap_logon_path: str = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe',
                        wait_secs_timeout: int = 30) -> bool:
        """ Inicia o SAP Logon

        Abre o executável do SAP Logon conforme o parâmetro sap_logon_path,
        caso já esteja aberto a função não é executada.

        Args:
            sap_logon_path (str): Caminho do executavel do SAP Logon.
            wait_secs_timeout (int): Tempo máximo de espera para o SAP Logon abrir.
        """

        if SapGui.sap_running(): return True

        # noinspection PyBroadException
        try: os.startfile(sap_logon_path)
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