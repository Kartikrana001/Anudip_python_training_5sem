num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid input!")
else:
    reverse = num[::-1]

    print("Reverse:", reverse)

    if num == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
