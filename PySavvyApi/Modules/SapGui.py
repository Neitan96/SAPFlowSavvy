import time
from typing import Optional

import pywinauto
import win32com.client
import os

from PySavvyApi.SapGuiWrapper import GuiApplication

class SapGui:
    """ Classe feita para fazer manipulação na aplicação do Sap Gui.
    """

    @staticmethod
    def get_sap_gui_object(on_raise: bool = False) -> Optional[win32com.client.CDispatch]:
        """ Obtém o objeto CDispatch do Sap Gui
        Args:
            on_raise: quando verdadeiro e o SAP Gui não está disponivel ocasiona um erro
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
    def get_sap_application() -> Optional[GuiApplication]:
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
        return (element.element_info.class_name == 'Button'
                and element.element_info.control_type == 'Button'
                and (element.element_info.rich_text == 'Não' or element.element_info.rich_text == 'No'
                     or element.element_info.rich_text == 'OK')
                )

    @staticmethod
    def __filter_windows_titles(window):
        return ('SAP GUI for Windows' in window.element_info.rich_text
                or 'Version Error' in window.element_info.rich_text)

    @staticmethod
    def close_all_popups():
        """ Fecha popups de timeout e erros de conexão
        """
        # noinspection PyBroadException
        try:
            popup_app = pywinauto.Application(backend='uia').connect(title_re='SAP GUI for Windows .*', found_index=0, timeout=15)
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