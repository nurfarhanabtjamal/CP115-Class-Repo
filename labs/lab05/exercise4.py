item_name1 = input("Enter the name of the item 1: ")
item_name2 = input("Enter the name of the item 2: ")
item_name3 = input("Enter the name of the item 3: ")
item1_price = float(input("Enter the price of the item 1: "))
item2_price = float(input("Enter the price of the item 2: "))
item3_price = float(input("Enter the price of the item 3: "))
quantity1 = int(input(f"Enter the quantity of {item_name1}: "))
quantity2 = int(input(f"Enter the quantity of {item_name2}: "))
quantity3 = int(input(f"Enter the quantity of {item_name3}: "))
tax_rate = 0.06

subtotal = int((item1_price*quantity1) + (item2_price*quantity2) + (item3_price*quantity3))
tax_amount = subtotal*tax_rate
totalcost = subtotal + tax_amount

print(f"subtotal = {subtotal}")
print(f"tax_amount = {tax_amount}")
print(f"totalcost = {totalcost}")