num = int(input("Enter a number: "))

# Validation
if num <= 0:
    print("Invalid input! Please enter a positive integer.")
else:
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    if len(factors) == 2:
        print(f"{num} is a Prime Number")
    else:
        print("Factors:", *factors)
        print(f"{num} is not a Prime Number")
