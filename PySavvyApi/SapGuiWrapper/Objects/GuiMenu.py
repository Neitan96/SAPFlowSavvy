from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiMenu(GuiVComponent):
    """ Um GuiMenu pode ter outros objetos GuiMenu como filhos.
    O prefixo do tipo é menu, o nome é o texto do item de menu.
    Caso o item não possua texto, como o caso dos separadores, então o nome é a última parte do id, menu[n].
    """

    def select(self) -> None:
        """ Selecione o menu.
        """
        self.component.Select()