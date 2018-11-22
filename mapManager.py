import pygame
from pygame.locals import *
from maps import maps

class mapManager(object):

    def __init__(self):
        self.size = None
        self.mapPath = None
        self.currentMap = None
        self.currentMatrix = None
        self.platformImg = pygame.image.load("assets/sprites/platform00.png")

    def loadMap(self, name):
        self.currentMap = maps[name]
        self.size = (maps[name]["width"], maps[name]["height"])
        self.currentMatrix = maps[name]["data"]

    def draw(self, gM):
        for y in range(len(self.currentMatrix)):
            for x in range(len(self.currentMatrix[y])):
                if self.currentMatrix[y][x] == 1:
                    gM.blit(self.platformImg, (x*32, y*32))

    def getMatrix(self):
        return self.currentMatrix

    def update(self, timeELapsed):
        #UPDATES THE MAP
        pass
