# Employee performance data
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Task 1: Employees scoring above 80
print("Employees Scoring Above 80:")

for emp in performance:
    if performance[emp] > 80:
        print(emp)

# Task 2: Count employees needing improvement
improvement = 0

for emp in performance:
    if performance[emp] < 60:
        improvement += 1

print("\nEmployees Needing Improvement:", improvement)

# Task 3: Top performer
top_emp = ""
top_score = 0

for emp in performance:
    if performance[emp] > top_score:
        top_score = performance[emp]
        top_emp = emp

print("Top Performer:", top_emp, "(", top_score, ")", sep="")

# Task 4: Average performance score
total = 0

for emp in performance:
    total += performance[emp]

average = total / len(performance)

print("Average Score:", average)

# Task 5: Separate lists
excellent = []
good = []
average_list = []
poor = []

for emp in performance:
    score = performance[emp]

    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)
