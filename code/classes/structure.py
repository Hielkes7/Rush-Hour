import csv, os, random, statistics, time, copy
import code.algorithms.algorithms
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
        This function solves the game and then returns in how many moves it
        has done so.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")

        # user input way
        game_number = input("What game do you want to play? 1, 2, 3, 4, 5, 6 or 7: ")
        if game_number == "1" or game_number == "2" or game_number == "3":
            game_size = "6x6_"
            gridsize = 6
        elif game_number == "4" or game_number == "5" or game_number == "6":
            game_size = "9x9_"
            gridsize = 9
        elif game_number == "7":
            game_size = "12x12_"
            gridsize = 12
        else:
            print("Wrong input. Quiting")
            quit()
        csvfile = "gameboards/Rushhour" + game_size + game_number + ".csv"

        # prompting user for option to give an animation and/or save frames.
        animation = input("Do you want to see an animation of the solution? 'yes' or 'no': ")
        plots = input("Do you want all moves saved as png images? 'yes' or 'no': ")

        game = Game(csvfile, gridsize)

        # frame of the begin state
        if animation == "yes":
            plt.figure()
            ax = plt.axes()
            functions.frame(ax, game.grid)

        # save plot begin state
        if plots == "yes":
            all_grids = []
            all_grids.append(copy.deepcopy(game.grid))

        # loop through game with algorithms until the win condition is matched
        gamewon = False
        while not gamewon:
            algorithms.random_max_step_non_recurring(game)
            if algorithms.make_path_free(game):
                gamewon = True
                break

            algorithms.random_max_step_non_recurring(game)

            if animation == "yes":
                functions.frame(ax, game.grid)

            if plots == "yes":
                all_grids.append(copy.deepcopy(game.grid))

        # frame of the final state
        if animation == "yes":
            functions.frame(ax, game.grid)

        # save final frame
        if plots == "yes":
            all_grids.append(copy.deepcopy(game.grid))

        print()
        print(f"Done! It took {game.moves} moves to win the game.")
        print(f"All moves have been writen in a csv file called 'output.csv'.")

        # writing all moves in an output.csv file
        with open('output.csv', mode='w') as output_file:
            output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['car', ' move'])

            for move in game.list_moves:
                output_writer.writerow([move[0], move[1]])

        # save all plots
        if plots == "yes":
            counter = 0
            for grid in all_grids:
                file_name = "frame" + str(counter) + ".png"
                functions.save_plot(file_name, grid)
                counter += 1
            print()
            print("All frames have been saved in the folder 'frames'.")
            print("SIDENOTE: the amount of frames does not match the amount of moves due to our 'make_path_free' win condition.")


if __name__ == "__main__":
    Play()
