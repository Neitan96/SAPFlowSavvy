from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiCalendar(GuiShell):
    """ O controle de calendário pode ser usado para selecionar datas ou períodos únicos.
    """

    def context_menu(self, ctx_menu_id: int, ctx_menu_cell_row: int, ctx_menu_cell_col: int, date_begin: str, date_end: str) -> None:
        """ Chama esta função para abrir um menu de contexto.

        O parâmetro CtxMenuId indica o tipo de célula na qual o menu de contexto foi aberto:
        Valor   Tipo de Célula  Descrição
        0       Data            Invocação em uma célula com uma única data
        1       Dia da Semana   Invocação em um botão para um determinado dia da semana
        2       Semana          Invocação em um botão para uma semana específica
        """
        self.component.ContextMenu(ctx_menu_id, ctx_menu_cell_row, ctx_menu_cell_col, date_begin, date_end)

    def create_date(self, day: int, month: int, year: int) -> str:
        """ Cria uma data no formato "YYYYMMDD" a partir dos parâmetros de dia, mês e ano.
        """
        return self.component.CreateDate(day, month, year)

    def get_color(self, from_color: str) -> int:
        """ Retorna a cor associada a partir do valor de cor especificado.
        """
        return self.component.GetColor(from_color)

    def get_color_info(self, color: int) -> str:
        """ Retorna a explicação definida pela aplicação para cores semânticas usadas no GuiCalendar (começando com índice 0).
        """
        return self.component.GetColorInfo(color)

    def get_date_tooltip(self, date: str) -> str:
        """ Retorna o texto de dica de ferramenta da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetDateTooltip(date)

    def get_day(self, date: str) -> int:
        """ Retorna o dia da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetDay(date)

    def get_month(self, date: str) -> int:
        """ Retorna o mês da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetMonth(date)

    def get_weekday(self, date: str) -> str:
        """ Retorna o dia da semana da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetWeekday(date)

    def get_week_number(self, date: str) -> int:
        """ Retorna o número da semana da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetWeekNumber(date)

    def get_year(self, date: str) -> int:
        """ Retorna o ano da data especificada no formato "YYYYMMDD".
        """
        return self.component.GetYear(date)

    def is_weekend(self, date: str) -> int:
        """ Retorna True se a data especificada pelo parâmetro estiver em um fim de semana.
        """
        return self.component.IsWeekend(date)

    def select_month(self, month: int, year: int) -> None:
        """ Seleciona o mês especificado pelos parâmetros (começando com índice 1).
        """
        self.component.SelectMonth(month, year)

    def select_range(self, from_date: str, to_date: str) -> None:
        """ Seleciona o intervalo especificado pelos parâmetros (no formato "YYYYMMDD").
        """
        self.component.SelectRange(from_date, to_date)

    def select_week(self, week: int, year: int) -> None:
        """ Seleciona a semana especificada pelos parâmetros (começando com índice 0).
        """
        self.component.SelectWeek(week, year)

    @property
    def end_selection(self) -> str:
        """ O último dia do intervalo de datas selecionado (no formato "YYYYMMDD").
        """
        return self.component.EndSelection

    @property
    def first_visible_date(self) -> str:
        """ Esta é a data mais antiga visível no controle de calendário.
        """
        return self.component.FirstVisibleDate

    @first_visible_date.setter
    def first_visible_date(self, date: str = None) -> None:
        """ Esta é a data mais antiga visível no controle de calendário.
        """
        self.component.FirstVisibleDate = date

    @property
    def focus_date(self) -> str:
        """ A data atualmente focada (identificada pela borda de foco) no controle de calendário está disponível no formato "YYYYMMDD".
        """
        return self.component.FocusDate

    @focus_date.setter
    def focus_date(self, date: str = None) -> None:
        """ A data atualmente focada (identificada pela borda de foco) no controle de calendário está disponível no formato "YYYYMMDD".
        """
        self.component.FocusDate = date

    @property
    def focused_element(self) -> int:
        """ Esta propriedade indica qual parte de um controle GuiCalendar composto atualmente tem o foco.
        Os valores possíveis são:
        0 - "InputField": O campo de entrada (seletor) para inserir manualmente uma data atualmente tem foco
        1 - "Button": O botão de pressão para abrir o painel de navegação atualmente tem foco
        2 - "Navigator": O painel de navegação pop-up está aberto e atualmente tem foco
        """
        return self.component.FocusedElement

    @property
    def horizontal(self) -> bool:
        """ Esta propriedade contém True se o GuiCalendar tiver orientação horizontal, caso contrário, contém False.
        """
        return self.component.Horizontal

    @property
    def last_visible_date(self) -> str:
        """ A última data que está atualmente sendo exibida pelo GuiCalendar (no formato "YYYYMMDD").
        """
        return self.component.LastVisibleDate

    @last_visible_date.setter
    def last_visible_date(self, date: str = None) -> None:
        """ A última data que está atualmente sendo exibida pelo GuiCalendar (no formato "YYYYMMDD").
        """
        self.component.LastVisibleDate = date

    @property
    def selection_interval(self) -> str:
        """ O intervalo é representado por duas strings de data concatenadas separadas por uma vírgula.
        """
        return self.component.SelectionInterval

    @selection_interval.setter
    def selection_interval(self, interval: str = None) -> None:
        """ O intervalo é representado por duas strings de data concatenadas separadas por uma vírgula.
        """
        self.component.SelectionInterval = interval

    @property
    def start_selection(self) -> str:
        """ O primeiro dia do intervalo de datas selecionado (no formato "YYYYMMDD").
        """
        return self.component.StartSelection

    @property
    def today(self) -> str:
        """ O dia atual (no formato "YYYYMMDD").
        """
        return self.component.Today