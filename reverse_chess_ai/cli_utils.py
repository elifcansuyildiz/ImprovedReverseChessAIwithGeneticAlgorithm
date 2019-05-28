import chess
import chess.variant
import sys

def board_to_str(board, message=None):
    tmp = ''
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        tmp += board.unicode(invert_color=True)
    else:
        tmp += str(board) # For Windows

    tmp_list = tmp.split('\n')
    board_str = "\n\n\n   a b c d e f g h\n  -----------------\n"
    for i in range(8):
        board_str += str(8-i) + "| " + tmp_list[i] + " |" + str(8-i)

        # Right Panel:
        if (message is not None and i == 3):
            board_str += '  [' + message + ']'
        if (board.result() == '1/2-1/2' and i == 4):
            board_str += '  [Draw!]'
        elif (board.result() == '1-0' and i == 4):
            board_str += '  [White Wins!]'
        elif (board.result() == '0-1' and i == 4):
            board_str += '  [Black Wins!]'

        board_str += "\n"
    board_str += "  -----------------\n   a b c d e f g h"

    return board_str
