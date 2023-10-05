from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiLabel(GuiVComponent):
    """ GuiLabel representa uma etiqueta de texto.
    O prefixo do tipo é lbl, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Retorna propriedades de contêineres em geral.
        property: A propriedade que você deseja obter. Consulte a documentação para opções disponíveis.
        Retorna o valor da propriedade especificada.
        """
        # TODO Verificar documentação novamente e fazer funções auxiliares
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Veja GuiLabel::GetListProperty para uma descrição dos atributos disponíveis.
        Ao contrário do método GetListProperty, GetListPropertyNonRec só retornará informações definidas para o elemento específico
        e ignorará as propriedades definidas para elementos pais.
        property: A propriedade que você deseja obter. Consulte a documentação para opções disponíveis.
        Retorna o valor da propriedade especificada.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def caret_position(self) -> int:
        """ Definir a posição do cursor dentro de um rótulo é possível, mesmo que não seja visualizada como um cursor pelo SAP GUI.
        No entanto, a posição é transmitida para o servidor, para que a lógica da aplicação ABAP possa depender dessa posição.
        """
        return self.component.CaretPosition

    @caret_position.setter
    def caret_position(self, caret_position: int = None) -> None:
        """ Definir a posição do cursor dentro de um rótulo é possível, mesmo que não seja visualizada como um cursor pelo SAP GUI.
        No entanto, a posição é transmitida para o servidor, para que a lógica da aplicação ABAP possa depender dessa posição.
        """
        self.component.CaretPosition = caret_position

    @property
    def color_index(self) -> int:
        """ Este número define o índice da cor da lista deste elemento.
        """
        return self.component.ColorIndex

    @property
    def color_intensified(self) -> bool:
        """ Esta propriedade é True se a flag Intensified estiver definida no screen painter para este elemento dynpro.
        """
        return self.component.ColorIntensified

    @property
    def color_inverse(self) -> bool:
        """ Esta propriedade é True se o estilo de cor inversa estiver definido no screen painter para o elemento.
        """
        return self.component.ColorInverse

    @property
    def displayed_text(self) -> str:
        """ Esta propriedade contém o texto conforme exibido na tela, incluindo espaços em branco precedentes ou subsequentes.
        Esses espaços em branco são removidos da propriedade de texto.
        """
        return self.component.DisplayedText

    @property
    def highlighted(self) -> bool:
        """ Esta propriedade é True se a flag Highlighted estiver definida no screen painter para o elemento dynpro.
        """
        return self.component.Highlighted

    @property
    def is_hotspot(self) -> bool:
        """ Elementos dynpro, como rótulos, podem ser configurados para causar uma viagem de ida e volta quando clicados.
        Nesse caso, o cursor do mouse muda para a forma de mão. Isso é chamado de ponto de acesso.
        """
        return self.component.IsHotspot

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é definida se o rótulo foi atribuído como rótulo esquerdo de outro controle.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é definida se o rótulo foi atribuído como rótulo direito de outro controle.
        """
        return self.component.IsRightLabel

    @property
    def max_length(self) -> int:
        """ O comprimento máximo do texto de um rótulo é contado em unidades de código. Em clientes não Unicode, essas unidades são equivalentes a bytes.
        """
        return self.component.MaxLength

    @property
    def numerical(self) -> bool:
        """ Esta bandeira é True se o rótulo só puder conter números.
        """
        return self.component.Numerical

    @property
    def row_text(self) -> str:
        """ Esta propriedade está disponível apenas em telas de lista ABAP. Ela retorna o texto da linha inteira que contém o componente atual.
        """
        return self.component.RowText
