from structure import Game, Car
import algorithms, csv
import functions
import random
import sys
import gamefunctions

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
        self.csvfile = "gameboards/Rushhour6x6_1.csv"
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
            grid_string = functions.string(game.grid)
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
                    grid_string = functions.string(game.grid)
                    game_grids.append(grid_string)

            list_length = game.moves - 1

            for i in range(amount_of_steps):
                move_list = game_moves[-amount_of_steps+i:]
                grid = game_grids[list_length - i]

                if grid in self.grid_dictionary:
                    if len(self.grid_dictionary[grid]) > (i + 1):
                        self.grid_dictionary[grid] = move_list
                else:
                    self.grid_dictionary[grid] = move_list
        # for key, value in self.grid_dictionary.items():
        #     print(key, value)


    def random_moves_backtrack(self, amount_of_games):
        """
            Moves random and checks if current grid is already known.
        """

        for i in range(amount_of_games):
            game = Game(self.csvfile, self.gridsize)
            gamewon = False
            while not gamewon:
                step = algorithms.random_max_step_non_recurring(game)
                car_step = step[0]
                x_step = step[1]
                y_step = step[2]
                print(car_step, x_step, y_step)
                print
                grid_string = functions.string(game.grid)
                if grid_string in self.grid_dictionary:
                        moves = self.grid_dictionary[grid_string]
                        print(moves)
                        amount_of_moves = len(self.grid_dictionary[grid_string])
                        print(self.grid_dictionary[grid_string])
                        print(amount_of_moves)
                        print("found a path!")
                        # print(f"moves: {moves}")
                        for i in range(amount_of_moves):
                            move = moves[i]
                            # print(f"current move: {move}")
                            car = move[0]
                            x = move[1]
                            y = move[2]
                            print(f"current move: {car}, {x}, {y}")
                            gamefunctions.update(game, car, x, y)
                            amount_of_moves -= 1
                        gamewon = True
                else:
                    algorithms.check_path_free(game)
                    gamewon = gamefunctions.win(game)
            print(f"done! Game was won in {game.moves} moves")

            # writing all moves in an output.csv file
            with open('output.csv', mode='w') as output_file:
                output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                output_writer.writerow(['car', ' move'])

                for move in game.list_moves:
                    output_writer.writerow([move[0], move[1]])


if __name__ == "__main__":

    # start a backtrack algorithm
    backtrack = Backtrack()

    # add the 5 last grids from 10 games to the dictionary
    backtrack.add_final_grids(1000, 5)


    # check from 10 games if the grids are in the dictionary
    backtrack.random_moves_backtrack(10)
