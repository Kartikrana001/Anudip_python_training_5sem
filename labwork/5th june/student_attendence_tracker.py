#  Student Attendance Tracker
# Problem Statement
# Attendance for 15 days is recorded as:
# attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Write a program to:
# * Count present and absent days.
# * Calculate attendance percentage.
# * Determine eligibility (minimum 75% attendance).
# * Display positions where the student was absent.
# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present = 0
absent = 0

for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present Days:", present)
print("Absent Days:", absent)

# Calculate attendance percentage
percentage = (present / len(attendance)) * 100

print("\nAttendance Percentage:", percentage)

# Check eligibility
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Display absent positions
print("\nAbsent on Days:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)
