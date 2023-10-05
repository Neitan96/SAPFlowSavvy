from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiPicture(GuiShell):
    """ O controle de imagem exibe uma imagem em uma tela SAP GUI.
    """

    def click(self) -> None:
        """ Emula um clique único em uma imagem.
        """
        self.component.Click()

    def click_control_area(self, x: int, y: int) -> None:
        """ Emula um clique em uma posição específica. As coordenadas devem ser fornecidas em píxeis em relação ao controle da imagem conforme exibido na tela.
        """
        self.component.ClickControlArea(x, y)

    def click_picture_area(self, x: int, y: int) -> None:
        """ Emula um clique em uma posição específica. As coordenadas devem ser fornecidas em píxeis em relação ao arquivo de imagem original. Elas podem diferir das coordenadas em píxeis da imagem exibida devido ao dimensionamento.
        """
        self.component.ClickPictureArea(x, y)

    def context_menu(self, x: int, y: int) -> None:
        """ Abre um menu de contexto na posição especificada. As coordenadas devem ser fornecidas em píxeis em relação ao controle da imagem conforme exibido na tela.
        """
        self.component.ContextMenu(x, y)

    def double_click(self) -> None:
        """ Emula um clique duplo em uma imagem.
        """
        self.component.DoubleClick()

    def double_click_control_area(self, x: int, y: int) -> None:
        """ Emula um clique duplo em uma posição específica. As coordenadas devem ser fornecidas em píxeis
        em relação ao controle da imagem conforme exibido na tela.
        """
        self.component.DoubleClickControlArea(x, y)

    def double_click_picture_area(self, x: int, y: int) -> None:
        """ Emula um clique duplo em uma posição específica. As coordenadas devem ser fornecidas em píxeis em
        relação ao arquivo de imagem original. Elas podem diferir das coordenadas em píxeis da imagem exibida devido ao dimensionamento.
        """
        self.component.DoubleClickPictureArea(x, y)

    @property
    def alt_text(self) -> str:
        """ Esta propriedade contém o texto alternativo que pode ser atribuído a uma imagem (por exemplo, usado
        para pessoas com deficiência visual quando um leitor de tela é usado) (somente leitura).
        """
        return self.component.AltText

    @property
    def display_mode(self) -> str:
        """ Modo de exibição da imagem (somente leitura).
        Valores possíveis desta propriedade são:
        - "Normal": A imagem é mostrada em seu tamanho original. Se o tamanho da imagem for maior do que o tamanho do controle,
        o controle fornece barras de rolagem. Se o tamanho da imagem for menor do que o tamanho do controle, a imagem é mostrada
        no canto superior esquerdo do controle.
        - "Stretch": A imagem é redimensionada de forma que sempre ocupe a área completa do controle.
        - "Fit": A imagem é redimensionada de forma que ela se ajusta à área de controle sem a necessidade de mostrar barras de rolagem.
        Ao contrário de "Stretch", o modo "Fit" preserva a proporção de largura e altura da imagem.
        - "NormalCenter": semelhante a "Normal", exceto que a imagem não é mostrada no canto superior esquerdo, mas no centro do controle.
        - "FitCenter": semelhante a "Fit", exceto que a imagem não é mostrada no canto superior esquerdo, mas no centro do controle.
        """
        return self.component.DisplayMode

    @property
    def icon(self) -> str:
        """ Retorna o código de ícone SAPGUI (por exemplo, "@01@") do ícone exibido. Se nenhum ícone for exibido, a propriedade contém
        uma string vazia (somente leitura).
        """
        return self.component.Icon

    @property
    def url(self) -> str:
        """ Retorna a URL da imagem exibida. Se um ícone estiver sendo exibido (consulte a propriedade "icon"), a propriedade contém uma
        string vazia. Dependendo da aplicação que utiliza o controle, a URL pode conter partes temporárias da URL (por exemplo, UUIDs) (somente leitura).
        """
        return self.component.Url