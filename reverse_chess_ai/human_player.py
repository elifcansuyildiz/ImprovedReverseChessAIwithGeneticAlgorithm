import sys
import chess
from cli_utils import *

class HumanPlayer:
    def __init__(self, is_white):
        self.is_white = is_white

    def play(self, board):
        message = 'Legal Moves: '
        for i in board.legal_moves:
            message = message + '[' + str(i) + '] '
        try_again = True
        while (try_again == True):
            try:
                print(board_to_str(board))
                print(message)
                player_move = chess.Move.from_uci( input("Enter move: ") )
                return player_move, None
                try_again = False
            except Exception:
                print('-----')
                print('Wrong input. Try again!')
                try_again = True