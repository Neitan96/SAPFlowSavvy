from __future__ import annotations

import time
from typing import Optional

from ..SavvyLogger import SavvyLogger
from ..SavvyHelper import check_strings

from .SapGui import SapGui
from .SavvyCredentials import SavvyCredentials
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

    @staticmethod
    def _login_after_sign_in(session: GuiSession) -> GuiSession:

        field_count_fails = session.find_by_id(SapFields.POP_UP_COUNT_FAILS_LABEL_LINE_1, False)
        if field_count_fails is not None: session.send_key().enter()

        copy_r = session.find_by_id_cast('wnd[1]', False).GuiFrameWindow()
        if copy_r is not None and copy_r.text == 'Copyright':
            session.send_key().enter()

        if session.info.transaction != SapTransactions.LOGIN and session.info.transaction != SapTransactions.MAIN_MENU:
            session.send_command(SapCommands.RETURN_MENU)

        bnt_to_menu = session.find_by_id_cast(SapFields.LOGIN_TO_MENU, False).GuiButton()
        if bnt_to_menu is not None:
            bnt_to_menu.press()

        return session

    @staticmethod
    def login_sign_in(session: GuiSession, try_max: int = 3) -> Optional[GuiSession]:
        """ Realiza o login no SAP

        Args:
            session (SapSession): sessão na tela de login
            try_max (int): máxima de tentativas falhas de login com credenciais inválidas
        """
        if session is None or session.component is None or not session.connected_sap():
            return None

        session = SavvySapSingIn._login_after_sign_in(session)

        if session.info.transaction != SapTransactions.LOGIN:
            return session

        conn_name = session.parent_cast.GuiConnection().description

        if SavvySapSingIn.creds_get_type == SingInCredsType.WAIT:
            session.active_window.set_focus_windows()
            while not check_strings(session.info.user):
                time.sleep(0.5)

        elif SavvySapSingIn.creds_get_type in [SingInCredsType.FILE_USER_FOLDER, SingInCredsType.INPUT_BOX]:
            if SavvySapSingIn.credentials is None:
                if SavvySapSingIn.creds_get_type == SingInCredsType.FILE_USER_FOLDER:
                    SavvySapSingIn.credentials = SavvyCredentials()
                else:
                    SavvySapSingIn.credentials = SavvyCredentials(None)

            user_name, password = SavvySapSingIn.credentials.get_credentials(conn_name)
            if not check_strings(user_name, password): return None

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
                return None

            if not session.connected_sap():
                SavvySapSingIn.credentials.clear_credentials(conn_name)
                return None

        if session.get_alert_status_pane().has_in_text('logon)'):
            SavvySapSingIn.credentials.clear_credentials(conn_name)
            if try_max > 0:
                return SavvySapSingIn.login_sign_in(session=session, try_max=try_max-1)
            return None

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

                new_session = sap_app.open_connection(conn_name, True).sessions.last_item_cast().GuiSession()
                return SavvySapSingIn.login_sign_in(session=new_session, try_max=try_max)

        return SavvySapSingIn._login_after_sign_in(session)

    def get_session_loged(self, conn_name: str, reuse_sessions: bool = True) -> Optional[GuiSession]:
        SapGui.close_all_time_out_popups()
        if not SapGui.start_sap_logon(): return None

        sap_app = SapGui.get_sap_application()
        if sap_app is None: return None

        connections = sap_app.connections_list(conn_name)

        if len(connections) <= 0:
            conn = sap_app.open_connection(conn_name, True)
            if conn is None: return None
            return self.login_sign_in(conn.sessions.last_item_cast().GuiSession())

        if reuse_sessions:
            for conn in connections:
                sessions = conn.sessions_in_transaction(SapTransactions.MAIN_MENU, SapTransactions.MAIN_MENU_RETURN)
                if len(sessions) > 0:
                    return self._login_after_sign_in(sessions[0])

        for conn in connections:
            sessions = conn.sessions_in_transaction(SapTransactions.LOGIN)
            if len(sessions) > 0: return self.login_sign_in(sessions[0])

        for conn in connections:
            if conn.sessions.count < 6:
                session = conn.create_session()
                return self.login_sign_in(session)

        return None
