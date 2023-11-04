# Hangman in Python
This is a python project from college that I have completed for my finals. My python knowledge at the time of creating this consists of one semester's worth of studies in an Intro to Python college course. The course's curriculum did not go over some of the coding techniques found in the source code, I took the initiative to learn further and beyond the scope of the curriculum.
The project itself took 1 week to plan and execute.

The premise of this python project is create a simple and lightweight game of "Hangman." I have created the game with a GUI for a positive user experience, as well as to go beyond my professor's expectations.

This project is no longer being updated after being submitted for my finals. What this repo displays is how the project was submitted to my professor.

# Starting the game
Upon executing the game using Python IDLE, the GUI will launch.

![pythonw_H0aY1MHrms](https://github.com/henryl95/hangman/assets/149839431/8c20e344-4278-4ef4-8e58-3db558ae6037)

The game consists of pre-determined words found in the code, and the program will randomly select a word from the array.

# Playing the game
The user will then try to guess the word using the interactive GUI that I have created.

![pythonw_ORuPJbh6Uz](https://github.com/henryl95/hangman/assets/149839431/7cfaed7b-87de-4e62-b6b6-2d6f37468f3d)

Selecting the wrong letter will result in the GUI widget to become red and refresh the ASCII, signifying the user's lives.

![pythonw_kQd0zvQHKf](https://github.com/henryl95/hangman/assets/149839431/b40669da-9cd9-4ccf-9587-7501c789988e)

If the user were to guess a correct letter, the GUI widget will become green and the selected letter will fill in the space of the pre-determined word; the ASCII will not update in this case.

![pythonw_Sh762tRMmx](https://github.com/henryl95/hangman/assets/149839431/2d956c37-d5ce-46f3-9790-28f6ea3b8ad4)

Upon failure, the program will prompt the user that they have ran out of lives and the game is over. The user may choose to play again, then a new pre-determined word within the array will be selected and the game resumes anew.

![pythonw_VjtfAmgzyy](https://github.com/henryl95/hangman/assets/149839431/dbf901ec-c354-47ef-9d9b-242e4c29b05e)

Likewise, if the user succeeds the game and has guessed the pre-determined word without losing all of their lives, the program will congratulate the user and will then prompt the user if they would like to play again. The same code to restart the game with a new pre-determined word will be executed.

![pythonw_x4gETtEpEf](https://github.com/henryl95/hangman/assets/149839431/2d5f7ae1-d0ad-4315-bbf4-3c76e588910d)

# Lives

The maximum amount of incorrect guesses is 6, represented by the ASCII shown in the GUI.

![pythonw_cdNgClmKAe](https://github.com/henryl95/hangman/assets/149839431/6d12cd32-dc8b-44cb-9a3d-3401893777b4)

Each incorrect guess refreshes the ASCII to reflect on the player's remaining lives. Upon reaching 6 incorrect guesses, the game ends.

![pythonw_6LosHtMTnL](https://github.com/henryl95/hangman/assets/149839431/39c35f68-79eb-487c-ba4c-e268ece664d8)
![pythonw_znmUdeBVdQ](https://github.com/henryl95/hangman/assets/149839431/d01930c0-2e30-4e39-b514-452ddf3574bb)
![pythonw_Wi2GwRp9Wc](https://github.com/henryl95/hangman/assets/149839431/9f5d8dd8-9682-46ee-8640-65ebffa2bcb0)
![pythonw_AjUblyC731](https://github.com/henryl95/hangman/assets/149839431/6e7b85f0-bafa-470d-9be8-b199b91e2c39)
![pythonw_sIQRdQtyaM](https://github.com/henryl95/hangman/assets/149839431/66259632-1395-4dd2-bbdd-d2b395ad78e4)
![pythonw_c9luFQHYHy](https://github.com/henryl95/hangman/assets/149839431/0ab5c120-111f-4855-81c2-6f7222986b6b)

# Why hangman?

At the time of creating this project, my professor has taught us the basics of python and expected a simple program to be submitted for everyone's final project. Simple programs such as BMI calculators, grocery lists, and diaries. While those programs would have been sufficient and challenging for what was taught in the course's curriculum, I wanted to go even further beyond and learn beyond the scope of the curriculum. I decided on hangman because it involves three key details that the course did not go over: randomness, ASCII and user interface.

The course has taught us the very basics of creating a GUI, but my professor did not teach us how to utilize GUI in a user friendly environment.

Using a regular ticking-down counter as the player's lives felt boring and uninspiring, so I utilized an ASCII to identify the player's lives. This adds to the user experience and is the core part of Hangman.



