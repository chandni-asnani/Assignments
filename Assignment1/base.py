
from Billings.rgp import RGP
from Billings.nonrgp import Nonrgp
from Billings.glp import Glp
from Billings.ltp import Ltp
from Billings.ltmd1 import Ltmd_1
from Billings.sl import SL
from Billings.lev import Lev
from Billings.tmp import Tmp

data = {
        "RGP":  RGP,
        "NON-RGP": Nonrgp,
        "GLP": Glp,
        "LTP" : Ltp,
        "LTMD1" : Ltmd_1,
        "SL" : SL,
        "Lev" : Lev,
        "Tmp" : Tmp

    }

class Bill:

    def __init__(self,number):
        self.i = number

    


    def calculate(self, category=None, sub=None):
        if sub == 'rgp':
            data["RGP"](self.i).rgp()
        elif sub == 'bpl':
            data["RGP"](self.i).bpl()
        else:
            data[category](self.i).cal()



