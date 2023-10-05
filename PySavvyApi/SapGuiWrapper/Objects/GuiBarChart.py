from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiBarChart(GuiShell):
    """ O GuiBarChart é uma ferramenta poderosa para exibir e modificar diagramas de escala de tempo.
    O objeto é de natureza muito técnica. Deve ser utilizado apenas para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    """

    def bar_count(self, chart_id: int) -> int:
        """ Retorna o número de barras no gráfico especificado.
        """
        return self.component.BarCount(chart_id)

    def get_bar_content(self, chart_id: int, bar_id: int, text_id: int) -> str:
        """ Retorna o conteúdo da barra especificada.
        """
        return self.component.GetBarContent(chart_id, bar_id, text_id)

    def get_grid_line_content(self, chart_id: int, grid_line_id: int, text_id: int) -> str:
        """ Retorna o conteúdo da linha de grade especificada.
        """
        return self.component.GetGridLineContent(chart_id, grid_line_id, text_id)

    def grid_count(self, chart_id: int) -> int:
        """ Retorna o número de grades dentro do gráfico especificado.
        """
        return self.component.GridCount(chart_id)

    def link_count(self, chart_id: int) -> int:
        """ Retorna o número de links dentro do gráfico especificado.
        """
        return self.component.LinkCount(chart_id)

    def send_data(self, dados: str) -> None:
        """ Envia dados para o servidor.
        """
        self.component.SendData(dados)

    @property
    def chart_count(self) -> int:
        """ Número de gráficos.
        """
        return self.component.ChartCount