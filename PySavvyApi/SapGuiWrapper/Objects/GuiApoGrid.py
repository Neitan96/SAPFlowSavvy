from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiApoGrid(GuiShell):
    """ Observações
    O GuiApoGrid é um objeto criado especificamente para aplicações SAP SCM.
    Ele implementa um quadro de planejamento, semelhante a um controle GuiGridView.

    As colunas e linhas são identificadas pela sua posição começando em zero:
    0 <= linha <Contagem de linhas
    0 <= coluna <Contagem de colunas
    Após uma busca detalhada, as linhas são renumeradas para que o número de qualquer linha possa mudar. A rolagem horizontal não afeta o número de uma coluna.
    """

    def cancel_cut(self) -> None:
        """ Aborta a operação de corte.
        """
        self.component.CancelCut()

    def clear_selection(self) -> None:
        """ Chamar clearSelection remove todas as seleções de linhas, colunas e células.
        """
        self.component.ClearSelection()

    def context_menu(self, coluna: int, linha: int) -> None:
        """ Chamar contextMenu emula a solicitação de menu de contexto.
        """
        self.component.ContextMenu(coluna, linha)

    def cut(self) -> None:
        """ Corta as células selecionadas.
        """
        self.component.Cut()

    def deselect_cell(self, coluna: int, linha: int) -> None:
        """ Deseleciona as células especificadas. Esta função remove as células especificadas da coleção de células selecionadas.
        """
        self.component.DeselectCell(coluna, linha)

    def deselect_column(self, coluna: int) -> None:
        """ Esta função remove a coluna especificada da coleção de colunas selecionadas.
        """
        self.component.DeselectColumn(coluna)

    def deselect_row(self, linha: int) -> None:
        """ Esta função remove a linha especificada da coleção de linhas selecionadas.
        """
        self.component.DeselectRow(linha)

    def double_click_cell(self, coluna: int, linha: int) -> None:
        """ Esta função emula um duplo clique do mouse em uma célula específica se os parâmetros forem válidos e gera uma exceção caso contrário.
        """
        self.component.DoubleClickCell(coluna, linha)

    def get_bgd_color_info(self, linha: int, coluna: int) -> str:
        """ Esta função retorna a cor de fundo da célula especificada.
        """
        return self.component.GetBgdColorInfo(linha, coluna)

    def get_cell_changeable(self, coluna: int, linha: int) -> bool:
        """ Esta função retorna True se a célula especificada for editável.
        """
        return self.component.GetCellChangeable(coluna, linha)

    def get_cell_format(self, coluna: int, linha: int) -> str:
        """ Retorna o formato da célula especificada.
        """
        return self.component.GetCellFormat(coluna, linha)

    def get_cell_tooltip(self, coluna: int, linha: int) -> str:
        """ Esta função retorna a dica de ferramenta da célula especificada.
        """
        return self.component.GetCellTooltip(coluna, linha)

    def get_cell_value(self, coluna: int, linha: int) -> str:
        """ Esta função retorna o valor da célula especificada como uma string.
        """
        return self.component.GetCellValue(coluna, linha)

    def get_fgd_color_info(self, linha: int, coluna: int) -> str:
        """ Esta função retorna a cor da fonte da célula especificada.
        """
        return self.component.GetFgdColorInfo(linha, coluna)

    def get_icon_info(self, linha: int, coluna: int) -> str:
        """ Retorna informações do ícone da célula especificada.
        """
        return self.component.GetIconInfo(linha, coluna)

    def is_cell_selected(self, coluna: int, linha: int) -> bool:
        """ Retorna True se a célula especificada estiver selecionada.
        """
        return self.component.IsCellSelected(coluna, linha)

    def is_col_selected(self, coluna: int) -> bool:
        """ Retorna True se a coluna especificada estiver selecionada.
        """
        return bool(self.component.IsColSelected(coluna))

    def is_row_selected(self, linha: int) -> bool:
        """ Retorna True se a linha especificada estiver selecionada.
        """
        return bool(self.component.IsRowSelected(linha))

    def paste(self, valores_celula: object, num_colunas: int) -> int:
        """ Aciona uma operação de colar.
        """
        return self.component.Paste(valores_celula, num_colunas)

    def press_enter(self) -> None:
        """ Emula a pressão da tecla Enter.
        """
        self.component.PressEnter()

    def select_all(self) -> None:
        """ Esta função seleciona todo o conteúdo da grade (ou seja, todas as linhas e colunas).
        """
        self.component.SelectAll()

    def select_cell(self, coluna: int, linha: int) -> None:
        """ Seleciona a célula especificada.
        """
        self.component.SelectCell(coluna, linha)

    def select_column(self, coluna: int) -> None:
        """ Seleciona a coluna especificada.
        """
        self.component.SelectColumn(coluna)

    def select_row(self, linha: int) -> None:
        """ Seleciona a linha especificada.
        """
        self.component.SelectRow(linha)

    def set_cell_value(self, coluna: int, linha: int, valor: str) -> str:
        """ Esta função insere o valor especificado na célula especificada.
        """
        return self.component.SetCellValue(coluna, linha, valor)

    @property
    def column_count(self) -> int:
        """ Esta propriedade representa o número de colunas no controle.
        """
        return self.component.ColumnCount

    @property
    def current_cell_column(self) -> int:
        """ O índice da coluna que contém a célula atual.
        """
        return self.component.CurrentCellColumn

    @property
    def current_cell_row(self) -> int:
        """ O índice da linha atual varia de 0 ao número de linhas menos 1, com -1 sendo o índice da linha do título.
        """
        return self.component.CurrentCellRow

    @property
    def first_visible_column(self) -> int:
        """ Esta propriedade representa a primeira coluna visível da área rolável do controle APOGrid.
        """
        return self.component.FirstVisibleColumn

    @property
    def first_visible_row(self) -> int:
        """ Este é o índice da primeira linha visível na grade. Definir esta propriedade para um índice de linha inválido gerará uma exceção.
        """
        return self.component.FirstVisibleRow

    @property
    def fixed_columns_left(self) -> int:
        """ O número de colunas fixas no lado esquerdo da grade.
        """
        return self.component.FixedColumnsLeft

    @property
    def fixed_columns_right(self) -> int:
        """ O número de colunas fixas no lado direito da grade.
        """
        return self.component.FixedColumnsRight

    @property
    def fixed_rows_bottom(self) -> int:
        """ O número de linhas fixas na parte inferior da grade.
        """
        return self.component.FixedRowsBottom

    @property
    def fixed_rows_top(self) -> int:
        """ O número de linhas fixas na parte superior da grade.
        """
        return self.component.FixedRowsTop

    @property
    def row_count(self) -> int:
        """ Esta propriedade representa o número de linhas no controle.
        """
        return self.component.RowCount

    @property
    def selected_cells(self) -> object:
        """ A coleção de células selecionadas. Tentar definir esta propriedade como um valor inválido gerará uma exceção.
        """
        return self.component.SelectedCells

    @property
    def selected_columns(self) -> str:
        """ As colunas selecionadas estão disponíveis como uma coleção. Configurar esta propriedade pode gerar uma exceção se a nova coleção contiver uma coluna inválida.
        """
        return self.component.SelectedColumns

    @property
    def selected_columns_object(self) -> object:
        """ Retorna a coleção de colunas selecionadas como um objeto.
        """
        return self.component.SelectedColumnsObject

    @property
    def selected_rows(self) -> str:
        """ As linhas selecionadas estão disponíveis como uma coleção. Configurar esta propriedade pode gerar uma exceção se a nova coleção contiver uma linha inválida.
        """
        return self.component.SelectedRows

    @property
    def selected_rows_object(self) -> object:
        """ Retorna a coleção de linhas selecionadas como um objeto.
        """
        return self.component.SelectedRowsObject

    @property
    def visible_column_count(self) -> int:
        """ Recupera o número de colunas visíveis da grade.
        """
        return self.component.VisibleColumnCount

    @property
    def visible_row_count(self) -> int:
        """ Recupera o número de linhas visíveis da grade.
        """
        return self.component.VisibleRowCount
