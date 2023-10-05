from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiMessageWindow(GuiVComponent):
    """ GuiMessageWindow é uma caixa de mensagem exibida pela mensagem showMessageBox do GuiUtils.
    """

    @property
    def focused_button(self) -> int:
        """ Índice baseado em zero do botão que atualmente tem foco (somente leitura).
        """
        return self.component.FocusedButton

    @property
    def help_button_help_text(self) -> str:
        """ Texto de ajuda do botão de ajuda (leitura/escrita).
        """
        return self.component.HelpButtonHelpText

    @help_button_help_text.setter
    def help_button_help_text(self, help_text: str = None) -> None:
        """ Texto de ajuda do botão de ajuda (leitura/escrita).
        """
        self.component.HelpButtonHelpText = help_text

    @property
    def help_button_text(self) -> str:
        """ Texto do botão de ajuda (leitura/escrita).
        """
        return self.component.HelpButtonText

    @help_button_text.setter
    def help_button_text(self, text: str = None) -> None:
        """ Texto do botão de ajuda (leitura/escrita).
        """
        self.component.HelpButtonText = text

    @property
    def message_text(self) -> str:
        """ Texto da mensagem (leitura/escrita).
        """
        return self.component.MessageText

    @message_text.setter
    def message_text(self, text: str = None) -> None:
        """ Texto da mensagem (leitura/escrita).
        """
        self.component.MessageText = text

    @property
    def message_type(self) -> int:
        """ Tipo de mensagem (leitura/escrita).
        """
        return self.component.MessageType

    @message_type.setter
    def message_type(self, message_type: int = None) -> None:
        """ Tipo de mensagem (leitura/escrita).
        """
        self.component.MessageType = message_type

    @property
    def ok_button_help_text(self) -> str:
        """ Texto de ajuda do botão OK (leitura/escrita).
        """
        return self.component.OKButtonHelpText

    @ok_button_help_text.setter
    def ok_button_help_text(self, help_text: str = None) -> None:
        """ Texto de ajuda do botão OK (leitura/escrita).
        """
        self.component.OKButtonHelpText = help_text

    @property
    def ok_button_text(self) -> str:
        """ Texto do botão OK (leitura/escrita).
        """
        return self.component.OKButtonText

    @ok_button_text.setter
    def ok_button_text(self, text: str = None) -> None:
        """ Texto do botão OK (leitura/escrita).
        """
        self.component.OKButtonText = text

    @property
    def visible(self) -> bool:
        """ Esta propriedade é True se o controle é visível, e False se estiver oculto (leitura/escrita).
        """
        return self.component.Visible

    @visible.setter
    def visible(self, visible: bool = None) -> None:
        """ Esta propriedade é True se o controle é visível, e False se estiver oculto (leitura/escrita).
        """
        self.component.Visible = visible
