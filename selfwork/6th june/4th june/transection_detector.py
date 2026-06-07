high = 0
low = 0
total = 0

while True:

    amt = int(input("Enter Amount (-1 to Stop): "))

    if amt == -1:
        break

    total += amt

    if amt > 50000:
        high += 1

    if amt < 1000:
        low += 1

print("Above 50000 =", high)
print("Below 1000 =", low)
print("Total Amount =", total)
