from PySavvyApi.Modules.SavvySessionsManager import SavvySessionsManager
from PySavvyApi.SapGuiWrapper import *
from PySavvyApi.StdTCodes import *

# Aqui obtemos o gerenciador de sessões, que pode obter sessões disponíveis para uso.
# isso inclui abrir o sap quando não estiver aberto, abrir sessão quando não tiver sessão
# aberta disponível para uso, se deseja considerar sessões no menu principal como sessões
# disponíveis para uso defina o parâmetro main_menu_available como verdadeiro.
sessions_manager = SavvySessionsManager(SapConnNames.ECC, SapConnNames.EWM)

# Aqui obtemos uma sessão disponível para uso com o gerenciador.
session = sessions_manager.get_available_session(SapConnNames.EWM)

if not session.start_transaction('VA03'):
    print('Erro: Não foi possivel iniciar a transação VA03 pelo usuário ' + session.info.user)
    exit(0)

session.user_area(0).find_by_name_ex('VBAK-VBELN', GuiComponentType.GuiCTextField).text = '7062515975'
session.send_key().enter()
value_liq = session.find_by_id_cast('wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/txtVBAK-NETWR').GuiTextField()
print(f'Valor líquido do pedido é: {float(value_liq.text.replace(",",".")):.2f}')
session.close_session(True)
