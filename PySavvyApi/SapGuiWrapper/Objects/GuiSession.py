from __future__ import annotations

from typing import Optional

from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiContainer
from PySavvyApi.SapGuiWrapper.Objects.GuiStatusPane import GuiStatusPane
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection
from PySavvyApi.SapGuiWrapper.Objects.GuiFrameWindow import GuiFrameWindow
from PySavvyApi.SapGuiWrapper.Objects.GuiSessionInfo import GuiSessionInfo
from PySavvyApi.SapGuiWrapper.Objects.GuiConnection import GuiConnection
from PySavvyApi.SapGuiWrapper.Helpers.StdTCodes import *


class GuiSession(GuiContainer):
    """ A GuiSession fornece o contexto no qual um usuário executa uma determinada tarefa, como trabalhar com uma transação.
    É, portanto, o ponto de acesso para aplicações, que gravam as ações de um usuário em relação a uma tarefa específica ou reproduzem essas ações.
    """

    def send_key(self, v_key: int) -> None:
        """ A chave virtual v_key é executada na janela ativa da sessão.
        As VKeys são definidas no pintor de menus.
        """
        self.active_window.send_v_key(v_key=v_key)

    def get_alert_status_pane(self) -> GuiStatusPane:
        """ Obtém a barra de alerta principal.
        """
        # noinspection PyTypeChecker
        return self.find_by_id(SapFields.ALERT_STATUS_PANE, False)

    @property
    def parent(self) -> GuiConnection:
        """ Obtém a conexão da sessão
        """
        return GuiConnection(self.component.Parent)

    def as_std_number_format(self, number: str) -> str:
        """ Dependendo do formato numérico do sistema, o sinal de menos dos números pode ser colocado à direita do número.
        Usando esta função, o sinal de menos é movido para a esquerda.
        """
        return self.component.AsStdNumberFormat(number)

    def clear_error_list(self) -> None:
        """ Este método limpa a lista de erros que podem ser criados quando controles ActiveX são encontrados em uma tela que não suporta scripts SAP GUI.
        Caso contrário, a lista será limpa após um evento de erro ser gerado. Isso acontece no final de uma viagem de ida e volta.
        """
        return self.component.ClearErrorList()

    def create_session(self) -> Optional[GuiSession]:
        """ Esta função abre uma nova sessão, que é então visualizada por uma nova janela principal.
        Isso se assemelha ao comando "/o" que pode ser executado no campo de comando.
        """
        conn = self.Parent()
        ses_count = conn.Sessions().Count()
        self.component.CreateSession()
        if ses_count < conn.Sessions().Count():
            return conn.Sessions().LastItem()

        return None

    def close_session(self, ignore_popup_logoff: bool = False) -> None:
        if ignore_popup_logoff and self.Parent().Sessions().Count() <= 1:
            self.SendCommand(SapCommands.CLOSE_ALL_SESSIONS)
        else:
            self.SendCommand(SapCommands.CLOSE_SESSION)

    def enable_jaws_events(self) -> None:
        """ Habilite o envio de eventos para o leitor de tela Freedom Scientific JAWS,
        que se comunica com SAP GUI para Windows através da API de Scripting.
        Por padrão o envio de eventos está ativado.
        """
        return self.component.EnableJawsEvents()

    def end_transaction(self) -> None:
        """ Chamar esta função tem o mesmo efeito que SendCommand("/n").
        """
        return self.component.EndTransaction()

    def find_by_position(self, x: int, y: int, on_raise: bool = True) -> GuiCollection:
        """ Este método pode ser usado para fazer um hittest em uma sessão SAP GUI.
        Os parâmetros x e y devem ser fornecidos em coordenadas de tela.
        Se nenhum componente for encontrado, uma exceção será gerada, a menos que raise seja definido como False.
        Nesse caso, um objeto None é retornado.
        """
        return GuiCollection(self.component.FindByPosition(x, y, on_raise))

    def get_icon_resource_name(self, text: str) -> str:
        """ No SAP GUI, os ícones são frequentemente descritos como texto no formato @nn@, onde nn é um número.
        A função getIconResourceName traduz a notação @nn@ no nome do recurso em sapbtmp.dll.
        """
        return self.component.GetIconResourceName(text)

    def get_v_key_description(self, v_key: int) -> str:
        """ Quando um script é gravado, ele geralmente contém chamadas sendVKey(n), onde n é um número.
        O método getVKeyDescription traduz esses números em um texto legível. Por exemplo, o número 0 é traduzido no texto “Enter”.
        """
        return self.component.GetVKeyDescription(v_key)

    def lock_session_ui(self) -> None:
        """ Este método bloqueia a sessão para que nenhuma interação do usuário seja
        possível até que a sessão seja desbloqueada usando UnlockSessionUI.
        """
        return self.component.LockSessionUI()

    def unlock_session_ui(self) -> None:
        """ Este método desbloqueia a sessão após ela ter sido bloqueada usando LockSessionUI.
        """
        return self.component.UnlockSessionUI()

    def send_command(self, command: str) -> None:
        """ Usando esta função você pode executar qualquer string de comando,
        que de outra forma poderia ser inserida na caixa de combinação do campo de comando.
        """
        return self.component.SendCommand(command)

    def start_transaction(self, transaction: str, new_session: bool = False) -> bool:
        """ Chamar esta função com o parâmetro "xyz" tem o mesmo efeito que SendCommand("/nxyz").
        """
        if transaction.startswith('/o/') or transaction.startswith('/o/'):
            transaction = transaction[3:]

        t_transaction = ('/o/' + transaction) if new_session else ('/n/' + transaction)
        if new_session:
            ses_count = self.Parent().Sessions().Count()
            self.component.StartTransaction(t_transaction)
            return self.Parent().Sessions().Count() > ses_count
        else:
            self.component.StartTransaction(t_transaction)
            return self.Info().Transaction == transaction

    @property
    def acc_enhanced_tab_chain(self) -> bool:
        """ Esta propriedade será True se a respectiva opção "Incluir elementos somente leitura e desabilitados na cadeia de guias"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        return self.component.AccEnhancedTabChain

    @acc_enhanced_tab_chain.setter
    def acc_enhanced_tab_chain(self, option: bool = None) -> None:
        """ Esta propriedade será True se a respectiva opção "Incluir elementos somente leitura e desabilitados na cadeia de guias"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        self.component.AccEnhancedTabChain = option

    @property
    def acc_symbol_replacement(self) -> bool:
        """ Esta propriedade é True se a respectiva opção "Exibir símbolos em listas como letras"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        return self.component.AccSymbolReplacement

    @acc_symbol_replacement.setter
    def acc_symbol_replacement(self, option: bool = None) -> None:
        """ Esta propriedade é True se a respectiva opção "Exibir símbolos em listas como letras"
        tiver sido definida na caixa de diálogo de opções do SAP GUI.
        """
        self.component.AccSymbolReplacement = option

    @property
    def active_window(self) -> GuiFrameWindow:
        """ Todas as janelas podem ser encontradas na coleção Children do GuiSession.
        No entanto, na maioria das vezes, um aplicativo acessará a janela da sessão atualmente ativada,
        pois essa é a janela com a qual o usuário provavelmente irá interagir. Esta propriedade pretende ser um atalho para esta janela.
        """
        return GuiFrameWindow(self.component.ActiveWindow)

    @property
    def busy(self) -> bool:
        """ Enquanto o SAP GUI aguarda dados do servidor, nenhuma chamada de script será retornada,
        bloqueando o thread em execução. Isto pode não ser aceitável para aplicações avançadas.
        Uma forma de evitar isso é verificar a propriedade Busy da sessão.
        Se esta propriedade for True, então uma chamada de Scripting subsequente aguardará o término da comunicação com o servidor.
        """
        return self.component.Busy

    @busy.setter
    def busy(self, option: bool = None) -> None:
        """ Enquanto o SAP GUI aguarda dados do servidor, nenhuma chamada de script será retornada,
        bloqueando o thread em execução. Isto pode não ser aceitável para aplicações avançadas.
        Uma forma de evitar isso é verificar a propriedade Busy da sessão.
        Se esta propriedade for True, então uma chamada de Scripting subsequente aguardará o término da comunicação com o servidor.
        """
        self.component.Busy = option

    @property
    def error_list(self) -> GuiCollection:
        return GuiCollection(self.component.ErrorList)

    @error_list.setter
    def error_list(self, errors: GuiCollection = None) -> None:
        self.component.ErrorList = errors.component

    @property
    def info(self) -> GuiSessionInfo:
        """ As informações são do tipo GuiSessionInfo.
        Ele contém informações técnicas sobre a conexão atual, os dados de login, o aplicativo SAP em execução e muito mais.
        """
        return GuiSessionInfo(self.component.Info)

    @property
    def is_active(self) -> bool:
        """ TRUE se a janela da sessão estiver ativa.
        """
        return self.component.IsActive

    @is_active.setter
    def is_active(self, option: bool = None) -> None:
        """ TRUE se a janela da sessão estiver ativa.
        """
        self.component.IsActive = option

    @property
    def is_list_box_active(self) -> bool:
        """ Esta propriedade é True se uma caixa de listagem estiver aberta no momento (para um GuiComboBox).
        """
        return self.component.IsListBoxActive

    @property
    def list_box_curr_entry(self) -> int:
        """ O índice da entrada da caixa de listagem atualmente selecionada.
        """
        return self.component.ListBoxCurrEntry

    @property
    def list_box_curr_entry_height(self) -> int:
        """ A altura da entrada atual da caixa de listagem em píxeis.
        """
        return self.component.ListBoxCurrEntryHeight

    @property
    def list_box_curr_entry_left(self) -> int:
        """ A posição esquerda da entrada atual da caixa de listagem em píxeis.
        """
        return self.component.ListBoxCurrEntryLeft

    @property
    def list_box_curr_entry_top(self) -> int:
        """ A posição superior da entrada atual da caixa de listagem em píxeis.
        """
        return self.component.ListBoxCurrEntryTop

    @property
    def list_box_curr_entry_width(self) -> int:
        """ A largura da entrada atual da caixa de listagem em pixels.
        """
        return self.component.ListBoxCurrEntryWidth

    @property
    def list_box_height(self) -> int:
        """ A altura da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxHeight

    @property
    def list_box_left(self) -> int:
        """ A posição esquerda da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxLeft

    @property
    def list_box_top(self) -> int:
        """ A posição superior da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxTop

    @property
    def list_box_width(self) -> int:
        """ A largura da caixa de listagem aberta em pixels.
        """
        return self.component.ListBoxWidth

    @property
    def passport_pre_system_id(self) -> str:
        """ O ID do pré-sistema. Parte das informações do passaporte.
        """
        return self.component.PassportPreSystemId

    @passport_pre_system_id.setter
    def passport_pre_system_id(self, option: str = None) -> None:
        """ O ID do pré-sistema. Parte das informações do passaporte.
        """
        self.component.PassportPreSystemId = option

    @property
    def passport_system_id(self) -> str:
        """ O ID do sistema. Parte das informações do passaporte.
        """
        return self.component.PassportSystemId

    @passport_system_id.setter
    def passport_system_id(self, option: str = None) -> None:
        """ O ID do sistema. Parte das informações do passaporte.
        """
        self.component.PassportSystemId = option

    @property
    def passport_transaction_id(self) -> str:
        """ O ID exclusivo da transação. Parte das informações do passaporte.
        """
        return self.component.PassportTransactionId

    @passport_transaction_id.setter
    def passport_transaction_id(self, option: str = None) -> None:
        """ O ID exclusivo da transação. Parte das informações do passaporte.
        """
        self.component.PassportTransactionId = option

    @property
    def progress_percent(self) -> int:
        """ A porcentagem exibida pelo indicador de progresso do SAP GUI.
        """
        return self.component.ProgressPercent

    @property
    def progress_text(self) -> str:
        """ O texto exibido pelo indicador de progresso.
        """
        return self.component.ProgressText

    @property
    def record(self) -> bool:
        """ Definir esta propriedade como True habilita o modo de gravação da sessão.
        Neste modo, as alterações nos elementos da interface do usuário são registradas no SAP GUI e enviadas
        para um aplicativo de gravação usando o evento Change descrito posteriormente.
        Observações:
        Alguns elementos da interface do usuário podem se comportar de maneira diferente no modo de gravação e durante a reprodução ou interação manual.
        * A caixa de diálogo de ajuda F4 é sempre exibida como uma janela modal.
        * Arrastar e soltar está desativado.
        """
        return self.component.Record

    @record.setter
    def record(self, option: bool = None) -> None:
        """ Definir esta propriedade como True habilita o modo de gravação da sessão.
        Neste modo, as alterações nos elementos da interface do usuário são registradas no SAP GUI e enviadas
        para um aplicativo de gravação usando o evento Change descrito posteriormente.
        Observações:
        Alguns elementos da interface do usuário podem se comportar de maneira diferente no modo de gravação e durante a reprodução ou interação manual.
        * A caixa de diálogo de ajuda F4 é sempre exibida como uma janela modal.
        * Arrastar e soltar está desativado.
        """
        self.component.Record = option

    @property
    def record_file(self) -> str:
        """ Uma maneira simples de gravar um script é definir a propriedade recordFile com um nome de arquivo válido e,
        em seguida, ativar a propriedade record. Um arquivo Visual Basic Script com o nome fornecido será criado na
        pasta SAP GUI Scripts no PC cliente.
        Observações: Esta propriedade aceita apenas nomes de arquivos simples sem informações de caminho.
        """
        return self.component.RecordFile

    @record_file.setter
    def record_file(self, option: str = None) -> None:
        """ Uma maneira simples de gravar um script é definir a propriedade recordFile com um nome de arquivo válido e,
        em seguida, ativar a propriedade record. Um arquivo Visual Basic Script com o nome fornecido será criado na
        pasta SAP GUI Scripts no PC cliente.
        Observações: Esta propriedade aceita apenas nomes de arquivos simples sem informações de caminho.
        """
        self.component.RecordFile = option

    @property
    def save_as_unicode(self) -> bool:
        """ Se esta propriedade estiver configurada como TRUE, os scripts gravados serão salvos na codificação UNICODE.
        Overwise é a página de código do sistema atual.
        """
        return self.component.SaveAsUnicode

    @save_as_unicode.setter
    def save_as_unicode(self, option: bool = None) -> None:
        """ Se esta propriedade estiver configurada como TRUE, os scripts gravados serão salvos na codificação UNICODE.
        Overwise é a página de código do sistema atual.
        """
        self.component.SaveAsUnicode = option

    @property
    def show_dropdown_keys(self) -> bool:
        """ Se esta propriedade for TRUE, os menus suspensos mostrarão não apenas o texto das entradas suspensas, mas também as chaves.
        """
        return self.component.ShowDropdownKeys

    @show_dropdown_keys.setter
    def show_dropdown_keys(self, option: bool = None) -> None:
        """ Se esta propriedade for TRUE, os menus suspensos mostrarão não apenas o texto das entradas suspensas, mas também as chaves.
        """
        self.component.ShowDropdownKeys = option

    @property
    def suppress_backend_popups(self) -> bool:
        return self.component.SuppressBackendPopups

    @suppress_backend_popups.setter
    def suppress_backend_popups(self, option: bool = None) -> None:
        self.component.SuppressBackendPopups = option

    @property
    def test_tool_mode(self) -> int:
        """ Durante os testes internos, alguns aspectos da interface do usuário mostraram-se difíceis de lidar com
        ferramentas de teste que usam a API de script para automatizar o SAP GUI. Por esta razão foi adicionado um
        modo especial no qual as seguintes alterações são administradas.

        * Embora as mensagens de sucesso (S), aviso (W) e erro (E) sejam sempre exibidas na barra de status,
            as mensagens de informação (I) e de aborto (A) são exibidas como janelas pop-up, a menos que testToolMode esteja definido.
        * O modo de atualização do servidor de aplicativos é alterado para modo imediato para a conexão.
        * As mensagens do sistema são ignoradas para não interromper a gravação ou reprodução de scripts.

        0: Desativar TestToolMode
        1: Habilite TestToolMode
        """
        return self.component.TestToolMode

    @test_tool_mode.setter
    def test_tool_mode(self, option: int = None) -> None:
        """ Durante os testes internos, alguns aspectos da interface do usuário mostraram-se difíceis de lidar com
        ferramentas de teste que usam a API de script para automatizar o SAP GUI. Por esta razão foi adicionado um
        modo especial no qual as seguintes alterações são administradas.

        * Embora as mensagens de sucesso (S), aviso (W) e erro (E) sejam sempre exibidas na barra de status,
            as mensagens de informação (I) e de aborto (A) são exibidas como janelas pop-up, a menos que testToolMode esteja definido.
        * O modo de atualização do servidor de aplicativos é alterado para modo imediato para a conexão.
        * As mensagens do sistema são ignoradas para não interromper a gravação ou reprodução de scripts.

        0: Desativar TestToolMode
        1: Habilite TestToolMode
        """
        self.component.TestToolMode = option