
class RGP():

    def __init__(self,i):
        self.i = i
        

    def rgp(self):
            if self.i in range(1,51):
                res1 = self.i*(320/100)
                
            elif self.i in range(51,201):
                res2 = self.i - 50
                res3 = 50 * (320/100)
                res4 = res2 * (395/100)
                res1 = res4+res3

            else:
                res2 = self.i - 200
                res3 = 50 * (320/100)
                res4 = 150 * (395/100)
                res5 = res2 * (500/100)
                res1 = res3+res4+res5




            charge = 0
            print("select phase")  
            phase = int(input())      
            if phase == 1:
                charge = 25
            elif phase == 3:
                charge == 65

            result = res1 + charge
            return result

        
    def bpl(self):
        
            if self.i in range(1,51):
                res1 = self.i*(150/100)
                
            elif self.i in range(51,201):
                res2 = self.i - 50
                res3 = 50 * (150/100)
                res4 = res2 * (395/100)
                res1 = res4+res3
            else:
                res2 = self.i - 200
                res3 = 50 * (150/100)
                res4 = 150 * (395/100)
                res5 = res2 * (500/100)
                res1 = res3+res4+res5

            charge = 5
            result = res1 +  charge
            return result
        

    