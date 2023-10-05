from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiHTMLViewer(GuiShell):
    """ O GuiHTMLViewer é usado para exibir um documento HTML dentro do SAP GUI.
    """

    def context_menu(self):
        """ Chamar contextMenu simula a solicitação do menu de contexto.
        Observe que essa função se aplica apenas a menus de contexto fornecidos pelo backend,
        não ao menu de contexto local, gerado pelo controle HTML.
        """
        self.component.ContextMenu()

    def sap_event(self, frame_name: str, post_data: str, url: str):
        """ Esta função envia um formulário HTML para o backend.

        Observações:

        Se o formulário deve ser enviado usando o método GET, os dados são anexados ao nome do evento
        no formato usual de URL HTTP, por exemplo:

        Exemplo de código:
        sapEvent("Frame1", "", "sapevent:SUBMIT_FORM_AS_GET_METHOD?FirstName=John&LastName=Smith")

        Neste caso, PostData é sempre uma string vazia.

        Se o formulário deve ser enviado usando o método POST, os dados são transportados no parâmetro PostData:

        Exemplo de código:
        sapEvent("Frame1", "FirstName=John&LastName=Smith", "sapevent:SUBMIT_FORM_AS_POST_METHOD")

        FrameName: Este é o nome do quadro no qual o formulário HTML que foi enviado está localizado.
        PostData: Contém os dados do formulário quando um envio é feito usando o método POST.
        Url: Este é o URL enviado para o backend. O nome do protocolo para a string de URL é "sapevent:"
            Isso é seguido pelo nome do evento conforme definido na Propriedade de Ação do formulário HTML
            que está sendo chamado.
        """
        self.component.SapEvent(frame_name, post_data, url)

    @property
    def browser_handle(self) -> object:
        return self.component.BrowserHandle

    @property
    def document_complete(self) -> int:
        return self.component.DocumentComplete