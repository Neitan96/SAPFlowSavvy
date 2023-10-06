import win32com.client


class GuiScrollbar:
    """ A classe GuiScrollbar é uma classe utilitária usada, por exemplo, em GuiScrollContainer ou GuiTableControl.
    """

    # TODO Fazer mais funções de auxilio

    def __init__(self, component: win32com.client.CDispatch):
        # self.class_attrs = ['component']
        self.component = component

    @property
    def maximum(self) -> int:
        """ Esta é a posição máxima da barra de rolagem.
        """
        return self.component.Maximum

    @property
    def minimum(self) -> int:
        """ Esta é a posição mínima da barra de rolagem.
        """
        return self.component.Minimum

    @property
    def page_size(self) -> int:
        """ Quando o usuário rola uma página para baixo, a posição será aumentada pelo valor de pageSize.
        """
        return self.component.PageSize

    @property
    def position(self) -> int:
        """ A posição do polegar da barra de rolagem pode ser definida em valores do mínimo ao máximo.
        """
        return self.component.Position

    @position.setter
    def position(self, position: int):
        """ A posição do polegar da barra de rolagem pode ser definida em valores do mínimo ao máximo.
        """
        self.component.Position = position

    def load_all(self) -> None:
        """ Faz o carregamento completo do componente, rolando do começo até o fim do scroll.
        """
        self.position = self.minimum
        while self.position < self.maximum:
            new_pos = min(self.maximum, self.position+self.page_size)
            self.position = new_pos

