# SapGuiApiHelper
Bibliotecas para auxiliar na automatização do SAP Gui

![Static Badge](https://img.shields.io/badge/Autor-Neitan96-purple?link=https%3A%2F%2Fgithub.com%2FNeitan96%2F)
![Static Badge](https://img.shields.io/badge/version-Alpha%200.1-blue)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

## Exemplos:

#### Python
```python
sap_gui = SapGui()
session = sap_gui.GetSessionLoged()
```

## Melhorias futuras:
* Registro de execução e erros
* Funções para lidar com tabelas do SAP
  * Funções para selecão de layouts
* Funções para pop-ups padrões:
  * Seleção multipla
  * Filtros
  * Etc
* Verificar tela de login ao verificar timeout

### Todo only Python:
* Nenhuma

### Todo only VBA:
* Voltar ao menu principal ao fazer login
* Retorna a nova sessão ao fazer login, para os casos que criamos nova sessão para login