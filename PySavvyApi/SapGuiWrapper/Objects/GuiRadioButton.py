from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent

class GuiRadioButton(GuiVComponent):
    """ O prefixo do tipo é rad, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def select(self) -> None:
        """ Selecionar um botão de opção automaticamente desmarca todos os outros botões dentro do mesmo grupo.
        Isso pode causar uma viagem de ida e volta ao servidor, dependendo da definição do botão no screen painter.
        """
        self.component.Select()

    @property
    def char_height(self) -> int:
        """ Altura do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiRadioButton em métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def flushing(self) -> bool:
        """ Alguns componentes, como botões de rádio ou caixas de seleção, podem causar uma viagem de ida e volta quando seu valor é alterado. Se for o caso, a propriedade Flushing é True.
        """
        return self.component.Flushing

    @property
    def group_count(self) -> int:
        """ O número de botões de rádio no mesmo grupo ao qual o objeto atual pertence.
        """
        return self.component.GroupCount

    @property
    def group_members(self) -> object:
        """ A coleção de objetos GuiRadioButton pertencentes ao mesmo grupo de botões de rádio.
        """
        return self.component.GroupMembers

    @property
    def group_pos(self) -> int:
        """ A posição do botão de rádio no respectivo grupo de botões de rádio (vária de 1 a GroupCount).
        """
        return self.component.GroupPos

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign left'.
        """
        return self.component.IsLeftLabel

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é True se o componente tiver a flag 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def left_label(self) -> object:
        """ Rótulo esquerdo do GuiRadioButton. O rótulo é atribuído no Screen Painter, usando a flag 'assign left'.
        """
        return self.component.LeftLabel

    @property
    def right_label(self) -> object:
        """ Rótulo direito do GuiRadioButton. Esta propriedade é definida no Screen Painter usando a flag 'assign right'.
        """
        return self.component.RightLabel
