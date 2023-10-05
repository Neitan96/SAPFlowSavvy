from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiSplit(GuiShell):
    # TODO Criar descrição

    def get_col_size(self, id_column: int) -> int:
        """ Obtém o tamanho da coluna do divisor especificado.
        Id: O índice da coluna do divisor (começando com índice 1).
        Retorna o tamanho da coluna do divisor especificado em porcentagem.
        """
        return self.component.GetColSize(id_column)

    def get_row_size(self, id_row: int) -> int:
        """ Obtém o tamanho da linha do divisor especificado.
        Id: O índice da linha do divisor (começando com índice 1).
        Retorna o tamanho da linha do divisor especificado em porcentagem.
        """
        return self.component.GetRowSize(id_row)

    def set_col_size(self, id_column: int, size: int):
        """ Define o tamanho da coluna do divisor especificado.
        Id: O índice da coluna do divisor (começando com índice 1).
        Size: O tamanho desejado em porcentagem.
        """
        self.component.SetColSize(id_column, size)

    def set_row_size(self, id_row: int, size: int):
        """ Define o tamanho da linha do divisor especificado.
        Id: O índice da linha do divisor (começando com índice 1).
        Size: O tamanho desejado em porcentagem.
        """
        self.component.SetRowSize(id_row, size)

    @property
    def is_vertical(self) -> bool:
        """ Esta propriedade contém True se as células divisoras do GuiSplit estiverem alinhadas verticalmente e False se estiverem alinhadas horizontalmente.
        """
        return self.component.IsVertical