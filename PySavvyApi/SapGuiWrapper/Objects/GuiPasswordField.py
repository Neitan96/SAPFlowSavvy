from PySavvyApi.SapGuiWrapper.Objects.GuiTextField import GuiTextField


class GuiPasswordField(GuiTextField):
    """ A única diferença entre GuiTextField e GuiPasswordField é que a propriedade Text não pode ser lida para um campo de senha.
    O texto retornado está sempre vazio. Durante a gravação a senha também não é salva no script gravado. GuiPasswordField
    estende o GuiTextField. O prefixo do tipo é pwd, o nome é o nome do campo retirado do dicionário de dados SAP.
    """

    pass
