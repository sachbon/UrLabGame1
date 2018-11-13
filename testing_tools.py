def printer(board):
	for i in range(len(board)):
		print("|",end="")
		for k in range(len(board[i])):
			if board[i][k][1] == 1:
				print("1",end="")
			elif board[i][k][1] == 2:
				print("2",end="")
			else:
				if board[i][k][0]:
					print("_",end="")
				else:
					print(" ",end="")
		print("|")
