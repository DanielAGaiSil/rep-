#numguesser

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)

        if(guess < random_number):
            print("Try again, too low!")
        elif guess > random_number:
            print("Try again, too high!")

    print(f"Congratulations, you have correctly guessed the number! {random_number} was the right answer.")

guess(100)