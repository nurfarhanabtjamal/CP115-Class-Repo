income = int(input())
if income <= 50000:
    tax = 0.0
else:
    if income >= 100000:
        tax = 0.02
    else:
        tax = 0.01
totalTax = (income * tax)
print(totalTax)
