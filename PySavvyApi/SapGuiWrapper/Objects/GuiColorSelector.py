from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiColorSelector(GuiShell):
    """ GuiColorSelector exibe um conjunto de cores para seleção.
    """

    def change_selection(self, i: int) -> None:
        """ Esta função emula a seleção da cor pelo usuário na posição de índice especificada.
        """
        self.component.ChangeSelection(i)