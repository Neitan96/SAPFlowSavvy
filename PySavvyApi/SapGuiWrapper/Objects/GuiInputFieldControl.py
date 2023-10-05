from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiInputFieldControl(GuiShell):
    """ GuiInputFieldControl oferece um campo de entrada que pode ser usado dentro de
    contêineres de controle (ao contrário do elemento Dynpro representado por GuiTextField)
    """

    def submit(self):
        """ Submete a entrada para a aplicação.
        Esta função envia a entrada inserida para a aplicação.
        """
        self.component.Submit()

    @property
    def button_tooltip(self) -> str:
        """ Tooltip do botão de envio/consulta.
        """
        return self.component.ButtonTooltip

    @property
    def find_button_activated(self) -> bool:
        """ Esta propriedade é True quando o botão Find está ativo.
        """
        return self.component.FindButtonActivated

    @property
    def history_opened(self) -> bool:
        """ Esta propriedade é True quando o histórico de entrada está aberto.
        """
        return self.component.HistoryOpened

    @property
    def label_text(self) -> str:
        """ O texto do rótulo pertencente ao campo de entrada.
        """
        return self.component.LabelText

    @property
    def text(self) -> str:
        """ Conteúdo de texto do campo de entrada em si.
        """
        return self.component.Text

    @text.setter
    def text(self, new_text: str = None) -> None:
        """ Conteúdo de texto do campo de entrada em si.
        """
        self.component.Text = new_text