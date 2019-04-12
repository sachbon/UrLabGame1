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
        self.movementState = "idle"

    """
        function draw : draw the player in its current state and place on the map
        inputs : gM, the gameManager object wich includes the screen
    """
    def draw(self, gM):
        x_plus = 0
        y_plus = 0
        if self.state == 1 and self.currentTimeBetweenMovement != 0:
            if self.nextMovements[0] == "right":
                x_plus = self.currentTimeBetweenMovement*(32/self.timeBetweenMovement)
            elif self.nextMovements[0] == "left":
                x_plus = -self.currentTimeBetweenMovement*(32/self.timeBetweenMovement)
            elif self.nextMovements[0] == "up":
                y_plus = -self.currentTimeBetweenMovement*(32/self.timeBetweenMovement)
            elif self.nextMovements[0] == "down":
                y_plus = self.currentTimeBetweenMovement*(32/self.timeBetweenMovement)
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
                    self.movementState = "right"
                    self.pos[0] += 1
                elif dir == "left":
                    self.movementState = "left"
                    self.pos[0] -= 1
                elif dir == "up":
                    self.movementState = "jumping"
                    self.pos[1] -= 1
                elif dir == "down":
                    self.movementState = "falling"
                    self.pos[1] += 1

                self.currentTimeBetweenMovement = 0
                del self.nextMovements[0]
                self.fall(map)
        elif self.state == 1 and len(self.nextMovements) == 0:
            self.movementState = "idle"
            self.fall(map)
            self.state = 0
        else:
            self.state = 0
            self.movementState = "idle"

    """
        function addMovement : adds a movement for the next time of movement
        inputs : movement, the movement to add
    """
    def addMovement(self, movement):
        if len(self.nextMovements) < self.maxMovements:
            print("Adding movement " + movement)
            self.nextMovements.append(movement)
            print("Len of nextMovements = " + str(len(self.nextMovements)))
        if len(self.nextMovements) >= self.maxMovements:
            self.state = 1

    """
        function fall : Makes the player fall if the position under him is empty
        inputs : map, the matrix containing the map
    """
    def fall(self, map):
        if self.movementState != "jumping":
            if self.pos[0] >= 0 and self.pos[0] < len(map[0]):
                if self.pos[1] >= 0 and self.pos[1] < len(map):
                    if map[self.pos[1]+1][self.pos[0]] == 0:
                        print("x=" + str(self.pos[0]) + "-y=" + str(self.pos[1]+1) + " is empty")
                        self.nextMovements.insert(0, "down")

    """
        function hit : Decrease the player health by the parameter given when the function is called
        inputs : hitpoints, the amount of health points the player will lose
    """
    def hit(self, hitpoints):
        self.currentLife -= hitpoints

    """
        function isDead : return wether the player is dead or not
        output : the function return true if the player is dead, false otherwise
    """
    def isDead(self):
        if self.currentLife <= 0:
            return True
        return False
