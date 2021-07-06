from base import Bill

d = {1 : "RGP",
    2:"GLP",
    3:"NON-RGP",
    4:"LTP",
    5:"LTMD1",
    6:"SL",
    7:"Lev",
    8:"Tmp",
    9:"LTMD2",
    10:"HTMD1",
    11:"HTMD2",
    12:"HTMD3",
    13:"EV"
}
print("enter units")
number = int(input())
print("enter 1 for rgp, 2 for glp, 3 for non-rgp ,4 for ltp, 5 for ltmd_1, 6 for sl, 7 for lev , 8 for tmp, 9 for ltmd2 , 10 for htmd1, 11 for htmd2, 12 for htmd3, 13 for ev")
category = int(input())
if category == 1:
    print("enter 1 for rgp and 2 for bpl")
    sub_cat = {
        1: "rgp",
        2: "bpl",
    }
    sub = int(input())
    print(Bill(number).calculate(category=d[category], sub=sub_cat[sub]))
else:
    print(Bill(number).calculate(category=d[category]))














































































