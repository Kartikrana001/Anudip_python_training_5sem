# Employee Payroll Management System

def load_employees():
    employees = []

    file = open("employees.txt", "r")

    for line in file:
        data = line.strip().split(",")
        employees.append(data)

    file.close()
    return employees


def display_employees(employees):
    print("\nEmployee Records")
    for emp in employees:
        print(emp[0], emp[1], emp[2])


def search_employee(employees):
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp[0] == emp_id:
            print("\nEmployee Found")
            print("ID:", emp[0])
            print("Name:", emp[1])
            print("Salary:", emp[2])
            return

    print("Employee Not Found")


def average_salary(employees):
    total = 0

    for emp in employees:
        total += int(emp[2])

    avg = total / len(employees)

    print("Average Salary =", avg)


def highest_lowest_salary(employees):
    highest = employees[0]
    lowest = employees[0]

    for emp in employees:

        if int(emp[2]) > int(highest[2]):
            highest = emp

        if int(emp[2]) < int(lowest[2]):
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest)

    print("\nLowest Paid Employee")
    print(lowest)


def salary_above_50000(employees):
    print("\nEmployees earning above 50000")

    for emp in employees:
        if int(emp[2]) > 50000:
            print(emp)


def add_employee(employees):

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")

    employees.append([emp_id, name, salary])

    file = open("employees.txt", "a")
    file.write("\n" + emp_id + "," + name + "," + salary)
    file.close()

    print("Employee Added Successfully")


def salary_category(employees):

    print("\nSalary Categories")

    for emp in employees:

        salary = int(emp[2])

        if salary >= 60000:
            category = "High"

        elif salary >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(emp[1], "-", category)


# Main Program

employees = load_employees()

while True:

    print("\n===== Employee Payroll Management =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Salary Above 50000")
    print("6. Add Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_employees(employees)

    elif choice == 2:
        search_employee(employees)

    elif choice == 3:
        average_salary(employees)

    elif choice == 4:
        highest_lowest_salary(employees)

    elif choice == 5:
        salary_above_50000(employees)

    elif choice == 6:
        add_employee(employees)

    elif choice == 7:
        salary_category(employees)

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
