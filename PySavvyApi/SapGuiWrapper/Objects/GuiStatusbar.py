from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiStatusbar(GuiVComponent):
    """ GuiStatusbar representa a mensagem que exibe parte da barra de status na parte inferior da janela SAP GUI.
    Ele não inclui as informações do sistema e de login exibidas na área mais à direita da barra de status,
    pois estão disponíveis no objeto GuiSessionInfo. GuiStatusbar estende o objeto GuiVComponent. O prefixo do tipo é sbar.
    """

    def double_click(self) -> None:
        self.component.DoubleClick()

    @property
    def handle(self) -> int:
        """ O identificador de janela do controle que está conectado ao GuiShell.
        """
        return self.component.Handle

    @property
    def message_as_popup(self) -> bool:
        """ Algumas mensagens podem ser exibidas não apenas na barra de status, mas também como uma janela pop-up.
        Nesses casos, esta propriedade é definida como True para que um script saiba que precisa fechar um pop-up para continuar.
        """
        return self.component.MessageAsPopup

    @property
    def message_id(self) -> str:
        """ Este é o nome da classe de mensagem usada na chamada de mensagem ABAP.
        """
        return self.component.MessageId

    @property
    def message_number(self) -> str:
        """ Este é o nome do número da mensagem usado na chamada de mensagem ABAP.
        Geralmente será um número, mas isso não é imposto pelo sistema.
        """
        return self.component.MessageNumber

    @property
    def message_parameter(self) -> str:
        """ Estes são os valores dos parâmetros usados para expandir os espaços reservados na definição do texto da mensagem no dicionário de dados.
        A propriedade text do GuiStatusbar já contém o texto expandido da mensagem. Um máximo de 8 valores de parâmetros podem
        ser fornecidos na codificação ABAP, portanto o índice deve estar na faixa de 0 a 7.
        """
        return self.component.MessageParameter

    @property
    def message_type(self) -> str:
        """ Esta propriedade pode ter qualquer um dos seguintes valores:
        S - Success
        W - Warning
        E - Error
        A - Abort
        I - Information
        """
        return self.component.MessageType
