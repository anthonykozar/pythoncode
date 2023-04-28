# Number Guessing Game

# The next line tells Python that we want to use the randrange function from the random module (a module is like an extension).
from random import randrange

print('I am thinking of a number between 1 and 100. Try to guess my number!')
print('You have 7 guesses.  After each guess I will tell you if you are too high, too low, or have won.')

# Select a random number between 1-100
winningNumber = randrange(1,100)

# Loop seven times
for i in range(7):
    guess = int(input('Enter your guess: '))
    if guess == winningNumber:
        print(guess, 'is correct. You win!')
        # stop the program
        sys.exit(0)
    if guess > winningNumber:
        print(guess, 'is too high. Try again!')
    if guess < winningNumber:
        print(guess, 'is too low. Try again!')

# If the program gets this far, then the player has run out of guesses without winning.
print('Game over! Better luck next time.')
