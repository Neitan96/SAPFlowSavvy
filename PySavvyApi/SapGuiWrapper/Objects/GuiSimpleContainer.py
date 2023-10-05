from PySavvyApi.SapGuiWrapper.Objects.GuiVContainer import GuiVContainer


class GuiSimpleContainer(GuiVContainer):
    """ Este contêiner representa subtelas não roláveis. Ele não possui nenhuma funcionalidade
    além das interfaces herdadas.
    O prefixo do tipo é sub, o nome é gerado a partir das configurações do dicionário de dados.
    """

    def get_list_property(self, property_name: str) -> str:
        """ Obtém uma propriedade da lista.
        property: A propriedade que você deseja obter. Consulte a documentação do objeto GuiLabel para obter mais informações.
        Retorna o valor da propriedade especificada.
        """
        return self.component.GetListProperty(property_name)

    def get_list_property_non_rec(self, property_name: str) -> str:
        """ Obtém uma propriedade da lista sem considerar propriedades de elementos pais.
        property: A propriedade que você deseja obter. Consulte a documentação do objeto GuiLabel para obter mais informações.
        Retorna o valor da propriedade especificada, ignorando propriedades de elementos pais.
        """
        return self.component.GetListPropertyNonRec(property_name)

    @property
    def is_list_element(self) -> bool:
        """ Esta propriedade é True se o elemento estiver em uma lista ABAP, não em uma tela dynpro.
        """
        return self.component.IsListElement

    @property
    def is_step_loop(self) -> bool:
        """ Esta propriedade é True se o contêiner for um contêiner de loop de etapa.
        """
        return self.component.IsStepLoop

    @property
    def loop_col_count(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de colunas no loop de etapa.
        """
        return self.component.LoopColCount

    @property
    def loop_current_col(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número atual da linha no loop de etapa.
        """
        return self.component.LoopCurrentCol

    @property
    def loop_current_col_count(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de colunas na linha atual do loop de etapa.
        """
        return self.component.LoopCurrentColCount

    @property
    def loop_current_row(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número atual da coluna no loop de etapa.
        """
        return self.component.LoopCurrentRow

    @property
    def loop_row_count(self) -> int:
        """ Se o contêiner for um contêiner de loop de etapa, esta propriedade conterá o número de linhas no loop de etapa.
        """
        return self.component.LoopRowCount