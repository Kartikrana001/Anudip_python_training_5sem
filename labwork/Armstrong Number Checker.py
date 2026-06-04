num = input("Enter a number: ")

# Validation
if not num.isdigit() or int(num) <= 0:
    print("Invalid input! Please enter a positive integer.")
else:
    num = int(num)
    digits = len(str(num))
    temp = num
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** digits
        temp //= 10

    if armstrong_sum == num:
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is not an Armstrong Number")
