from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiContainerShell(GuiShell):
    """ Um GuiContainerShell é um wrapper para um conjunto de objetos GuiShell.
    GuiContainerShell estende o objeto GuiVContainer.
    O prefixo do tipo é shellcont, o nome é a última parte do id, shellcont[n].
    """

    @property
    def docker_is_vertical(self) -> bool:
        """ Será TRUE se o contêiner for um controle de janela de encaixe vertical.
        """
        return self.component.DockerIsVertical

    @property
    def docker_pixel_size(self) -> int:
        """ Retorna o tamanho do controle do Docker em píxeis.
        """
        return self.component.DockerPixelSize