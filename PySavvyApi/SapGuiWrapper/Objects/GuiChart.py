from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiChart(GuiShell):
    """ O objeto GuiChart é de natureza muito técnica. Deve ser utilizado apenas para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    """

    def value_change(self, series: int, point: int, x_value: str, y_value: str, data_change: bool, id_container: str, z_value: str, change_flag: int):
        """
        Série: Número do conjunto de dados dentro da linha que deve ser alterado.
        point: Número do ponto de dados na linha que deve ser alterado.
        x_value: novo valor de x.
        y_value: novo valor de y.
        data_change: definir este parâmetro como True significa que o valor não foi alterado interativamente no gráfico,
            mas sim inserindo o novo valor na página de propriedades do DataPoint.
        id_container: ID do contêiner de dados GFW do ponto alterado. Pode ser usado em vez do par série/ponto.
        z_value: novo valor z.
        ChangeFlag: Notifica qual valor foi alterado ou se foi um valor de tempo.
            O valor é definido como uma matriz de bits, usando os 5 bits inferiores.
            1 x
            2 y
            4 x é o valor do tempo
            8 y é o valor do tempo
            16 z
            Se o novo valor for um momento específico, ele deverá ser definido usando uma string no formato mm/dd/aaaa hh:mm:ss.
        """
        self.component.ValueChange(series, point, x_value, y_value, data_change, id_container, z_value, change_flag)