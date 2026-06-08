# Runs scored by players
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# Task 1: Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player in runs:
    if runs[player] > 500:
        print(player)

# Task 2: Orange Cap winner
winner = ""
highest = 0

for player in runs:
    if runs[player] > highest:
        highest = runs[player]
        winner = player

print("\nOrange Cap Winner:", winner, "(", highest, ")", sep="")

# Task 3: Lowest scorer
low_player = ""
low_runs = list(runs.values())[0]

for player in runs:
    if runs[player] < low_runs:
        low_runs = runs[player]
        low_player = player

print("Lowest Scorer:", low_player, "(", low_runs, ")", sep="")

# Task 4: Total runs
total = 0

for player in runs:
    total += runs[player]

print("Total Tournament Runs:", total)

# Task 5: Players below 400 runs
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("Players Scoring Below 400:")
print(below_400)

# Task 6: Players between 400 and 600 runs
count = 0

for player in runs:
    if 400 <= runs[player] <= 600:
        count += 1

print("Players Between 400 and 600 Runs:", count)
