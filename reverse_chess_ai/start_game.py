import random
import sys
import numpy as np
import chess
import chess.variant
import chess.uci
from multiprocessing import Pool

from chess_game import ChessGame
from ai_player import AIPlayer
from human_player import HumanPlayer


max_turn = None
param_population = 20
param_mutationRate = 5  # [0 - 100]
param_selectionRate = 0.4   # [0.0 - 1.0]
param_whiteDepth = 2  # [Normal Ai]
param_blackDepth = 4  # [Trained Ai]
param_maxTurn = 150
param_epoch = 20
THREAD_COUNT = 8
table_multiplier = 50.0

def main():
    selected_game_mode = -1
    while (selected_game_mode < 0 or selected_game_mode > 3):
        print('Select game mode:')
        print('1. Normal chess')
        print('2. Reverse chess (suicide mode)')
        selected_game_mode = int(input('Selection: '))
        print('')

    selected_scenario = -1
    while (selected_scenario < 0 or selected_scenario > 7):
        print('Select game scenario:')
        print('1. Train AI')
        print('2. Watch trained AI vs trained AI')
        print('3. Watch trained AI vs normal AI')
        print('4. Watch normal AI vs normal AI')
        print('5. Play against trained AI')
        print('6. Play against normal AI')
        selected_scenario = int(input('Selection: '))

    # Select playing color if human vs ai
    selected_color = -1
    if (selected_scenario > 4 and selected_scenario <= 6):
        while (selected_color < 0 or selected_color > 3):
            print('Select Color:')
            print('1. White')
            print('2. Black')
            selected_color = int(input('Selection: '))


    game_variant = None
    if (selected_game_mode == 1):
        game_variant = 'chess'
    elif (selected_game_mode == 2):
        game_variant = 'suicide'
    else:
        raise Exception('Invalid game mode!')

    # Load train data if a scenario including 'trained AI' is selected
    # train_data = np.load('train_file.npy')

    # [1. Train AI]
    if (selected_scenario == 1):
        # todoooooooooooooooooooooooooo------------------------------------------
        pass
    else:
        white_player = None
        black_player = None
        # [2. Watch trained AI vs trained AI]
        if (selected_scenario == 2):
            white_player = AIPlayer(is_white=True, depth=3, piece_square_table=None)
            black_player = AIPlayer(is_white=False, depth=3, piece_square_table=None)
        # [3. Watch trained AI vs normal AI]
        elif (selected_scenario == 3):
            white_player = AIPlayer(is_white=True, depth=3, piece_square_table=None)
            black_player = AIPlayer(is_white=False, depth=3, piece_square_table=None)
        # [4. Watch normal AI vs normal AI]
        elif (selected_scenario == 4):
            white_player = AIPlayer(is_white=True, depth=3, piece_square_table=None)
            black_player = AIPlayer(is_white=False, depth=3, piece_square_table=None)
        # [5. Play against trained AI]
        elif (selected_scenario == 5):
            # [1. White]
            if (selected_color == 1):
                white_player = HumanPlayer(is_white=True)
                black_player = AIPlayer(is_white=False, depth=3, piece_square_table=None)
            # [2. Black]
            elif (selected_color == 2):
                white_player = AIPlayer(is_white=True, depth=3, piece_square_table=None)
                black_player = HumanPlayer(is_white=False)
            else:
                raise Exception('Invalid color!')
        # [6. Play against normal AI]
        elif (selected_scenario == 6):
            # [1. White]
            if (selected_color == 1):
                white_player = HumanPlayer(is_white=True)
                black_player = AIPlayer(is_white=False, depth=3, piece_square_table=None)
            # [2. Black]
            elif (selected_color == 2):
                white_player = AIPlayer(is_white=True, depth=3, piece_square_table=None)
                black_player = HumanPlayer(is_white=False)
            else:
                raise Exception('Invalid color!')
        else:
            raise Exception('Invalid scenario!')

        chess_game = ChessGame(white_player=white_player, black_player=black_player, variant=game_variant, max_turn=None)

        gameover = False
        result = None
        while (not gameover):
            gameover, result = chess_game.play_half_turn()
        print(gameover)
        print(result)


if __name__ == "__main__":
    main()

# def selection_train():
#     # Prepare genetic algorithm
#     g = Genetic(param_population, param_mutationRate, param_selectionRate, param_whiteDepth, param_blackDepth, param_maxTurn)

#     for i in range(param_epoch):
#         print('Fitness')
#         g.fitness()

#         np.save("train_file", g.players[0].piece_square_table)

#         print('Selection')
#         g.selection()
#         print("Cross-over")
#         g.cross_over()
#         print("Mutation")
#         g.mutuation()
#     g.fitness()
#     np.save("new_train_file", g.players[0].piece_square_table)
