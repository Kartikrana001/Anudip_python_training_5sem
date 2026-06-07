total_students = 30
present_students = 0
absent_students = 0
i=1
while i <= total_students:
    attendence =input(f"student {i} is present (P) or absent (A)? ").upper()
    if(attendence == "p"):
        present_students += 1
    elif(attendence == "a"):
        absent_students += 1
    else:
        print("Invalid input...")
    i += 1
print("Attendance recorded successfully!")
print(f"Total students: {total_students}")
print(f"Present students: {present_students}")
print(f"Absent students: {absent_students}")
