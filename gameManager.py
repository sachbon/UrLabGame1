import time
import pygame
from pygame.locals import *

class gameManager(object):

    """
        function init : defines the basic variables of the gameManager
        inputs : size, a tuple representing the size of the screen (sizeX, sizeY)
                 name, the name of the window
    """
    def __init__(self, size, name):

        self.sizeMultiplier = 3

        self.windowSize = size[0]*self.sizeMultiplier, size[1]*self.sizeMultiplier
        self.timeElapsed = 0
        self.startTime = time.time()

        self.window = pygame.display.set_mode(self.windowSize)
        self.preWindow = pygame.Surface(size)
        pygame.display.set_caption(name)

        self.hasGrid = False
        self.gridSize = 0

    """
        function setGrid : Defines wether there is a grid on the screen or not
        inputs : grid, bool representing wether if there is a grid or not
                 size, the size of the squares of the grid
    """
    def setGrid(self, grid, size):
        self.hasGrid = grid
        self.gridSize = size*self.sizeMultiplier

    """
        function update : updates the timeELapsed variable
    """
    def update(self):
        self.timeElapsed = time.time() - self.startTime
        self.startTime = time.time()

    """
        function blit : blits the image given at the given position
        inputs : image, the image to blit on the screen
                 pos, a tuple representing the position (x, y)
    """
    def blit(self, image, pos):
        self.preWindow.blit(image, pos)

    """
        function flip : updates the screen, drawing a grid on it if needed
    """
    def flip(self):
        self.window.blit(pygame.transform.scale(self.preWindow, self.windowSize), (0, 0))
        if self.hasGrid:
            for x in range(self.windowSize[0]//self.gridSize):
                pygame.draw.line(self.window, (0, 0, 0), (x*self.gridSize, 0), (x*self.gridSize, self.windowSize[1]))

            for y in range(self.windowSize[1]//self.gridSize):
                pygame.draw.line(self.window, (0, 0, 0), (0, y*self.gridSize), (self.windowSize[0], y*self.gridSize))

        pygame.display.flip()
