amount = int(input("Enter Amount: "))

notes = [500, 200, 100, 50, 20, 10]

for note in notes:
    count = amount // note

    if count > 0:
        print(note, "x", count)

    amount = amount % note
