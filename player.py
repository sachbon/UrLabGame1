"""
    Author : Fgrimau
    Date : 13/11/2018
    Project : Skeleton for player class
"""

class player(object):

    """
        function __init__ : Inits the player's characteristics
        inputs : posX, the X position of the player in the grid
                 posY, the Y position of the player in the grid
                 color, an array representing the color of the player in RGB
        output : None
    """
    def __init__(self, posX, posY, color):
        self.pos = [posX, posY]
        self.color = color

    """
        function update : Moves the player by reading the movement array created by calling the function addMovement
        inputs : timeElapsed, the amount of time that passed since the last loop tour
                 map, the matrix representing the map
    """
    def update(self, timeElapsed, map):
        continue

    def addMovement(self, movement):
        continue

    def hit(self, hitpoints):
        continue
