from structure import Game, Car


class Backtrack():
    """
        This class represents an algorithm that uses function "add finalgrids" to
        find n amount of final grids or grids that are steps before final grids
        and uses function "random moves backtrack" to randomly move and check if the
        current grid found randomly is known in the grid dictionary thus known
        how many moves until the end.
    """

    def __init__(self):

        # game information
        self.gridsize = 6
        self.csvfile = "Rushhour6x6_1.csv"
        self.grid_dictionary = {}

    def add_finalgrids(self, amount_of_games, amount_of_steps):
        """
            Creates a dictionary of grids of which is known how many steps it
            takes to reach the final state.
        """

        # creates a variable amount of games to fill the grid dictionary
        for i in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False
            game_moves = []
            game_grids = []
            game_grids.append(game.grid)

            # game continues until the winning gamestate is found
            while not gamewon:
                step = algorithms.random_max_step_non_recurrent(game)

                # makes a list with information about the executed move
                current_move = []
                current_move.append(step.car)
                current_move.append(step.x)
                current_move.append(step.y)

                # adds the move to the list with all game moves
                game_moves.append(current_move)

                # checks if the current gamestate is the winning gamestate
                gamewon = algorithms.win(game)

                # if game is not won, add the current grid to the gridlist
                if gamewon is False:
                    game_grids.append(game.grid)

            list_length = game.moves - 1
            move_list = []

            for i in range(amount_of_steps):
                move_list += game_moves[list_length - i]
                if game_grid[list_length - i] in self.grid_dictionary.keys():
                    # kijk of de values minder zijn
                    if len(self.grid_dictionary[game_grid[list_length - i]]) > (i + 1):
                        self.grid_dictionary[game_grid[list_length - i]] = move_list
                else:
                    self.grid_dictionary[game_grid[list_length - i]] = []
                    self.grid_dictionary[game_grid[list_length - i]] = move_list
                    # voeg er nog aan toe dat alle moves worden toegevoegd

    def random_moves_backtrack(self, amount_of_moves):
        """
            Moves random and checks if current grid is already known.
        """

        for i in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False
            while not gamewon:
                algorithms.random_max_step_non_recurrent(game)
                if game.grid in self.grid_dictionary.keys():
                        pass
                gamewon = algorithms.win(game)
