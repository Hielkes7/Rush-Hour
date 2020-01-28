from code.algorithms.backtrack import Backtrack
from code.classes.structure import Play
import code.algorithms.breadthfirst.breadthfirst_structure

def main(algorithm):

    # change to other csv file when other game should be checked
    csvfile = "Rushhour6x6_1.csv"

    # change gridsize if other csv file should be runned
    gridsize = 6

    # algorithm options that can be runned

    # backtrack algorithm
    if algorithm == 'A':

        #starts backtrack algorithm
        backtrack_algorithm = Backtrack(csvfile, gridsize)

        # arg 1: amount of dictionary games, arg 2: amount of last grids added
        backtrack_algorithm.add_final_grids(100, 10)

        # arg: amount of random games played
        print(backtrack_algorithm.random_moves_backtrack(100))

        # the average score of all moves is printed
        # the steps of the last game that is played are saved in output.csv

    # random algorithms
    if algorithm == 'B':

        # step size can be "single" or "max"
        step_size = "max"

        # non recurring can be True or False
        non_recurring = True

        # win condition can be "win", "check_path_free" or "make_path_free"
        win_codition = "make_path_free"

        # animation can be True or False
        animation = False

        Play(csvfile, gridsize, step_size, non_recurring, win_condition, animation)

        # the steps of the game that is played are saved in output.csv

















if __name__ == "__main__":

    # change letter to algorithm that you want to run
    main("B")
