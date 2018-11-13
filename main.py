"""
    Author: Olfg, fgrimau
    Date: 12/11/18
    Project: Skeleton for the main.py file for Turn Based Platformer (TBP)
"""

import time
from gameManager import gameManager as gM

#Implementing Board as a matrix wich contains the position of each platforms
board = [[[False, 0],[False, 0],[False, 0],[False, 0],[True , 0],[True , 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[True , 0],[True , 0],[True , 0],[True , 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0]],
         [[False, 0],[True , 0],[True , 0],[True , 0],[True , 0],[True , 0],[True , 0],[False, 0]]]

#Setting up the gameManager class, wich manipulate the screen, the time and the sounds
gameManagager = gM((256, 192), "L.A.G.")

#importing every images loaded in constants
from constant import *

#Setting up multiple variables
timeLeft = 0 #Contains the time left for a player to choose his movements
continueTime = False #Starts or stops the timer

timeElapsed = 0 #Contains the time that elasped between the last loop and the current one
startTime = time.time() #Contains the time from the start of the loop to calculate timeElapsed

running = True #While true, it will make the game update, if it steps to false, the game will stop

currentStep = 0 #The current step of the game (0, player 1 inputs his next movements, 1, player 2 inputs his next movement, 3 the game shows the movements of the players)

while running:

    gameManagager.blit(Background01, (0, 0)) #Blits the background on the screen
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x][0]:
                gameManagager.blit(platform00, (x*32, y*32)) #Blits a platform image if the x/y position on the matrix is true

    gameManagager.flip() #Updates the screen

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
