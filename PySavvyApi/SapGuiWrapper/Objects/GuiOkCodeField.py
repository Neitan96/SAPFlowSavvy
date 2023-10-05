from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiOkCodeField(GuiVComponent):
    """ O GuiOkCodeField é colocado na barra de ferramentas superior da janela principal.
    É uma caixa de combinação na qual comandos podem ser inseridos. Definir o texto de GuiOkCodeField
    não executará o comando até que a comunicação do servidor seja iniciada, por exemplo, emulando a tecla Enter (VKey 0).
    O prefixo do tipo é okcd, o nome está vazio.
    """

    def press_f1(self) -> None:
        """ Emule pressionando a tecla F1 enquanto o foco está no GuiOkCodeField.
        """
        self.component.PressF1()

    @property
    def opened(self) -> bool:
        """ Em designs SAP GUI mais recentes que o design Clássico, o GuiOkCodeField pode ser recolhido usando
        o botão de seta à direita dele. No SAP GUI para Windows, o GuiOkCodeField também pode ser recolhido por
        meio de uma configuração no registro do Windows.
        Esta propriedade contém False se o GuiOkCodeField estiver recolhido.
        """
        return self.component.Opened
