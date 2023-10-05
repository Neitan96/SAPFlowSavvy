from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiTextedit(GuiShell):
    """ O controle TextEdit é um controle de edição multilinha que oferece vários benefícios possíveis.
    No que diz respeito aos scripts, a possibilidade de proteger partes do texto contra edição pelo usuário
    é especialmente útil. GuiTextedit estende o objeto GuiShell.
    """

    def context_menu(self) -> None:
        """ Chamar ContextMenu emula a solicitação de menu de contexto.
        """
        self.component.ContextMenu()

    def double_click(self) -> None:
        """ Esta função emula um clique duplo do mouse.
        Para definir a seleção, a função setSelectionIndexes pode ser chamada antecipadamente.
        """
        self.component.DoubleClick()

    def get_line_text(self, n_line: int) -> str:
        """ Retorna o texto da linha especificada.
        """
        return self.component.GetLineText(n_line)

    def get_unprotected_text_part(self, part: int) -> str:
        """ Esta função recupera o conteúdo de uma parte de texto desprotegida usando o índice baseado em zero, part.
        """
        return self.component.GetUnprotectedTextPart(part)

    def is_breakpoint_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada contiver um ponto de interrupção.
        """
        return self.component.IsBreakpointLine(n_line)

    def is_comment_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada for uma linha de comentário.
        """
        return self.component.IsCommentLine(n_line)

    def is_highlighted_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada estiver destacada.
        """
        return self.component.IsHighlightedLine(n_line)

    def is_protected_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada estiver protegida.
        """
        return self.component.IsProtectedLine(n_line)

    def is_selected_line(self, n_line: int) -> int:
        """ Retorna VERDADEIRO se a linha especificada estiver selecionada.
        """
        return self.component.IsSelectedLine(n_line)

    def modified_status_changed(self, status: int) -> None:
        """ Esta função emula a alteração do status modificado.
        """
        self.component.ModifiedStatusChanged(status)

    def multiple_files_dropped(self, files: list) -> None:
        """ Emula uma operação de arrastar e soltar, na qual vários arquivos são soltos no controle de texto.
        A lista contém, para cada arquivo, o nome completo do arquivo como uma string.
        """
        self.component.MultipleFilesDropped(files)

    def press_f1(self) -> None:
        """ Esta função emula a pressão da tecla F1 no teclado.
        """
        self.component.PressF1()

    def press_f4(self) -> None:
        """ Esta função emula a pressão da tecla F4 no teclado.
        """
        self.component.PressF4()

    def set_selection_indexes(self, start: int, end: int) -> None:
        """ Esta função define a faixa de texto visualmente selecionada. start e end são índices absolutos de caracteres baseados em zero.
        start corresponde à posição onde a seleção começa e end é a posição do primeiro caractere após a seleção.
        Observe que definir start igual a end resulta na definição do cursor nessa posição.
        """
        self.component.SetSelectionIndexes(start, end)

    def set_unprotected_text_part(self, part: int, text: str) -> int:
        """ Esta função atribui o conteúdo do texto à parte de texto desprotegida com índice baseado em zero, part.
        A função retorna True se foi possível realizar a atribuição. Caso contrário, retorna False.
        """
        return self.component.SetUnprotectedTextPart(part, text)

    def single_file_dropped(self, filename: str) -> None:
        """ Esta função emula a queda de um único arquivo com o caminho do diretório fileName.
        """
        self.component.SingleFileDropped(filename)

    @property
    def current_column(self) -> int:
        """ O número da coluna na qual o cursor de texto está atualmente posicionado.
        """
        return self.component.CurrentColumn

    @property
    def current_line(self) -> int:
        """ O número da linha na qual o cursor de texto está atualmente posicionado.
        """
        return self.component.CurrentLine

    @property
    def first_visible_line(self) -> int:
        """ A primeira linha visível é visualizada na borda superior do controle.
        """
        return self.component.FirstVisibleLine

    @first_visible_line.setter
    def first_visible_line(self, line_number: int = None) -> None:
        """ A primeira linha visível é visualizada na borda superior do controle.
        """
        self.component.FirstVisibleLine = line_number

    @property
    def last_visible_line(self) -> int:
        """ O número da última linha que está atualmente visível.
        """
        return self.component.LastVisibleLine

    @property
    def line_count(self) -> int:
        """ O número de todas as linhas no documento atual.
        """
        return self.component.LineCount

    @property
    def number_of_unprotected_text_parts(self) -> int:
        """ O número de partes de texto não protegidas, que estão contidas.
        """
        return self.component.NumberOfUnprotectedTextParts

    @property
    def selected_text(self) -> str:
        """ O texto atualmente selecionado.
        """
        return self.component.SelectedText

    @property
    def selection_end_column(self) -> int:
        """ O número da coluna na qual a seleção atual termina.
        """
        return self.component.SelectionEndColumn

    @property
    def selection_end_line(self) -> int:
        """ O número da linha na qual a seleção atual termina.
        """
        return self.component.SelectionEndLine

    @property
    def selection_index_end(self) -> int:
        """ Recupera o índice de caractere absoluto, baseado em zero, do ponto final da faixa de texto visualmente selecionada, ou seja, a posição onde a seleção termina.
        """
        return self.component.SelectionIndexEnd

    @property
    def selection_index_start(self) -> int:
        """ Recupera o índice de caractere absoluto, baseado em zero, do ponto de partida da faixa de texto visualmente selecionada, ou seja, a posição onde a seleção começa.
        """
        return self.component.SelectionIndexStart

    @property
    def selection_start_column(self) -> int:
        """ O número da coluna na qual a seleção atual começa.
        """
        return self.component.SelectionStartColumn

    @property
    def selection_start_line(self) -> int:
        """ O número da linha na qual a seleção atual começa.
        """
        return self.component.SelectionStartLine
