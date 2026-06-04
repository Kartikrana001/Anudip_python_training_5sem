charging_percentage = int(input("Enter the percentage of phone charge: "))
electricity_status = True
while charging_percentage < 100 and electricity_status:
    print(f"Phone is charging... {charging_percentage}%")
    charging_percentage += 10
else:
    print("Phone is charged..")
