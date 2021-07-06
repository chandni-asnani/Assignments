class Htmd:

    def cal(self):
        res1 = self.i *(self.price[1]/100)
        max = 100
        print("enter billing demand")
        demand = int(input())
        if demand <= max:
            res2 = demand*(self.price[2])
        else:
            res2 = demand*(self.price[3])


        print("enter power factor in %")
        power_factor = int(input())
        if power_factor in range(90,96):
            res3 = res1 - (self.i* (self.price[4]/100)) 
        elif power_factor >95 :
            res3 =res1 -  (self.i*(self.price[5]/100)) 
        else:
            res3 = (self.i*(self.price[6]/100)) + res1

        tou = self.i*(self.price[7]/100)
        nighttime = self.i*(self.price[8]/100)

        result = res1 + res2 + res3 + tou + nighttime 
        return result