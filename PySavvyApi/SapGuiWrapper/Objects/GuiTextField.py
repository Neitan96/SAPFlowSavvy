from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent

class GuiTextField(GuiVComponent):
    """ GuiTextField estende o objeto GuiVComponent. O prefixo do tipo é txt, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Retorna uma propriedade de lista específica.
        Para mais informações, consulte a documentação sobre o método GetListProperty no objeto GuiLabel.
        """
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Este método retorna informações compiladas no servidor para aprimorar as listas ABAP com informações de acessibilidade.
        Consulte GuiLabel::GetListProperty para uma descrição dos atributos disponíveis.
        Ao contrário do método GetListProperty, o GetListPropertyNonRec retornará apenas informações definidas para o elemento
        específico e ignorará propriedades de lista definidas para elementos pais.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def caret_position(self) -> int:
        """ A posição do cursor dentro de um campo de texto.
        """
        return self.component.CaretPosition

    @caret_position.setter
    def caret_position(self, caret_position: int = None) -> None:
        """ A posição do cursor dentro de um campo de texto.
        """
        self.component.CaretPosition = caret_position

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
    def history_cur_entry(self) -> str:
        """ Texto da entrada atualmente focada na lista de histórico.
        """
        return self.component.HistoryCurEntry

    @property
    def history_cur_index(self) -> int:
        """ Índice atualmente focado na lista suspensa de histórico.
        """
        return self.component.HistoryCurIndex

    @property
    def history_is_active(self) -> bool:
        """ Esta propriedade é True se o histórico local do campo de entrada estiver atualmente aberto.
        """
        return self.component.HistoryIsActive

    @property
    def history_list(self) -> object:
        """ Lista de entradas na caixa de histórico local.
        """
        return self.component.HistoryList

    @property
    def is_hotspot(self) -> bool:
        """ Elementos dynpro, como rótulos, podem ser configurados para causar uma ida e volta quando clicados. Nesse caso, o cursor do mouse muda para a forma de mão. Isso é chamado de hot spot.
        """
        return self.component.IsHotspot

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign left'.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_o_field(self) -> bool:
        """ OField é um elemento especial de dynpro ABAP, o Output Field. Esses campos podem ser definidos programaticamente com um valor em tempo de execução. Nesse aspecto, eles diferem dos rótulos. No entanto, eles não podem ser usados para inserir dados, portanto, não são campos de entrada.
        """
        return self.component.IsOField

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def left_label(self) -> object:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo esquerdo do controle.
        """
        return self.component.LeftLabel

    @property
    def max_length(self) -> int:
        """ O comprimento máximo do texto que pode ser escrito em um campo de texto é contado em unidades de código. Em clientes não Unicode, essas unidades são equivalentes a bytes.
        """
        return self.component.MaxLength

    @property
    def numerical(self) -> bool:
        """ Se esta flag estiver definida, apenas números e caracteres especiais podem ser escritos no campo de texto.
        """
        return self.component.Numerical

    @property
    def required(self) -> bool:
        """ Esta propriedade é True se o componente for um valor obrigatório para a tela.
        """
        return self.component.Required

    @property
    def right_label(self) -> object:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo direito do controle.
        """
        return self.component.RightLabel
