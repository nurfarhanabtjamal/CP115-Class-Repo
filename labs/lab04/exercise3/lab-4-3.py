hours = int(input())
if hours <= 2:
    parkingFee = 0
else:
    if hours > 5:
        parkingFee = 6 + ((hours - 5) * 3)
    else:
        parkingFee = ((hours - 2)* 2)
    if parkingFee > 30:
        parkingFee = 30
print(parkingFee)
