import win32com.client

class GuiEnum:
    """ GuiEnum é a classe base para alguns enumeradores usados em scripts SAP GUI.
    """

    class_attrs: list[str]
    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        self.class_attrs = ['component']
        self.component = component

    def next(self, celt: int, rgvar, pcelt_fetched: int):
        return self.component.Next(celt, rgvar, pcelt_fetched)

    def reset(self):
        return self.component.Reset()

    def skip(self, celt: int):
        return self.component.Skip(celt)