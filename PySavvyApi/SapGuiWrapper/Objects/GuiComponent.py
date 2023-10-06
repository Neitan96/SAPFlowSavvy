from __future__ import annotations
import win32com.client

from .ComponentCast import ComponentCast


class GuiComponent:
    """ GuiComponent é a classe base para a maioria das classes na API de script do SAP.
    """

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        self.class_attrs = ['component']
        self.component = component

    def __getattr__(self, attr):
        return getattr(self.component, attr)

    def __setattr__(self, attr, value):
        if attr in self.__dict__ or attr == 'class_attrs' or attr in self.class_attrs:
            super().__setattr__(attr, value)
        else:
            setattr(self.component, attr, value)

    @property
    def is_container_type(self) -> bool:
        """ Retorna True se o objeto é um container
        """
        return self.component.ContainerType

    @property
    def id(self) -> str:
        """ Um ID de objeto é um identificador textual exclusivo para o objeto.
        Isso é construído em uma formatação semelhante à URL, começando no GuiApplication
        e detalhando o respectivo objeto.
        """
        return self.component.Id

    @property
    def name(self) -> str:
        """ A propriedade name é especialmente útil ao trabalhar com scripts simples que acessam apenas campos de tela.
        Nesse caso um campo pode ser encontrado usando seu nome e informações de tipo,
        que é mais fácil de ler do que um ID possivelmente muito longo. No entanto,
        não há garantia de que não existam dois objetos com o mesmo nome.
        """
        return self.component.Name

    @property
    def parent(self) -> GuiComponent:
        """ O objeto pai acima na hierarquia de tempo de execução.
        Um objeto está sempre na coleção filhos de seu pai.
        """
        return ComponentCast.get_instance(self.component.Parent)

    @property
    def parent_cast(self) -> ComponentCast:
        """ Retorna o Parent pronto para fazer o Cast.
        """
        return ComponentCast(self.component.Parent)

    @property
    def type(self) -> str:
        """ Nome do tipo do objeto.
        As informações de tipo de GuiComponent podem ser usadas para determinar quais propriedades e métodos um objeto suporta.
        """
        return self.component.Type

    @property
    def type_as_number(self) -> int:
        """Embora a propriedade Type seja um valor de string,
        A propriedade TypeAsNumber é um valor numerico que pode ser usado alternativamente para identificar o tipo de um objeto.
        Foi adicionado para melhor desempenho em métodos como FindByIdEx.
        """
        return self.component.TypeAsNumber

    def cast_to(self) -> ComponentCast:
        """ Retorna a uma classe para fazer o cast do componente atual.
        """
        return ComponentCast(self.component)

    def connected_sap(self) -> bool:
        """ Verifica se o componente ainda está conectado ao SAP.
        """
        # noinspection PyBroadException
        try:
            # noinspection PyCallingNonCallable
            self.type_as_number()
            return True
        except:
            return False
