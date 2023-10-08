
from PySavvyApi.Modules.SavvySingIn import SavvySapSingIn
from PySavvyApi.SapGuiWrapper import *
from PySavvyApi.StdTCodes import *

# Essa função vai obter uma sessão do SAP independente da condição,
# se o SAP tiver fechado ele irá abrir, se não tiver conexão aberta
# ele vai abrir a conexão
session = SavvySapSingIn().get_session_loged(SapConnNames.ECC)
if not session.start_transaction('VA03'):
    print('Erro: Não foi possivel iniciar a transação VA03 pelo usuário ' + session.info.user)
    exit(0)

session.user_area(0).find_by_name_ex('VBAK-VBELN', GuiComponentType.GuiCTextField).text = '7062515975'
session.send_key().enter()
value_liq = session.find_by_id_cast('wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/txtVBAK-NETWR').GuiTextField()
print(f'Valor líquido do pedido é: {float(value_liq.text.replace(",",".")):.2f}')
session.close_session(True)
