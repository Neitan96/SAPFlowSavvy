from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiScrollbar import GuiScrollbar


class GuiScrollContainer(GuiVContainer):
    """ Este contêiner representa subtelas roláveis. Uma subtela pode ser rolável sem realmente ter uma barra de rolagem,
    porque a existência de uma barra de rolagem depende da quantidade de dados exibidos e do tamanho da GuiUserArea.
    O prefixo do tipo é ssub, o nome é gerado a partir das configurações do dicionário de dados.
    """

    @property
    def horizontal_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem horizontal do contêiner de rolagem.
        """
        return GuiScrollbar(self.component.HorizontalScrollbar)

    @property
    def vertical_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem vertical do contêiner de rolagem.
        """
        return GuiScrollbar(self.component.VerticalScrollbar)