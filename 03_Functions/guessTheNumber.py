# This is a guess game
import random
secretNumber = random.randint(1, 21)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your number is too low.')
    elif guess > secretNumber:
        print('Your number is too high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You gussed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
