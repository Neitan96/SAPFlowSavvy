from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiOfficeIntegration(GuiShell):
    """ O objeto GuiOfficeIntegration (Desktop Office Integration) oferece um contêiner para hospedar
    diversos tipos de aplicativos Office (Microsoft Word, Microsoft Excel, Microsoft Powerpoint).
    """

    def append_row(self, name: str, row: str) -> None:
        """ Adiciona uma nova linha a uma tabela especificada pelo parâmetro "name" na coleção de tabelas.
        O parâmetro "row" é a representação em base64 da linha binária.
        """
        self.component.AppendRow(name, row)

    def close_document(self, cookie: int, ever_changed: int, changed_after_save: int) -> None:
        """ Envia o evento de fechamento do documento especificado pelo parâmetro "cookie" para o servidor.
        O parâmetro "ever_changed" é do tipo Byte e indica se o documento foi alterado permanentemente.
        O parâmetro "changed_after_save" é do tipo Byte e indica se o documento foi alterado após o salvamento.
        """
        self.component.CloseDocument(cookie, ever_changed, changed_after_save)

    def custom_event(self, cookie: int, event_name: str, param_count: int, *params) -> None:
        """ Envia o evento personalizado "eventName" para o servidor.
        O documento especificado pelo parâmetro "cookie" é a fonte do evento.
        Os parâmetros adicionais, "par1" a "par12", são opcionais e podem ser usados para enviar até 12 parâmetros para o evento personalizado.
        """
        self.component.CustomEvent(cookie, event_name, param_count, *params)

    def remove_content(self, name: str) -> None:
        """ Remove o conteúdo de uma tabela na coleção de tabelas.
        O parâmetro "name" é o nome da tabela a ser removida.
        """
        self.component.RemoveContent(name)

    def save_document(self, cookie: int, changed: int) -> None:
        """ Envia o evento de salvamento do documento especificado pelo parâmetro "cookie" para o servidor.
        O parâmetro "changed" é do tipo Byte e indica se o documento foi alterado.
        """
        self.component.SaveDocument(cookie, changed)

    def set_document(self, index: int, document: str) -> None:
        """ Substitui ou adiciona um novo documento com o índice especificado.
        O parâmetro "document" é a representação em base64 do documento binário.
        """
        self.component.SetDocument(index, document)

    @property
    def document(self) -> object:
        """ O documento hospedado dentro do objeto GuiOfficeIntegration (somente leitura).
        """
        return self.component.Document

    @property
    def hosted_application(self) -> int:
        """ Este índice identifica a aplicação hospedada no objeto GuiOfficeIntegration (somente leitura).
        Valores possíveis são:
        1 - Microsoft Word
        2 - Microsoft Excel
        3 - Microsoft PowerPoint
        """
        return self.component.HostedApplication