#J'ai effectue des modifications dans ce fichier
import random

isGuessRight = False
number = random.randint(1, 10)

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

while isGuessRight != True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("You guessed {}. That is correct! You win! 👌".format(guess))
        isGuessRight = True
    elif guess < number:
        print("You guessed {}. Too low! Try again. ❌".format(guess))
    else:
        print("You guessed {}. Too high! Try again. ❌".format(guess))