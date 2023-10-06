from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiVComponent import GuiVComponent


class GuiFrameWindow(GuiVContainer):
    """ Um GuiFrameWindow é um objeto visual de alto nível na hierarquia de tempo de execução.
    Pode ser a janela principal ou uma janela pop-up modal. Consulte as seções GuiMainWindow e GuiModalWindow para obter exemplos.
    O próprio GuiFrameWindow é uma interface abstrata. GuiFrameWindow estende o objeto GuiVContainer. O prefixo do tipo é wnd, o nome
    é wnd mais o número da janela entre colchetes.
    """

    def close(self) -> None:
        """ A função tenta fechar a janela. Tentar fechar a última janela principal de uma sessão não terá sucesso imediato
        a caixa de diálogo 'Você realmente deseja fazer logoff?' será exibida primeiro.
        """
        self.component.Close()

    def comp_bitmap(self, filename_1: str, filename_2: str) -> int:
        """ Este método compara dois arquivos bitmap píxel por píxel.
        Tipo de retorno:
        O método retorna um dos seguintes valores:
        0: Os arquivos não diferem
        1: Os arquivos diferem em tamanho
        2: Os arquivos possuem conteúdo diferente
        3: Houve um erro
        """
        return self.component.CompBitmap(filename_1, filename_2)

    def hard_copy(self, filename: str, image_type: int = 0, x_pos: int = None, y_pos: int = None, n_width: int = None, n_height: int = None) -> str:
        """ Esta função despeja uma cópia impressa da janela como um arquivo bitmap no disco.
        O parâmetro é o nome do arquivo.
        Se a função for bem-sucedida, o valor de retorno será o caminho totalmente qualificado do arquivo.
        Se nenhuma informação de caminho for fornecida, o arquivo será gravado na pasta de documentos SAP GUI.
        Caso os parâmetros opcionais xPos, yPos, nWidth e nHeight forem definidos, apenas o retângulo especificado da janela principal será capturado.
        image_type:
        0: BMP
        1: JPG
        2: PNG
        3: GIF
        4: TIFF
        """
        return self.component.HardCopy(filename, image_type, x_pos, y_pos, n_width, n_height)

    def hard_copy_to_memory(self, image_type: int = 0):
        """ Esta função retorna uma cópia impressa da janela como uma matriz segura de bytes.
        image_type:
        0: BMP
        1: JPG
        2: PNG
        3: GIF
        4: TIFF
        """
        # TODO Verificar retorno no python
        return self.component.HardCopyToMemory(image_type)

    def is_v_key_allowed(self, v_key: int) -> bool:
        """ Esta função retorna True se a chave virtual VKey estiver disponível no momento.
        As VKeys são definidas no pintor de menus.
        """
        return self.component.IsVKeyAllowed(v_key)

    def iconify(self) -> None:
        """ Isso definirá uma janela para o estado iconificado.
        Não é possível iconificar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão iconificados.
        """
        self.component.Iconify()

    def minimize(self) -> None:
        """ Isso definirá uma janela para o estado iconificado.
        Não é possível iconificar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão iconificados.
        """
        self.iconify()

    def maximize(self) -> None:
        """ Isso maximizará uma janela. Não é possível maximizar uma janela modal,
        é sempre a janela principal que será maximizada.
        """
        self.component.Maximize()

    def restore(self) -> None:
        """ Isso restaurará uma janela de seu estado iconificado.
        não é possível restaurar uma janela específica de uma sessão, tanto a janela principal quanto todos os modais existentes serão restaurados.
        """
        self.component.Restore()

    def set_focus_windows(self) -> None:
        """ Isso faz o windows focar na janela indepedente do estado atual do mesmo.
        """
        self.minimize()
        self.maximize()

    def send_v_key(self, v_key: int) -> None:
        """ A chave virtual VKey é executada na janela. As VKeys são definidas no pintor de menus.
        """
        return self.component.SendVKey(v_key)

    def show_message_box(self, title: str, text: str, msg_icon: int, msg_type: int) -> int:
        """ Mostra uma caixa de mensagem.
        O valor de retorno será uma das constantes GuiMessageBoxResult.
        title: Título da caixa de mensagem
        text: texto da caixa de mensagem.
        msg_icon: MsgIcon define o ícone a ser usado para a caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxType.
        msg_type: MsgType define os botões disponíveis na caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxOption.
        """
        return self.component.ShowMessageBox(title, text, msg_icon, msg_type)

    def jump_backward(self) -> None:
        """ Executa a tecla Ctrl+Shift+Tab na janela para retroceder um bloco.
        """
        self.component.JumpBackward()

    def jump_forward(self) -> None:
        """ Execute a tecla Ctrl+Tab na janela para avançar um bloco.
        """
        self.component.JumpForward()

    def tab_backward(self) -> None:
        """ Execute a tecla Shift+Tab na janela para retroceder um elemento.
        """
        self.component.TabBackward()

    def tab_forward(self) -> None:
        """ Execute a tecla Tab na janela para avançar um elemento.
        """
        self.component.TabForward()

    @property
    def element_visualization_mode(self) -> bool:
        """ Quando elementVisualizationMode está habilitado, um teste de acerto pode ser executado no
        SAP GUI movendo o cursor sobre a janela. O evento hit da sessão é disparado quando um componente é encontrado na posição do mouse.
        """
        return self.component.ElementVisualizationMode

    @element_visualization_mode.setter
    def element_visualization_mode(self, option: bool = None) -> None:
        """ Quando elementVisualizationMode está habilitado, um teste de acerto pode ser executado no
        SAP GUI movendo o cursor sobre a janela. O evento hit da sessão é disparado quando um componente é encontrado na posição do mouse.
        """
        self.component.ElementVisualizationMode = option

    @property
    def gui_focus(self) -> GuiVComponent:
        """ O SystemFocus suporta apenas elementos dynpro.
        Para receber informações sobre o controle ActiveX atualmente em foco você pode acessar a propriedade GuiFocus.
        """
        # TODO Retorna ao component cast
        return GuiVComponent(self.component.GuiFocus)

    @property
    def handle(self) -> int:
        """ O identificador de janela do controle que está conectado ao GuiShell.
        Este é o identificador da janela subjacente no Microsoft Windows.
        """
        return self.component.Handle

    @property
    def iconic(self) -> bool:
        """ Esta propriedade é True se a janela estiver iconificada.
        É possível executar comandos de script em uma janela iconificada, mas pode haver resultados indefinidos,
        especialmente quando controles estão envolvidos, pois estes podem ter configurações de tamanho inválidas.
        """
        return self.component.Iconic

    @property
    def system_focus(self) -> GuiVComponent:
        """ O SystemFocus especifica o componente que o sistema SAP está atualmente vendo como sendo focado.
        Este valor é válido apenas para elementos dynpro e pode, portanto, diferir do foco visto no frontend.
        """
        # TODO Retorna ao component cast
        return GuiVComponent(self.component.SystemFocus)

    @property
    def working_pane_height(self) -> int:
        """ Esta é a altura do painel de trabalho na métrica de caracteres.
        """
        return self.component.WorkingPaneHeight

    @property
    def working_pane_width(self) -> int:
        """ Esta é a largura do painel de trabalho na métrica de caracteres.
        O painel de trabalho é a área entre as barras de ferramentas na parte superior da janela e a barra de status na parte inferior da janela.
        """
        return self.component.WorkingPaneWidth
