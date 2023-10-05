from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer


class GuiTab(GuiVContainer):
    """ Os objetos GuiTab são filhos de um objeto GuiTabStrip.
    O prefixo do tipo é tabp, o nome é o id do botão da aba retirado do dicionário de dados SAP.
    """

    def scroll_to_left(self) -> None:
        #TODO explicar melhor
        """ ScrollToLeft desloca as guias para que uma determinada guia se torne a leftTab da faixa de guias.
        """
        self.component.ScrollToLeft()

    def select(self) -> None:
        """ Esta função define a guia como a guia selecionada na faixa de guias.
        Alterar a guia selecionada de uma faixa de guias pode causar comunicação com o servidor.
        """
        self.component.Select()