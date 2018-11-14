import time
import pygame
from pygame.locals import *

class gameManager(object):

    def __init__(self, size, name):
        self.windowSize = size
        self.timeElapsed = 0
        self.startTime = time.time()

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(name)

        self.hasGrid = False
        self.gridSize = 0

    def setGrid(self, grid, size):
        self.hasGrid = grid
        self.gridSize = size

    def update(self):
        self.timeElapsed = time.time() - self.startTime
        self.startTime = time.time()

    def blit(self, image, pos):
        self.window.blit(image, pos)

    def flip(self):
        if self.hasGrid:
            for x in range(self.windowSize[0]//self.gridSize):
                pygame.draw.line(self.window, (0, 0, 0), (x*self.gridSize, 0), (x*self.gridSize, self.windowSize[1]))

            for y in range(self.windowSize[1]//self.gridSize):
                pygame.draw.line(self.window, (0, 0, 0), (0, y*self.gridSize), (self.windowSize[0], y*self.gridSize))

        pygame.display.flip()
