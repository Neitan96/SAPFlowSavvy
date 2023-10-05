from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiToolbarControl(GuiShell):
    # TODO Criar descrição

    def get_button_checked(self, button_pos: int) -> int:
        """ Retorna se o botão na posição especificada está atualmente marcado (pressionado).
        """
        return self.component.GetButtonChecked(button_pos)

    def get_button_enabled(self, button_pos: int) -> int:
        """ Indica se o botão na posição especificada pode ser pressionado.
        """
        return self.component.GetButtonEnabled(button_pos)

    def get_button_icon(self, button_pos: int) -> str:
        """ Retorna o nome do ícone do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonIcon(button_pos)

    def get_button_id(self, button_pos: int) -> str:
        """ Retorna o ID do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonId(button_pos)

    def get_button_text(self, button_pos: int) -> str:
        """ Retorna o texto do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonText(button_pos)

    def get_button_tooltip(self, button_pos: int) -> str:
        """ Retorna a dica de ferramenta do botão de barra de ferramentas especificado.
        """
        return self.component.GetButtonTooltip(button_pos)

    def get_button_type(self, button_pos: int) -> str:
        """ Retorna o tipo do botão de barra de ferramentas especificado. Valores possíveis são: "Button", "ButtonAndMenu", "Menu", "Separator", "Group", "CheckBox".
        """
        return self.component.GetButtonType(button_pos)

    def get_menu_item_id_from_position(self, pos: int) -> str:
        """ Esta função retorna o identificador do item de menu com índice Position.
        """
        return self.component.GetMenuItemIdFromPosition(pos)

    def press_button(self, id_button: str) -> None:
        """ Esta função emula o pressionamento do botão com o ID fornecido.
        """
        self.component.PressButton(id_button)

    def press_context_button(self, id_button: str) -> None:
        """ Esta função emula o pressionamento do botão de contexto com o ID fornecido.
        """
        self.component.PressContextButton(id_button)

    def select_menu_item(self, id_item: str) -> None:
        """ Esta função emula a seleção do item de menu com o ID fornecido.
        """
        self.component.SelectMenuItem(id_item)

    def select_menu_item_by_text(self, str_text: str) -> None:
        """ Esta função emula a seleção do item de menu pelo texto do item de menu.
        """
        self.component.SelectMenuItemByText(str_text)

    @property
    def button_count(self) -> int:
        """ O número de botões da barra de ferramentas, incluindo separadores.
        """
        return self.component.ButtonCount

    @property
    def focused_button(self) -> int:
        """ O índice baseado em zero do botão que atualmente tem o foco.
        """
        return self.component.FocusedButton

    @focused_button.setter
    def focused_button(self, focused_button_index: int = None) -> None:
        """ O índice baseado em zero do botão que atualmente tem o foco.
        """
        self.component.FocusedButton = focused_button_index