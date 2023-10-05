from __future__ import annotations
import win32com.client

class GuiCollection:
    """ GuiCollection é semelhante à coleção GuiComponentCollection, mas seus membros não são necessariamente extensões do objeto GuiComponent.
    Pode ser usado para passar uma coleção como parâmetro para funções de objetos programáveis.
    Um objeto desta classe é criado chamando a função CreateGuiCollection do objeto GuiApplication.
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

    def add(self, item):
        """ Após a criação de uma GuiCollection, os itens podem ser adicionados chamando a função add.
        """
        self.component.Add(item)

    def element_at(self, index) -> object:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Se nenhum membro puder ser encontrado para o index fornecido, uma exceção será gerada.
        """
        return self.component.ElementAt(index)

    def item(self, index) -> object:
        """ Esta função retorna o membro da coleção na posição index, onde o index pode variar de 0 a contagem-1.
        Foi adicionado para compatibilidade com coleções do Microsoft Visual Basic.
        Se nenhum membro puder ser encontrado para o index fornecido, uma exceção será gerada.
        """
        return self.component.Item(index)

    @property
    def count(self) -> int:
        """ O número de elementos na coleção. Esta propriedade foi adicionada para compatibilidade com coleções do Microsoft Visual Basic.
        """
        return self.component.Count

    @property
    def length(self) -> int:
        """ O número de elementos na coleção.
        """
        return self.component.Length

    def to_list(self) -> [object]:
        """ Retorna uma list com todos os itens da coleção.
        """
        itens = []
        for index in range(0, self.Count()):
            itens.append(self.Item(index))
        return itens

    def last_item(self) -> object:
        """ Retona o útimo item da coleção.
        """
        return self.ElementAt(self.Count() - 1)

    @property
    def type(self) -> str:
        """ As informações de tipo podem ser usadas para determinar quais propriedades e métodos um objeto suporta.
        O valor é o nome do tipo retirado desta documentação.
        O valor para GuiCollection é 'GuiCollection'.
        """
        return self.component.Type

    @property
    def type_as_number(self) -> int:
        """ Embora a propriedade Type seja um valor de string, a propriedade TypeAsNumber é um valor longo
        que pode ser usado alternativamente para identificar o tipo de um objeto.
        Foi adicionado para melhor desempenho em métodos como FindByIdEx.
        Os valores possíveis para esta propriedade são obtidos da enumeração GuiComponentType.
        """
        return self.component.TypeAsNumber
