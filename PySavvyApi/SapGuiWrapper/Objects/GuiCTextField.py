from PySavvyApi.SapGuiWrapper.Objects.GuiTextField import GuiTextField


class GuiCTextField(GuiTextField):
    """ Se o cursor estiver definido em um campo de texto do tipo GuiCTextField,
    um botão de caixa de combinação será exibido à direita do campo de texto.
    Pressionar este botão equivale a pressionar a tecla F4. O botão não é representado no
    modelo de objeto de script como um objeto separado; é considerado parte do campo de texto.
    Não há outras diferenças entre GuiTextField e GuiCTextField. GuiCTextField estende o GuiTextField.
    O prefixo do tipo é ctxt, o nome é o Fieldname retirado do dicionário de dados SAP.
    """

    # TODO Adicionar funções auxiliares

    pass
