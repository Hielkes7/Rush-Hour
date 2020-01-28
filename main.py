from code.algorithms.backtrack import Backtrack
from code.classes.structure import Play
from code.algorithms.breadthfirst.breadthfirst_structure import breadthfirst

def main(algorithm):

    # change to other csv file when other game should be checked
    csv_file = "gameboards/Rushhour6x6_1.csv"

    # change gridsize if other csv file should be runned
    grid_size = 6

    # algorithm options that can be runned

    # random algorithms
    if algorithm == 'A':

        # step size can be "single" or "max"
        step_size = "max"

        # non recurring can be True or False
        non_recurring = True

        # win condition can be "win", "check_path_free" or "make_path_free"
        win_condition = "make_path_free"

        # animation can be True or False
        animation = False
        moves = Play(csv_file, grid_size, step_size, non_recurring, win_condition, animation)
        print(f"Amount of moves: {moves}")
        print("the steps of the game that is played are saved in output.csv")

    # backtrack algorithm
    if algorithm == 'B':

        #starts backtrack algorithm
        backtrack_algorithm = Backtrack(csv_file, grid_size)

        # arg 1: amount of dictionary games, arg 2: amount of last grids added
        backtrack_algorithm.add_final_grids(100, 10)

        # arg: amount of random games played
        average = backtrack_algorithm.random_moves_backtrack(100)
        print(f"the average score of all moves is: {average}")
        print("The steps of the last game that is played are saved in output.csv")

    # breadthfirst algorithm
    if algorithm == 'C':

        # step size can be "single" or "max"
        step_size = "max"

        # win condition can be "path_free" or "one_blocker"
        win_condition = "make_path_free"

        # pruning can be "pre" or "post"
        pruning = "pre"

        moves = Breadthfirst(grid_size, csv_file, step_size, win_condition, pruning)
        print(f"The minimum amount of moves is: {moves}")
        print("The steps of the best game that is played are saved in output.csv")

if __name__ == "__main__":

    # change letter to algorithm that you want to run
    main("C")
