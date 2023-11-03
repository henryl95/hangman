from tkinter import *
import tkinter.messagebox
import sys
import os
import random

class hMan:
    def __init__(self, parent):
        self.myParent = parent
        self.lives = '''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
        
        self.word = ["PYTHON", "INTEL", "WATER", "ORANGE", "MONKEY", "DRAGON"]
        self.randomWord = random.choice(self.word)
        self.intro = Label(root)
        self.intro.configure(text="Click [Play] to start!\nBy: Henry Le", font=("Calibri", 30))
        self.intro.place(x=15,y=75)

        #======BUTTONS========
        self.buttonQ = Button(root)
        self.buttonQ.configure(text="Q", width="3", command=self.qClick)
        self.buttonQ.place(x=25,y=200)
        
        self.buttonW = Button(root)
        self.buttonW.configure(text="W", width="3", command=self.wClick)
        self.buttonW.place(x=55,y=200)
        
        self.buttonE = Button(root)
        self.buttonE.configure(text="E", width="3", command=self.eClick)
        self.buttonE.place(x=85,y=200)
        
        self.buttonR = Button(root)
        self.buttonR.configure(text="R", width="3", command=self.rClick)
        self.buttonR.place(x=115,y=200)
        
        self.buttonT = Button(root)
        self.buttonT.configure(text="T", width="3", command=self.tClick)
        self.buttonT.place(x=145,y=200)
        
        self.buttonY = Button(root)
        self.buttonY.configure(text="Y", width="3", command=self.yClick)
        self.buttonY.place(x=175,y=200)
        
        self.buttonU = Button(root)
        self.buttonU.configure(text="U", width="3", command=self.uClick)
        self.buttonU.place(x=205,y=200)
        
        self.buttonI = Button(root)
        self.buttonI.configure(text="I", width="3", command=self.iClick)
        self.buttonI.place(x=235,y=200)
        
        self.buttonO = Button(root)
        self.buttonO.configure(text="O", width="3", command=self.oClick)
        self.buttonO.place(x=265,y=200)
        
        self.buttonP = Button(root)
        self.buttonP.configure(text="P", width="3", command=self.pClick)
        self.buttonP.place(x=295,y=200)
        
        self.buttonA = Button(root)
        self.buttonA.configure(text="A", width="3", command=self.aClick)
        self.buttonA.place(x=40,y=227)
        
        self.buttonS = Button(root)
        self.buttonS.configure(text="S", width="3", command=self.sClick)
        self.buttonS.place(x=70,y=227)
        
        self.buttonD = Button(root)
        self.buttonD.configure(text="D", width="3", command=self.dClick)
        self.buttonD.place(x=100,y=227)
        
        self.buttonF = Button(root)
        self.buttonF.configure(text="F", width="3", command=self.fClick)
        self.buttonF.place(x=130,y=227)
        
        self.buttonG = Button(root)
        self.buttonG.configure(text="G", width="3", command=self.gClick)
        self.buttonG.place(x=160,y=227)
        
        self.buttonH = Button(root)
        self.buttonH.configure(text="H", width="3", command=self.hClick)
        self.buttonH.place(x=190,y=227)
        
        self.buttonJ = Button(root)
        self.buttonJ.configure(text="J", width="3", command=self.jClick)
        self.buttonJ.place(x=220,y=227)
        
        self.buttonK = Button(root)
        self.buttonK.configure(text="K", width="3", command=self.kClick)
        self.buttonK.place(x=250,y=227)
        
        self.buttonL = Button(root)
        self.buttonL.configure(text="L", width="3", command=self.lClick)
        self.buttonL.place(x=280,y=227)
        
        self.buttonZ = Button(root)
        self.buttonZ.configure(text="Z", width="3", command=self.zClick)
        self.buttonZ.place(x=70,y=254)
        
        self.buttonX = Button(root)
        self.buttonX.configure(text="X", width="3", command=self.xClick)
        self.buttonX.place(x=100,y=254)
        
        self.buttonC = Button(root)
        self.buttonC.configure(text="C", width="3", command=self.cClick)
        self.buttonC.place(x=130,y=254)
        
        self.buttonV = Button(root)
        self.buttonV.configure(text="V", width="3", command=self.vClick)
        self.buttonV.place(x=160,y=254)
        
        self.buttonB = Button(root)
        self.buttonB.configure(text="B", width="3", command=self.bClick)
        self.buttonB.place(x=190,y=254)
        
        self.buttonN = Button(root)
        self.buttonN.configure(text="N", width="3", command=self.nClick)
        self.buttonN.place(x=220,y=254)
        
        self.buttonM = Button(root)
        self.buttonM.configure(text="M", width="3", command=self.mClick)
        self.buttonM.place(x=250,y=254)

        self.buttonPlay = Button(root, text="Play", width="8", fg="green", command=self.clickPlay).place(x=100,y=300)
        self.buttonCancel = Button(root, text="Close", width="8", fg="red", command=self.clickCancel).place(x=200,y=300)
        self.buttonRetry = Button(root, text="Retry", width = "8", fg="blue", command=self.clickRetry).place(x=150,y=350)


    #=======FUNCTIONS=========
    def clickPlay(self):
        self.randomWord = random.choice(self.word) #Selects a word from self.word at random
        self.intro.place_forget() #Removes the intro label
        self.cGuess = ''
        self.wGuess = ''
        self.hangman = Label(root, text=self.lives[0]).place(x=250,y=60) #Reveals the hangman lives
        self.underscore = "-" * len(self.randomWord) #The amount of underscores is equivalent to the amount of characters in the random word
        self.wordLabel = Label(root, text=self.underscore, font=("Calibri", 38)).place(x=50,y=100) #Reveals the underscores
    def clickCancel(self):
        self.myParent.destroy() #Closes the game
    def clickRetry(self):
        self.restart_program() #This function resets the program
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    #=======BUTTON FUNCTIONS=========
    def qClick(self):
        self.guess = "Q"
        self.check()
        if self.guess in self.cGuess:
            self.buttonQ.configure(text="Q", width="3", command=self.qClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonQ.configure(text="Q", width="3", command=self.qClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def wClick(self):
        self.guess = "W"
        self.check()
        if self.guess in self.cGuess:
            self.buttonW.configure(text="W", width="3", command=self.wClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonW.configure(text="W", width="3", command=self.wClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def eClick(self):
        self.guess = "E"
        self.check()
        if self.guess in self.cGuess:
            self.buttonE.configure(text="E", width="3", command=self.eClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonE.configure(text="E", width="3", command=self.eClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def rClick(self):
        self.guess = "R"
        self.check()
        if self.guess in self.cGuess:
            self.buttonR.configure(text="R", width="3", command=self.rClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonR.configure(text="R", width="3", command=self.rClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def tClick(self):
        self.guess = "T"
        self.check()
        if self.guess in self.cGuess:
            self.buttonT.configure(text="T", width="3", command=self.tClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonT.configure(text="T", width="3", command=self.tClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def yClick(self):
        self.guess = "Y"
        self.check()
        if self.guess in self.cGuess:
            self.buttonY.configure(text="Y", width="3", command=self.yClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonY.configure(text="Y", width="3", command=self.yClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def uClick(self):
        self.guess = "U"
        self.check()
        if self.guess in self.cGuess:
            self.buttonU.configure(text="U", width="3", command=self.uClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonU.configure(text="U", width="3", command=self.uClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def iClick(self):
        self.guess = "I"
        self.check()
        if self.guess in self.cGuess:
            self.buttonI.configure(text="I", width="3", command=self.iClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonI.configure(text="I", width="3", command=self.iClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def oClick(self):
        self.guess = "O"
        self.check()
        if self.guess in self.cGuess:
            self.buttonO.configure(text="O", width="3", command=self.oClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonO.configure(text="O", width="3", command=self.oClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def pClick(self):
        self.guess = "P"
        self.check()
        if self.guess in self.cGuess:
            self.buttonP.configure(text="P", width="3", command=self.pClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonP.configure(text="P", width="3", command=self.pClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def aClick(self):
        self.guess = "A"
        self.check()
        if self.guess in self.cGuess:
            self.buttonA.configure(text="A", width="3", command=self.aClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonA.configure(text="A", width="3", command=self.aClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def sClick(self):
        self.guess = "S"
        self.check()
        if self.guess in self.cGuess:
            self.buttonS.configure(text="S", width="3", command=self.sClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonS.configure(text="S", width="3", command=self.sClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def dClick(self):
        self.guess = "D"
        self.check()
        if self.guess in self.cGuess:
            self.buttonD.configure(text="D", width="3", command=self.dClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonD.configure(text="D", width="3", command=self.dClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def fClick(self):
        self.guess = "F"
        self.check()
        if self.guess in self.cGuess:
            self.buttonF.configure(text="F", width="3", command=self.fClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonF.configure(text="F", width="3", command=self.fClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def gClick(self):
        self.guess = "G"
        self.check()
        if self.guess in self.cGuess:
            self.buttonG.configure(text="G", width="3", command=self.gClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonG.configure(text="G", width="3", command=self.gClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def hClick(self):
        self.guess = "H"
        self.check()
        if self.guess in self.cGuess:
            self.buttonH.configure(text="H", width="3", command=self.hClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonH.configure(text="H", width="3", command=self.hClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def jClick(self):
        self.guess = "J"
        self.check()
        if self.guess in self.cGuess:
            self.buttonJ.configure(text="J", width="3", command=self.jClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonJ.configure(text="J", width="3", command=self.jClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def kClick(self):
        self.guess = "K"
        self.check()
        if self.guess in self.cGuess:
            self.buttonK.configure(text="K", width="3", command=self.kClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonK.configure(text="K", width="3", command=self.kClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def lClick(self):
        self.guess = "L"
        self.check()
        if self.guess in self.cGuess:
            self.buttonL.configure(text="L", width="3", command=self.lClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonL.configure(text="L", width="3", command=self.lClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def zClick(self):
        self.guess = "Z"
        self.check()
        if self.guess in self.cGuess:
            self.buttonZ.configure(text="Z", width="3", command=self.zClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonZ.configure(text="Z", width="3", command=self.zClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def xClick(self):
        self.guess = "X"
        self.check()
        if self.guess in self.cGuess:
            self.buttonX.configure(text="X", width="3", command=self.xClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonX.configure(text="X", width="3", command=self.xClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def cClick(self):
        self.guess = "C"
        self.check()
        if self.guess in self.cGuess:
            self.buttonC.configure(text="C", width="3", command=self.cClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonC.configure(text="C", width="3", command=self.cClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def vClick(self):
        self.guess = "V"
        self.check()
        if self.guess in self.cGuess:
            self.buttonV.configure(text="V", width="3", command=self.vClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonV.configure(text="V", width="3", command=self.vClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def bClick(self):
        self.guess = "B"
        self.check()
        if self.guess in self.cGuess:
            self.buttonB.configure(text="B", width="3", command=self.bClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonB.configure(text="B", width="3", command=self.bClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def nClick(self):
        self.guess = "N"
        self.check()
        if self.guess in self.cGuess:
            self.buttonN.configure(text="N", width="3", command=self.nClick, relief="sunken", bg="green", state="disabled")
        else:
            self.buttonN.configure(text="N", width="3", command=self.nClick, relief="sunken", bg="red", state="disabled")
        return self.guess
    def mClick(self):
        self.guess = "M"
        self.check()
        if self.guess in self.cGuess: #If your guess is correct, the button widget turns green and becomes disabled
            self.buttonM.configure(text="M", width="3", command=self.mClick, relief="sunken", bg="green", state="disabled")
        else: #If not, the button widget turns red and becomes disabled
            self.buttonM.configure(text="M", width="3", command=self.mClick, relief="sunken", bg="red", state="disabled")

    #=========CORE FUNCTIONS==========
    def check(self):
        if self.guess in self.randomWord: #If self.guess contains a letter from self.randomWord, add the letter to self.cGuess
            self.cGuess = self.cGuess + self.guess
            self.check2()
        else:
            self.wGuess = self.wGuess + self.guess #If not, add the letter to self.wGuess
            self.hangman = Label(root, text=self.lives[len(self.wGuess)]).place(x=250,y=60) #Lives are dependent on the length of self.wGuess.
            if len(self.wGuess) == len(self.lives) - 1: #If there are 6 letters in self.wGuess, it's game over
                if tkinter.messagebox.askyesno("Game Over!", "Play again?"): #Game over popup box
                    self.restart_program()
                else:
                    self.myParent.destroy()

    def check2(self):
        for i in range(len(self.randomWord)):
            if self.randomWord[i] in self.cGuess:
                self.underscore = self.underscore[:i] + self.randomWord[i] + self.underscore[i+1:] #Replaces the underscores with correct letters
                self.wordLabel = Label(root, text=self.underscore, font=("Calibri", 38)).place(x=50,y=100) #The label is then refreshed
        if len(self.cGuess) == len(self.randomWord): #If the player guesses the word correctly
            tkinter.messagebox.showinfo("Game over!", "You win!")
    
    

root = Tk()
root.geometry("350x400+300+300")
root.title("Hangman")
myapp = hMan(root)
root.mainloop()

