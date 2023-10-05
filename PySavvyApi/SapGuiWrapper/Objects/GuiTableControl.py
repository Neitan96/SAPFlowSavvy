from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiModalWindow import GuiModalWindow
from PySavvyApi.SapGuiWrapper.Objects.GuiTableRow import GuiTableRow
from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection
from PySavvyApi.SapGuiWrapper.Objects.GuiScrollbar import GuiScrollbar


class GuiTableControl(GuiVContainer):
    """ O controle table é um elemento dynpro padrão, em contraste com o GuiCtrlGridView, que é semelhante.
    O prefixo do tipo é tbl, o nome é o nome do campo retirado do dicionário de dados SAP.
    """
    # TODO Funções adicionais

    def configure_layout(self) -> GuiModalWindow:
        """ Na caixa de diálogo de configuração o layout da tabela pode ser alterado. Esta caixa de diálogo é uma GuiModalWindow.
        """
        return GuiModalWindow(self.component.ConfigureLayout())

    def deselect_all_columns(self) -> None:
        """ Esta função pode ser usada para controles de tabela com um botão que permite desmarcar todas as colunas em uma única etapa.
        """
        return self.component.DeselectAllColumns()

    def get_absolute_row(self, index: int) -> GuiTableRow:
        """ Ao contrário da coleção de linhas, a indexação suportada por esta função não redefine o índice após a rolagem,
        mas conta as linhas começando pela primeira linha em relação à primeira posição de rolagem.
        Se a linha selecionada não estiver visível no momento, uma exceção será gerada.
        """
        return GuiTableRow(self.component.GetAbsoluteRow(index))

    def get_cell(self, row: int, column: int) -> GuiVComponent:
        """ Este método retorna uma determinada célula da tabela.
        É mais eficiente do que acessar uma única célula usando coleções de linhas ou colunas.
        """
        return GuiVComponent(self.component.GetCell(row, column))

    def reorder_table(self, permutation: str) -> None:
        """ A permutação de parâmetros descreve uma nova ordem das colunas.
        Por exemplo, "1 3 2" moverá a coluna 3 para a segunda posição.
        """
        # TODO Melhorar a função usando o nome das colunas
        self.component.ReorderTable(permutation)

    def select_all_columns(self) -> None:
        """ Esta função pode ser usada para controles de tabela com um botão que permite selecionar todas as colunas em uma única etapa.
        """
        self.component.SelectAllColumns()

    @property
    def char_height(self) -> int:
        """ Altura do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharHeight

    @property
    def char_left(self) -> int:
        """ Coordenada esquerda do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharLeft

    @property
    def char_top(self) -> int:
        """ Coordenada superior do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharTop

    @property
    def char_width(self) -> int:
        """ Largura do GuiTableControl na métrica de caracteres.
        """
        return self.component.CharWidth

    @property
    def col_select_mode(self) -> int:
        """ Existem três modos diferentes para selecionar colunas ou linhas, definidos no tipo de enumeração GuiTableSelectionType.
        """
        return self.component.ColSelectMode

    @property
    def columns(self) -> GuiCollection:
        """ Os membros desta coleção são do tipo GuiTableColumn.
        Portanto, eles não suportam propriedades como id ou nome.
        """
        return GuiCollection(self.component.Columns)

    @property
    def current_col(self) -> int:
        """ Índice baseado em zero da coluna atual.
        """
        return self.component.CurrentCol

    @property
    def current_row(self) -> int:
        """ Índice baseado em zero da linha atual.
        """
        return self.component.CurrentRow

    @property
    def horizontal_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem horizontal do controle de tabela.
        """
        return GuiScrollbar(self.component.HorizontalScrollbar)

    @property
    def row_count(self) -> int:
        """ Número de linhas na tabela. Isso inclui linhas invisíveis. Para o número de linhas visíveis está disponível a propriedade VisibleRowCount.
        """
        return self.component.RowCount

    @property
    def rows(self) -> GuiCollection:
        """ Os membros desta coleção são do tipo GuiTableRow.
        A indexação começa com 0 para a primeira linha visível, independente da posição atual da barra de rolagem horizontal.
        Após a rolagem, uma linha diferente terá o índice 0.
        """
        return GuiCollection(self.component.Rows)

    @property
    def row_select_mode(self) -> int:
        """ Existem três modos diferentes para selecionar colunas ou linhas,
        definidos no tipo de enumeração GuiTableSelectionType.
        """
        return self.component.RowSelectMode

    @property
    def table_field_name(self) -> str:
        """ A propriedade name do controle de tabela contém o nome do programa ABAP além do nome do campo simples.
        Esta propriedade contém apenas o nome do campo.
        """
        return self.component.TableFieldName

    @property
    def vertical_scrollbar(self) -> GuiScrollbar:
        """ A barra de rolagem vertical do controle de tabela.
        """
        return GuiScrollbar(self.component.VerticalScrollbar)

    @property
    def visible_row_count(self) -> int:
        """ Número de linhas visíveis na tabela. Para o número de todas as linhas a propriedade RowCount está disponível.
        """
        return self.component.VisibleRowCount
