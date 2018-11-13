import PyQt5
import time
from gameManager import gameManager as gM

"""
    Author: Olfg, fgrimau
    Date: 12/11/18
    Project: Skeleton for the main.py file for Turn Based Platformer (TBP)
"""

#Implementing Board
board = [[[False, 0],[False, 0],[False, 0],[False, 0],[True , 0],[True , 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[True , 0],[True , 0],[True , 0],[True , 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0]],
         [[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0],[False, 0]],
         [[False, 0],[True , 0],[True , 0],[True , 0],[True , 0],[True , 0],[True , 0],[False, 0]]]


#Setting up multiple variables
timeLeft = 0 #Contains the time left for a player to choose his movements
continueTime = False #Starts or stops the timer

timeBetweenFlips = 5 #TEMPORAIRE : Contains the current time since last update of the screen
maxTimeBetweenFlips = 1 #TEMPORAIRE : Contains the max time (in seconds), between 2 screen updates

timeElapsed = 0 #Contains the time that elasped between the last loop and the current one
startTime = time.time() #Contains the time from the start of the loop to calculate timeElapsed

screen = gM((16, 10))

running = True #While true, it will make the game update, if it steps to false, the game will stop

currentStep = 0 #The current step of the game (0, player 1 inputs his next movements, 1, player 2 inputs his next movement, 3 the game shows the movements of the players)

while running:
    timeElapsed = time.time() - startTime
    startTime = time.time()

    timeBetweenFlips += timeElapsed

    if timeBetweenFlips > maxTimeBetweenFlips:
        timeBetweenFlips = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x][0]:
                    screen.blit("#", (x, y))

        screen.flip()
