from __future__ import annotations

from PySavvyApi.SapGuiWrapper.Objects.GuiComponent import GuiComponent
from PySavvyApi.SapGuiWrapper.Objects.GuiCollection import GuiCollection
from PySavvyApi.SapGuiWrapper.Objects.GuiComponentCollection import GuiComponentCollection
from PySavvyApi.SapGuiWrapper.Helpers.ComponentCast import ComponentCast


class GuiVComponent(GuiComponent):
    """ A interface GuiVComponent é exposta por todos os objetos visuais, como janelas, botões ou campos de texto.
    Assim como o GuiComponent, é uma interface abstrata. Qualquer objeto que suporte a interface GuiVComponent também expõe
    a interface GuiComponent.
    """

    def dump_state(self, inner_object: str) -> GuiCollection:
        """ Esta função despeja o estado do objeto. O parâmetro innerObject pode ser usado para especificar para qual
        objeto interno os dados devem ser despejados. Somente os componentes mais complexos, como o GuiCtrlGridView, suportam esse parâmetro.
        Todos os outros componentes sempre descartam seu estado completo. Todos os componentes que suportam este parâmetro têm em
        comum o fato de retornarem informações gerais sobre o estado do controle se o parâmetro “innerObject” contiver uma string vazia.
        Os valores disponíveis para o parâmetro innerObject são especificados como parte da descrição da classe dos componentes que o suportam.
        """
        return ComponentCast.get_instance(self.component.DumpState(inner_object))

    def set_focus(self) -> None:
        """ Esta função pode ser usada para definir o foco em um objeto. Se um usuário interagir com SAP GUI,
        ele moverá o foco sempre que a interação for com um novo objeto. Interagir com um objeto por meio do componente
        de script não altera o foco. Há alguns casos em que o aplicativo SAP verifica explicitamente o foco e
        se comporta de maneira diferente dependendo do objeto em foco.
        """
        self.component.SetFocus()

    def visualize(self, on: bool, inner_object: str) -> bool:
        """ Chamar este método de um componente exibirá uma moldura vermelha ao redor do componente especificado se o parâmetro on for verdadeiro.
        O quadro será removido se on for falso. Alguns componentes, como GuiCtrlGridView, suportam a exibição do quadro em torno de objetos internos,
        como células. O formato da string innerObject é o mesmo do método dumpState.
        """
        return self.component.Visualize(on, inner_object)

    @property
    def acc_label_collection(self) -> GuiComponentCollection:
        """ A coleção contém objetos do tipo GuiLabel que foram atribuídos a este controle no ABAP Screen Painter.
        """
        return ComponentCast.get_instance(self.component.AccLabelCollection)

    @property
    def acc_text(self) -> str:
        """ Um texto adicional para suporte de acessibilidade.
        """
        return self.component.AccText

    @property
    def acc_text_on_request(self) -> str:
        """ Um texto adicional para suporte de acessibilidade.
        """
        return self.component.AccTextOnRequest

    @property
    def acc_tooltip(self) -> str:
        """ Um texto de dica adicional para suporte de acessibilidade.
        """
        return self.component.AccTooltip

    @property
    def changeable(self) -> bool:
        """ Um objeto pode ser alterado se não estiver desabilitado nem somente leitura.
        """
        return self.component.Changeable

    @property
    def default_tooltip(self) -> str:
        """ Texto de dica de ferramenta gerado a partir do texto curto definido no
        dicionário de dados para determinado tipo de elemento de tela.
        """
        return self.component.DefaultTooltip

    @property
    def icon_name(self) -> str:
        """ Se ao objeto foi atribuído um ícone, então esta propriedade é o nome do ícone, caso contrário, é uma string vazia.
        """
        return self.component.IconName

    @property
    def is_symbol_font(self) -> bool:
        """ A propriedade é TRUE se o texto do componente for visualizado na fonte do símbolo SAP.
        """
        return self.component.IsSymbolFont

    @property
    def modified(self) -> bool:
        """ Um objeto é modificado se seu estado tiver sido alterado pelo usuário e essa alteração ainda não tiver sido enviada ao sistema SAP.
        """
        return self.component.Modified

    @property
    def parent_frame(self) -> GuiComponent:
        """ Se o controle estiver hospedado no objeto Frame, o valor da propriedade será esse quadro.
        """
        return ComponentCast.get_instance(self.component.ParentFrame)

    @property
    def text(self) -> str:
        """ O valor desta propriedade depende muito do tipo de objeto no qual ela é chamada.
        Isto é óbvio para campos de texto ou itens de menu. Por outro lado, esta propriedade está vazia para botões da
        barra de ferramentas e é o ID da classe para shells. Você pode ler a propriedade de texto de um rótulo, mas não
        pode alterá-la, enquanto só pode definir a propriedade de texto de um campo de senha, mas não lê-la.
        """
        return self.component.Text

    @text.setter
    def text(self, text: str = None) -> None:
        """ O valor desta propriedade depende muito do tipo de objeto no qual ela é chamada.
        Isto é óbvio para campos de texto ou itens de menu. Por outro lado, esta propriedade está vazia para botões da
        barra de ferramentas e é o ID da classe para shells. Você pode ler a propriedade de texto de um rótulo, mas não
        pode alterá-la, enquanto só pode definir a propriedade de texto de um campo de senha, mas não lê-la.
        """
        self.component.Text = text

    @property
    def tooltip(self) -> str:
        """ A dica de ferramenta contém um texto projetado para ajudar o usuário a entender o significado de um determinado campo de texto ou botão.
        """
        return self.component.Tooltip

    @property
    def screen_left(self) -> int:
        """ A posição y do componente nas coordenadas da tela.
        """
        return self.component.ScreenLeft

    @property
    def screen_top(self) -> int:
        """ A posição x do componente nas coordenadas da tela.
        """
        return self.component.ScreenTop

    @property
    def top(self) -> int:
        """ Coordenada superior do elemento nas coordenadas da tela.
        """
        return self.component.Top

    @property
    def left(self) -> int:
        """ Posição esquerda do elemento nas coordenadas da tela.
        """
        return self.component.Left

    @property
    def width(self) -> int:
        """ Largura do componente em pixels.
        """
        return self.component.Width

    @property
    def height(self) -> int:
        """ Altura do componente em pixels.
        """
        return self.component.Height
