from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiNetChart(GuiShell):
    """ O GuiNetChart é uma ferramenta poderosa para exibir e modificar diagramas de relacionamento entre entidades.
    É de natureza muito técnica e só deve ser utilizado para gravação e reprodução,
    pois a maioria dos parâmetros não pode ser determinada de outra forma.
    """

    def get_link_content(self, link_id: int, text_id: int) -> str:
        """ Retorna o conteúdo do link.
        link_id: índice do link.
        text_id: valor interno a ser determinado durante a gravação.
        """
        return self.component.GetLinkContent(link_id, text_id)

    def get_node_content(self, node_id: int, text_id: int) -> str:
        """ Retorna o conteúdo do nó.
        node_id: índice do nó.
        text_id: valor interno a ser determinado durante a gravação.
        """
        return self.component.GetNodeContent(node_id, text_id)

    def send_data(self, data: str) -> None:
        """ Emula a saída de cada ação acionada no lado do controle. O resultado da ação é enviado para o servidor.
        Atualmente, não é possível selecionar ou desselecionar objetos individuais no lado do cliente e reproduzir/criptografar essas ações "locais".
        """
        self.component.SendData(data)

    @property
    def link_count(self) -> int:
        """ Número de links na rede (somente leitura).
        """
        return self.component.LinkCount

    @property
    def node_count(self) -> int:
        """ Número de nós na rede (somente leitura).
        """
        return self.component.NodeCount
