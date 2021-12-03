import random
from words import word_list
from time import sleep

#  Print a diagram of hangman
print('============ HANGMAN ========')
print('   ',  '______')
print('   ',  '|    |')
print('   ',  '|    O')
print('   ',  '|   /|\\')
print('   ',  '|   / \\')
print()
print('=============================')

print('Thinking of a word')

# Time delay function
def delay():
    for i in range(3):
        print('.', end="")
        sleep(.3)  # wait 3 seconds
    print()
delay()


def get_word():
    # randomly chooses a word from the list
    word = random.choice(word_list)
    return word.upper()  # make word uppercase

def start_playing():
    """
    display random word as string of underscore
    create variables for storing lists of
    guessed letters, words and number of valid guesses
    """
    secret_word = "_" * len(word)
    print("The word has", len(secret_word), "letters")
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    print()
    print('==============================')
    print(body_parts(attempts))
    print(secret_word)
    print('')
    print('')
