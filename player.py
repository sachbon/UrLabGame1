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
    def __init__(self, img, pos, color):
        self.pos = pos
        self.color = color
        self.nextMovements = []
        self.maxMovements = 1
        self.img = img
        self.currentLife = 100
        self.maxLife = 100

        self.timeBetweenMovement = 0.5
        self.currentTimeBetweenMovement = 0

        self.state = 0

    def draw(self, gM):
        gM.blit(self.img, (self.pos[0]*32, self.pos[1]*32))

    """
        function update : Moves the player by reading the movement array created by calling the function addMovement
        inputs : timeElapsed, the amount of time that passed since the last loop tour
                 map, the matrix representing the map
    """
    def update(self, timeElapsed, map):
        if self.state == 1 and len(self.nextMovements) > 0:
            self.currentTimeBetweenMovement += timeElapsed
            if self.currentTimeBetweenMovement >= self.timeBetweenMovement:
                dir = self.nextMovements[0]
                if dir == "right":
                    self.pos[0] += 1
                elif dir == "left":
                    self.pos[0] -= 1
                elif dir == "up":
                    if self.pos[1] >= 0 and self.pos[1] < len(map) and self.pos[0] >= 0 and self.pos[0] < len(map[0]):
                        for y in range(1, abs(self.pos[1] - len(map))):
                            if map[self.pos[1]-y][x][0]:
                                self.pos[1] = self.pos[1] - y - 1
                                break
                elif dir == "down":
                    if self.pos[1] >= 0 and self.pos[1] < len(map) and self.pos[0] >= 0 and self.pos[0] < len(map[0]):
                        for y in range(1, len(map) - self.pos[1]):
                            if map[self.pos[1]+y][self.pos[0]][0]:
                                self.pos[1] = self.pos[1]+y-1
                self.currentTimeBetweenMovement = 0
                self.nextMovements.remove(0)
        else:
            self.state = 1

    def addMovement(self, movement):
        if len(self.nextMovements) <= self.maxMovements:
            self.nextMovements.append(movement)
        else:
            self.state = 1

    def move(self, dir):
        pass

    def hit(self, hitpoints):
        self.currentLife -= hitpoints

    def isDead(self):
        if self.currentLife <= 0:
            return True
        return False
