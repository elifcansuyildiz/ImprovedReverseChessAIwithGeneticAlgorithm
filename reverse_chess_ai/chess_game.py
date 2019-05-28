import chess
import chess.variant
from cli_utils import *
from ai_player import AIPlayer

class ChessGame:
    def __init__(self, white_player, black_player, variant='suicide', max_turn=None, white_starts=True):
        if (variant == 'suicide'):
            self.board = chess.variant.SuicideBoard()
        elif (variant == 'chess'):
            self.board = chess.Board()
        else:
            raise Exception('Unknown chess variant: ' % variant)

        self.white_player = white_player
        self.black_player = black_player
        if (white_starts):
            self.current_player = white_player
        else:
            self.current_player = black_player
        self.max_turn = max_turn

    def play_half_turn(self):
        """ Makes current_player play for one turn then switch players then checks for game over
            Returns game over state and end result
        """
        
        move, point = self.current_player.play(self.board)
        self.board.push(move)

        if (isinstance(self.current_player, AIPlayer)):
            message = ''
            if (self.current_player == self.white_player):
                message += 'Turn ' + str(self.board.fullmove_number) + ' - White plays ' + str(move)
            else:
                message += 'Turn ' + str(self.board.fullmove_number) + ' - Black plays ' + str(move)
            print( board_to_str(self.board, message) )

        if (self.max_turn is not None and self.board.fullmove_number >= self.max_turn):
            True, self.board.result()

        if (self.current_player == self.white_player):
            self.current_player = self.black_player
        else:
            self.current_player = self.white_player

        return self.board.is_game_over(), self.board.result()
