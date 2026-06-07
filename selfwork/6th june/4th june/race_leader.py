n = int(input("Enter Number of Racers: "))

times = []

for i in range(n):
    t = float(input("Enter Lap Time: "))
    times.append(t)

fastest = min(times)
slowest = max(times)

fastest_pos = times.index(fastest) + 1
slowest_pos = times.index(slowest) + 1

print("Fastest Racer Position =", fastest_pos)
print("Slowest Racer Position =", slowest_pos)
print("Difference =", slowest - fastest)
