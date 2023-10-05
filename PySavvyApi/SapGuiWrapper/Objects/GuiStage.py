from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiStage(GuiShell):
    """ Para o controle de palco apenas estão disponíveis membros básicos do GuiShell.
    A gravação e a reprodução não são possíveis.
    """

    def context_menu(self, str_id: str) -> None:
        """ Chamar esta função abre um menu de contexto.
        str_id: ID do menu de contexto.
        """
        self.component.ContextMenu(str_id)

    def double_click(self, str_id: str) -> None:
        """ Esta função emula um clique duplo do mouse.
        str_id: ID do elemento no qual ocorrerá o clique duplo.
        """
        self.component.DoubleClick(str_id)

    def select_items(self, str_items: str) -> None:
        """ Seleciona os itens especificados pelo parâmetro str_items.
        str_items: uma string contendo os itens a serem selecionados.
        """
        self.component.SelectItems(str_items)