import win32com.client


class GuiUtils:

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch):
        self.class_attrs = ['component']
        self.component = component

    def __getattr__(self, attr):
        return getattr(self.component, attr)

    def __setattr__(self, attr, value):
        if attr in self.__dict__ or attr == 'class_attrs' or attr in self.class_attrs:
            super().__setattr__(attr, value)
        else:
            setattr(self.component, attr, value)

    def close_file(self, file: int) -> None:
        """ Esta função fecha um arquivo que foi aberto usando OpenFile.
        """
        self.component.CloseFile(file)

    def open_file(self, name: str) -> int:
        """ O arquivo será criado na pasta de documentos SAP GUI.
        O valor de retorno é um identificador para o arquivo.
        name: Nome do arquivo de texto a ser criado. Por motivos de segurança, este nome não deve conter nenhuma informação de caminho.
        """
        return self.component.OpenFile(name)

    def show_message_box(self, title: str, text: str, msg_icon: int, msg_type: int) -> int:
        """ Mostra uma caixa de mensagem.
        O valor de retorno será uma das constantes GuiMessageBoxResult.
        title: título da caixa de mensagem
        text: texto da caixa de mensagem.
        msg_icon: msg_icon define o ícone a ser usado para a caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxType.
        msg_type: msg_type define os botões disponíveis na caixa de mensagem e deve ser definido como uma das constantes GuiMessageBoxOption.
        """
        return self.component.ShowMessageBox(title, text, msg_icon, msg_type)

    def write(self, file: int, text: str) -> None:
        """ Escreva texto em um arquivo aberto sem uma nova linha no final.
        """
        return self.component.Write(file, text)

    def write_line(self, file: int, text: str) -> None:
        """ Escreva o texto em um arquivo aberto com uma nova linha no final.
        """
        return self.component.WriteLine(file, text)
