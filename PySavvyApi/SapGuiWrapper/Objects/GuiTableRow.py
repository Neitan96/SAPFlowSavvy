from .GuiComponentCollection import GuiComponentCollection


class GuiTableRow(GuiComponentCollection):
    """ GuiTableRow representa uma linha em um controle de tabela.
    """

    # TODO Funções de auxilio

    @property
    def selectable(self) -> bool:
        """ Esta propriedade será True se a linha puder ser selecionada.
        """
        return self.component.Selectable

    @property
    def selected(self) -> bool:
        """ Esta propriedade é verdadeira se a linha estiver selecionada.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, option: bool) -> None:
        """ Esta propriedade é verdadeira se a linha estiver selecionada.
        """
        self.component.Selected = option
