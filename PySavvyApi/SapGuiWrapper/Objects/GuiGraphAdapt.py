from PySavvyApi.SapGuiWrapper.Objects.GuiShell import GuiShell


class GuiGraphAdapt(GuiShell):
    """ Para o controle do adaptador gráfico, apenas membros básicos do GuiShell estão disponíveis. A gravação e a reprodução não são possíveis.
    Observações
    Além dos novos controles baseados em ActiveX, o SAP GUI também vem com um conjunto de executáveis gráficos externos,
    por exemplo, para exibir um gráfico GANTT. Esses executáveis não são suportados pela API.
    Se durante a execução de um script um desses executáveis for iniciado, o script será bloqueado.
    Se você precisar automatizar um processo durante o qual um executável gráfico é exibido, você precisará de uma ferramenta
    de automação que permita manipular o SAP GUI usando a API de script e outros aplicativos do Windows usando métodos nativos.
    """

    pass