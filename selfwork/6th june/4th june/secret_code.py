code = input("Enter Secret Code: ")

if len(code) == 6:
    first = int(code[0]) + int(code[1]) + int(code[2])
    last = int(code[3]) + int(code[4]) + int(code[5])

    if first == last:
        print("Valid Code")
    else:
        print("Invalid Code")
else:
    print("Invalid Code")
