from typing import Optional

from .GuiVContainer import GuiVContainer
from .GuiComponent import GuiComponent
from .GuiContextMenu import GuiContextMenu
from .GuiScrollbar import GuiScrollbar
from .ComponentCast import ComponentCast


# noinspection PyBroadException
class GuiUserArea(GuiVContainer):
    """ A GuiUserArea compreende a área entre a barra de ferramentas e a barra de status para janelas do
    tipo GuiMainWindow e a área entre a barra de título e a barra de ferramentas para janelas modais,
    podendo também ser limitada por controles docker. Os elementos dynpro padrão podem ser encontrados apenas
    nesta área, com exceção dos botões, que também são encontrados nas barras de ferramentas.
    """

    def find_by_label(self, text: str, type_component: str, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Um método muito simples para encontrar um objeto é pesquisar especificando o texto do respectivo rótulo.
        """
        if on_raise: return ComponentCast.get_instance(self.component.FindByLabel(text, type_component))
        else:
            try: return ComponentCast.get_instance(self.component.FindByLabel(text, type_component))
            except: pass

        return None

    @property
    def current_context_menu(self) -> GuiContextMenu:
        """ Esta propriedade só é definida quando um menu de contexto está disponível no objeto shell.
        """
        return ComponentCast.get_instance(self.component.CurrentContextMenu)

    @property
    def horizontal_scrollbar(self) -> GuiScrollbar:
        """ A área do usuário é definida para ser rolável mesmo que as barras de rolagem nem sempre estejam visíveis.
        """
        return ComponentCast.get_instance(self.component.HorizontalScrollbar)

    @property
    def vertical_scrollbar(self) -> GuiScrollbar:
        """ A área do usuário é definida para ser rolável mesmo que as barras de rolagem nem sempre estejam visíveis.
        """
        return ComponentCast.get_instance(self.component.VerticalScrollbar)

    @property
    def is_otf_preview(self) -> bool:
        """ Esta propriedade é TRUE, caso seja exibido um Controle de Preview SAPScript na área do usuário.
        """
        return self.component.IsOTFPreview