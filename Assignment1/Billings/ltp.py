class Ltp():

    def __init__(self,i):
        self.i = i
        

    def cal(self):
            res1 = (340/100)*self.i


            print("enter bhp")
            bhp = int(input())
            bhp*= 10
            result = res1 + bhp
            print(result)

