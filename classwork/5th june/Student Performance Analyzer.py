marks = [78, 45, 92, 35, 88, 40, 99, 56]

passed = []
failed = 0
merit = []

highest = marks[0]
lowest = marks[0]

for m in marks:
    if m >= 40:
        passed.append(m)
    else:
        failed += 1

    if m > highest:
        highest = m

    if m < lowest:
        lowest = m

    if m > 75:
        merit.append(m)

print("Passed Students:", passed)
print("Failed Count:", failed)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)
