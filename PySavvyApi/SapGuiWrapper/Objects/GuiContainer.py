from __future__ import annotations

from PySavvyApi.SapGuiWrapper.Helpers.ComponentCast import ComponentCast
from PySavvyApi.SapGuiWrapper.Objects.GuiComponent import GuiComponent
from PySavvyApi.SapGuiWrapper.Objects.GuiComponentCollection import GuiComponentCollection


class GuiContainer(GuiComponent):
    """ Um objeto herda a interface GuiContainer se ela puder ter filhos.
    Exemplos desta interface são janelas e subtelas, barras de ferramentas ou controles com filhos, como o controle divisor.
    """

    def find_by_id(self, id_element: str, on_raise: bool = True) -> object | GuiComponent:
        """ Pesquise nos descendentes do objeto um determinado objeto que corresponde ao ID.
        Se nenhum descendente com o ID fornecido puder ser encontrado, a função gera uma exceção,
        a menos que o parâmetro opcional on_raise seja definido como False.
        """
        result = self.component.findById(id_element, on_raise)
        if result is not None: return ComponentCast.get_instance(result)
        return None

    def find_by_id_cast(self, id_element: str, on_raise: bool = True) -> None | ComponentCast:
        """ Pesquise nos descendentes do objeto um determinado objeto que corresponde ao ID.
        Se nenhum descendente com o ID fornecido puder ser encontrado, a função gera uma exceção,
        a menos que o parâmetro opcional on_raise seja definido como False.
        O Componente será retornado em uma classe de cast para fazer o hint no tipo desejado.
        """
        result = self.component.findById(id_element, on_raise)
        if result is not None: return ComponentCast(result)
        return None

    @property
    def children(self) -> GuiComponentCollection:
        """ Esta coleção contém todos os filhos diretos do objeto.
        """
        return GuiComponentCollection(self.component.Children)
