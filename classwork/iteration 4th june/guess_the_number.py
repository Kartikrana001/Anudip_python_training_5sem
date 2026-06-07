secret_number = 7
count=1

while True:
  guess = int(input("Guess the Number: "))
  if guess == secret_number:
    print("Congratulations! You guessed the correct number...",f"\n you take {count} terns to guess correct...")
    break
  else:
    print("guess again")
    count += 1

