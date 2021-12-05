import random
from words import word_list
from time import sleep
from hangman_parts import stages 
import os
import sys


# clear screen
def screen_clear():
    os.system('cls')


#  Print a diagram of hangman
print('===================== HANGMAN ===============')
print('')
print('  1. Enter a letter or whole word')
print('  2. You are allowed 6 attempts')
print('  3. Letters already tried will not count against player')
print('  4. Select "X" or "R" to exit or restart the game')
print()
print('=============================================')

print('Thinking of a word')

# Time delay function
def delay():
    """
    time delay function
    delay game start by 5 seconds
    """
    for i in range(5):
        print('.', end="")
        sleep(.5)
    print()
delay()


def get_word():
    """
    randomly choose a word from the word_list
    imported from file words
    """
    word = random.choice(word_list)
    return word.upper()  

 
def start_playing(word):
    """
    run game,display random word as string of underscore
    create variables for storing lists of
    guessed letters, words and number of valid guesses
    """
    secret_word = "-" * len(word)
    print("The word has", len(secret_word), "letters")
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    print()
    print(body_parts(attempts)) # print hangman stages
    print(secret_word)  # print random placeholders
    print('')
    

    # Check if word has been guessed and attempts are more than zero
    while not guessed and attempts > 0:

        # join guessed letters to existing string
        print(attempts, 'tries left, letters used ', ' '.join(guessed_letters))

        # receive user input and convert to uppercase
        user_input = input('please guess a letter or a word: ').upper()
        """
        check if one letter has been inputted
        and if it has been tried before
        otherwise if the letter is not in the word say so
        """
        if len(guess) == 1 and user_input in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if user_input in guessed_letters:
                print(' Letter already tried', user_input)
            elif user_input not in word:
                print(user_input, 'is not in the word')
                """
                decrement from remaining attempts
                add guessed letters to guessed_letters list
                """
                attempts -= 1
                guessed_letters.append(user_input)
                print('incorrect letters already tried: ', user_input)
            else:
                print('This letter,', user_input, 'is in the word!')
                guessed_letters.append(user_input)
                """
                Convert from string to list for
                indexing and store in new variable
                """
                word_as_list = list(secret_word)
                """
                Find indices where guess is in the
                word and the letter at each index
                """
                ind = [i for i, letter in enumerate(word)
                       if letter == user_input]
                # replace underscore with user_input
                for index in ind:
                    word_as_list[index] = user_input
                secret_word = "".join(word_as_list)
                if '-' not in secret_word:
                    guessed = True
        elif len(user_input) == len(word) and user_input.isalpha():
            if user_input in guessed_words:
                print(user_input, 'you already tried that word')
            elif user_input != word:
                print(user_input, 'is not the word')
                attempts -= 1
                guessed_words.append(user_input)
            else:
                guessed = True
                secret_word = word
                print("=============================================")

        else:
            print(user_input, 'is not a valid input')
        print(body_parts(attempts))
        print('==================================')
        print('')
        print(secret_word)
        print()
    if guessed:
        print('Well done, you guessed the word!', word)
    else:
        print('you ran out of attempts. The word is: ', word)
        userInput = input("Enter 'R' to restart or 'X' to exit: ")


def body_parts(attempts):
    """
    function that prints hangman body parts
    """
    return stages[attempts]


def hangman():
    word = get_word()
    start_playing(word)
    while input("Try again? (Y/N) \n").upper() == "Y":
        word = get_word()
        start_playing(word)


if __name__ == "__main__":
    hangman()
        
