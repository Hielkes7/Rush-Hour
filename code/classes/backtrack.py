from structure import Game, Car
import algorithms

class Backtrack():
    """
        This class represents an algorithm that uses function "add final grids" to
        find final grids or grids that are a variable steps before final grids
        and uses function "random moves backtrack" to randomly move and check if the
        current grid is known in the grid dictionary thus it known how many moves until
        the end.
    """

    def __init__(self):

        # game information
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
            game_grids.append(game.grid)

            # game continues until the winning gamestate is found
            while not gamewon:

                # executes a random step and returns a list with info about the step
                current_move = algorithms.random_max_step_non_recurring(game)

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
                if game_grids[list_length - i] in self.grid_dictionary.keys():
                    # kijk of de values minder zijn
                    if len(self.grid_dictionary[game_grid[list_length - i]]) > (i + 1):
                        self.grid_dictionary[game_grid[list_length - i]] = move_list
                else:
                    self.grid_dictionary[game_grid[list_length - i]] = []
                    self.grid_dictionary[game_grid[list_length - i]] = move_list
                    # voeg er nog aan toe dat alle moves worden toegevoegd

    def random_moves_backtrack(self, amount_of_games):
        """
            Moves random and checks if current grid is already known.
        """

        for i in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False
            while not gamewon:
                algorithms.random_max_step_non_recurring(game)
                if game.grid in self.grid_dictionary.keys():
                        moves = self.grid_dictionary[game.grid]
                        for move in moves:
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
    backtrack = Backtrack()
    backtrack.add_final_grids(10, 5)
    backtrack.random_moves_backtrack(10)
