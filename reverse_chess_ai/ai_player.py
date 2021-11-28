import sys
import chess
import chess.variant
import random

class AIPlayer:
    def __init__(self, is_white, depth, piece_square_table=None):
        self.piece_square_table = piece_square_table
        self.is_white = is_white
        self.depth = depth
        self.piece_to_point = {'P':100, 'N':320, 'B':325, 'R':500, 'Q':975, 'K':100,'p':-100, 'n':-320, 'b':-325, 'r':-500, 'q':-975, 'k':-100, 'None':0}
        self.piece_to_num = {'P':0, 'N':1, 'B':2, 'R':3, 'Q':4, 'K':5,'p':6, 'n':7, 'b':8, 'r':9, 'q':10, 'k':11, 'None':-1}
        self.positive_infinity = sys.maxsize
        self.negative_infinity = - sys.maxsize - 1

    def play(self, board):
        """ Interface used connecting to ChessGame class. Makes player make one move.
            Returns best move and best value (predicted)
        """
        if (type(board).uci_variant == 'suicide'):
            return self.calculate_bestmove(board, self.depth, maximize=False)
        elif (type(board).uci_variant == 'chess'):
            return self.calculate_bestmove(board, self.depth, maximize=True)
        else:
            raise Exception('Unknown chess variant: ' % type(board).uci_variant)

    def calculate_bestmove(self, board, depth, maximize=True, alpha=(-sys.maxsize-1), beta=sys.maxsize):
        """ Calculates best move. Does minimax and alpha-beta pruning. On suicide game maximize must be False
            Returns best move and best value
        """
        if (depth == 0):
            return None, self.evaluate(board)

        if (maximize):
            best_point = self.negative_infinity
            best_move = None
            new_point = None

            # Randomize legal_moves list
            legal_moves = []
            for i in board.legal_moves:
                legal_moves.append(i)
            random.shuffle(legal_moves)

            for i in legal_moves:
                board.push(i)

                # Do not continue searching to leafs if game over
                if (board.result() == '1/2-1/2' or (self.is_white and board.result() == '0-1') or ((not self.is_white) and board.result() == '1-0')):
                    new_point = self.negative_infinity
                else:
                    _, new_point = self.calculate_bestmove(board, depth-1, not maximize, alpha, beta)

                if (new_point >= best_point):
                    best_point = new_point
                    best_move = i
                board.pop()

                # beta cut-off
                alpha = max(alpha, best_point)
                if (beta <= alpha):
                    break
            return best_move, best_point
        else:
            best_point = self.positive_infinity
            best_move = None
            new_point = None

            # Randomize legal_moves list
            legal_moves = []
            for i in board.legal_moves:
                legal_moves.append(i)
            random.shuffle(legal_moves)

            for i in legal_moves:
                board.push(i)

                # Do not continue searching to leafs if game over
                if (board.result() == '1/2-1/2' or (self.is_white and board.result() == '0-1') or ((not self.is_white) and board.result() == '1-0')):
                    new_point = self.positive_infinity
                else:
                    _, new_point = self.calculate_bestmove(board, depth-1, not maximize, alpha, beta)

                if (new_point <= best_point):
                    best_point = new_point
                    best_move = i
                board.pop()
                
                # alpha cut-off
                beta = min(beta, best_point)
                if (beta <= alpha):
                    break
            return best_move, best_point

    def evaluate(self, board):
        """ Does piece value evaluation based on ai color and uses piece-square table evaluation if given
            Returns evaluation point based on normal chess game. Dont forget to make result negative manually if playing suicide chess mode or etc.
        """
        total_point = 0.0
        for i in range(0,64):
            piece_str = str(board.piece_at(i))
            piece_int = self.piece_to_num[piece_str]
            if (piece_int >= 0 and self.piece_square_table is not None):
                total_point = total_point + self.piece_to_point[piece_str] + self.piece_square_table[piece_int][i]
            else:
                total_point = total_point + self.piece_to_point[piece_str]

        if (self.is_white):
            return total_point
        return -total_point