total = 0

price = int(input("Enter Item Price: "))

while price != 0:
    total = total + price
    price = int(input("Enter Item Price: "))

print("Total Bill Amount: ₹", total)
