from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiTree(GuiShell):
    """ O Tree Control oferece suporte a três tipos de árvore.
    """

    def change_checkbox(self, node_key: str, item_name: str, checked: bool) -> None:
        """ Emula a mudança de estado de uma caixa de seleção.
        """
        self.component.ChangeCheckbox(node_key, item_name, checked)

    def click_link(self, node_key: str, item_name: str) -> None:
        """ Emula a ativação de um link.
        """
        self.component.ClickLink(node_key, item_name)

    def collapse_node(self, node_key: str) -> None:
        """ Fecha o nó com a chave de nó especificada.
        """
        self.component.CollapseNode(node_key)

    def default_context_menu(self) -> None:
        """ Solicita um menu de contexto para todo o Controle de Árvore.
        """
        self.component.DefaultContextMenu()

    def double_click_item(self, node_key: str, item_name: str) -> None:
        """ Emula o duplo clique em um item de texto.
        """
        self.component.DoubleClickItem(node_key, item_name)

    def double_click_node(self, node_key: str) -> None:
        """ Emula o duplo clique em um nó.
        """
        self.component.DoubleClickNode(node_key)

    def ensure_visible_horizontal_item(self, node_key: str, item_name: str) -> None:
        """ Desloca a Árvore horizontalmente até que o item seja visível.
        """
        self.component.EnsureVisibleHorizontalItem(node_key, item_name)

    def expand_node(self, node_key: str) -> None:
        """ Expande o nó com a chave de nó especificada.
        """
        self.component.ExpandNode(node_key)

    def find_node_key_by_path(self, path: str) -> str:
        """ Encontra a chave de nó pelo seu caminho.
        """
        return self.component.FindNodeKeyByPath(path)

    def get_abap_image(self, key: str, name: str) -> str:
        """ Recupera o código do ícone de uma imagem exibida no item especificado.
        """
        return self.component.GetAbapImage(key, name)

    def get_all_node_keys(self):
        """ Retorna uma coleção de todas as chaves de nó presentes no Controle de Árvore.
        """
        return self.component.GetAllNodeKeys()

    def get_check_box_state(self, node_key: str, item_name: str) -> int:
        """ Recupera o estado da caixa de seleção (1 = Marcado, 0 = Desmarcado).
        """
        return self.component.GetCheckBoxState(node_key, item_name)

    def get_column_col(self, col_name: str):
        """ Retorna as chaves de todos os itens na coluna especificada.
        """
        return self.component.GetColumnCol(col_name)

    def get_column_headers(self):
        """ Retorna uma coleção de cabeçalhos de coluna.
        """
        return self.component.GetColumnHeaders()

    def get_column_index_from_name(self, key: str) -> int:
        """ Retorna o índice da coluna (começando em 1) da coluna especificada.
        """
        return self.component.GetColumnIndexFromName(key)

    def get_column_names(self):
        """ Retorna uma coleção de nomes de coluna.
        """
        return self.component.GetColumnNames()

    def get_column_title_from_name(self, key: str) -> str:
        """ Retorna o título da coluna especificada pelo parâmetro.
        """
        return self.component.GetColumnTitleFromName(key)

    def get_column_titles(self):
        """ Retorna uma coleção de títulos de coluna.
        """
        return self.component.GetColumnTitles()

    def get_focused_node_key(self) -> str:
        """ Retorna a chave do nó que está com foco.
        """
        return self.component.GetFocusedNodeKey()

    def get_hierarchy_level(self, key: str) -> int:
        """ Retorna o nível hierárquico da chave especificada, começando no nível 0.
        """
        return self.component.GetHierarchyLevel(key)

    def get_hierarchy_title(self) -> str:
        """ Retorna o título hierárquico.
        """
        return self.component.GetHierarchyTitle()

    def get_is_disabled(self, node_key: str, item_name: str) -> int:
        """ Retorna se o item especificado está desativado (1 = Desativado, 0 = Não desativado).
        """
        return self.component.GetIsDisabled(node_key, item_name)

    def get_is_high_lighted(self, node_key: str, item_name: str) -> int:
        """ Retorna se o item especificado está destacado (1 = Destacado, 0 = Não destacado).
        """
        return self.component.GetIsHighLighted(node_key, item_name)

    def get_item_height(self, node_key: str, item_name: str) -> int:
        """ Recupera a altura do item especificado em píxeis.
        """
        return self.component.GetItemHeight(node_key, item_name)

    def get_item_left(self, node_key: str, item_name: str) -> int:
        """ Recupera a posição esquerda do item especificado em píxeis.
        """
        return self.component.GetItemLeft(node_key, item_name)

    def get_item_style(self, node_key: str, item_name: str) -> int:
        """ Recupera o estilo do item especificado.
        """
        return self.component.GetItemStyle(node_key, item_name)

    def get_item_text(self, key: str, name: str) -> str:
        """ Retorna o texto do item especificado pelos parâmetros-chave e nome.
        """
        return self.component.GetItemText(key, name)

    def get_item_text_color(self, key: str, name: str) -> int:
        """ Recupera a cor da fonte do item especificado.
        """
        return self.component.GetItemTextColor(key, name)

    def get_item_tool_tip(self, key: str, name: str) -> str:
        """ Recupera a dica do item especificado.
        """
        return self.component.GetItemToolTip(key, name)

    def get_item_top(self, node_key: str, item_name: str) -> int:
        """ Recupera a posição superior do item especificado em píxeis.
        """
        return self.component.GetItemTop(node_key, item_name)

    def get_item_type(self, key: str, name: str) -> int:
        """ Recupera o tipo de item da árvore de colunas:
        trvTreeStructureHierarchy = 0
        trvTreeStructureImage = 1
        trvTreeStructureText = 2
        trvTreeStructureBool = 3
        trvTreeStructureButton = 4
        trvTreeStructureLink = 5
        """
        return self.component.GetItemType(key, name)

    def get_item_width(self, node_key: str, item_name: str) -> int:
        """ Recupera a largura do item especificado em pixels.
        """
        return self.component.GetItemWidth(node_key, item_name)

    def get_list_tree_node_item_count(self, node_key: str) -> int:
        """ Retorna o número de itens visíveis do nó especificado em uma árvore de lista.
        """
        return self.component.GetListTreeNodeItemCount(node_key)

    def get_next_node_key(self, node_key: str) -> str:
        """ Retorna a chave do próximo nó pertencente ao mesmo nó um nível acima.
        """
        return self.component.GetNextNodeKey(node_key)

    def get_node_abap_image(self, key: str) -> str:
        """ Recupera o código de ícone do nó especificado.
        """
        return self.component.GetNodeAbapImage(key)

    def get_node_children_count(self, key: str) -> int:
        """ Retorna o número de filhos diretos visíveis do nó especificado.
        """
        return self.component.GetNodeChildrenCount(key)

    def get_node_children_count_by_path(self, path: str) -> int:
        """ Retorna o número de filhos visíveis do nó especificado pelo caminho.
        """
        return self.component.GetNodeChildrenCountByPath(path)

    def get_node_height(self, key: str) -> int:
        """ Retorna a altura do nó especificado em pixels.
        """
        return self.component.GetNodeHeight(key)

    def get_node_index(self, key: str) -> int:
        """ Retorna o índice da chave especificada dentro do seu nó.
        """
        return self.component.GetNodeIndex(key)

    def get_node_item_headers(self, node_key: str):
        """ Retorna um objeto com os cabeçalhos de item do nó especificado.
        """
        return self.component.GetNodeItemHeaders(node_key)

    def get_node_key_by_path(self, path: str) -> str:
        """ Chave do nó especificado pelo caminho dado.
        """
        return self.component.GetNodeKeyByPath(path)

    def get_node_left(self, key: str) -> int:
        """ Retorna a posição esquerda do nó especificado em píxeis.
        """
        return self.component.GetNodeLeft(key)

    def get_node_path_by_key(self, key: str) -> str:
        """ Dado uma chave de nó, o caminho é recuperado (por exemplo, "2\1\2").
        """
        return self.component.GetNodePathByKey(key)

    def get_nodes_col(self):
        """ A coleção contém as chaves de todos os nós na árvore.
        """
        return self.component.GetNodesCol()

    def get_node_style(self, node_key: str) -> int:
        """ Recupera o estilo do nó especificado.
        """
        return self.component.GetNodeStyle(node_key)

    def get_node_text_by_key(self, key: str) -> str:
        """ Retorna o texto do nó especificado pela chave dada.
        """
        return self.component.GetNodeTextByKey(key)

    def get_node_text_by_path(self, path: str) -> str:
        """ O texto de um nó definido pelo caminho dado é retornado.
        """
        return self.component.GetNodeTextByPath(path)

    def get_node_text_color(self, key: str) -> int:
        """ Retorna a cor da fonte do nó especificado.
        """
        return self.component.GetNodeTextColor(key)

    def get_node_tool_tip(self, node_key: str) -> str:
        """ Retorna a dica de ferramenta do nó especificado.
        """
        return self.component.GetNodeToolTip(node_key)

    def get_node_top(self, key: str) -> int:
        """ Retorna a posição superior do nó especificado em píxeis.
        """
        return self.component.GetNodeTop(key)

    def get_node_width(self, key: str) -> int:
        """ Retorna a largura do nó especificado em pixels.
        """
        return self.component.GetNodeWidth(key)

    def get_parent(self, ckey: str) -> str:
        """ Chave do nó pai do nó especificado pela chave dada.
        """
        return self.component.GetParent(ckey)

    def get_previous_node_key(self, node_key: str) -> str:
        """ Retorna a chave do nó anterior pertencente ao mesmo nó um nível acima.
        """
        return self.component.GetPreviousNodeKey(node_key)

    def get_selected_nodes(self):
        """ Retorna uma coleção de nós selecionados.
        """
        return self.component.GetSelectedNodes()

    def get_selection_mode(self) -> int:
        """ Retorna o modo de seleção do Controle de Árvore:
        0: Seleção de Nó Único
        1: Seleção de Múltiplos Nós
        2: Seleção de Item Único
        3: Seleção de Múltiplos Itens
        """
        return self.component.GetSelectionMode()

    def get_style_description(self, n_style: int) -> str:
        """ Retorna a descrição do estilo especificado.
        """
        return self.component.GetStyleDescription(n_style)

    def get_sub_nodes_col(self, path: str):
        """ Retorna uma coleção de chaves de todos os subníveis do nó especificado pela chave dada.
        """
        return self.component.GetSubNodesCol(path)

    def get_tree_type(self) -> int:
        """ Retorna o tipo de árvore:
        0: Árvore Simples
        1: Árvore de Lista
        2: Árvore de Coluna
        """
        return self.component.GetTreeType()

    def header_context_menu(self, header_name: str) -> None:
        """ Solicita um menu de contexto para um cabeçalho.
        """
        self.component.HeaderContextMenu(header_name)

    def is_folder(self, node_key: str) -> int:
        """ Retorna True se o objeto especificado for um nó e não uma folha.
        """
        return self.component.IsFolder(node_key)

    def is_folder_expandable(self, node_key: str) -> int:
        """ Retorna True se a pasta pertencente ao nó especificado pode ser expandida.
        """
        return self.component.IsFolderExpandable(node_key)

    def is_folder_expanded(self, node_key: str) -> int:
        """ Retorna True se a pasta pertencente ao nó especificado estiver expandida.
        """
        return self.component.IsFolderExpanded(node_key)

    def item_context_menu(self, node_key: str, item_name: str) -> None:
        """ Solicita um menu de contexto para um item.
        """
        self.component.ItemContextMenu(node_key, item_name)

    def node_context_menu(self, node_key: str) -> None:
        """ Solicita um menu de contexto para um nó.
        """
        self.component.NodeContextMenu(node_key)

    def press_button(self, node_key: str, item_name: str) -> None:
        """ Emula o pressionamento de um botão.
        """
        self.component.PressButton(node_key, item_name)

    def press_header(self, header_name: str) -> None:
        """ Emula o clique em um cabeçalho.
        """
        self.component.PressHeader(header_name)

    def press_key(self, key: str) -> None:
        """ Emula o pressionamento de uma tecla.
        """
        self.component.PressKey(key)

    def select_column(self, column_name: str) -> None:
        """ Adiciona uma coluna à seleção de colunas, removendo a seleção de nós ou itens.
        """
        self.component.SelectColumn(column_name)

    def selected_item_column(self) -> str:
        """ Retorna o nome da coluna do item selecionado.
        """
        return self.component.SelectedItemColumn()

    def selected_item_node(self) -> str:
        """ Retorna a chave do nó do item selecionado.
        """
        return self.component.SelectedItemNode()

    def select_item(self, node_key: str, item_name: str) -> None:
        """ Emula a seleção de um item, removendo todas as outras seleções.
        """
        self.component.SelectItem(node_key, item_name)

    def select_node(self, node_key: str) -> None:
        """ Adiciona o nó com a chave especificada à seleção de nós.
        """
        self.component.SelectNode(node_key)

    def set_check_box_state(self, node_key: str, item_name: str, state: int) -> None:
        """ Marca ou desmarca a caixa de seleção na célula especificada do controle de árvore.
        Se o parâmetro "state" for igual a 0, a caixa de seleção é desmarcada; se o parâmetro for igual a 1, a caixa de seleção é marcada.
        """
        self.component.SetCheckBoxState(node_key, item_name, state)

    def set_column_width(self, column_name: str, width: int) -> None:
        """ Define a largura de uma coluna em pixels.
        """
        self.component.SetColumnWidth(column_name, width)

    def unselect_all(self) -> None:
        """ Remove todas as seleções.
        """
        self.component.UnselectAll()

    def unselect_column(self, column_name: str) -> None:
        """ Remove uma coluna da seleção de colunas.
        """
        self.component.UnselectColumn(column_name)

    def unselect_node(self, node_key: str) -> None:
        """ Remove o nó com a chave especificada da seleção de nós.
        """
        self.component.UnselectNode(node_key)

    @property
    def column_order(self) -> object:
        """ A propriedade ColumnOrder é usada para trabalhar com a sequência de colunas.
            O nome de cada coluna na árvore de colunas deve ocorrer exatamente uma vez.
        """
        return self.component.ColumnOrder

    @column_order.setter
    def column_order(self, column_order: object = None) -> None:
        """ A propriedade ColumnOrder é usada para trabalhar com a sequência de colunas.
            O nome de cada coluna na árvore de colunas deve ocorrer exatamente uma vez.
        """
        self.component.ColumnOrder = column_order

    @property
    def hierarchy_header_width(self) -> int:
        """ A largura do Hierarchy Header em pixels.
        """
        return self.component.HierarchyHeaderWidth

    @hierarchy_header_width.setter
    def hierarchy_header_width(self, width: int = None) -> None:
        """ A largura do Hierarchy Header em pixels.
        """
        self.component.HierarchyHeaderWidth = width

    @property
    def selected_node(self) -> str:
        """ Esta propriedade representa a chave do nó atualmente selecionado.
            A seleção de um nó remove outras seleções (ou seja, seleção de coluna e seleção de item).
        """
        return self.component.SelectedNode

    @selected_node.setter
    def selected_node(self, node_key: str = None) -> None:
        """ Esta propriedade representa a chave do nó atualmente selecionado.
            A seleção de um nó remove outras seleções (ou seja, seleção de coluna e seleção de item).
        """
        self.component.SelectedNode = node_key

    @property
    def top_node(self) -> str:
        """ Esta propriedade influencia a rolagem vertical do controle de árvore.
            TopNode contém a chave do nó que está localizado na borda superior do controle de árvore.
            A definição de um nó x como nó superior só é possível se houver nós visíveis suficientes abaixo de x para preencher a área de exibição do controle de árvore.
        """
        return self.component.TopNode

    @top_node.setter
    def top_node(self, top_node_key: str = None) -> None:
        """ Esta propriedade influencia a rolagem vertical do controle de árvore.
            TopNode contém a chave do nó que está localizado na borda superior do controle de árvore.
            A definição de um nó x como nó superior só é possível se houver nós visíveis suficientes abaixo de x para preencher a área de exibição do controle de árvore.
        """
        self.component.TopNode = top_node_key
