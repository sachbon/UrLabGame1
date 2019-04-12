"""
    Author : fgrimau @jurofloem

"""

import pygame
from pygame.locals import *

#Initialization of the graphic library
pygame.init()

#Loading images
imBackground01 = pygame.image.load("assets/sprites/background01.png").convert_alpha()
imPlatform00   = pygame.image.load("assets/sprites/platform00.png").convert_alpha()
imPlayer       = pygame.image.load("assets/sprites/king.png").convert_alpha()
