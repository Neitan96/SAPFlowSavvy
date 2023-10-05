from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection

class GuiGridView(GuiShell):
    """ A visualização em grade é semelhante ao controle de tabela dynpro, mas significativamente mais poderosa.
    """

    def clear_selection(self) -> None:
        """ Chamar ClearSelection remove todas as seleções de linhas, colunas e células.
        """
        self.component.ClearSelection()

    def click(self, row: int, column: str) -> None:
        """ Esta função emula um clique do mouse em uma determinada célula se os parâmetros forem válidos e gera uma exceção caso contrário.
        """
        self.component.Click(row, column)

    def click_current_cell(self) -> None:
        """ Esta função emula um clique do mouse na célula atual.
        """
        self.component.ClickCurrentCell()

    def context_menu(self) -> None:
        """ Chamar ContextMenu emula a solicitação do menu de contexto.
        """
        self.component.ContextMenu()

    def current_cell_moved(self) -> None:
        """ Esta função notifica o servidor de que uma célula diferente se tornou a célula atual.
        Deve ser chamado sempre que a célula atual for alterada.
        """
        self.component.CurrentCellMoved()

    def delete_rows(self, rows: str) -> None:
        """ As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        """
        # TODO Funções auxiliares
        self.component.DeleteRows(rows)

    def deselect_column(self, column: str) -> None:
        """ Esta função remove a coluna especificada da coleção de colunas selecionadas.
        """
        self.component.DeselectColumn(column)

    def double_click(self, row: int, column: str) -> None:
        """ Esta função emula um clique duplo do mouse em uma determinada célula se os parâmetros forem válidos e gera uma exceção caso contrário.
        """
        self.component.DoubleClick(row, column)

    def double_click_current_cell(self) -> None:
        """ Esta função emula um clique duplo do mouse na célula atual.
        """
        self.component.DoubleClickCurrentCell()

    def duplicate_rows(self, rows: str) -> None:
        """ As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        Para qualquer índice único, uma cópia da linha será inserida no índice fornecido.
        Se um intervalo de índices for duplicado, todas as novas linhas serão inseridas como um bloco, antes das linhas antigas.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        """
        # TODO Funções auxiliares
        self.component.DuplicateRows(rows)

    def get_cell_changeable(self, row: int, column: str) -> bool:
        """ Esta função retorna True se a célula especificada puder ser alterada.
        """
        return self.component.GetCellChangeable(row, column)

    def get_cell_check_box_checked(self, row: int, column: str) -> bool:
        """ Retorna True se a caixa de seleção na posição especificada estiver marcada.
        Lança uma exceção se não houver caixa de seleção na célula especificada.
        """
        return self.component.GetCellCheckBoxChecked(row, column)

    def get_cell_color(self, row: int, column: str) -> int:
        """ Retorna um identificador para a cor da célula.
        Isso pode ser usado para recuperar as informações de cores usando GetColorInfo.
        """
        return self.component.GetCellColor(row, column)

    def get_cell_height(self, row: int, column: str) -> int:
        """ Retorna a altura da célula em pixels.
		"""
        return self.component.GetCellHeight(row, column)

    def get_cell_icon(self, row: int, column: str) -> str:
        """ Retorna a sequência de ícones da célula, se a célula contiver um ícone.
        A string tem o formato de ícone ABAP '@xy@', onde xy é um número ou caractere.
        """
        return self.component.GetCellIcon(row, column)

    def get_cell_left(self, row: int, column: str) -> int:
        """ Retorna a posição esquerda da célula nas coordenadas do cliente.
		"""
        return self.component.GetCellLeft(row, column)

    def get_cell_max_length(self, row: int, column: str) -> int:
        """ Retorna o comprimento máximo da célula em número de bytes.
	    """
        return self.component.GetCellMaxLength(row, column)

    def get_cell_state(self, row: int, column: str) -> str:
        """ Retorna o estado da célula. Os valores possíveis são:
        Normal
        Error
        Warning
        Info
        """
        return self.component.GetCellState(row, column)

    def get_cell_tooltip(self, row: int, column: str) -> str:
        """ Retorna a dica de ferramenta da célula.
        """
        return self.component.GetCellTooltip(row, column)

    def get_cell_top(self, row: int, column: str) -> int:
        """ Retorna a posição superior da célula nas coordenadas do cliente.
		"""
        return self.component.GetCellTop(row, column)

    def get_cell_type(self, row: int, column: str) -> str:
        """ Esta função retorna o tipo da célula especificada. Os valores possíveis são:
        Normal
        Button
        Checkbox
        ValueList
        RadioButton
        """
        return self.component.GetCellType(row, column)

    def get_cell_value(self, row: int, column: str) -> str:
        """ Retorna o valor da célula como uma string.
        """
        return self.component.GetCellValue(row, column)

    def get_cell_width(self, row: int, column: str) -> int:
        """ Retorna a largura da célula em pixels.
        """
        return self.component.GetCellWidth(row, column)

    def get_color_info(self, color: int) -> str:
        """ Retorna a descrição da cor da célula.
        """
        return self.component.GetColorInfo(color)

    def get_column_data_type(self, column: str) -> str:
        """ Retorna o tipo de dados da coluna conforme os 'tipos de dados integrados' do padrão de esquema XML.
        """
        return self.component.GetColumnDataType(column)

    def get_column_position(self, column: str) -> int:
        """ Retorna a posição da coluna conforme mostrado na tela, começando em 1.
        """
        return self.component.GetColumnPosition(column)

    def get_column_sort_type(self, column: str) -> str:
        """ Retorna o tipo de classificação da coluna. Os valores possíveis são:
        None
        Ascending
        Descending
        """
        return self.component.GetColumnSortType(column)

    def get_column_titles(self, column: str) -> object:
        """ Esta função retorna uma coleção de strings usadas para exibir o título de uma coluna.
        O controle escolhe o título apropriado conforme a largura da coluna.
        """
        # TODO Verificar retorno
        return self.component.GetColumnTitles(column)

    def get_column_tooltip(self, column: str) -> str:
        """ A dica de ferramenta de uma coluna contém um texto projetado para ajudar o usuário a compreender o significado da coluna.
        """
        return self.component.GetColumnTooltip(column)

    def get_column_total_type(self, column: str) -> str:
        """ Retorna o tipo total da coluna. Os valores possíveis são:
        None
        Total
        Subtotal
        """
        return self.component.GetColumnTotalType(column)

    def get_displayed_column_title(self, column: str) -> str:
        """ Esta função retorna o título da coluna exibida atualmente.
        Este texto é um dos valores da coleção retornada da função "getColumnTitles".
        """
        return self.component.GetDisplayedColumnTitle(column)

    def get_row_total_level(self, row: int) -> int:
        """ Retorna o nível da linha.
        """
        return self.component.GetRowTotalLevel(row)

    def get_symbol_info(self, symbol: str) -> str:
        """ Retorna a descrição do símbolo na célula.
        """
        return self.component.GetSymbolInfo(symbol)

    def get_toolbar_button_checked(self, button_pos: int) -> bool:
        """ Retorna True se o botão estiver marcado (pressionado).
        """
        return self.component.GetToolbarButtonChecked(button_pos)

    def get_toolbar_button_enabled(self, button_pos: int) -> bool:
        """ Indica se o botão pode ser pressionado.
        """
        return self.component.GetToolbarButtonEnabled(button_pos)

    def get_toolbar_button_icon(self, button_pos: int) -> str:
        """ Retorna o nome do ícone do botão da barra de ferramentas especificado.
        """
        return self.component.GetToolbarButtonIcon(button_pos)

    def get_toolbar_button_id(self, button_pos: int) -> str:
        """ Retorna o ID do botão da barra de ferramentas especificado, conforme definido no dicionário de dados ABAP.
        """
        return self.component.GetToolbarButtonId(button_pos)

    def get_toolbar_button_text(self, button_pos: int) -> str:
        """ Retorna o texto do botão da barra de ferramentas especificado.
        """
        return self.component.GetToolbarButtonText(button_pos)

    def get_toolbar_button_tooltip(self, button_pos: int) -> str:
        """ Retorna a dica de ferramentas do botão da barra de ferramentas especificado.
        """
        return self.component.GetToolbarButtonTooltip(button_pos)

    def get_toolbar_button_type(self, button_pos: int) -> str:
        """ Retorna o tipo do botão da barra de ferramentas especificado. Os valores possíveis são:
        Button
        ButtonAndMenu
        Menu
        Separator
        Group
        CheckBox
        """
        return self.component.GetToolbarButtonType(button_pos)

    def get_toolbar_focus_button(self) -> int:
        """ Retorna a posição do botão da barra de ferramentas com o foco. Se nenhum botão na barra de ferramentas tiver o foco, o método retorna -1.
        """
        return self.component.GetToolbarFocusButton()

    def has_cell_f4_help(self, row: int, column: str) -> bool:
        """ Retorna True se a célula tiver um valor de ajuda.
        """
        return self.component.HasCellF4Help(row, column)

    def history_cur_entry(self, row: int, column: str) -> str:
        """ Retorna o texto da entrada selecionada atualmente da lista de histórico na célula especificada.
        """
        return self.component.HistoryCurEntry(row, column)

    def history_cur_index(self, row: int, column: str) -> int:
        """ Retorna o índice (base zero) da entrada selecionada atualmente na lista de histórico da célula especificada.
        """
        return self.component.HistoryCurIndex(row, column)

    def history_is_active(self, row: int, column: str) -> bool:
        """ Este método retorna True se a lista de histórico de entrada estiver aberta para a célula especificada.
        """
        return self.component.HistoryIsActive(row, column)

    def history_list(self, row: int, column: str) -> GuiCollection:
        """ Este método recupera a lista de entradas de histórico de entrada da célula GuiGridView especificada como uma GuiCollection.
        Os valores da lista de histórico dependem do valor atual contido na célula.
        """
        return GuiCollection(self.component.HistoryList(row, column))

    def insert_rows(self, rows: str) -> None:
        """ As linhas de parâmetro são uma sequência separada por vírgulas de índices ou intervalos de índices, por exemplo “3,5-8,14,15”.
        Para qualquer índice único, uma nova linha será adicionada no índice fornecido, movendo a linha antiga uma linha para baixo.
        Se um intervalo de índices for inserido, todas as novas linhas serão inseridas como um bloco, antes das linhas antigas.
        As entradas devem ser ordenadas e não sobrepostas, caso contrário será gerada uma exceção.
        """
        # TODO Funções auxiliares
        self.component.InsertRows(rows)

    def is_cell_hotspot(self, row: int, column: str) -> bool:
        """ Retorna True se a célula for um link.
        """
        return self.component.IsCellHotspot(row, column)

    def is_cell_symbol(self, row: int, column: str) -> bool:
        """ Retorna True se o texto na célula for exibido na fonte de símbolo SAP.
        """
        return self.component.IsCellSymbol(row, column)

    def is_cell_total_expander(self, row: int, column: str) -> bool:
        """ Retorna True se a célula contiver um botão de expansão total.
        """
        return self.component.IsCellTotalExpander(row, column)

    def is_column_filtered(self, column: str) -> bool:
        """ Retorna True se um filtro foi aplicado à coluna.
        """
        return self.component.IsColumnFiltered(column)

    def is_column_key(self, column: str) -> bool:
        """ Retorna True se a coluna estiver marcada como uma coluna de chave.
        """
        return self.component.IsColumnKey(column)

    def is_total_row_expanded(self, row: int) -> bool:
        """ Retorna True se a linha que contém um botão de expansão estiver atualmente expandida.
        """
        return self.component.IsTotalRowExpanded(row)

    def modify_cell(self, row: int, column: str, value: str) -> None:
        """ Se a linha e a coluna identificarem uma célula editável válida e o valor tiver um tipo válido para essa célula,
        o valor da célula será alterado. Caso contrário, uma exceção será gerada.
        """
        self.component.ModifyCell(row, column, value)

    def modify_check_box(self, row: int, column: str, checked: bool) -> None:
        """ Se a linha e a coluna identificarem uma célula editável válida contendo uma caixa de seleção e o valor tiver um tipo válido para essa célula,
        o valor da célula será alterado. Caso contrário, uma exceção será gerada.
        """
        self.component.ModifyCheckBox(row, column, checked)

    def move_rows(self, from_row: int, to_row: int, dest_row: int) -> None:
        """ As linhas com um índice maior ou igual a from_row até um índice menor, ou igual a to_row são movidas para a posição de dest_row.
        Passar valores de índice inválidos como parâmetros gera uma exceção.
        """
        self.component.MoveRows(from_row, to_row, dest_row)

    def press_button(self, row: int, column: str) -> None:
        """ Esta função emula o pressionamento de um botão colocado em uma célula específica.
        Ela gera uma exceção se a célula não contiver um botão ou se nem mesmo existir.
        """
        self.component.PressButton(row, column)

    def press_button_current_cell(self) -> None:
        """ Esta função emula o pressionamento de um botão colocado na célula atual.
        Ela gera uma exceção se a célula não contiver um botão.
        """
        self.component.PressButtonCurrentCell()

    def press_column_header(self, column: str) -> None:
        """ Esta função emula um clique do mouse no cabeçalho da coluna se o parâmetro identificar uma coluna válida.
        Caso contrário, gera uma exceção.
        """
        self.component.PressColumnHeader(column)

    def press_enter(self) -> None:
        """ Esta função emula a pressão da tecla Enter.
        """
        self.component.PressEnter()

    def press_f1(self) -> None:
        """ Esta função emula a pressão da tecla F1 enquanto o foco está na visualização da grade.
        """
        self.component.PressF1()

    def press_f4(self) -> None:
        """ Esta função emula a pressão da tecla F4.
        """
        self.component.PressF4()

    def press_toolbar_button(self, button_id: str) -> None:
        """ Esta função emula o clique em um botão na barra de ferramentas da visualização da grade.
        """
        self.component.PressToolbarButton(button_id)

    def press_toolbar_context_button(self, button_id: str) -> None:
        """ Esta função emula a abertura do menu de contexto na barra de ferramentas da visualização da grade.
        """
        self.component.PressToolbarContextButton(button_id)

    def press_total_row(self, row: int, column: str) -> None:
        """ Esta função emula a pressão do botão da linha total, que expande ou condensa as linhas agrupadas.
        """
        self.component.PressTotalRow(row, column)

    def press_total_row_current_cell(self) -> None:
        """ Esta função difere de PressTotalRow apenas no fato de tentar pressionar o botão de expansão na célula atual.
        """
        self.component.PressTotalRowCurrentCell()

    def select_all(self) -> None:
        """ Esta função seleciona todo o conteúdo da grade (ou seja, todas as linhas e todas as colunas).
        """
        self.component.SelectAll()

    def select_column(self, column: str) -> None:
        """ Esta função adiciona a coluna especificada à coleção das colunas selecionadas.
        """
        self.component.SelectColumn(column)

    def selection_changed(self) -> None:
        """ Esta função notifica o servidor que a seleção foi alterada.
        """
        self.component.SelectionChanged()

    def select_toolbar_menu_item(self, item_id: str) -> None:
        """ Esta função emula a seleção de um item no menu de contexto da barra de ferramentas da visualização da grade.
        """
        self.component.SelectToolbarMenuItem(item_id)

    def set_column_width(self, column: str, width: int) -> None:
        """ Esta função define a largura de uma coluna em caracteres.
        """
        self.component.SetColumnWidth(column, width)

    def set_current_cell(self, row: int, column: str) -> None:
        """ Se a linha e a coluna identificarem uma célula válida, essa célula se tornará a célula atual.
        """
        self.component.SetCurrentCell(row, column)

    def trigger_modified(self) -> None:
        """ Notifica o servidor sobre várias alterações nas células.
        """
        self.component.TriggerModified()

    @property
    def column_count(self) -> int:
        """ Esta propriedade representa o número de colunas no controle.
        """
        return self.component.ColumnCount

    @property
    def column_order(self) -> object:
        """ Esta coleção contém todos os identificadores de coluna na ordem em que estão atualmente exibidos.
        """
        # TODO Verificar retorno
        return self.component.ColumnOrder

    @column_order.setter
    def column_order(self, order: object = None) -> None:
        """ Esta coleção contém todos os identificadores de coluna na ordem em que estão atualmente exibidos.
        """
        # TODO Verificar retorno
        self.component.ColumnOrder = order

    @property
    def current_cell_column(self) -> str:
        """ A string que identifica uma coluna é o nome do campo definido no dicionário de dados do SAP.
        """
        return self.component.CurrentCellColumn

    @current_cell_column.setter
    def current_cell_column(self, column: str = None) -> None:
        """ A string que identifica uma coluna é o nome do campo definido no dicionário de dados do SAP.
        """
        self.component.CurrentCellColumn = column

    @property
    def current_cell_row(self) -> int:
        """ O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        """
        return self.component.CurrentCellRow

    @current_cell_row.setter
    def current_cell_row(self, row: int = None) -> None:
        """ O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        """
        self.component.CurrentCellRow = row

    @property
    def first_visible_column(self) -> str:
        """ Esta propriedade representa a primeira coluna visível da área de rolagem da visualização da grade.
        """
        return self.component.FirstVisibleColumn

    @first_visible_column.setter
    def first_visible_column(self, column: str = None) -> None:
        """ Esta propriedade representa a primeira coluna visível da área de rolagem da visualização da grade.
        """
        self.component.FirstVisibleColumn = column

    @property
    def first_visible_row(self) -> int:
        """ Este é o índice da primeira linha visível na grade.
        """
        return self.component.FirstVisibleRow

    @first_visible_row.setter
    def first_visible_row(self, row: int = None) -> None:
        """ Este é o índice da primeira linha visível na grade.
        """
        self.component.FirstVisibleRow = row

    @property
    def frozen_column_count(self) -> int:
        """ Esta propriedade representa o número de colunas excluídas da rolagem horizontal.
        """
        return self.component.FrozenColumnCount

    @property
    def row_count(self) -> int:
        """ Esta propriedade representa o número de linhas no controle.
        """
        return self.component.RowCount

    @property
    def selected_cells(self) -> object:
        """ A coleção de células selecionadas contém strings no formato "<índice da linha>,<identificador da coluna>", como "0,CARRID".
        """
        # TODO Verificar retorno
        return self.component.SelectedCells

    @selected_cells.setter
    def selected_cells(self, cells: object = None) -> None:
        """ A coleção de células selecionadas contém strings no formato "<índice da linha>,<identificador da coluna>", como "0,CARRID".
        """
        # TODO Verificar retorno
        self.component.SelectedCells = cells

    @property
    def selected_columns(self) -> object:
        """ As colunas selecionadas estão disponíveis como uma coleção de strings, assim como a string CurrentCellColumn.
        """
        # TODO Verificar retorno
        return self.component.SelectedColumns

    @selected_columns.setter
    def selected_columns(self, columns: object = None) -> None:
        """ As colunas selecionadas estão disponíveis como uma coleção de strings, assim como a string CurrentCellColumn.
        """
        # TODO Verificar retorno
        self.component.SelectedColumns = columns

    @property
    def selected_rows(self) -> str:
        """ A string é uma lista separada por vírgulas de números de índice de linha ou intervalos de índice, como "1,2,4-8,10".
        """
        return self.component.SelectedRows

    @selected_rows.setter
    def selected_rows(self, rows: str = None) -> None:
        """ A string é uma lista separada por vírgulas de números de índice de linha ou intervalos de índice, como "1,2,4-8,10".
        """
        self.component.SelectedRows = rows

    @property
    def selection_mode(self) -> str:
        """ Retorna o modo de seleção atual da grade.
        """
        return self.component.SelectionMode

    @property
    def title(self) -> str:
        """ Esta propriedade representa o título do controle da grade.
        """
        return self.component.Title

    @property
    def toolbar_button_count(self) -> int:
        """ O número de botões da barra de ferramentas, incluindo separadores.
        """
        return self.component.ToolbarButtonCount

    @property
    def visible_row_count(self) -> int:
        """ Recupera o número de linhas visíveis da grade.
        """
        return self.component.VisibleRowCount
