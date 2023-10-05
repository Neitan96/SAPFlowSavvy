from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent
from PySavvyApi.SapGuiWrapper.Objects.GuiComboBoxEntry import GuiComboBoxEntry
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection


class GuiComboBox(GuiVComponent):
    """ O GuiComboBox é um pouco semelhante ao GuiCTextField, mas tem uma implementação completamente diferente.
    Enquanto pressionar o botão da caixa de combinação de um GuiCTextField abrirá um novo dynpro ou controle no qual uma
    seleção pode ser feita, o GuiComboBox recupera todas as opções possíveis na inicialização do servidor, para que a
    seleção seja feita exclusivamente no cliente. GuiComboBox estende o objeto GuiVComponent. O prefixo do tipo é cmb,
    o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    def set_key_space(self) -> None:
        """ Esta função define a propriedade key da caixa de combinação para o caractere de espaço. Foi introduzido para eCATT.
        """
        self.component.SetKeySpace()

    @property
    def char_height(self) -> int:
        """ Altura do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiComboBox em métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def cur_list_box_entry(self) -> GuiComboBoxEntry:
        """ A entrada atualmente focada na lista suspensa.
        """
        return GuiComboBoxEntry(self.component.CurListBoxEntry)

    @property
    def entries(self) -> GuiCollection:
        """ Todos os membros desta coleção são do tipo GuiComboBoxEntry e têm apenas duas propriedades,
        chave e valor, ambas do tipo String. O key data pode ser exibido no SAP GUI configurando as
        opções 'Show keys... ' no diálogo de opções do SAP GUI.
        """
        return GuiCollection(self.component.Entries)

    @property
    def flushing(self) -> bool:
        """ Alguns componentes, como botões de rádio, caixas de seleção ou caixas de combinação,
        podem causar uma round trip quando seu valor é alterado. Se for o caso, a propriedade Flushing é Verdadeira.
        """
        return self.component.Flushing

    @property
    def highlighted(self) -> bool:
        """ Esta propriedade é Verdadeira se a flag Highlighted estiver definida no Screen Painter para a caixa de combinação.
        """
        return self.component.Highlighted

    @property
    def is_left_label(self) -> bool:
        """ Esta propriedade é Verdadeira se a caixa de combinação tiver a flag 'assign left'.
        """
        return self.component.IsLeftLabel

    @property
    def is_list_box_active(self) -> bool:
        """ Esta propriedade é Verdadeira se a lista suspensa da caixa de combinação estiver atualmente aberta.
        """
        return self.component.IsListBoxActive

    @property
    def is_right_label(self) -> bool:
        """ Esta propriedade é Verdadeira se a caixa de combinação tiver a flag 'assign right'.
        """
        return self.component.IsRightLabel

    @property
    def key(self) -> str:
        """ Esta é a chave do item atualmente selecionado. Você pode alterar este item definindo a propriedade Key para um novo valor.
        """
        return self.component.Key

    @key.setter
    def key(self, key: str = None) -> None:
        """ Esta é a chave do item atualmente selecionado. Você pode alterar este item definindo a propriedade Key para um novo valor.
        """
        self.component.Key = key

    @property
    def left_label(self) -> str:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo esquerdo da caixa de combinação.
        """
        return self.component.LeftLabel

    @property
    def required(self) -> bool:
        """ Se a flag Required estiver definida para uma caixa de combinação, a entrada vazia não poderá ser selecionada na lista.
        """
        return self.component.Required

    @property
    def right_label(self) -> GuiVComponent:
        """ Este rótulo foi definido no ABAP Screen Painter para ser o rótulo direito da caixa de combinação.
        """
        return GuiVComponent(self.component.RightLabel)

    @property
    def show_key(self) -> bool:
        """ Esta propriedade é Verdadeira se a caixa de combinação mostrar tanto as chaves
        quanto os valores (isso pode ser configurado definindo as opções 'Show keys... '
        no diálogo de opções do SAP GUI).
        """
        return self.component.ShowKey

    @property
    def value(self) -> str:
        """ Este é o valor do item atualmente selecionado. Você pode alterar este item definindo a propriedade Value para um novo valor.
        """
        return self.component.Value

    @value.setter
    def value(self, value: str = None) -> None:
        """ Este é o valor do item atualmente selecionado. Você pode alterar este item definindo a propriedade Value para um novo valor.
        """
        self.component.Value = value
