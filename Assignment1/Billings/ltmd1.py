class Ltmd_1:


    def __init__(self, i):
        self.i = i

    def cal(self):
        print("Enter Billing demand")
        d = int(input())
        if d <= 50:
            res1 = self.i * (465/100)
        else:
            res1 = self.i * (480/100)
        
        if d <= 50:
            res2 = d*150
        elif d in range(50,81):
            res2 = d*185
        else:
            res2 = d*245


        print("enter power factor in %")
        power_factor = int(input())
        if power_factor in range(90,96):
            res3 = (self.i* (0.15/100)) + self.i
        elif power_factor >95 :
            res3 = (self.i*(0.27/100)) + self.i
        else:
            res3 = (self.i*(3/100)) + self.i

        result = res1 + res2 + res3
        print(result)



