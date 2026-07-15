kwh = int(input())
if kwh == 100:
    charges = 0.3
else:
    if kwh >= 100 and kwh <= 200:
        charges = 0.5
    else:
        charges = 0.75
totalBill = charges * kwh
print(totalBill)
