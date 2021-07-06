from base import Bill

d = {1 : "RGP",
    2:"GLP",
    3:"NON-RGP",
    4:"LTP",
    5:"LTMD1",
    6:"SL",
    7:"Lev",
    8:"Tmp"
}
print("enter units")
number = int(input())
print("enter 1 for rgp, 2 for glp, 3 for non-rgp ,4 for ltp, 5 for ltmd_1, 6 for sl, 7 for lev , 8 for tmp")
category = int(input())
if category == 1:
    print("enter 1 for rgp and 2 for bpl")
    sub_cat = {
        1: "rgp",
        2: "bpl",
    }
    sub = int(input())
    Bill(number).calculate( category=d[category], sub=sub_cat[sub])
else:
    Bill(number).calculate(category=d[category])














































































