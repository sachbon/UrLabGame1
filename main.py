"""
    Author: Olfg
    Date: 12/11/18
    Project: Skeleton for Turn Based Platformer (TBP)
"""
#Implementing Board
board = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
for i in range(len(board)):
    for k in range(len(board[i])):
        board[i][k] = [False,0]
        """
        for board[i][k][0], True if there is a platform, False if there isn't.
        for board[i][k][1], 0 if they are no players, 1 if player 1 is on platform, 2 if player 2 is on platform.
        """
