def create_board(hight,lenght):
	board = []
	for i in range(hight):
		board.append([])
		for k in range(lenght):
			board[i].append([False,0])
	return board

#place a platform of given size
def set_platform(board,first_coord,size=1):
	hight = first_coord[0]
	begin = first_coord[1]
	for i in range(begin,begin+size-1):
		board[hight][i][0] = True

#place the player on a small platform
def set_player_spawn(board,coord,player):
	board[coord[0]][coord[1]] = [True,player]
