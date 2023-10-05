from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer


class GuiCustomControl(GuiVContainer):
    """ O GuiCustomControl é um objeto wrapper usado para colocar controles ActiveX em telas dynpro.
    Embora GuiCustomControl seja um elemento dynpro, seus filhos são do tipo GuiContainerShell, que é um contêiner
    para controles. GuiCustomControl estende o objeto GuiVContainer. O prefixo do tipo é cntl, o nome é o
    nome do campo retirado do dicionário de dados SAP.
    """

    @property
    def char_height(self) -> int:
        """ Altura do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiCustomControl em métrica de caracteres.
        """
        return self.component.CharWidth