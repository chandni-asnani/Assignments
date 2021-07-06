
from Billings.rgp import RGP
from Billings.nonrgp import Nonrgp
from Billings.glp import Glp
from Billings.ltp import Ltp
from Billings.ltmd1 import Ltmd_1
from Billings.sl import SL
from Billings.lev import Lev
from Billings.tmp import Tmp
from Billings.ltmd2 import Ltmd_2
from Billings.htmd_1 import Htmd_1
from Billings.htmd_2 import Htmd_2
from Billings.htmd_3 import Htmd_3
from Billings.ev import Ev

data = {
        "RGP":  RGP,
        "NON-RGP": Nonrgp,
        "GLP": Glp,
        "LTP" : Ltp,
        "LTMD1" : Ltmd_1,
        "SL" : SL,
        "Lev" : Lev,
        "Tmp" : Tmp,
        "LTMD2" : Ltmd_2,
        "HTMD1" : Htmd_1,
        "HTMD2" :Htmd_2,
        "HTMD3" : Htmd_3,
        "EV": Ev

    }

class Bill:

    def __init__(self,number):
        self.i = number
        

    


    def calculate(self, category=None, sub=None):
        if sub == 'rgp':
            return data["RGP"](self.i).rgp()
        elif sub == 'bpl':
            return data["RGP"](self.i).bpl()
        else:
            return data[category](self.i).cal()





