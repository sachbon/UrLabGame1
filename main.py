"""
    Author: Olfg, fgrimau
    Date: 12/11/18
    Project: Skeleton for the main.py file for Turn Based Platformer (TBP)
"""

import time
from gameManager import gameManager as gM
from player import player as pl
from mapManager import mapManager

#Setting up the gameManager class, wich manipulate the screen, the time and the sounds
gameManager = gM((320, 256), "L.A.G.")
gameManager.setGrid(True, 32)
#importing every images loaded in constants
from constant import *

#Player Object
player1 = pl(imPlayer, [2, 0], None)
map1 = mapManager()
map1.loadMap("test")

#Setting up multiple variables
timeLeft = 0 #Contains the time left for a player to choose his movements
continueTime = False #Starts or stops the timer

timeElapsed = 0 #Contains the time that elasped between the last loop and the current one
startTime = time.time() #Contains the time from the start of the loop to calculate timeElapsed

running = True #While true, it will make the game update, if it steps to false, the game will stop

currentStep = 0 #The current step of the game (0, player 1 inputs his next movements, 1, player 2 inputs his next movement, 3 the game shows the movements of the players)

while running:

    gameManager.blit(imBackground01, (0, 0)) #Blits the background on the screen
    map1.draw(gameManager)

    player1.draw(gameManager)
    player1.update(gameManager.timeElapsed, map1.getMatrix())

    gameManager.flip() #Updates the screen

    gameManager.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_d:
                player1.addMovement("right")
            elif event.key == K_q:
                player1.addMovement("left")
            elif event.key == K_z:
                player1.addMovement("up")
