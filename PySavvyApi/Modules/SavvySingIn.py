from __future__ import annotations

import time
from typing import Optional

from ..SavvyLogger import SavvyLogger
from ..SavvyHelper import check_strings

from .SapGui import SapGui
from .SavvyCredentials import SavvyCredentials
from .SavvySessionsFilter import SavvySessionsFilter
from ..StdTCodes import SapFields, SapCommands, SapTransactions
from ..SapGuiWrapper import GuiSession


class SingInCredsType:

    # Armazena as credenciais em um arquivo da pasta pessoal do usuário, obtém as credenciais por meio de inputbox
    FILE_USER_FOLDER = 'FileUserFolder'

    # Obtém o login e senha por meio de inputbox e guarda em variáveis até que o programa seja interrompido
    INPUT_BOX = 'InputBox'

    # Abre a tela de login e aguarda o usuário fazer login
    WAIT = 'Wait'


class SingInForceType:

    # Cancela o login
    EXIT = 'Exit'

    # Força o login fazer desconectar da outra máquina
    FORCE = 'Force'

    # Fica tentando fazer login até que desconecte da outra máquina
    WAIT = 'Wait'


class SavvySapSingIn:

    credentials = None
    creds_get_type: SingInCredsType = SingInCredsType.FILE_USER_FOLDER  # Método de obtenção das credenciais de login
    force_type: SingInForceType = SingInForceType.FORCE  #  Tipo de comportamento ao fazer e o usuário já está logado em outra máquina
    mandt: str = None  # Mandante do login
    language: str = None  # Línguagem para fazer login do SAP
    max_session = 6  # Quantidade máxima de sessões que o SAP permiti

    @staticmethod
    def get_credentials(conn_name: str) -> (str, str):
        """ Obtém as credenciais de uma conexão.
        Args:
            conn_name (str): Nome da conexão
        """
        if SavvySapSingIn.credentials is None:
            if SavvySapSingIn.creds_get_type == SingInCredsType.FILE_USER_FOLDER:
                SavvySapSingIn.credentials = SavvyCredentials()
            else:
                SavvySapSingIn.credentials = SavvyCredentials(None)

        user_name, password = SavvySapSingIn.credentials.get_credentials(conn_name)
        if not check_strings(user_name, password): return None, None
        return user_name, password

    @staticmethod
    def _set_credentials_in_login(session: GuiSession, try_max: int = 3) -> Optional[GuiSession]:
        """ Faz o preenchimento das credenciais na tela de login.
        Se algum erro ocorrer durante o login a função irá fechar a sessão e retornar None,
        erros como a falta das credenciais ou ao preencher as credenciais.
        Args:
            session (GuiSession): uma sessão na tela de login
        Returns:
            GuiSession: retorna a mesma sessão caso não tenha dado nenhum erro
        """
        if session.is_loged(): return session

        if SavvySapSingIn.creds_get_type == SingInCredsType.WAIT:
            session.active_window.set_focus_windows()
            while session.connected_sap() and not check_strings(session.info.user):
                time.sleep(0.5)
            if session.connected_sap(): return session
            else: return None

        conn_name = session.parent_cast.GuiConnection().description
        user_name, password = SavvySapSingIn.get_credentials(conn_name)
        if not check_strings(user_name, password):
            if session.connected_sap(): session.close_session(True)
            return None

        # noinspection PyBroadException
        try:
            if SavvySapSingIn.mandt is not None:
                session.find_by_id(SapFields.LOGIN_MANDT).text = SavvySapSingIn.mandt
            if SavvySapSingIn.language is not None:
                session.find_by_id(SapFields.LOGIN_LANGUAGE).text = SavvySapSingIn.language

            session.find_by_id(SapFields.LOGIN_USERNAME).text = user_name
            session.find_by_id(SapFields.LOGIN_PASSWORD).text = password
            session.send_key().enter()
        except:
            SavvyLogger.error('SAP Init', 'Erro ao preencher as credenciais de login')
            if session.connected_sap(): session.close_session(True)
            return None

        if not session.connected_sap():
            SavvySapSingIn.credentials.clear_credentials(conn_name)
            return None

        if session.get_alert_status_pane().has_in_text('logon)'):
            SavvySapSingIn.credentials.clear_credentials(conn_name)
            if try_max > 0:
                return SavvySapSingIn._set_credentials_in_login(session=session, try_max=try_max-1)
            return None

        return session

    @staticmethod
    def _force_login_trat(session: GuiSession) -> Optional[GuiSession]:
        """ Faz o tratamento de tipo de forçamento do login quando o usuário já está logado em outra máquina.
        Args:
            session (GuiSession): sessão com o popup de multi login aberto
        Returns:
            GuiSession: Retorna a sessão com o login feito, importate pegar o retorno,
                devido o método de login wait não faz login na mesma sessão.
        """
        force_sign_bnt = session.find_by_id_cast(SapFields.POPUP_MULTI_LOGIN_RAD_FORCE, False).GuiRadioButton()
        if force_sign_bnt is not None:
            if SavvySapSingIn.force_type == SingInForceType.EXIT:
                session.send_key().f12()
                return None

            if SavvySapSingIn.force_type == SingInForceType.FORCE:
                force_sign_bnt.select()
                session.send_key().enter()

            if SavvySapSingIn.force_type == SingInForceType.WAIT:
                sap_app = session.parent.parent_cast.GuiApplication()
                session.send_key().f12()
                time.sleep(10)

                conn_name = session.parent_cast.GuiConnection().description
                new_session = sap_app.open_connection(conn_name, True).sessions.last_item_cast().GuiSession()
                return SavvySapSingIn.login_sign_in(session=new_session)
        return session

    @staticmethod
    def _login_after_sign_in(session: GuiSession) -> GuiSession:
        """ Faz alguns tratamentos após o login, sendo:
        - Fecha o popup de quantidade de tentativas de login falhadas.
        - Fecha o pop de Copyright (geralmente aparece quando altera o idioma de login).
        - Retorna ao menu principal.
        Args:
            session: Sessão após o login bem sucessido.
        Returns:
            GuiSession: A mesma sessão passada nos parâmetros
        """
        popup_window = session.find_by_id_cast('wnd[1]', False).GuiModalWindow()
        if popup_window is not None and popup_window.text in ['Information', 'Informação']:
            if session.find_by_id_cast(SapFields.POP_UP_COUNT_FAILS_LABEL_LINE_1, False) is not None:
                session.send_key().enter()

        copy_r = session.find_by_id_cast('wnd[1]', False).GuiModalWindow()
        if copy_r is not None and copy_r.text == 'Copyright':
            session.send_key().enter()

        if session.info.transaction not in [SapTransactions.LOGIN, SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN]:
            session.send_command(SapCommands.RETURN_MENU)

        bnt_to_menu = session.find_by_id_cast(SapFields.LOGIN_TO_MENU, False).GuiButton()
        if bnt_to_menu is not None:
            bnt_to_menu.press()

        return session

    @staticmethod
    def login_sign_in(session: GuiSession, try_max: int = 3) -> Optional[GuiSession]:
        """ Realiza o login no SAP fazendo todas as tratativas, garantindo que a sessão esteja no menu principal.
        Args:
            session (SapSession): sessão na tela de login
            try_max (int): máxima de tentativas falhas de login com credenciais inválidas
        """
        if session is None or not session.connected_sap():
            return None

        session = SavvySapSingIn._login_after_sign_in(session)
        if session.is_loged(): return session

        session = SavvySapSingIn._set_credentials_in_login(session, try_max)
        session = SavvySapSingIn._force_login_trat(session)
        return SavvySapSingIn._login_after_sign_in(session)

    @staticmethod
    def get_session_loged(conn_name: str, any_user: bool = False, in_transaction: str = None) -> Optional[GuiSession]:
        SapGui.close_all_time_out_popups()
        if not SapGui.start_sap_logon(): return None

        sap_app = SapGui.get_sap_application()
        if sap_app is None: return None

        sessions_filter = SavvySessionsFilter(sap_app)
        sessions_filter.conn_name(conn_name)
        if not any_user:
            username, password = SavvySapSingIn.get_credentials(conn_name)
            sessions_filter.user(username)

        sessions = sessions_filter.get_sessions()
        if len(sessions) <= 0:
            conn = sap_app.open_connection(conn_name, True)
            if conn is None: return None
            session = SavvySapSingIn.login_sign_in(conn.sessions_list[0])
            if in_transaction is not None and session is not None:
                session.start_transaction(in_transaction)
            return session

        if in_transaction is None or not len(in_transaction) > 0:
            sessions_filter.in_transaction(SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN)
        else:
            sessions_filter.in_transaction(in_transaction)

        sessions_transactions = sessions_filter.get_sessions()

        if len(sessions_transactions) > 0:
            return SavvySapSingIn.login_sign_in(sessions_transactions[0])

        if sessions[0].parent_cast.GuiConnection().sessions.count < SavvySapSingIn.max_session:
            return sessions[0].create_session()

        return None
