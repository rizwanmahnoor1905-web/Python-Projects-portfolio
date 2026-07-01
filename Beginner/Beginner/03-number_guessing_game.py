import random

numbers = list(range(1, 101))
computer_choice = random.choice(numbers)

user_choice = int(input("Enter your number: "))

while user_choice != computer_choice:
    if user_choice > computer_choice:
        print("Too high")
    else:
        print("Too low")

    user_choice = int(input("Guess again: "))

print("Congratulations! You guessed correctly.")
print(f"The number was {computer_choice}.")
