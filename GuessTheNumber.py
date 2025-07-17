from random import randint

number = randint(1, 10)
guess = -1
attempts = 0

print("Try to guess the number between 1 and 10.")

while guess != number:
    attempts += 1
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess > number:
        print("Too high! Try a lower number.")
    elif guess < number:
        print("Too low! Try a higher number.")

print(f"Congratulations! You found the number in {attempts} tries.")