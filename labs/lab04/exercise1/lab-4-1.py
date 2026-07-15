kwh = int(input())
if kwh == 100:
    totalBill = kwh * 0.3
else:
    if kwh >= 100 and kwh <= 200:
        totalBill = 100 * 0.3 + kwh - 100 * 0.5
    else:
        if kwh > 200:
            totalBill = 100 * 0.3 + kwh - 100 * 0.75
print(totalBill)
