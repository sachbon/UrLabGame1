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

    def update(self, timeElapsed, map):
        continue

    def addMovement(self, movement):
        continue

    def hit(self, hitpoints):
        continue
