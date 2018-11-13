import map_edit as me
import testing_tools as tt

board = me.create_board(6,8)
me.set_platform(board,[3,2],3)
me.set_player_spawn(board,[1,2],1)
me.set_player_spawn(board,[4,5],2)
tt.printer(board)
