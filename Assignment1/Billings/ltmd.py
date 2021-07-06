class Ltmd:


    def cal(self):
        print("Enter Billing demand")
        d = int(input())
        if d <= 50:
            res1 = self.i * (self.price[1]/100)
        else:
            res1 = self.i * (self.price[2]/100)
        
        if d <= 50:
            res2 = d*(self.price[3])
        elif d in range(50,81):
            res2 = d*(self.price[4])
        else:
            res2 = d*(self.price[5])


        print("enter power factor in %")
        power_factor = int(input())
        if power_factor in range(90,96):
            res3 = (self.i* (self.price[6]/100)) + self.i
        elif power_factor >95 :
            res3 = (self.i*(self.price[7]/100)) + self.i
        else:
            res3 = (self.i*(self.price[8]/100)) + self.i

        result = res1 + res2 + res3
        return result




