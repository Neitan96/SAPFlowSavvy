from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiAbapEditor(GuiShell):
    """ O objeto GuiAbapEditor representa o novo controle do editor ABAP disponível a partir do SAP_BASIS release 6.20 (ver também SAP Note 930742).
    GuiAbapEditor estende GuiShell.
    """

    def auto_brace_enabled(self) -> bool:
        """ Retorna True se a função de autocolchetes estiver atualmente ativada. """
        return self.component.AutoBraceEnabled()

    def auto_complete(self):
        """ Invoca a caixa de lista de auto-completar. """
        self.component.AutoComplete()

    def auto_correct_enabled(self) -> bool:
        """ Retorna True se a função de correção automática estiver atualmente ativada. """
        return self.component.AutoCorrectEnabled()

    def auto_expand(self):
        """ Ativa o mecanismo de autoexpansão de modelos de código. """
        self.component.AutoExpand()

    def auto_indent_enabled(self) -> bool:
        """ Retorna True se a função de autoindentação estiver atualmente ativada. """
        return self.component.AutoIndentEnabled()

    def capitalize(self):
        """ Torna maiúscula a primeira letra alfabética de cada palavra no texto selecionado. Todas as outras letras são transformadas em minúsculas. """
        self.component.Capitalize()

    def clipboard_copy(self):
        """ Realiza uma operação de cópia para a área de transferência no texto atualmente selecionado. """
        self.component.ClipboardCopy()

    def clipboard_cut(self):
        """ Realiza uma operação de corte para a área de transferência no texto atualmente selecionado. """
        self.component.ClipboardCut()

    def clipboard_paste(self):
        """ Cole o conteúdo atual da área de transferência a partir da posição atual do cursor. """
        self.component.ClipboardPaste()

    def clipboard_ring_paste(self, index: int):
        """ Cole uma entrada do anel da área de transferência do editor no editor.
        Index: Índice com base em 1 da entrada da área de transferência conforme aparece no menu de contexto do editor ABAP.
        """
        self.component.ClipboardRingPaste(index)

    def code_hints_enabled(self) -> bool:
        """ Retorna True se as dicas de código estiverem atualmente ativadas. """
        return self.component.CodeHintsEnabled()

    def comment_selected_lines(self):
        """ Coloca as linhas selecionadas entre comentários. """
        self.component.CommentSelectedLines()

    def correct_caps_enabled(self) -> bool:
        """ Retorna True se a função de correção de maiúsculas estiver atualmente ativada. """
        return self.component.CorrectCapsEnabled()

    def delete(self):
        """ Exclui o caractere que segue a posição atual do cursor. Equivalente a pressionar a tecla <DEL>. """
        self.component.Delete()

    def delete_back(self):
        """ Move o cursor para a coluna anterior, excluindo o caractere atualmente presente lá. Equivalente a pressionar a tecla de retrocesso. """
        self.component.DeleteBack()

    def delete_range(self, line_start: int, column_start: int, line_end: int, column_end: int):
        """ Define uma região de texto para exclusão.
        LineStart: Especifica o número da linha a partir da qual a exclusão deve começar.
        ColumnStart: Especifica o número da coluna a partir da qual a exclusão deve começar.
        LineEnd: Especifica o número da linha onde a exclusão terminará.
        ColumnEnd: Especifica o número da coluna onde a exclusão terminará.
        """
        self.component.DeleteRange(line_start, column_start, line_end, column_end)

    def delete_selection(self) -> None:
        """ Exclui o texto atualmente selecionado.
        """
        self.component.DeleteSelection()

    def delete_word(self) -> None:
        """ Exclui a palavra que precede a posição atual do cursor.
        """
        self.component.DeleteWord()

    def delete_word_back(self) -> None:
        """ Exclui a palavra que precede a posição atual do cursor.
        """
        self.component.DeleteWordBack()

    def duplicate_line(self) -> None:
        """ Duplica o conteúdo da linha na qual o cursor está atualmente e insere uma cópia do conteúdo da linha abaixo do cursor.
        """
        self.component.DuplicateLine()

    def format_selected_lines(self) -> None:
        """ Formata as linhas selecionadas conforme as configurações de "Pretty Printer" e "Formatting", como Auto Indent e Smart Tab.
        """
        self.component.FormatSelectedLines()

    def get_auto_complete_entry_count(self) -> int:
        """ Retorna o número de entradas disponíveis exibidas na caixa de lista de auto-completar.
        """
        return self.component.GetAutoCompleteEntryCount()

    def get_auto_complete_entry_text(self, index: int) -> str:
        """ Retorna uma string representando a entrada na caixa de lista de autocompletar correspondente ao índice fornecido como parâmetro.
        """
        return self.component.GetAutoCompleteEntryText(index)

    def get_auto_complete_icon_type(self, index: int) -> int:
        """ Retorna o índice da imagem associada à entrada de autocompletar especificada no índice. Retorna -1 se nenhuma imagem estiver associada.
        """
        return self.component.GetAutoCompleteIconType(index)

    def get_auto_complete_sub_icon_type(self, index: int) -> int:
        """ Retorna o índice da subimagem associada à entrada de autocompletar especificada no índice. Retorna -1 se nenhuma subimagem estiver associada.
        """
        return self.component.GetAutoCompleteSubIconType(index)

    def get_auto_complete_toolbar_button_tool_tip(self, index: int) -> str:
        """ Retorna o texto de dica de ferramenta exibido pelo botão de barra de ferramentas de autocompletar especificado no índice.
        """
        return self.component.GetAutoCompleteToolbarButtonToolTip(index)

    def get_auto_complete_tool_tip_delay(self) -> int:
        """ Retorna o número de milissegundos que passam entre a realçar uma entrada na lista de autocompletar e a exibição da dica de ferramenta correspondente.
        """
        return self.component.GetAutoCompleteToolTipDelay()

    def get_current_tool_tip_text(self) -> str:
        """ Recupera o texto na dica de ferramenta atualmente exibida para dica de código ou lista de auto-completar. Múltiplas linhas são separadas por caracteres \n.
        """
        return self.component.GetCurrentToolTipText()

    def get_cursor_column_position(self) -> int:
        """ Retorna o número da coluna em que o cursor atualmente reside.
        """
        return self.component.GetCursorColumnPosition()

    def get_cursor_line_position(self) -> int:
        """ Retorna o número da linha em que o cursor atualmente reside.
        """
        return self.component.GetCursorLinePosition()

    def get_first_visible_line(self) -> int:
        """ Retorna o número da linha superior visível na sessão atual do editor.
        """
        return self.component.GetFirstVisibleLine()

    def get_html_clipboard_contents(self) -> str:
        """ Retorna uma string contendo o conteúdo atual da área de transferência no formato HTML. Retorna uma string vazia se a área de transferência não contiver nada no formato HTML.
        """
        return self.component.GetHTMLClipboardContents()

    def get_last_visible_line(self) -> int:
        """ Retorna o número da linha inferior visível na sessão atual do editor.
        """
        return self.component.GetLastVisibleLine()

    def get_line_count(self) -> int:
        """ Retorna o número total de linhas contidas no documento na sessão atual.
        """
        return self.component.GetLineCount()

    def get_line_text(self, line: int) -> str:
        """ Retorna uma string contendo o conteúdo da linha especificada pelo parâmetro Line.
        """
        return self.component.GetLineText(line)

    def get_numbered_bookmarks(self, line: int) -> object:
        """ Retorna uma coleção de números de marcadores atribuídos à linha especificada pelo parâmetro Line. O número do marcador pode variar de 0 a 9. Se nenhum marcador numerado estiver atribuído, a coleção estará vazia.
        """
        return self.component.GetNumberedBookmarks(line)

    def get_rtf_clipboard_contents(self) -> str:
        """ Retorna uma string contendo o conteúdo atual da área de transferência no formato Rich Text. Retorna uma string vazia se a área de transferência não contiver nada no formato Rich Text.
        """
        return self.component.GetRTFClipboardContents()

    def get_selected_auto_complete(self) -> int:
        """ Retorna o índice base zero da entrada atualmente selecionada na caixa de lista de autocompletar. O método retornará -1 se nenhuma entrada estiver selecionada.
        """
        return self.component.GetSelectedAutoComplete()

    def get_selected_text(self) -> str:
        """ Retorna uma string contendo o texto atualmente destacado ou selecionado na sessão do editor. Se o texto selecionado abranger mais de uma linha, quaisquer caracteres de terminador de linha serão incluídos na string retornada por este método.
        """
        return self.component.GetSelectedText()

    def get_structure_block_end_line(self, line: int) -> int:
        """ Retorna a linha final do bloco de estrutura relevante para a linha especificada pelo parâmetro Line. Se a linha não estiver dentro de um bloco de estrutura, o método retorna -1.
        """
        return self.component.GetStructureBlockEndLine(line)

    def get_structure_block_start_line(self, line: int) -> int:
        """ Retorna a linha inicial do bloco de estrutura relevante para a linha especificada pelo parâmetro Line. Se a linha estiver dentro de um bloco de estrutura aninhado, a linha inicial do bloco mais interno será retornada. Se a linha não estiver dentro de um bloco de estrutura, o método retorna -1.
        """
        return self.component.GetStructureBlockStartLine(line)

    def get_undo_position(self) -> int:
        """ Retorna a posição atual do documento no buffer de desfazer/refazer.
        """
        return self.component.GetUndoPosition()

    def get_word_wrap_mode(self) -> int:
        """ Retorna um número inteiro correspondente ao modo atual de quebra de linha:
        0 - Quebra de linha desativada.
        1 - Quebra na borda da janela.
        2 - Quebra pela largura da página.
        3 - Quebra pela largura da página inserindo quebra rígida.
        """
        return self.component.GetWordWrapMode()

    def get_word_wrap_position(self) -> int:
        """ Retorna a largura da página atualmente atribuída à quebra de linha. O número retornado é o número de colunas após o qual a quebra de linha será aplicada.
        """
        return self.component.GetWordWrapPosition()

    def go_next_book_mark(self) -> None:
        """ Navega até a linha onde o próximo marcador não numerado está definido.
        """
        self.component.GoNextBookMark()

    def go_numbered_bookmark(self, mark: int) -> None:
        """ Navega até a linha onde o marcador numerado Mark está localizado.
        """
        self.component.GoNumberedBookmark(mark)

    def go_previous_book_mark(self) -> None:
        """ Navega até a linha onde o marcador não numerado anterior está definido.
        """
        self.component.GoPreviousBookMark()

    def insert_tab(self) -> None:
        """ Insere uma TAB na posição atual do cursor. Equivalente a pressionar a tecla TAB.
        """
        self.component.InsertTab()

    def insert_text(self, text: str, line: int, column: int) -> None:
        """ Insere o texto especificado em Text na posição especificada em Line e Column como se o texto tivesse sido digitado no editor a partir do teclado.
        """
        self.component.InsertText(text, line, column)

    def is_auto_complete_entry_bold(self, index: int) -> bool:
        """ Retorna True se a entrada de auto-completar especificada no índice estiver em negrito.
        """
        return bool(self.component.IsAutoCompleteEntryBold(index))

    def is_auto_complete_open(self) -> bool:
        """ Retorna True se a caixa de lista de autocompletar estiver atualmente aberta.
        """
        return bool(self.component.IsAutoCompleteOpen())

    def is_auto_complete_toolbar_button_pressed(self, index: int) -> bool:
        """ Retorna True se o botão da barra de ferramentas de autocompletar especificado no índice estiver atualmente pressionado. Caso contrário, retorna False.
        """
        return bool(self.component.IsAutoCompleteToolbarButtonPressed(index))

    def is_auto_complete_tool_tip_visible(self) -> bool:
        """ Retorna True se a dica de ferramenta correspondente a uma entrada na caixa de lista de autocompletar estiver atualmente visível.
        """
        return bool(self.component.IsAutoCompleteToolTipVisible())

    def is_bookmark(self, line: int) -> bool:
        """ Retorna True se a linha estiver marcada com um marcador padrão que não é numerado. O método não fornece informações sobre se a linha está marcada com um marcador numerado.
        """
        return bool(self.component.IsBookmark(line))

    def is_breakpoint_set(self, line: int) -> bool:
        """ Retorna True se um ponto de interrupção estiver definido na linha especificada pelo parâmetro Line.
        """
        return bool(self.component.IsBreakpointSet(line))

    def is_line_collapsed(self, line: int) -> bool:
        """ Retorna True se o número da linha passado corresponder a uma linha que marca o início de um bloco colapsável que está atualmente no estado colapsado.
        """
        return bool(self.component.IsLineCollapsed(line))

    def is_line_comment(self, line: int) -> bool:
        """ Retorna True se a linha especificada em Line contiver comentários. Caso contrário, retorna False.
        """
        return bool(self.component.IsLineComment(line))

    def is_line_modified(self, line: int) -> bool:
        """ Retorna True se a linha foi modificada durante a sessão atual do editor.
        """
        return bool(self.component.IsLineModified(line))

    def is_modified(self) -> bool:
        """ Retorna True se alguma parte do documento atual foi modificada durante a sessão atual do editor.
        """
        return bool(self.component.IsModified())

    def join_selected_lines(self) -> None:
        """ Mescla as linhas de texto atualmente selecionadas em uma única linha de texto.
        """
        self.component.JoinSelectedLines()

    def lower_case(self) -> None:
        """ Força o texto selecionado a ficar em letras minúsculas.
        """
        self.component.LowerCase()

    def move_cursor_document_end(self) -> None:
        """ Posiciona o cursor na última coluna da última linha do documento.
        """
        self.component.MoveCursorDocumentEnd()

    def move_cursor_line_down(self) -> None:
        """ Move o cursor uma linha para baixo a partir de sua posição atual.
        """
        self.component.MoveCursorLineDown()

    def move_cursor_line_end(self) -> None:
        """ Posiciona o cursor na última coluna da linha atual.
        """
        self.component.MoveCursorLineEnd()

    def move_cursor_line_home(self) -> None:
        """ Posiciona o cursor na primeira coluna da linha atual.
        """
        self.component.MoveCursorLineHome()

    def move_cursor_line_up(self) -> None:
        """ Move o cursor uma linha para cima a partir de sua posição atual.
        """
        self.component.MoveCursorLineUp()

    def move_line_down(self) -> None:
        """ Move o conteúdo da linha em que o cursor está para a linha abaixo e move o conteúdo da linha abaixo do cursor para cima de uma linha.
        """
        self.component.MoveLineDown()

    def move_line_up(self) -> None:
        """ Move o conteúdo da linha em que o cursor está para a linha acima e move o conteúdo da linha acima do cursor para baixo de uma linha.
        """
        self.component.MoveLineUp()

    def move_word_left(self) -> None:
        """ Move o cursor para a coluna que precede a próxima palavra encontrada à esquerda da posição atual do cursor.
        """
        self.component.MoveWordLeft()

    def move_word_right(self) -> None:
        """ Move o cursor para a coluna que precede a próxima palavra encontrada à direita da posição atual do cursor.
        """
        self.component.MoveWordRight()

    def overwrite_mode_enabled(self) -> bool:
        """ Retorna True se o modo de substituição estiver habilitado, false se estiver no modo de inserção.
        """
        return bool(self.component.OverwriteModeEnabled())

    def remove_all_bookmarks(self) -> None:
        """ Remove todos os tipos de marcadores do documento. Tanto os marcadores numerados quanto os não numerados são removidos.
        """
        self.component.RemoveAllBookmarks()

    def remove_all_breakpoints(self) -> None:
        """ Remove todos os pontos de interrupção do documento atual.
        """
        self.component.RemoveAllBreakpoints()

    def remove_bookmarks(self, bookmarks: str) -> None:
        """ Remove todos os marcadores especificados na string fornecida.
        """
        self.component.RemoveBookmarks(bookmarks)

    def remove_breakpoint(self, line: int) -> None:
        """ Remove o ponto de interrupção na linha especificada pelo parâmetro Line.
        """
        self.component.RemoveBreakpoint(line)

    def replace_selection(self, text: str) -> None:
        """ Substitui o texto atualmente selecionado pelo texto contido no parâmetro Text.
        """
        self.component.ReplaceSelection(text)

    def save_to_file(self, file_path: str) -> None:
        """ Salva o documento atual em um arquivo no caminho especificado em p1.
        """
        self.component.SaveToFile(file_path)

    def scroll_to_line(self, line: int) -> None:
        """ Rolamento para a linha especificada pelo parâmetro Line, se ainda não estiver visível na tela.
        """
        self.component.ScrollToLine(line)

    def select_all(self) -> None:
        """ Realça todo o texto no documento atual para seleção.
        """
        self.component.SelectAll()

    def select_block_range(self, line_start: int, column_start: int, line_end: int, column_end: int) -> None:
        """ Realça uma região de texto no modo de bloco para seleção. Equivalente a pressionar a tecla ALT enquanto arrasta o mouse sobre o texto.
        LineStart especifica o número da linha a partir da qual a seleção deve começar.
        ColumnStart especifica o número da coluna a partir da qual a seleção deve começar.
        LineEnd especifica o número da linha onde a seleção terminará.
        ColumnEnd especifica o número da coluna onde a seleção terminará.
        """
        self.component.SelectBlockRange(line_start, column_start, line_end, column_end)

    def select_range(self, line_start: int, column_start: int, line_end: int, column_end: int) -> None:
        """ Realça uma região de texto para seleção.
        LineStart especifica o número da linha a partir da qual a seleção deve começar.
        ColumnStart especifica o número da coluna a partir da qual a seleção deve começar.
        LineEnd especifica o número da linha onde a seleção terminará.
        ColumnEnd especifica o número da coluna onde a seleção terminará.
        """
        self.component.SelectRange(line_start, column_start, line_end, column_end)

    def select_word_left(self) -> None:
        """ Seleciona a palavra à esquerda da posição atual do cursor.
        """
        self.component.SelectWordLeft()

    def select_word_right(self) -> None:
        """ Seleciona a palavra à direita da posição atual do cursor.
        """
        self.component.SelectWordRight()

    def sentencize(self) -> None:
        """ Torna maiúscula a primeira letra de cada sentença. As sentenças são delimitadas por caracteres ".". Todos os outros caracteres são transformados em minúsculas.
        """
        self.component.Sentencize()

    def set_auto_brace(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de autocompletar colchetes.
        """
        self.component.SetAutoBrace(status)

    def set_auto_correct(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de autocorreção automática.
        """
        self.component.SetAutoCorrect(status)

    def set_auto_indent(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de recuo automático.
        """
        self.component.SetAutoIndent(status)

    def set_bookmarks(self, bookmarks: str) -> None:
        """ Define marcadores.
        Aceita uma string no seguinte formato:
        <linha>[(<número>)][,<linha>] por exemplo, "10(1),22(2),33,42", <linha>={1,...,n}, <número>={1,...
        """
        self.component.SetBookmarks(bookmarks)

    def set_breakpoint(self, line: int) -> None:
        """ Define um ponto de interrupção na linha especificada pelo parâmetro Line.
        """
        self.component.SetBreakpoint(line)

    def set_code_hints(self, status: bool) -> None:
        """ Ativa ou desativa as dicas de código.
        """
        self.component.SetCodeHints(status)

    def set_correct_caps(self, status: bool) -> None:
        """ Ativa ou desativa a correção automática de maiúsculas.
        """
        self.component.SetCorrectCaps(status)

    def set_line_feed_style(self, style: int) -> None:
        """ Define o estilo de quebra de linha.
        """
        self.component.SetLineFeedStyle(style)

    def set_overwrite_mode(self, status: bool) -> None:
        """ Alterna entre os modos de Inserção e Sobrescrita. Se chamado com True, o modo de Sobrescrita é ativado. Caso contrário, o editor está no modo de Inserção.
        """
        self.component.SetOverwriteMode(status)

    def set_selection_pos_in_line(self, linha: int, coluna: int) -> None:
        """ Posiciona o cursor na linha <Linha> e coluna <Coluna>.
        """
        self.component.SetSelectionPosInLine(linha, coluna)

    def set_smart_tab(self, status: bool) -> None:
        """ Ativa ou desativa a funcionalidade de Smart Tab.
        """
        self.component.SetSmartTab(status)

    def set_word_wrap_mode(self, modo: int) -> None:
        """ Define o modo de quebra de linha conforme o número fornecido em Modo:
        0 - Quebra de linha desativada.
        1 - Quebrar na borda da janela.
        2 - Quebrar na largura da página.
        3 - Quebrar na largura da página inserindo quebra rígida.
        """
        self.component.SetWordWrapMode(modo)

    def set_word_wrap_position(self, pos: int) -> None:
        """ Pos especifica o número de colunas a serem exibidas antes da quebra de palavras ser aplicada.
        """
        self.component.SetWordWrapPosition(pos)

    def smart_tab_enabled(self) -> bool:
        """ Retorna True se a funcionalidade de Smart Tab estiver habilitada, false caso contrário.
        """
        return bool(self.component.SmartTabEnabled())

    def sort_selected_lines(self) -> None:
        """ Rearranja as linhas selecionadas em ordem alfanumérica.
        """
        self.component.SortSelectedLines()

    def swap_case(self) -> None:
        """ Inverte a configuração de maiúsculas/minúsculas para o texto selecionado. Os caracteres maiúsculos são trocados por minúsculos e vice-versa.
        """
        self.component.SwapCase()

    def toggle_caps_lock(self) -> None:
        """ Ativa ou desativa a tecla Caps Lock.
        """
        self.component.ToggleCapsLock()

    def toggle_numbered_bookmark(self, marcador: int, linha: int) -> None:
        """ Alterna o estado do marcador numerado <Marcador> na linha <Linha>. Se já existir um marcador com o número <Marcador> na linha, ele será removido. Caso contrário, ele será adicionado.
        """
        self.component.ToggleNumberedBookmark(marcador, linha)

    def toggle_structure_block(self, linha: int) -> None:
        """ Se o número da linha especificado em <Linha> for a primeira linha de um bloco de código recolhível, este método alternará o status expandido/recolhido do bloco.
        """
        self.component.ToggleStructureBlock(linha)

    def transpose_line(self) -> None:
        """ Troca o conteúdo da linha em que o cursor está atualmente com o conteúdo da linha acima da posição atual do cursor.
        """
        self.component.TransposeLine()

    def uncomment_selected_lines(self) -> None:
        """ Remove os comentários das linhas selecionadas.
        """
        self.component.UncommentSelectedLines()

    def undo(self, posicao_undo: int) -> None:
        """ Realiza um undo ou redo, dependendo de PosicaoUndo. PosicaoUndo especifica uma posição baseada em zero no buffer de undo/redo. Se -1 for passado, um único passo de undo será executado.
        """
        self.component.Undo(posicao_undo)

    def un_tab(self) -> None:
        """ Remove uma TAB na posição atual do cursor. Equivalente a pressionar <SHIFT> + <TAB>.
        """
        self.component.UnTab()

    def upper_case(self) -> None:
        """ Força o texto selecionado a ficar em maiúsculas.
        """
        self.component.UpperCase()
