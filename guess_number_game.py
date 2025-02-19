import random

max_number = 100
random_number = random.randint(1, max_number) 
temp_number = 0
while temp_number != random_number:
    number = int(input(f"Guess a number between 1 and {max_number}: "))
    temp_number = number
    if number == random_number:
        print("You guessed the number correctly!")
    elif number < random_number:
        print("You guessed too low!")
    else:
        print("You guessed too high!")