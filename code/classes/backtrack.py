from structure import Game, Car
import algorithms
import functions

class Backtrack():
    """
        This class represents an algorithm that uses function "add final grids" to
        find final grids or grids that are a variable steps before final grids
        and uses function "random moves backtrack" to randomly move and check if the
        current grid is known in the grid dictionary thus it known how many moves until
        the end.
    """

    def __init__(self):

        # initializes game information
        self.gridsize = 6
        self.csvfile = "Rushhour6x6_1.csv"
        self.grid_dictionary = {}

    def add_final_grids(self, amount_of_games, amount_of_steps):
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
            grid_string = functions.string(game.grid)
            game_grids.append(grid_string)

            # game continues until the winning gamestate is found
            while not gamewon:

                # executes a random step and returns a list with info about the step
                current_move = algorithms.random_max_step(game)

                # adds the move to the list with all game moves
                game_moves.append(current_move)

                # checks if the current gamestate is the winning gamestate
                gamewon = algorithms.win(game)

                # if game is not won, add the current grid to the gridlist
                if gamewon is False:
                    grid_string = functions.string(game.grid)
                    game_grids.append(grid_string)

            list_length = game.moves - 1
            move_list = []

            for i in range(amount_of_steps):
                move_list += game_moves[list_length - i]
                grid = game_grids[list_length - i]

                if grid in self.grid_dictionary.keys():
                    if len(self.grid_dictionary[grid]) > (i + 1):
                        self.grid_dictionary[grid] = move_list
                else:
                    self.grid_dictionary[grid] = []
                    self.grid_dictionary[grid] = move_list
            print("done with one liz")

    def random_moves_backtrack(self, amount_of_games):
        """
            Moves random and checks if current grid is already known.
        """

        for i in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False
            while not gamewon:
                algorithms.random_max_step(game)
                grid_string = functions.string(game.grid)
                if grid_string in self.grid_dictionary.keys():
                        moves = self.grid_dictionary[grid_string]
                        while moves:
                            move = moves.pop()
                            car = move[0]
                            x = move[1]
                            y = move[2]
                            algorithms.update(game, car, x, y)
                        gamewon = True
                        print("endstate found!")
                else:
                    algorithms.check_path_free(game)
                    gamewon = algorithms.win(game)
            print(f"done! Game was won in {game.moves} moves")


if __name__ == "__main__":

    # start a backtrack algorithm
    backtrack = Backtrack()

    # add the 5 last grids from 10 games to the dictionary
    backtrack.add_final_grids(100, 5)

    # check from 10 games if the grids are in the dictionary
    backtrack.random_moves_backtrack(200)
