n = int(input("How many numbers: "))

current = 1
longest = 1

prev = int(input("Enter Number: "))

for i in range(n - 1):
    num = int(input("Enter Number: "))

    if num > prev:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

    prev = num

print("Longest Sequence Length =", longest)
