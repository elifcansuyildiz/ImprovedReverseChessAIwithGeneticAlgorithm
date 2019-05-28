class Genetic:
    def __init__(self, population, mutationRate, selectionRate, white_depth, black_depth, max_turn):
        self.population = population
        self.mutationRate = mutationRate
        self.selectionRate = selectionRate
        self.players = []
        for i in range(population):
            self.players.append( AI_Player(np.random.rand(12,64) * table_multiplier) )
        self.ref_ai = AI_Player (np.zeros((12,64)))
        self.white_depth = white_depth
        self.black_depth = black_depth
        self.max_turn = max_turn


    def selection(self):
        """ Applies selection for all players in genetic object according to selection value
        """
        #to sort the list in place
        self.players.sort(key=lambda x: x.fitness, reverse=True)
        self.players = self.players[0:int(self.population * self.selectionRate)]


        for i in self.players:
            print(i.fitness)

    def cross_over(self):
        """ Applies crossover for all players according to rate value
        """
        cross_over_tuple = [self.cross_over_pair(p1, p2) for p1 in self.players for p2 in self.players if p1 != p2]
        cross_over_list = []
        for i in cross_over_tuple:
            a, b = i
            cross_over_list.append(a)
            cross_over_list.append(b)
        random.shuffle(cross_over_list)
        self.players = cross_over_list[0:self.population]

    def cross_over_pair(self, ai_player1, ai_player2):
        """ Applies crossover between ai_player1 and ai_player2, produces new two ai players. 
        """
        x = random.randint(0, 768-1) # 12*8*8 = 768
        a1 = ai_player1.piece_square_table.flatten()
        a2 = ai_player2.piece_square_table.flatten()
        tmp = a2[:x].copy()
        a2[:x], a1[:x]  = a1[:x], tmp
        #print(a1.shape, a2.shape)
        return AI_Player( a1.reshape((12,64)) ), AI_Player( a2.reshape((12,64)) )

    def mutuation(self):
        """ Applies mutation for all players in genetic object according to rate value
        """
        for player in self.players:
            for i in range(12):
                for j in range(64):
                    if (random.randint(0, 99) < self.mutationRate):
                        player.piece_square_table[i,j] = random.uniform(-1,1) * table_multiplier

    def fitness(self):
        """ Applies fitness calculation with making all players play versus the reference player (only depth based search)
            This calculations will be made in multithreaded
        """
        pool = Pool(processes=THREAD_COUNT)
        fitness_list = pool.map(self.fitness_thread, self.players)
        for i in range(self.population):
            self.players[i].fitness = fitness_list[i]
        print(fitness_list)

    def fitness_thread(self, player):
        """ Child of fitness(). For multithreading purposes
        """
        game = ChessGame(player, self.white_depth, self.ref_ai, self.black_depth, self.max_turn)
        result, point = game.run()
        return self.decodeResult(result)*750 + point

    def decodeResult(self, result):
        """ Decodes result '1-0': WhiteWon, '0-1': BlackWon, else : Draw
            Returns 1 for white-won, -1 for black-won, 0 for draw
        """
        if (result == '1-0'):
            return +1
        elif (result == '0-1'):
            return -1
        else:
            return 0


PLAY CHESSIN ICINDEN GETIRDIM. BURAYA UYDURULACAK


    # runs in background, for training
    def run(self):
        """ Runs a game against white and black players
            Returns result ('1-0' for white-win, '0-1' for black-win, or something else for draw) 
                    AND final point of white player
        """
        final_point = 0
        #printBoard(self.board)
        for i in range(self.maxTurn):
            # WHITE PLAYS:
            ai_move, ai_value = self.white_player.bestMove(self.board, self.white_depth, True)
            if (ai_value != MAX_VALUE and ai_value != MIN_VALUE):
                final_point = ai_value + self.maxTurn - i
            self.board.push(ai_move)
            #printBoard(self.board)
            if (self.board.is_game_over()):
                return self.board.result(), final_point

            # BLACK PLAYS:
            ai_move, ai_value = self.black_player.bestMove(self.board, self.black_depth, False)
            if (ai_value != MAX_VALUE and ai_value != MIN_VALUE):
                final_point = -ai_value + self.maxTurn - i
            self.board.push(ai_move)
            #printBoard(self.board)
            if (self.board.is_game_over()):
                return self.board.result(), final_point