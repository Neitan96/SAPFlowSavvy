import win32com.client

from .Objects.GuiApplication import GuiApplication

class SapGui:
    @staticmethod
    def get_sap_gui_object():
        return win32com.client.GetObject("SAPGUI")

    @staticmethod
    def get_sap_application() -> GuiApplication:
        return GuiApplication(SapGui.get_sap_gui_object().GetScriptingEngine)