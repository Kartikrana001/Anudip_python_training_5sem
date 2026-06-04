balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            print("Amount Deposited Successfully.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("Withdrawal Successful.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
