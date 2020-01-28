import csv, os, random, statistics, time, copy
from code.algorithms import algorithms
import code.functions.gamefunctions
import code.functions.functions
import matplotlib.pyplot as plt


class Game():
    """
        Creates a game.
    """

    def __init__(self, csvfile, gridsize):

        # variable for non recurring algorithm, start with dummy value
        self.previous_car_id = None

        # variable for correct output, start with dummy value
        # format: "car_id, +/- size_move"
        self.list_moves = []

        # gridsize and grid creation
        self.gridsize = gridsize - 1
        self.gridexit = int((gridsize / 2) + 1) - 1
        self.grid = []
        self.moves = 0
        for i in range(gridsize):
            gridrow = []
            for j in range(gridsize):
                gridrow.append(0)
            self.grid.append(gridrow)

        # open and read the start file
        file = open(csvfile)
        reader = csv.reader(file, delimiter=',')

        # empty list for the cars used in the game
        self.cars = []

        # creates car objects and adds to list
        for car, orientation, coordinates, length in reader:
            self.coordinates = coordinates.split(",")
            x = self.coordinates[0]
            y = self.coordinates[1]
            newcar = Car(car, orientation, x, y, length)
            self.cars.append(newcar)
            if car == 'X':
                self.redcar = newcar

        # fills grid with car id's
        for car in self.cars:
            x = car.x
            y = car.y
            if car.orientation == "V":
                for i in range(car.length):
                    self.grid[x][y] = car.id
                    y += 1
            else:
                for i in range(car.length):
                    self.grid[x][y] = car.id
                    x += 1

    def __str__(self):
        """
            Returns the grid of the game.
        """

        return self.grid


class Car():
    """
        Creates a car object that is used for a game.
    """
    def __init__(self, car, orientation, x, y, length):
        self.id = car
        self.orientation = orientation
        self.x = int(x) - 1
        self.y = int(y) - 1
        self.length = int(length)

    def __str__(self):
        """
            Returns the id of a car.
        """
        return self.id


class Play():
    """
        This function solves the game according to a given combination of algorithms. It then returns
        how many steps it took and creates a file output.csv in the folder Rush-Hour/results/ with all the
        moves made to solve the problem.
    """

    def __init__(self, csvfile, grid_size, step_size, non_recurring, win_condition, animation):
        """
            csvfile: Rushhour6x6_1, Rushhour6x6_2, ...
            grid_size = 6, 9, 12
            step_size = single, max
            non_recurring = True, False
            win_condition = win, check_path_free, make_path_free
            animation = True, False
        """
        game = Game(csvfile, grid_size)

        # frame of the begin state
        if animation:
            plt.figure()
            ax = plt.axes()
            functions.frame(ax, game.grid)

        # loop through game with algorithms until the win condition is matched
        gamewon = False

        # all possible combinations of algorithms
        if step_size == "single":
            if win_condition == "win":
                while not gamewon:
                    algorithms.random_single_step(game)
                    if animation:
                        functions.frame(ax, game.grid)
                    if algorithms.win(game):
                        gamewon = True
                        break

            elif win_condition == "check_path_free":
                while not gamewon:
                    algorithms.random_single_step(game)
                    if animation:
                        functions.frame(ax, game.grid)
                    if algorithms.check_path_free(game):
                        gamewon = True
                        break

            elif win_condition == "make_path_free":
                while not gamewon:
                    algorithms.random_single_step(game)
                    if animation:
                        functions.frame(ax, game.grid)
                    if algorithms.make_path_free(game):
                        gamewon = True
                        break

        elif step_size == "max":
            if not non_recurring:
                if win_condition == "win":
                    while not gamewon:
                        algorithms.random_max_step(game)
                        if animation:
                            functions.frame(ax, game.grid)
                        if algorithms.win(game):
                            gamewon = True
                            break

                elif win_condition == "check_path_free":
                    while not gamewon:
                        algorithms.random_max_step(game)
                        if animation:
                            functions.frame(ax, game.grid)
                        if algorithms.check_path_free(game):
                            gamewon = True
                            break

                elif win_condition == "make_path_free":
                    while not gamewon:
                        algorithms.random_max_step(game)
                        if animation:
                            functions.frame(ax, game.grid)
                        if algorithms.make_path_free(game):
                            gamewon = True
                            break

            elif non_recurring:
                if win_condition == "win":
                    while not gamewon:
                        algorithms.random_max_step_non_recurring(game)
                        if animation:
                            functions.frame(ax, game.grid)
                        if algorithms.win(game):
                            gamewon = True
                            break

                elif win_condition == "check_path_free":
                    while not gamewon:
                        algorithms.random_max_step_non_recurring(game)
                        if animation:
                            functions.frame(ax, game.grid)
                        if algorithms.check_path_free(game):
                            gamewon = True
                            break

                elif win_condition == "make_path_free":
                    while not gamewon:
                        algorithms.random_max_step_non_recurring(game)
                        if animation:
                            functions.frame(ax, game.grid)
                        if algorithms.make_path_free(game):
                            gamewon = True
                            break

        # frame of the final state
        if animation:
            functions.plot(ax, game.grid)

        # writing all moves in an output.csv file
        with open('output.csv', mode='w') as output_file:
            output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['car', ' move'])

            for move in game.list_moves:
                output_writer.writerow([move[0], move[1]])

        self.moves = game.moves
    def __str__(self):
        return str(self.moves)
