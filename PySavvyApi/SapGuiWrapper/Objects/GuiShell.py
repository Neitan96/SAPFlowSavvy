from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiContextMenu import GuiContextMenu
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection


class GuiShell(GuiVContainer):
    """ GuiShell é um objeto abstrato cuja interface é suportada por todos os controles.
    GuiShell estende o objeto GuiVContainer. O prefixo do tipo é shell, o nome é a última parte do id, shell[n].
    """

    def select_context_menu_item(self, function_code: str) -> None:
        """ Selecione um item no menu de contexto do controle.
        """
        return self.component.SelectContextMenuItem(function_code)

    def select_context_menu_item_by_position(self, position_desc: str) -> None:
        """ Este método permite selecionar um item do menu de contexto usando a posição do item.
        Portanto, é independente do texto do item de menu.
        """
        return self.component.SelectContextMenuItemByPosition(position_desc)

    def select_context_menu_item_by_text(self, text: str) -> None:
        """ Selecione um item de menu de um menu de contexto usando o texto do item e possíveis menus de nível superior.
        """
        return self.component.SelectContextMenuItemByText(text)

    @property
    def acc_description(self) -> str:
        """ Descrição de acessibilidade do shell. Esta descrição pode ser usada para shells que não possuem um elemento de título.
        """
        return self.component.AccDescription

    @property
    def current_context_menu(self) -> GuiContextMenu:
        """ Esta propriedade só é definida quando um menu de contexto está disponível no objeto shell.
        """
        return GuiContextMenu(self.component.CurrentContextMenu)

    @property
    def drag_drop_supported(self) -> bool:
        """ Esta propriedade é True se o shell permitir operações de arrastar e soltar.
        """
        return self.component.DragDropSupported

    @property
    def handle(self) -> int:
        """ O identificador de janela do controle que está conectado ao GuiShell.
        """
        return self.component.Handle

    @property
    def ocx_events(self) -> GuiCollection:
        """ Retorna uma coleção contendo os IDs de eventos do controle ActiveX. Estes são os eventos que o controle pode enviar ao servidor.
        """
        return GuiCollection(self.component.OcxEvents)

    @property
    def sub_type(self) -> str:
        """ Informações adicionais de tipo para identificar o controle representado pelo shell, por exemplo, Picture, TextEdit, GridView…
        """
        return self.component.SubType
