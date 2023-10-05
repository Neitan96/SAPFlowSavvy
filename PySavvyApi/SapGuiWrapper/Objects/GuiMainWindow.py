from PySavvyApi.SapGuiWrapper.Objects.GuiFrameWindow import GuiFrameWindow


class GuiMainWindow(GuiFrameWindow):
    """ Esta janela representa a janela principal de uma sessão SAP GUI.
    """

    def resize_working_pane(self, width: int, height: int, throw_on_fail: bool) -> None:
        """ Redimensiona a janela para que a área de trabalho disponível tenha a largura e altura fornecidas em métrica de caracteres.
        throw_on_fail: O parâmetro throw_on_fail foi adicionado para uso no SAP GUI for Java, pois alguns gerenciadores de janelas podem não suportar um redimensionamento de janela controlado pelo programa.
        """
        self.component.ResizeWorkingPane(width, height, throw_on_fail)

    def resize_working_pane_ex(self, width: int, height: int, throw_on_fail: bool) -> None:
        """ Redimensiona a janela para que a área de trabalho disponível tenha a largura e altura fornecidas em píxeis.
        """
        self.component.ResizeWorkingPaneEx(width, height, throw_on_fail)

    @property
    def buttonbar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de botões da aplicação, a barra de ferramentas inferior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de botões da aplicação.
        """
        return self.component.ButtonbarVisible

    @buttonbar_visible.setter
    def buttonbar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de botões da aplicação, a barra de ferramentas inferior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de botões da aplicação.
        """
        self.component.ButtonbarVisible = visible

    @property
    def statusbar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de status na parte inferior da janela SAP GUI estiver visível.
        Configurar esta propriedade como False ocultará a barra de status.
        Quando a barra de status está oculta, as mensagens serão exibidas em uma janela pop-up.
        """
        return self.component.StatusbarVisible

    @statusbar_visible.setter
    def statusbar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de status na parte inferior da janela SAP GUI estiver visível.
        Configurar esta propriedade como False ocultará a barra de status.
        Quando a barra de status está oculta, as mensagens serão exibidas em uma janela pop-up.
        """
        self.component.StatusbarVisible = visible

    @property
    def titlebar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de título estiver visível.
        Configurar esta propriedade como False ocultará a barra de título.
        """
        return self.component.TitlebarVisible

    @titlebar_visible.setter
    def titlebar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de título estiver visível.
        Configurar esta propriedade como False ocultará a barra de título.
        """
        self.component.TitlebarVisible = visible

    @property
    def toolbar_visible(self) -> bool:
        """ Esta propriedade é True se a barra de ferramentas do sistema, a barra de ferramentas superior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de ferramentas do sistema.
        """
        return self.component.ToolbarVisible

    @toolbar_visible.setter
    def toolbar_visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se a barra de ferramentas do sistema, a barra de ferramentas superior dentro do SAP GUI, estiver visível.
        Configurar esta propriedade como False ocultará a barra de ferramentas do sistema.
        """
        self.component.ToolbarVisible = visible
