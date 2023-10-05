from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer


class GuiTabStrip(GuiVContainer):
    """ Uma faixa de guias é um contêiner cujos filhos são do tipo GuiTab.
    O prefixo do tipo é tabulações, o nome é o nome do campo retirado do dicionário de dados SAP.
    Os filhos da faixa de guias são as guias. Embora todas as guias estejam disponíveis a qualquer momento, apenas os filhos da guia selecionada
    existem na hierarquia de objetos para faixas de guias controladas pelo servidor.
    """

    @property
    def char_height(self) -> int:
        """ Altura do GuiTabStrip em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiTabStrip na métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiTabStrip na métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiTabStrip na métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def left_tab(self) -> int:
        """ Esta é a guia mais à esquerda cuja legenda está visível.
        A propriedade leftTab pode ser alterada chamando o método ScrollToLeft de um GuiTab diferente,
        conforme descrito na seção Objeto GuiTab.
        """
        return self.component.LeftTab

    @property
    def selected_tab(self) -> int:
        """ A aba selecionada é aquela cujos descendentes estão visualizados no momento.
        A aba selecionada possui exatamente um filho, que é um GuiScrollContainer. Para selecionar uma guia, você chama o método
        Select da respectiva página da guia. Veja também a seção Objeto GuiTab.
        """
        return self.component.SelectedTab
