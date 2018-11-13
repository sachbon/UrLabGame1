import time
import pygame
from pygame.locals import *

class gameManager(object):

    def __init__(self, size):
        self.windowSize = size
        self.timeElapsed = 0
        self.startTime = time.time()

        self.window = pygame.display.set_mode(size)

    def blit(self, image, pos):
        self.window.blit(image, pos)

    def flip(self):
        pygame.display.flip()
