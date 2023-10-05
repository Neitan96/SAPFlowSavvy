from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer


class GuiDialogShell(GuiVContainer):
    """ O GuiDialogShell é uma janela externa usada como contêiner para outros shells, por exemplo,
    uma barra de ferramentas. O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    """

    def close(self):
        """ Este método fecha a janela externa.
        """
        self.component.Close()

    @property
    def title(self) -> str:
        """ Título do diálogo.
        """
        return self.component.Title