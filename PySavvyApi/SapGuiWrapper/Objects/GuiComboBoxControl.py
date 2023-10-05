from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection


class GuiComboBoxControl(GuiShell):
    # TODO Criar uma descrição

    def fire_selected(self) -> None:
        """ Envia evento "selecionado".
        """
        self.component.FireSelected()

    @property
    def entries(self) -> GuiCollection:
        """ As entradas são novamente uma GuiCollection com: key(index=0), text(index=1) o texto de cada entrada que você pode obter por meio desta coleção.
        """
        return GuiCollection(self.component.Entries)

    @property
    def label_text(self) -> str:
        """ Texto da etiqueta.
        """
        return self.component.LabelText

    @property
    def selected(self) -> str:
        """ A chave da entrada atualmente selecionada da caixa de combinação.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, select: str = None) -> None:
        """ A chave da entrada atualmente selecionada da caixa de combinação.
        """
        self.component.Selected = select

    @property
    def text(self) -> str:
        """ Texto atual da caixa de combinação.
        """
        return self.component.Text