# Student Result Processing System

def load_students():

    students = []

    file = open("results.txt", "r")

    for line in file:
        data = line.strip().split(",")
        students.append(data)

    file.close()

    return students


# Requirement 1: Display all student records
def display_students(students):

    print("\nStudent Records")

    for student in students:
        print("ID:", student[0], "| Name:", student[1], "| Marks:", student[2])


# Requirement 2: Search student using Student ID
def search_student(students):

    student_id = input("Enter Student ID: ")

    for student in students:

        if student[0] == student_id:

            print("\nStudent Found")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Marks:", student[2])

            return

    print("Student Not Found")


# Requirement 3: Find topper and lowest scorer
def topper_lowest(students):

    topper = students[0]
    lowest = students[0]

    for student in students:

        if int(student[2]) > int(topper[2]):
            topper = student

        if int(student[2]) < int(lowest[2]):
            lowest = student

    print("\nTopper")
    print(topper)

    print("\nLowest Scorer")
    print(lowest)


# Requirement 4: Calculate class average
def class_average(students):

    total = 0

    for student in students:
        total += int(student[2])

    average = total / len(students)

    print("Class Average =", average)


# Requirement 5: Count pass and fail students
def pass_fail_count(students):

    pass_count = 0
    fail_count = 0

    for student in students:

        if int(student[2]) >= 40:
            pass_count += 1
        else:
            fail_count += 1

    print("Pass Students =", pass_count)
    print("Fail Students =", fail_count)


# Requirement 6: Generate grades and write to grades.txt
def generate_grades(students):

    file = open("grades.txt", "w")

    print("\nGrade Report")

    for student in students:

        marks = int(student[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        print(student[1], "-", grade)

        file.write(student[0] + "," +
                   student[1] + "," +
                   str(marks) + "," +
                   grade + "\n")

    file.close()

    print("Grades Saved in grades.txt")


# Main Program

students = load_students()

while True:

    print("\n===== Student Result Processing System =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades Report")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_students(students)

    elif choice == 2:
        search_student(students)

    elif choice == 3:
        topper_lowest(students)

    elif choice == 4:
        class_average(students)

    elif choice == 5:
        pass_fail_count(students)

    elif choice == 6:
        generate_grades(students)

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
