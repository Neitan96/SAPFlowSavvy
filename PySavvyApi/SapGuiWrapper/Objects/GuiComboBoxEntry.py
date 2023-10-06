import win32com.client

class GuiComboBoxEntry:

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    @property
    def key(self) -> str:
        """ Valor-chave da entrada da caixa de combinação.
        """
        return self.component.Key

    @property
    def pos(self) -> int:
        """ Posição da entrada da caixa de combinação. O intervalo vai de 1 ao número de entradas na caixa de combinação.
        """
        return self.component.Pos

    @property
    def value(self) -> str:
        """ Value of the combo box entry.
        """
        return self.component.Value
