# SAPFlowSavvy - Toolkit para Python

### Funções adicionais implementadas no Wrapper

- SapGuiConnection:
  - **is_loged()** → *bool*: Verifica se a conexão foi feito o login de usuário.
  - **user_loged()** → *str*: Retonar o nome do usuário logado na conexão.
  - **create_session()** → *GuiSession*: Abre uma nova sessão na conexão.
  - **sessions_list** → *list[GuiSession]*: Retorna uma lista com as sessões.
  - **sessions_user(user_name: str)** → *list[GuiSession]*: Obtém todas as sessões do usuário.
  - **sessions_in_transaction(transaction: str)** → *list[GuiSession]*: Obtém todas as sessões do usuário.


- GuiSession:
  - **get_alert_status_pane()** → *GuiStatusPane*: Obtém a barra de alerta principal.
  - **send_key(v_key: int)** → *None*: A chave virtual v_key é executada na janela ativa da sessão.


- GuiComponent:
  - **parent_cast** → *ComponentCast*:  Retorna o Parent pronto para fazer o Cast.
  - **cast_to()** → *ComponentCast*:  Retorna a uma classe para fazer o cast do componente atual.
  - **connected_sap()** → *bool*:  Verifica se o componente ainda está conectado ao SAP.


- GuiContainer:
  - **find_by_id_cast(id: str, on_raise: bool = True)** → *ComponentCast*:  O Componente será retornado em uma classe de cast para fazer o hint no tipo desejado.


- GuiComponentCollection:
  - **to_list()** → *list[GuiComponent]*: Retorna uma lista com todos os itens da coleção.
  - **last_item()** → *SapGuiComponent*: Retona o útimo item da coleção.
  - **last_item_cast()** → *ComponentCast*: Retona o útimo item da coleção em uma classe pronta para fazer o cast para o tipo do item desejado.
  - **item_cast(index: int, on_raise: bool = True)** → *ComponentCast*: O item será retornado em uma classe pronto para fazer o cast para o tipo do item desejado.


- GuiCollection:
  - **to_list()** → *list[object]*: Retorna uma list com todos os itens da coleção.


- GuiFrameWindow:
  - **set_focus_windows()** → *None*: Isso faz o windows focar na janela indepedente do estado atual do mesmo.


- GuiStatusPane:
  - **has_in_text(text: str)** → *bool*: Verifica se tem um texto específico dentro do texto do painel.


- GuiScrollbar:
  - **load_all()** → *None*: Faz o carregamento completo do componente, rolando do começo até o fim do scroll.