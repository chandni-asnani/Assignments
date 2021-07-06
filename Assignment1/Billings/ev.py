class Ev:

    def __init__(self,i):
        self.i = i
        

    def cal(self):
        result1 = self.i* (410/100)
        max = 100
        print("enter billing demand")
        demand = int(input())
        if demand <= max:
            res2 = demand*(25*30)
        else:
            res2 = demand*(50*30)
        result = result1+res2

        return result