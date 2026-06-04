units = input("Enter units consumed: ")

if not units.isdigit():
    print("Invalid input!")
else:
    units = int(units)

    if units <= 100:
        bill = units * 5
        category = "Low Consumption"
    elif units <= 200:
        bill = units * 7
        category = "Medium Consumption"
    else:
        bill = units * 10
        category = "High Consumption"

    print("Units Consumed:", units)
    print("Total Bill: ₹", bill)
    print("Category:", category)
