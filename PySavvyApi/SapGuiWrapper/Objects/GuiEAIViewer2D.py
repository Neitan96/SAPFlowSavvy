from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiEAIViewer2D(GuiShell):
    """ O controle GuiEAIViewer2D é utilizado para visualizar imagens gráficas bidimensionais no sistema SAP.
    O usuário pode realizar redlining sobre a imagem carregada. o wrapper de script para esse controle registra
    todas as ações do usuário durante o processo de redlining e reproduz as mesmas ações quando o script gravado é reproduzido.
    """

    def annotation_text_request(self, text: str) -> None:
        # TODO Criar descrição
        return self.component.annotationTextRequest(text)

    @property
    def annotation_enabled(self) -> int:
        """ O valor desta propriedade é definido como 1 quando a marcação está ativada.
        O controle wrapper começa a gravar as ações do usuário assim que esta propriedade é definida como valor 1.
        """
        return self.component.AnnotationEnabled

    @annotation_enabled.setter
    def annotation_enabled(self, enabled: int = None) -> None:
        """ O valor desta propriedade é definido como 1 quando a marcação está ativada.
        O controle wrapper começa a gravar as ações do usuário assim que esta propriedade é definida como valor 1.
        """
        self.component.AnnotationEnabled = enabled

    @property
    def annotation_mode(self) -> int:
        """ Durante a marcação, o modo de marcação selecionado é armazenado nesta propriedade.
        """
        return self.component.AnnotationMode

    @annotation_mode.setter
    def annotation_mode(self, mode: int = None) -> None:
        """ Durante a marcação, o modo de marcação selecionado é armazenado nesta propriedade.
        """
        self.component.AnnotationMode = mode

    @property
    def redlining_stream(self) -> str:
        """ Esta propriedade armazena a camada de marcação como um objeto BLOB (Binary Large Data Object).
        Durante a gravação, todo o BLOB é copiado para o script gerado.
        """
        return self.component.RedliningStream

    @redlining_stream.setter
    def redlining_stream(self, stream: str = None) -> None:
        """ Esta propriedade armazena a camada de marcação como um objeto BLOB (Binary Large Data Object).
        Durante a gravação, todo o BLOB é copiado para o script gerado.
        """
        self.component.RedliningStream = stream