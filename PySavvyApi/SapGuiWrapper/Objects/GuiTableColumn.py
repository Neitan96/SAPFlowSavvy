from .GuiComponentCollection import GuiComponentCollection


class GuiTableColumn(GuiComponentCollection):
    """ GuiTableColumn representa uma coluna em um controle de tabela.
    """

    @property
    def default_tooltip(self) -> str:
        """ Texto de dica de ferramenta gerado a partir do texto curto definido no dicionário de dados para determinado tipo de elemento de tela.
        """
        return self.component.DefaultTooltip

    @property
    def fixed(self) -> bool:
        """ Algumas colunas podem ser fixas, o que significa que não serão roladas com o restante das colunas.
        """
        return self.component.Fixed

    @property
    def icon_name(self) -> str:
        """ Se ao objeto foi atribuído um ícone, então esta propriedade é o nome do ícone, caso contrário, é uma string vazia.
        """
        return self.component.IconName

    @property
    def selected(self) -> bool:
        """ Esta propriedade é verdadeira se a coluna estiver selecionada.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, option: bool) -> None:
        """ Esta propriedade é verdadeira se a coluna estiver selecionada.
        """
        self.component.Selected = option

    @property
    def title(self) -> str:
        """ Esta é a legenda da coluna.
        """
        return self.component.Title

    @property
    def tooltip(self) -> str:
        """ A dica de ferramenta contém um texto projetado para ajudar o usuário a entender o significado de um determinado campo de texto ou botão.
        """
        return self.component.Tooltip