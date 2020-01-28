from code.classes.structure import Game, Car
from code.algorithms import algorithms
from code.functions.functions import string
from code.functions import gamefunctions
import csv, random


class Backtrack():
    """
        This class represents an algorithm that uses function "add final grids"
        to find final grids or grids that are a variable steps before final grids
        and uses function "random moves backtrack" to randomly move and check if
        the current grid is known in the grid dictionary thus it known how many
        moves until the end.
    """

    def __init__(self, csvfile, gridsize):

        # initializes game information
        self.csvfile = csvfile
        self.gridsize = gridsize
        self.grid_dictionary = {}

    def add_final_grids(self, amount_of_games, amount_of_steps):
        """
            Creates a dictionary of grids of which is known how many steps it
            takes to reach the final state.
        """

        # creates a variable amount of games to fill the grid dictionary
        for number in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False
            game_moves = []
            game_grids = []
            grid_string = string(game.grid)
            game_grids.append(grid_string)

            # game continues until the winning gamestate is found
            while not gamewon:

                # executes a random step and returns a list with info about the step
                current_move = algorithms.random_max_step_non_recurring(game)

                # adds the move to the list with all game moves
                game_moves.append(current_move)

                # checks if the current gamestate is the winning gamestate
                gamewon = gamefunctions.win(game)

                # if game is not won, add the current grid to the gridlist
                if gamewon is False:
                    grid_string = string(game.grid)
                    game_grids.append(grid_string)

            list_length = game.moves - 1
            amount_of_steps = list_length

            # adds a predetermined amount of items to the dictionary
            for i in range(amount_of_steps):

                # current game grid
                grid = game_grids[-amount_of_steps+i]

                # moves that should be done from that gamegrid to find the endstate
                move_list = game_moves[-amount_of_steps+i:]

                # checks if grid is already in dictionary
                if grid in self.grid_dictionary:

                    # checks if amount of moves in dictionary are less than
                    # the current amount of moves
                    if len(self.grid_dictionary[grid]) > len(move_list):
                        self.grid_dictionary[grid] = move_list
                else:
                    self.grid_dictionary[grid] = move_list

    def random_moves_backtrack(self, amount_of_games):
        """
            Moves random and checks if current grid is already known.
        """

        totalmoves = 0

        # executes a predetermined amount of games
        for i in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False

            # executes steps until the winning gamestate is found
            while not gamewon:

                # takes a random step
                algorithms.random_max_step_non_recurring(game)

                # changes the grid into a string
                grid_string = string(game.grid)

                # checks if the grid is already known
                if grid_string in self.grid_dictionary:

                        # executes the moves that should be done to find the endstate
                        moves = self.grid_dictionary[grid_string]
                        amount_of_moves = len(self.grid_dictionary[grid_string])
                        for i in range(amount_of_moves):
                            move = moves[i]
                            car = move[0]
                            x = move[1]
                            y = move[2]
                            gamefunctions.update(game, car, x, y)
                            amount_of_moves -= 1
                        gamewon = True
                else:

                    # checks if path is free
                    algorithms.check_path_free(game)

                    # checks if game is won
                    gamewon = gamefunctions.win(game)

            # saves the total moves done in all games to calculate the average
            totalmoves += game.moves

        # calculates the average moves
        average_moves = totalmoves / amount_of_games

        # writing all moves in an output.csv file
        with open('output.csv', mode='w') as output_file:
            output_writer = csv.writer(output_file, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['car', ' move'])

            for move in game.list_moves:
                output_writer.writerow([move[0], move[1]])

        # returns the average moves
        return int(average_moves)
