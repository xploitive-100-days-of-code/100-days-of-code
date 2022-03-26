import random

number = random.randint(1, 100)
count = 0
while True:
    guess = int(input("Guess a number between 1 and 100: \n"))
    if guess == number:
        print("\n Correct!\n")
        break
    elif guess < number:
        print("\n Guess is too low!\n")
        count += 1
    elif guess > number:
        print("\n Guess is too high!\n")
        count += 1
print(f"\n It took you {count} guesses!")
