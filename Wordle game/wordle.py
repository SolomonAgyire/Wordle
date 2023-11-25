import random
import sys

def main():
    # Get a random word.
    answer = getRandomWord()

    # Ask the user for the game mode
    hard_mode = chooseGameMode()

    # Start the game loop
    attempts = 1
    guess = ''
    while attempts < 6 and guess != answer:
        guess = getValidGuess()
        printGuessColors(guess, answer)

        if guess == answer:
            print(f"You Won! That took {attempts} guess(es).")

        elif attempts == 6 and guess != answer:
            print(f"You lost. The answer was {answer}.")

        attempts += 1

    if hard_mode and guess != answer:
        print("Hard Mode: You've used all 5 guesses!")

# A helper method that prints the guess with the
# correct colors to the console.
def printGuessColors(guess, answer):
    for index in range(len(guess)):
        result = letterColor(index, guess, answer)
        color_code = '\033[91m' if result == 'Red' else '\033[92m' if result == 'Green' else '\033[93m'
        print(f"{color_code}{guess[index]} - {result}\033[0m")

# A helper method that determines the color
# of the letter in the guess.
def letterColor(index, guess, answer):
    if guess[index] == answer[index]:
        return 'Green'
    elif guess[index] not in answer:
        return 'Red'
    else:
        return 'Yellow'

# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)

def chooseGameMode():
    mode = input("Choose game mode (Normal or Hard): ").lower()
    return mode == 'hard'

def getValidGuess():
    while True:
        guess = input('Enter a 5 letter guess:\n')
        if len(guess) == 5 and guess.isalpha():
            return guess.lower()
        else:
            print("Invalid guess. Please enter a 5 letter word.")

main()
