num = input("Enter Number: ")

length = len(num)

if length % 2 == 0:

    first = num[:length//2]
    second = num[length//2:]

    if first == second:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")

else:
    print("Not a Mirror Number")
