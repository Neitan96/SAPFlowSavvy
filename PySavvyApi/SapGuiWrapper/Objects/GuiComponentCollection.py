from __future__ import annotations

from typing import Optional

from .GuiComponent import GuiComponent
from .ComponentCast import ComponentCast

class GuiComponentCollection(GuiComponent):
    """ O GuiComponentCollection é usado para elementos de coleções, como a propriedade Children de contêineres.
    Cada elemento da coleção é uma extensão do GuiComponent.
    """

    def element_at(self, index: int, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.ElementAt(index))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.ElementAt(index))
            except:
                return None

    def item(self, index: int, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.Item(index))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast.get_instance(self.component.Item(index))
            except:
                return None

    def item_cast(self, index: int, on_raise: bool = True) -> Optional[ComponentCast]:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        O item será retornado em uma classe pronto para fazer o cast para o tipo do item desejado.
        Se nenhum membro puder ser encontrado para o índice fornecido e on_raise for True, a exceção Gui_Err_Enumerator_Index (614) será gerada.
        """
        if on_raise:
            return ComponentCast(self.component.Item(index))
        else:
            # noinspection PyBroadException
            try:
                return ComponentCast(self.component.Item(index))
            except:
                return None

    @property
    def count(self) -> int:
        """ O número de elementos na coleção.
        """
        return self.component.Count

    @property
    def length(self) -> int:
        """ O número de elementos na coleção.
        """
        return self.component.Length

    def to_list(self) -> list[GuiComponent]:
        """ Retorna uma lista com todos os itens da coleção.
        """
        itens = []
        for index in range(0, self.Count()):
            itens.append(self.item(index))
        return itens

    def last_item(self) -> GuiComponent:
        """ Retona o útimo item da coleção.
        """
        return self.element_at(self.count - 1)

    def last_item_cast(self) -> ComponentCast:
        """ Retona o útimo item da coleção em uma classe pronta para fazer o cast para o tipo do item desejado.
        """
        return self.item_cast(self.count - 1)