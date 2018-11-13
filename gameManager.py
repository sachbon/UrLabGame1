import time
import PyQt5

class gameManager(object):

    def __init__(self, size):
        self.windowSize = size
        self.timeElapsed = 0
        self.startTime = time.time()
        self.resetScreen()

    def resetScreen(self):
        self.screen = []
        for y in range(self.windowSize[1]):
            self.screen.append([])
            for x in range(self.windowSize[0]):
                self.screen[y].append(" ")

    def blit(self, char, pos):
        if len(char) == 1:
            self.screen[pos[1]][pos[0]] = char
        else:
            self.screen[pos[1]][pos[0]] = char[0]

    def flip(self):
        print("-" * (self.windowSize[0]+2))
        for y in range(self.windowSize[1]):
            print('|', end="")
            for x in range(self.windowSize[0]):
                print(self.screen[y][x], end="")
            print('|')
        print("-" * (self.windowSize[0]+2))
        self.resetScreen()
