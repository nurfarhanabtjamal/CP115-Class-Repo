hours = int(input())
if hours <= 2:
    parkingfee = 0
else:
    if hours <= 5:
        parkingfee = hours - 2 * 2
    else:
        parkingfee = hours - 2 * 3
    if fee > 30:
        fee = 30
print(parkingfee)
