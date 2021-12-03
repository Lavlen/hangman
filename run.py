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
    print(body_parts(attempts)) # print hangman stages
    print(secret_word)  # print random placeholders
    print('')
    print('')


    # Check if word has been guessed and attempts are more than zero
    while not guessed and attempts > 0:

        # join guessed letters to existing string
        print(attempts, 'tries left, letters used ', ' '.join(guessed_letters))

        # receive user input and convert to uppercase
        guess = input('please guess a letter: ').upper()
        """
        check if one letter has been inputted
        and if it has been tried before
        otherwise if the letter is not in the word say so
        """
        if len(guess) == 1 and guess in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if guess in guessed_letters:
                print('Letter already guessed', guess)
            elif guess not in word:
                print(guess, 'is not in the word')
                """
                decrement from remaining attempts
                add guessed letters to guessed_letters list
                """
                attempts -= 1
                guessed_letters.append(guess)
                print('incorrect letters already tried: ', guess)
            else:
                print('This letter,', guess, 'is in the word!')
                guessed_letters.append(guess)
                """
                Convert from string to list for
                indexing and store in new variable
                """
                word_as_list = list(secret_word)
                """
                Find indices where guess is in the
                word and the letter at each index
                """
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_as_list[index] = guess
                secret_word = "".join(word_as_list)
                if '_' not in secret_word:
                    guessed = True
        elif len(guess) > 1:
            print('Guess a letter at a time')
            attempts -= 1

        else:
            print('Only letters are allowed')
        print(body_parts(attempts))
        print('==================================')
        print('')
        print(secret_word)
        print()
    if guessed:
        print('Well done, you guessed the word!', word)
    else:
        print('you ran out of attempts. The word is: ', word)        




