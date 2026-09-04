import random

number = random.randint(1, 100)
attempts = 1

guess = int(input("Guess the number: "))

while guess != number:

    if guess > number:
        print("Too HIGH")
    else:
        print("Too LOW")

    guess = int(input("Guess again: "))
    attempts += 1

print("You got it!")
print("Attempts =", attempts)