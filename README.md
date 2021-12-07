# Hangman
Hangman is a "guess the word" game where the player tries to guess a random word chosen by the program. The objective of the game is to guess the secret word within a limited number of attempts before a digital representation of the player is hung after a number of failed attempts or victory if the word is guessed before the allowed attempts are expired

<img src="https://github.com/Lavlen/hangman/blob/main/responsiveness/hangman_responsive.PNG" style="max-width:50%;">

[View site here](https://hangm-n.herokuapp.com)

## How the game is played

* The program randomly chooses from a list a secret word for the player to guess.

* The word is displayed to the player as dashes, with each dash representing a letter of the word.

* Six attempts is given to the player to guess a secret word of varied length and difficulty

* For each correct letter guessed the placeholder dash will be replaced by the correct letter

* The game allows the player to guess the whole word in one attempt or a letter at a time.

* For each incorrect guess, whether word or letter, the number of attempts remaining reduces by one each time and the  corresponding hangman graphic is displayed. 

* The player wins when the secret word is guessed within six attempts. 

* The player loses if six attempts are made without guessing the secret word, in which event the final graphic of a whole man hanging from a gallow is displayed.

* The player is prompted when a word or letter is guessed more tha once but does not lose any attempts.

# Features

## Existing Features

General features
* Large list of words 
* Random word selection for player
* Varied word length and levels of word difficulty
* Underscore placeholders for each letter of the word
* Functionality that allows the user to guess the whole word in one attempt
* The number of attempts remaining is decremented and displayed while the game is in progress
* Hangman graphics is displayed with each incorrect entry

User Friendliness
* The program provides clear instructions on how to play the game.
* Each correct word guessed is displayed in the place it belongs.
* A list of letters already tried is displayed to avoid making the game tedious
* The program interacts with the user to guide the playing experience during and at the end of each game
* The game allows quick restart or game exit with option selection keys feature

Good Error Handling
* The program is not affected by keys not bound to a function
* The program will not process entry of a characters that are not letters and will instead prompt the user
* Error-checking functionaly handles user's operational errors such as pressing the wrong keys

### Features for the future

* Introduce secret phrases and additional hangman stages 
* Hints to assist with guessing words and phrases to make the game more interesting and interactive
* Design a more developed graphics of the hangman stages to improve the games visual appeal







