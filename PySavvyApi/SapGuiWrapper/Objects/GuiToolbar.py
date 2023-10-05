from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer


class GuiToolbar(GuiVContainer):
    """ Cada GuiFrameWindow possui uma GuiToolbar.
    O GuiMainWindow possui duas barras de ferramentas, a menos que a segunda tenha sido desativada pela aplicação ABAP.
    A barra de ferramentas superior é a barra de ferramentas do sistema, enquanto a segunda barra de ferramentas é a barra de ferramentas do aplicativo.
    Os filhos de uma GuiToolbar são botões. Os índices dos botões da barra de ferramentas são determinados pelos valores de chave virtual definidos para o botão.
    """

    pass