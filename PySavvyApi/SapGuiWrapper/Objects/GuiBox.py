from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiBox(GuiVComponent):
    """ Uma GuiBox é um quadro simples com um nome (também chamado de "Group Box").
    Os itens dentro da moldura não são filhos da caixa. O prefixo do tipo é "caixa".
    """

    @property
    def char_height(self) -> int:
        """ Altura do GuiBox em caracteres métricos.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiBox em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiBox em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiBox em métrica de caracteres.
        """
        return self.component.CharWidth