present = 0
absent = 0
student = 1

while student <= 30:
    status = input(f"Student {student} Attendance (Present/Absent): ")

    if status.lower() == "present":
        present += 1
    else:
        absent += 1

    student += 1

print("\nNo. of Students Present:", present)
print("No. of Students Absent:", absent)
