from PySavvyApi.Modules.SapSingIn import SavvySapSingIn
from PySavvyApi.StdTCodes import *
from PySavvyApi.SapGuiWrapper import *

singing_m = SavvySapSingIn()
singing_m.get_session_loged(SapConnNames.EWM)