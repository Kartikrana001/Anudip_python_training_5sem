# ------------------------------------------
# Program: Student Attendance Tracker
# Objective:
# Create an attendance tracker for 30 students
# using a dictionary where Roll Number is the
# key and Attendance (Present/Absent) is the value.
# Display the roll numbers of all present students.
# ------------------------------------------

# Dictionary to store attendance
attendance = {}

# Input attendance of 30 students
for i in range(30):
    roll = int(input("Enter Roll Number: "))
    status = input("Enter P for Present and A for Absent: ")

    attendance[roll] = status

# Display roll numbers of present students
print("\nPresent Students:")

for roll in attendance:
    if attendance[roll] == "P":
        print(roll)
