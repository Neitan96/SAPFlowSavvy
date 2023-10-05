from typing import Optional

from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent
from PySavvyApi.SapGuiWrapper.Objects.GuiComponent import GuiComponent
from PySavvyApi.SapGuiWrapper.Objects.GuiContainer import GuiContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiComponentCollection import GuiComponentCollection
from PySavvyApi.SapGuiWrapper.Helpers.ComponentCast import ComponentCast


# noinspection PyBroadException
class GuiVContainer(GuiVComponent, GuiContainer):
    """ Um objeto expõe a interface GuiVContainer se ela estiver visível e puder ter filhos.
    Exemplos dessa interface são janelas e subtelas, barras de ferramentas ou controles com filhos, como o controle divisor.
    GuiVContainer estende o objeto GuiContainer e o objeto GuiVComponent.
    """

    def find_all_by_name(self, name: str, type_component: str, on_raise: bool = True) -> Optional[GuiComponentCollection]:
        """ Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção quando FindAllByName ou FindAllByNameEx forem usados.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindAllByName(name, type_component))
        else:
            try:
                return ComponentCast.get_instance(self.component.FindAllByName(name, type_component))
            except:
                pass

        return None

    def find_all_by_name_ex(self, name: str, type_component: int, on_raise: bool = True) -> Optional[GuiComponentCollection]:
        """ Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção quando FindAllByName ou FindAllByNameEx forem usados.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindAllByNameEx(name, type_component))
        else:
            try:
                return ComponentCast.get_instance(self.component.FindAllByNameEx(name, type_component))
            except:
                pass

        return None

    def find_by_name(self, name: str, type_component: str, on_raise: bool = True) -> Optional[GuiComponent]:
        """ Ao contrário de FindById, esta função não garante um resultado único.
        Ele simplesmente retornará o primeiro descendente que corresponda aos parâmetros de nome e tipo.
        Esta é uma descrição mais natural do objeto do que o ID complexo, mas só faz sentido em objetos dynpro,
        pois a maioria dos outros objetos não tem um nome significativo. Se nenhum descendente com nome
        e tipo correspondentes for encontrado, a função gera uma exceção.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindByName(name, type_component))
        else:
            try:
                return ComponentCast.get_instance(self.component.FindByName(name, type_component))
            except:
                pass

        return None

    def find_by_name_ex(self, name: str, type_component: int, on_raise: bool = True) -> Optional[GuiComponentCollection]:
        """ Os métodos FindByName e FindByNameEx retornam apenas o primeiro objeto com nome e tipo correspondentes.
        No entanto, pode haver vários objetos correspondentes, que serão retornados como membros de uma coleção
        quando FindAllByName ou FindAllByNameEx forem usados.
        """
        if on_raise:
            return ComponentCast.get_instance(self.component.FindByNameEx(name, type_component))
        else:
            try:
                return ComponentCast.get_instance(self.component.FindByNameEx(name, type_component))
            except:
                pass

        return None