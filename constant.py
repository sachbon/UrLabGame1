"""
    Author : fgrimau @jurofloem
    
"""

import pygame
from pygame.locals import *

#Initialization of the graphic library
pygame.init()

#Loading images
Background01 = pygame.image.load("sprites/background01.png").convert_alpha()
platform00   = pygame.image.load("sprites/platform00.png").convert_alpha()
