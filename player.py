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
        self.maxMovements = 4
        self.img = img
        self.currentLife = 100
        self.maxLife = 100

        self.timeBetweenMovement = 0.5
        self.currentTimeBetweenMovement = 0

        self.lastMovement = None

        self.state = 0

    def draw(self, gM):
        x_plus = 0
        y_plus = 0
        if self.state == 1 and self.currentTimeBetweenMovement != 0:
            if self.nextMovements[0] == "right":
                x_plus = self.currentTimeBetweenMovement*(32/self.timeBetweenMovement)
            elif self.nextMovements[0] == "left":
                x_plus = -self.currentTimeBetweenMovement*(32/self.timeBetweenMovement)
            elif self.nextMovements[0] == "up":
                y_plus = -self.currentTimeBetweenMovement*(64/self.timeBetweenMovement)
            elif self.nextMovements[0] == "down":
                y_plus = self.currentTimeBetweenMovement*(64/self.timeBetweenMovement)
        gM.blit(self.img, (self.pos[0]*32 + x_plus, self.pos[1]*32 + y_plus))

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
                self.lastMovement = dir
                if dir == "right":
                    self.pos[0] += 1
                elif dir == "left":
                    self.pos[0] -= 1
                elif dir == "up":
                    self.pos[1] -= 2
                elif dir == "down":
                    self.pos[1] += 1

                self.currentTimeBetweenMovement = 0
                del self.nextMovements[0]
                self.fall(map)
        else:
            self.state = 0

    def addMovement(self, movement):
        if len(self.nextMovements) < self.maxMovements:
            print("Adding movement " + movement)
            self.nextMovements.append(movement)
            print("Len of nextMovements = " + str(len(self.nextMovements)))
        if len(self.nextMovements) >= self.maxMovements:
            self.state = 1

    def fall(self, map):
        if self.lastMovement == "left" or self.lastMovement == "right":
            if self.pos[0] >= 0 and self.pos[0] < len(map[0]):
                if self.pos[1] >= 0 and self.pos[1] < len(map):
                    if map[self.pos[1]+1][self.pos[0]][0] == False:
                        self.nextMovements.insert(0, "down")

    def hit(self, hitpoints):
        self.currentLife -= hitpoints

    def isDead(self):
        if self.currentLife <= 0:
            return True
        return False
