# User Experience UX

### Hangman
Hangman is a "guess the word" game where the player tries to guess a random word chosen by the program. The objective of the game is to guess the secret word within a limited number of attempts before a digital representation of the player is hung after a number of failed attempts or victory if the word is guessed before the allowed attempts are expired. The primary purpose of the game is for entertaininment and developed for novices to expert system users who enjoy playing word games. 


<img src="https://github.com/Lavlen/hangman/blob/main/responsiveness/responsiveness_of_game.PNG" style="max-width:50%;">

[View site here](https://hangm-n.herokuapp.com)

# User stories
* As a regular player I want to be kept entertained with a large vocabulary of words to guess that are not repeated often.
* As a computer novice I want to see clear instructions on how to play the game before I start.
* As a player I want to be able to guess the word if I think I know it in a single attempt.
* As a regular player of the classic game I do not want to lose attmpts when guessed the same word or letter repeatedly.
* As a computer novice the game should be able to handle any keystroke error I make without needing further input from me.
* AS a player of the classic game I expect the game to fill blank spaces with correct inputs to make it more entertaining and interactive.
* As a player I would like to see a graphical representation of the hangman images as in most versions of the game.
* As a player I would like to be able to track my progress and know how well I am playing the game. 
* As a player I need to be able to restart the game quickly and easily.
* As a inexperience user with command line interfaces, instructions on how to navigate the app should be readily available to me.

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

# Data Model
A flowchart was used during the design phase to map the processes and decisions the application would need to handle.

<img src="https://github.com/Lavlen/hangman/blob/main/design/flowchart.png" style="max-width:50%;">

# Features

## Existing Features
<p align="left"><img src="https://github.com/Lavlen/hangman/blob/main/features/instructions.PNG" style=width="300" height="250"></p>

* Instructions displayed at start of game.
* Large list of words 
* Random word selection for player
<p align="left"><img src="https://github.com/Lavlen/hangman/blob/main/features/hangman2.PNG" style=width="300" height="250"></p>

* Receives input from player
* Varied word length and levels of word difficulty
<p align="left"><img src="https://github.com/Lavlen/hangman/blob/main/features/hangman3.PNG" style=width="300" height="250"></p>

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

## Features for the future

* Introduce secret phrases and additional hangman stages 
* Hints to assist with guessing words and phrases to make the game more interesting and interactive
* Design a more developed graphics of the hangman stages to improve the games visual appeal

# Technologies
##    Languages
* [Python](https://www.python.org)

##  Programs and tools used
* [Draw.io](https://app.diagrams.net/)
Used to create the flowchart.

* [Am I responsive](http://ami.responsivedesign.is/) Website for testing responsiveness of web applications.

* [Snipping tool](https://www.microsoft.com/en-us/p/screenshot-snipping-tool/9n9kcj2f020j#activetab=pivot:overviewtab)
Used for screen snipping the code validation evidence from [Pep8](http://pep8online.com/), the test cases and proof of site responsiveness image.

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/free-office-online-for-the-web) for creating the test case file and resolved Pep8 failure with words.py file discussed in bugs section of the testing phase in this documentation.

* [Github](https://github.com/) Remote hosting version control platform for recording changes made to code by storing it in a repository

* [Gitpod](https://www.gitpod.io/docs/config-gitpod-file) Online IDE used for processing the code.

* [Heroku](https://id.heroku.com/login) used for deployment and hosting the application.

# Testing

The application was tested in both the Gitpod and Heroku terminals following test cases that can be found [here](https://github.com/Lavlen/hangman/tree/main/testing/test_cases.PNG)

The website pep8online.com was used to check and correct the structure of the code to ensure it conformed to the best practice standard. The validation results of all three files that comprises the program are listed below:
* [hangman_parts.py](https://github.com/Lavlen/hangman/tree/main/testing/hangman_partspy.PNG)
* [words.py](https://github.com/Lavlen/hangman/tree/main/testing/validatewordspy.PNG)
* [run.py](https://github.com/Lavlen/hangman/tree/main/testing/validaterunpy.PNG)

## Testing User Stories (UX) 

As a regular player I want to be kept entertained with a large vocabulary of words to guess that are not repeated often.
* The program chooses randomly from a list of over 500 words at the start of each game.

As a computer novice I want to see clear instructions on how to play the game before I start.
* When the game starts the user is given clear step by step instructions on how to play the game.

As a player I want to be able to guess the word if I think I know it in a single attempt.
* The program enables the user to guess the complete word in a single attempt.

As a regular player of the classic game I do not want to lose attempts when guessed the same word or letter repeatedly.
* The player does not lose lives for retrying words or letters.

As a player I would like to see a list of the words and letters already tried so I don't keep repeating input.
* The game tracks and displays a list of words and letters already tried to prevent the tediousness of the player constantly repeating tried inputs 

As a computer novice the game should be able to handle any keystroke error I make without needing further input from me.
* Error handling and input validation functionalities prompts the user when input errors are made whilst the game is in progress without interrupting the game.

AS a player of the classic game I expect the game to fill blank spaces with correct inputs to make it more entertaining and interactive.
* With each correct guess the placeholders are replaced by the correctly guessed letters.

As a player I would like to see a graphical representation of the hangman images as in most versions of the game.
* A new incomplete image of a hangman is displayed with every incorrect entry. A complete graphic of a man hanging from a gallow indicates the user has failed to guess the secret word within the number of allowed attempts. 

As a player I would like to be able to track my progress and know how well I am playing the game. 
* The game displays the 6 attempts players are given to guess the word. The number decrements by 1 with each incorrect new attempt and the user can be seen easily in the terminal while the game is in progress.

As a player I need to be able to restart the game quickly and easily.
* A player can restart the game quickly with a single keystroke which is displayed at the end of each game.

As an inexperienced user of command line interfaces, instructions on how to navigate the app should be readily available to me.
* Instructions on how the game is played is displayed upon entering the Heroku app website and clicking the run program button. At the end of the game the options available to the user are displayed within the terminal.

## Further testing
The game was executed within the Heroku application on the 5 most commonly used browsers for browser specific compatibility errors.The types were Google Chrome, Microsoft Edge, Internet Explorer, Safari and Firefox. Heroku rendered and executed the game correctly on all browsers.

The application was viewed and played on the following devices a Windows' desktop PC, a ProBook-450-G4 laptop, IPhone7, Samsung Galaxy S7 tablet, S7 and S9 smart phones. The game played and executed as it should on the various device sizes and no bugs were identified.

User testing was carried out by Friends and family members in an effort to locate bugs and or user experience issues.

### Bugs

Clear screen functionality does not appear to be functioning though the the method used is according to Windows standard.

Using 'clear' instead of 'cls' in the clear method resolved this issue.

The pep8 online checker identified a number of white space code structure issues and lines of code that were too long in the run.py. These were fixed within the editor window on the pep8online.com website at the same time.

The stuctural standard of the words.py file does not currently conform to the Pep8 standard because there is a space missing after the comma that follows each word. As the file potentially contains over 2,000 words fixing this bug will be too time consuming and as the function is not affected in anyway a decision was made not to amend the file. 

A solution was found which involved copying the entire word list and formatting it in Excel before pasting it back into the Gitpod terminal therefore this bug has been fixed.

# Deployment

The game was deployed via an online terminal developed by Code institute known as Heroku, developed to facilitate deployment and host applications created using backend languages such Python. The deployment process is as follows:

1. Create new Heroku app from Heroku dashboard 
2. Name the app with a name that is available.
3. Choose the region from which you are from (Europe)
4. Select the create app button
5. Select 'Settings' from the main menu
6. Scroll to 'Config Vars' section and select 'Reveal Config Vars'
7. In the 'Key' field input 'PORT' in the 'Value' field input '8000'
8. Press 'Add' to add the value just entered
9. Scroll down to 'Add buildpack' and select it
10. Select 'Python' and save changes 
11. Select 'Add buildpack' again and do the same with 'NodeJs'
12. Link the App to your repository
13. Select deploy  

## How to Clone the project

1. Go to https://github.com/
2. Log into account
3. Click on the repository to be cloned
4. Click the drop-down list arrow on the "Code" tab
5. Click on the copy link icon next to the url of the repository
6. Create a new repository and launch Gitpod to create a workspace from it
7. In the gitpod terminal type: "git clone"
8. paste the copied link and press enter

# Credits

## Code 
* [Kite](https://www.youtube.com/channel/UCxVRDu9ujwOrmDxu72V3ujQ)
* [Kylie Ying](https://youtu.be/cJJTnI22IF8)
* [wordlist source](https://www.randomlists.com/data/words.json)

## Acknowledgement
* My mentor for his guidance
* The Slack community



