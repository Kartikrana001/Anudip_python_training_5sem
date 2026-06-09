# Cricket Tournament Scorecard
# Problem Statement
# A batsman's scores in different matches are stored in a list.
# scores = [45, 78, 12, 100, 67, 8, 90, 55]
# Write a program to:
# * Count half-centuries and centuries.
# * Find the highest score.
# * Display all scores below 20.
# * Calculate the average score.

# List of batsman's scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Count half-centuries and centuries
half_centuries = 0
centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

# Find highest score
highest_score = max(scores)

# Display scores below 20
print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

# Calculate average score
average_score = sum(scores) / len(scores)

# Display results
print("\nHalf-Centuries:", half_centuries)
print("Centuries:", centuries)
print("Highest Score:", highest_score)
print("Average Score:", average_score)
