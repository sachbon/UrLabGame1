#place a platform of given size
#	x is begin coord, - the rest of the platform, 0 void
#
#	for exemple for setplatform(board,[1,3],4)
#
#	0000000000
#	000x---000
#	0000000000
#
def set_platform(board,first_coord,size=1):
	hight = first_coord[0]
	begin = first_coord[1]
	for i in range(begin,begin+size-1):
		board[hight][i][0] = True
#place the player on a small platform
def set_player_spawn(board,coord,player):
	board[coord[0]][coord[1]] = [True,player]
