# Daily Expense Tracker and Report Generator

def load_expenses():

    expenses = []

    file = open("expenses.txt", "r")

    for line in file:
        data = line.strip().split(",")
        expenses.append(data)

    file.close()

    return expenses


def save_expenses(expenses):

    file = open("expenses.txt", "w")

    for expense in expenses:
        file.write(expense[0] + "," + str(expense[1]) + "\n")

    file.close()


# Requirement 1: Display all expenses
def display_expenses(expenses):

    print("\nAll Expenses")

    for expense in expenses:
        print(expense[0], "-", expense[1])


# Requirement 2: Calculate total expenditure
def total_expenditure(expenses):

    total = 0

    for expense in expenses:
        total += int(expense[1])

    print("Total Expenditure =", total)


# Requirement 3: Find highest and lowest expense category
def highest_lowest_expense(expenses):

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        if int(expense[1]) > int(highest[1]):
            highest = expense

        if int(expense[1]) < int(lowest[1]):
            lowest = expense

    print("\nHighest Expense Category")
    print(highest[0], "-", highest[1])

    print("\nLowest Expense Category")
    print(lowest[0], "-", lowest[1])


# Requirement 4: Display expenses greater than 800
def expenses_above_800(expenses):

    print("\nExpenses Greater Than 800")

    for expense in expenses:

        if int(expense[1]) > 800:
            print(expense[0], "-", expense[1])


# Requirement 5: Add new expense category
def add_expense(expenses):

    category = input("Enter Category Name: ")
    amount = input("Enter Amount: ")

    expenses.append([category, amount])

    save_expenses(expenses)

    print("Expense Added Successfully")


# Requirement 6: Update existing expense amount
def update_expense(expenses):

    category = input("Enter Category Name: ")

    for expense in expenses:

        if expense[0].lower() == category.lower():

            new_amount = input("Enter New Amount: ")

            expense[1] = new_amount

            save_expenses(expenses)

            print("Expense Updated Successfully")

            return

    print("Category Not Found")


# Requirement 7: Generate report.txt
def generate_report(expenses):

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    above_800 = []

    for expense in expenses:

        amount = int(expense[1])

        total += amount

        if amount > int(highest[1]):
            highest = expense

        if amount < int(lowest[1]):
            lowest = expense

        if amount > 800:
            above_800.append(expense)

    file = open("report.txt", "w")

    file.write("===== Expense Report =====\n\n")

    file.write("Total Expenses : " + str(total) + "\n")

    file.write(
        "Highest Expense Category : "
        + highest[0]
        + " ("
        + str(highest[1])
        + ")\n"
    )

    file.write(
        "Lowest Expense Category : "
        + lowest[0]
        + " ("
        + str(lowest[1])
        + ")\n\n"
    )

    file.write("Categories Spending More Than 800\n")

    for expense in above_800:
        file.write(expense[0] + " - " + str(expense[1]) + "\n")

    file.close()

    print("Report Generated Successfully in report.txt")


# Main Program

expenses = load_expenses()

while True:

    print("\n===== Daily Expense Tracker =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Find Highest and Lowest Expense")
    print("4. Display Expenses Greater Than 800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Report")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_expenses(expenses)

    elif choice == 2:
        total_expenditure(expenses)

    elif choice == 3:
        highest_lowest_expense(expenses)

    elif choice == 4:
        expenses_above_800(expenses)

    elif choice == 5:
        add_expense(expenses)

    elif choice == 6:
        update_expense(expenses)

    elif choice == 7:
        generate_report(expenses)

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
