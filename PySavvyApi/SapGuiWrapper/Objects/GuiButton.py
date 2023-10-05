from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiButton(GuiVComponent):
    """ GuiButton representa todos os botões que estão no dynpros, na barra de ferramentas ou nos controles da tabela.
    O prefixo do tipo é btn, a propriedade name é o nome do campo obtido do dicionário de dados SAP.
    Há uma exceção: para botões de tabstrip, é o ID do botão definido no pintor de tela obtido do dicionário de dados SAP.
    """

    def press(self) -> None:
        """ Isso emula o pressionamento manual de um botão.
        Pressionar um botão sempre fará com que a comunicação do servidor ocorra,
        tornando inválidas todas as referências a elementos abaixo do nível da janela.
        """
        self.component.Press()

    @property
    def emphasized(self) -> bool:
        """ Esta propriedade é True se o botão for exibido enfatizado
        (no Fiori Visual Themes: O botão mais à esquerda no rodapé e botões configurados como "Fiori Usage D Display<->Change").
        """
        return self.component.Emphasized

    @property
    def left_label(self) -> GuiVComponent:
        """ Rótulo esquerdo do GuiButton. O rótulo é atribuído no Screen Painter, usando o sinalizador 'assign left'.
        """
        return GuiVComponent(self.component.LeftLabel)

    @property
    def right_label(self) -> GuiVComponent:
        """ Rótulo direito do GuiButton. Esta propriedade é definida no Screen Painter usando o sinalizador 'assign right'.
        """
        return GuiVComponent(self.component.RightLabel)