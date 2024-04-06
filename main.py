import random

gameover = False
tries = 10 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Do you want to play easy 'e' or hard 'h' mode?: ")
if mode == "h":
    tries = 5 

while not gameover and tries > 0:
    try:
        num = int(input("Guess a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    randnum = random.randint(1, 101)

    if num < randnum:
        print("Guess Higher")
    elif num > randnum:
        print("Guess Lower")
    else:
        print(f"You guessed it! 👍 The number was {randnum}")
        gameover = True

    tries -= 1
    if tries > 0:
        print(f"You have {tries} tries left")
    else:
        print(f"Game Over! The number was {randnum}")
        gameover = True
