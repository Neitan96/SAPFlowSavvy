from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiSplitterContainer(GuiShell):
    """ O GuiSplitterContainer representa o elemento divisor dynpro, que foi introduzido
    no Web Application Server ABAP no NetWeaver 7.1. O elemento divisor dynpro é semelhante
    ao controle divisor baseado em activeX, mas é um elemento dynpro simples.
    """

    @property
    def is_vertical(self) -> bool:
        """ Esta propriedade contém True se as células divisoras do GuiSplitterContainer estiverem alinhadas
        verticalmente e False se estiverem alinhadas horizontalmente.
        """
        return self.component.IsVertical

    @property
    def sash_position(self) -> int:
        """ Contém a posição da divisória do divisor em caracteres.
        """
        return self.component.SashPosition

    @sash_position.setter
    def sash_position(self, position: int = None) -> None:
        """ Contém a posição da divisória do divisor em caracteres.
        """
        self.component.SashPosition = position