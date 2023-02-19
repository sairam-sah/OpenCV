import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
guess = None
count = 0

while guess != number:
    guess = int(input("Take a guess: "))
    count += 1

    if guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
    else:
        print(f"Congratulations! You guessed the number in {count} tries!")
