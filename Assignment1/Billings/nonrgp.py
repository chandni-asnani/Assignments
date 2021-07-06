
class Nonrgp():

    def __init__(self, i):
        self.i = i
        


    def cal(self):
        res1 = (460/100)*self.i

        print("Enter KW")
        kw = int(input())


        if kw <= 5:
            res2 = 70
        elif kw in range(5,16):
            res2 = 90
        result = res1 + res2
        return result

            