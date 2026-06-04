rows = input("Enter number of rows: ")

if not rows.isdigit() or int(rows) <= 0:
    print("Invalid input!")
else:
    rows = int(rows)

    print("Pattern:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    print("Reverse Pattern:")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
