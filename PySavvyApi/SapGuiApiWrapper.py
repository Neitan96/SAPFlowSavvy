"""
SapGuiApiWrapper

Este arquivo contém enums e classes wrapper do SAP GUI Scripting API, com algumas funções extras.

Funções Adicionais nos Wrapper:

- SapGuiComponent:
  - CastTo() -> SapCastTo: Retorna a uma classe para fazer o cast do componente atual.
  - ParentCast() -> SapCastTo: Retorna o Parent pronto para fazer o Cast.
  - ConnectedSap() -> bool: Verifica se o componente ainda está conectado ao SAP.

- SapGuiContainer:
  - FindByIdCast(id: str, on_raise: bool = True) -> SapCastTo: O Componente será retornado em uma classe de cast para fazer o hint no tipo desejado.

- SapGuiConnection:
  - SessionsList() -> [SapGuiSession]: Retorna uma list com as sessões.

- SapGuiConnection:
  - ConnectionsList() -> [SapGuiConnection]: Retorna uma list com as conexões.
  - CreateSession() -> SapGuiSession: Abre uma nova sessão na conexão.
  - SessionsUser() -> [SapGuiSession]: Obtém todas sessões do usuário.
  - SessionsInTransaction() -> [SapGuiSession]: Obtém todas sessões que está na transação.

- SapGuiComponentCollection:
  - ToList() -> [SapGuiComponent]: Retorna uma list com todos os itens da coleção.
  - LastItem() -> SapGuiComponent: Retona o útimo item da coleção.
  - ItemCast(index: int, on_raise: bool = True) -> SapCastTo: O item será retornado em uma classe pronto para fazer o cast para o tipo do item desejado.

- SapGuiCollection:
  - ToList() -> [object]: Retorna uma list com todos os itens da coleção.
  - LastItem() -> object: Retona o útimo item da coleção.

- SapGuiFrameWindow:
  - SetFocusWindows() -> None: Isso faz o windows focar na janela indepedente do estado atual do mesmo.

- SapGuiSession:
  - GetAlertStatusPane() -> SapGuiStatusPane: Obtém a barra de alerta principal.

- SapGuiStatusPane:
  - HasInText(text: str) -> bool: Verifica se tem um texto específico dentro do texto do painel.

- GuiScrollbar:
  - load_all() -> None: Faz o carregamento completo do componente, rolando do começo até o fim do scroll.
"""