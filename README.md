# SAPFlowSavvy - Toolkit de automatização para SAP Gui

![GitHub](https://img.shields.io/github/license/Neitan96/SAPFlowSavvy)
![Static Badge](https://img.shields.io/badge/version-developing-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Neitan96/SAPFlowSavvy)
[![Python](https://img.shields.io/badge/python-3.9.6%2B-blue)](https://www.python.org/downloads/release/python-396/)
[![VBA](https://img.shields.io/badge/VBA-Excel-green)](https://docs.microsoft.com/en-us/office/vba/api/overview/excel)

Este repositório é uma coleção de APIs desenvolvidas em *Python* e *VBA* projetadas para simplificar e acelerar a criação de automações no SAP GUI. O SAP GUI é uma ferramenta poderosa para interagir com sistemas SAP, mas sua automação muitas vezes requer códigos extensos e complexos, essa API procura resolver esse problema, fornecendo funcionalidades pré-fabricadas que permite que você automatize tarefas SAP de forma eficiente e sem a necessidade de codificação extensiva.

## Autor - **Nathan Almeida** (Neitan96):

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/Neitan96)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/neitan96/)
[![Instagram](https://img.shields.io/badge/Instagram-Profile-orange?style=flat&logo=instagram)](https://www.instagram.com/neitan96/)

## Principais características

- (*Em andamento*) Constantes de **TCodes** comuns do SAP para uso rápido.
- **Multi-linguagem**: Disponível para *Python* e para *VBA*(com algumas limitações).
- **Classes Wrapper**(Embrulho) da API do Sap Gui para facilitar o code-complete.
- Classes Wrapper **documentadas em português** dispensando a consulta constante na documentação oficial do SAP.
- (*Em andamento*) **Funções customizadas** nas classes Wrapper para auxiliar no dia a dia.
- (*Em andamento*) **Scripts complexos pré-programados**, como:
  - ***Armazenamento de credenciais:*** Faz o armazenamento das credenciais do SAP para o usuário não precisar ficar logando manualmente, ótimo para scripts autônomos.
  - ***Login no SAP:*** Faz o login no SAP Verificando todas as possibilidades, login e senha errados, caixas pos login(tentativas de logins, multi-login, copyrigth, timeout), caso não tenha sessão aberta.

## Exemplos

#### **Python:**

```python
# TODO
```

#### **VBA:**
```vbs
' TODO
```

## Melhorias futuras
* Documentações e tutoriais
* Fluxograma do componentes SAP Gui
* Registro de execução e erros
* Funções para lidar com GridView
  * Selecão, alteração e criação de layouts
  * Possibilidade de exportar GridView que não tem a opção de exportar
  * Varredura e busca de valores em GridView
  * Carregamento rápido da GridView completa
  * Funções de filtros
  * Fórmulas para GridView, como soma, média e etc.
* Funções para pop-ups comuns:
  * Seleção múltipla.
  * Botões comuns: limpar, executar, cancelar e etc.
* Funções extras:
  * Verificação de timeout
* Funções de telas padrões do SAP
  * Migo
  * /SCWM/PACK
  * ...
* Função CastTo na classe base

## Links úteis SAP

- [SAP GUI Scripting API - Pdf](https://help.sap.com/doc/9215986e54174174854b0af6bb14305a/760.01/en-US/sap_gui_scripting_api_761.pdf)
- [SAP GUI Scripting API - Web](https://help.sap.com/docs/sap_gui_for_windows/b47d018c3b9b45e897faf66a6c0885a8/babdf65f4d0a4bd8b40f5ff132cb12fa.html)
- [TCodes do SAP](https://www.sap-tcodes.org/)
- [SAP Datasheet](https://www.sapdatasheet.org/)

## Aviso Legal

Este projeto não é afiliado, endossado ou mantido pela SAP SE. SAP é uma marca registrada da SAP SE em vários países.