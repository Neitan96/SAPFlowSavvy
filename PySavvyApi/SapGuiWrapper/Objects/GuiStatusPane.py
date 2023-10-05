from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiStatusPane(GuiVComponent):
    """ O pai dos objetos GuiStatusPane é a barra de status (veja também Objeto GuiStatusbar).
    Os objetos GuiStatusPane refletem as áreas individuais da barra de status, por exemplo, "pane[0]"
    refere-se à seção da barra de status onde as mensagens são exibidas. Veja também Objeto GuiStatusbar.
    """

    def has_in_text(self, text: str) -> bool:
        """ Verifica se tem um texto específico dentro do texto do painel.
        """
        return self.text is not None and text in self.text