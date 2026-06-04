import random

secret = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Enter your guess (1-50): ")

    if not guess.isdigit():
        print("Invalid input!")
        continue

    guess = int(guess)

    if guess < 1 or guess > 50:
        print("Enter a number between 1 and 50.")
        continue

    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break
