from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiCheckBox(GuiVComponent):
    """ GuiCheckBox representa uma CheckBox no SAP.
    O prefixo do tipo é chk, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Para mais informações consulte a documentação sobre o método GetListProperty dentro do GuiLabel Object.
        """
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Este método retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Consulte GuiLabel::GetListProperty para obter uma descrição dos atributos disponíveis.
        Em contraste com o método GetListProperty, GetListPropertyNonRec retornará apenas informações definidas para o elemento específico e
        ignorará as propriedades da lista definidas para elementos pais.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def color_index(self) -> int:
        """ Este número define o índice da cor da lista deste elemento.
        """
        return self.component.ColorIndex

    @property
    def color_intensified(self) -> bool:
        """ Esta propriedade será True se o sinalizador Intensificado estiver definido no Screen Painter para este elemento dynpro.
        """
        return self.component.ColorIntensified

    @property
    def color_inverse(self) -> bool:
        """ Esta propriedade será True se o estilo de cor inverso estiver definido no Screen Painter para o elemento.
        """
        return self.component.ColorInverse

    @property
    def flushing(self) -> bool:
        """ Alguns componentes, como botões de opção ou caixas de seleção, podem causar uma viagem de ida e
        volta quando seu valor for alterado. Se for esse o caso, a propriedade Flushing é True.
        """
        return self.component.Flushing

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver o sinalizador 'atribuir à esquerda'.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP e não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver o sinalizador 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def left_label(self) -> bool:
        """ Etiqueta esquerda do componente. O rótulo é atribuído no Screen Painter, usando o sinalizador 'assign left'.
        """
        return self.component.LeftLabel

    @property
    def right_label(self) -> bool:
        """ Etiqueta direita do componente.
        Esta propriedade é definida no Screen Painter usando o sinalizador 'assign right'.
        """
        return self.component.RightLabel

    @property
    def row_text(self) -> bool:
        """ Esta propriedade só está disponível em telas de lista ABAP.
        Ele retorna o texto da linha while que contém o componente atual.
        """
        return self.component.RowText

    @property
    def selected(self) -> bool:
        """ Assim como os botões de opção, marcar uma caixa de seleção pode
        causar comunicação com o servidor, dependendo da definição do ABAP Screen Painter.
        """
        return self.component.Selected

    @selected.setter
    def selected(self, option: bool) -> None:
        """ Assim como os botões de opção, marcar uma caixa de seleção pode
        causar comunicação com o servidor, dependendo da definição do ABAP Screen Painter.
        """
        self.component.Selected = option
