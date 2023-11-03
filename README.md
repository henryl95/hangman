# Hangman in Python
This is a python project from college that I have completed for my finals. This undertaking consists of one semester's worth of studies from an Intro to Python college course.
The project itself took 1 week to plan and execute.

The premise of this python project is create a simple and lightweight game of "Hangman." I have created the game with a GUI for a positive user experience, as well as to go beyond my professor's expectations.
This project is no longer being updated after being submitted for my finals. What this repo displays is how the project was submitted to my professor.

The game consists of pre-determined words found in the code, and the program will randomly select a code from the array. The user will then try to guess the word using the interactive GUI that I have created. Selecting the wrong letter will result in the GUI widget to become red and refresh the ASCII, signifying the user's lives. If the user were to guess a correct letter, the GUI widget will become green and the selected letter will fill in the space of the pre-determined word; the ASCII will not update in this case.

Upon failure, the program will prompt the user that they have ran out of lives and the game is over. The user may choose to play again, then a new pre-determined word within the array will be selected and the game resumes anew. Likewise, if the user succeeds the game and has guessed the pre-determined word without losing all of their lives, the program will congratulate the user and will then prompt the user if they would like to play again. The same code to restart the game with a new pre-determined word will be executed.
