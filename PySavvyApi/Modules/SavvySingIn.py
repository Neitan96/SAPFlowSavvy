from enum import Enum

from PySavvyApi.SapGuiWrapper import *
from PySavvyApi.StdTCodes import SapTransactions

class SingInResult(Enum):
    """ Enum com os diferentes resultados de uma tentativa de login
    """
    Sucess = 1
    PopupMultiLogin = 0
    WrongCredentials = -1
    ErrorFill = -2

class MultiLoginOption(Enum):
    """ Enum com as opções para o popup de multi-login do Sap.
    """
    Exit = -1
    Force = 1

class SavvySingIn:
    """ Essa classe permite realizar ações de login no SAP.
    ALgumas das possibilidades é o preenchimento das credenciais,
    tratamentos pós-login, como o fechamento de pop-ups ao fazer login
    e ações ao abrir o pop-up de multi login do SAP.
    """

    @staticmethod
    def close_popups_after_singin(session: GuiSession) -> None:
        """ Fecha os popups abertos após um login, sendo:
        - Popup de quantidade de tentativas de login falhadas.
        - Popup de Copyright
        Args:
            session: sessão após o login bem-sucedido
        """
        popup_window = session.find_by_id_cast('wnd[1]', False).GuiModalWindow()
        if popup_window is not None and popup_window.text in ['Information', 'Informação']:
            if session.find_by_id_cast(SapFields.POP_UP_COUNT_FAILS_LABEL_LINE_1, False) is not None:
                session.send_key().enter()

        copy_r = session.find_by_id_cast('wnd[1]', False).GuiModalWindow()
        if copy_r is not None and copy_r.text == 'Copyright':
            session.send_key().enter()

        if session.info.transaction == SapTransactions.MAIN_MENU_RETURN:
            bnt_to_menu = session.find_by_id_cast(SapFields.LOGIN_TO_MENU, False).GuiButton()
            if bnt_to_menu is not None:
                bnt_to_menu.press()

    @staticmethod
    def send_credentials(session: GuiSession, username: str, password: str, mandt: str = None, language: str = None) -> SingInResult:
        """ Realiza o login em uma sessão que está na tela login
        Args:
            session: sessão para fazer o login
            username: nome do usuário
            password: senha do usuário
            mandt: mandante
            language: idioma
        Returns:
            SingInResult: resultato da tentativa de login
        """
        if session.is_loged(): return SingInResult.Sucess

        # noinspection PyBroadException
        try:
            if mandt is not None: session.find_by_id(SapFields.LOGIN_MANDT).text = mandt
            if language is not None: session.find_by_id(SapFields.LOGIN_LANGUAGE).text = language

            session.find_by_id(SapFields.LOGIN_USERNAME).text = username
            session.find_by_id(SapFields.LOGIN_PASSWORD).text = password
            session.send_key().enter()
        except:
            return SingInResult.ErrorFill

        if not session.connected_sap():
            return SingInResult.WrongCredentials

        if session.get_alert_status_pane().has_in_text('logon)'):
            return SingInResult.WrongCredentials

        force_sign_bnt = session.find_by_id_cast(SapFields.POPUP_MULTI_LOGIN_RAD_FORCE, False).GuiRadioButton()
        if force_sign_bnt is not None:
            return SingInResult.PopupMultiLogin

        SavvySingIn.close_popups_after_singin(session)

        return SingInResult.Sucess

    @staticmethod
    def multi_login_select(session: GuiSession, force_type: MultiLoginOption) -> None:
        """ Seleciona uma opção para o popup de multi-login do Sap
        Args:
            session: sessão com o popup aberto
            force_type: opção para selecionar
        """
        force_sign_bnt = session.find_by_id_cast(SapFields.POPUP_MULTI_LOGIN_RAD_FORCE, False).GuiRadioButton()
        if force_sign_bnt is not None:
            if force_type == MultiLoginOption.Exit:
                session.send_key().f12()
                return None

            if force_type == MultiLoginOption.Force:
                force_sign_bnt.select()
                session.send_key().enter()
                SavvySingIn.close_popups_after_singin(session)