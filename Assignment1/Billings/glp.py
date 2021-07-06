
class Glp():

        def __init__(self, i):
                self.i = i
        

        def cal(self):
                if self.i in range(1,201):
                        res1 = self.i*(410/100)
                else:
                        res2 = self.i - 200
                        res3 = 200 * (410/100)
                        res4 = res2 * (480/100)
                        res1 = res3+res4

                charge = 0
                print("select phase")  
                phase = int(input())      
                if phase == 1:
                        charge = 30
                elif phase == 3:
                        charge = 70

                result = res1 + charge
                print(result)


                
                
                