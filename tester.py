import map_edit as me
import testing_tools as tt

board = me.create_board(6,8)
me.set_platform(board,[3,2],3)

tt.printer(board)
