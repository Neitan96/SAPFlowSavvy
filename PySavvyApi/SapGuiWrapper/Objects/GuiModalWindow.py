from PySavvyApi.SapGuiWrapper.Objects.GuiFrameWindow import GuiFrameWindow


class GuiModalWindow(GuiFrameWindow):
    """ Uma GuiModalWindow é uma caixa de diálogo pop-up.
    """

    @property
    def is_popup_dialog(self) -> bool:
        """ Algumas janelas modais representam caixas de diálogo pop-up.
        Neste caso a propriedade IsPopupDialog é True.
        As caixas de diálogo pop-up são identificadas verificando o nome da fonte ABAP e o número do dynpro.
        """
        return self.component.IsPopupDialog

    @property
    def popup_dialog_text(self) -> str:
        """ O texto dos campos de entrada da caixa de diálogo pop-up em formato concatenado.
        """
        return self.component.PopupDialogText