num = input("Enter a number: ")

if not num.isdigit() or int(num) < 0:
    print("Invalid input! Please enter a positive integer.")
else:
    num = int(num)
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10

        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        total += fact
        temp //= 10

    if total == num:
        print(f"{num} is a Strong Number")
    else:
        print(f"{num} is not a Strong Number")
