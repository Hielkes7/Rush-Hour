import csv, os, random, time
import matplotlib.pyplot as plt
import algorithms

csvfile = "Rushhour6x6_easy.csv"

class Game():
    """
        Creates a game.
    """

    def __init__(self, csvfile, gridsize):

        # variable for non recurrent algorithm, start with dummy value
        self.previous_car_id = None

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

    def save_plot(self, file_name):

        colors = {'A': "#cc3399",
                  'B': "#FFF000",
                  'C': "#008000",
                  'D': "#0000FF",
                  'E': "#000000",
                  'F': "#00FFFF",
                  'G': "#FF00FF",
                  'H': "#FFA500",
                  'I': "#FFE455",
                  'J': "#BC8F8F",
                  'K': "#DA70D6",
                  'L': "#00ff00",
                  'M': "#0066ff",
                  'N': "#663300",
                  'O': "#003366",
                  'P': "#660066",
                  'Q': "#666699",
                  'R': "#339966",
                  'S': "#666633",
                  'T': "#00cc00",
                  'U': "#ff0066",
                  'V': "#cc3300",
                  'W': "#ff9999",
                  'X': "#FF0000",
                  'Y': "#99cc00"
                }

        plt.figure()
        ax = plt.axes()
        for x in range(self.gridsize + 1):
            for y in range(self.gridsize + 1):
                if self.grid[x][y] != 0:
                    block = plt.Rectangle((x, y), 1, 1, fc=colors[self.grid[x][y]])
                    ax.add_patch(block)

        plt.axis('scaled')
        plt.xlim(0, self.gridsize + 1)
        plt.ylim(0, self.gridsize + 1)
        plt.grid()
        plt.savefig(file_name)
        plt.cla()

    def frame(self, ax):
        """
        This function returns a live plot of the given grid
        """
        colors = {'A': "#cc3399",
                  'B': "#FFF000",
                  'C': "#008000",
                  'D': "#0000FF",
                  'E': "#000000",
                  'F': "#00FFFF",
                  'G': "#FF00FF",
                  'H': "#FFA500",
                  'I': "#FFE455",
                  'J': "#BC8F8F",
                  'K': "#DA70D6",
                  'L': "#00ff00",
                  'M': "#0066ff",
                  'N': "#663300",
                  'O': "#003366",
                  'P': "#660066",
                  'Q': "#666699",
                  'R': "#339966",
                  'S': "#666633",
                  'T': "#00cc00",
                  'U': "#ff0066",
                  'V': "#cc3300",
                  'W': "#ff9999",
                  'X': "#FF0000",
                  'Y': "#99cc00"
                }

        for x in range(self.gridsize + 1):
            for y in range(self.gridsize + 1):
                if self.grid[x][y] != 0:
                    block = plt.Rectangle((x, y), 1, 1, fc=colors[self.grid[x][y]])
                    ax.add_patch(block)

        plt.xlim(0, self.gridsize + 1)
        plt.ylim(0, self.gridsize + 1)
        plt.grid()
        plt.draw()
        plt.pause(0.3)
        plt.cla()

    def print_grid_terminal(self):
        """
            This function prints the grid in the terminal
        """
        for y in range(self.gridsize + 1):
            for x in range(self.gridsize + 1):
                print(self.grid[y][x], " ", end="")
            print()

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
        gridsize = 6
        # csvfile = "Rushhour6x6_easy.csv"
        game = Game(csvfile, gridsize)
        gamewon = False
        game.print_grid_terminal()
        print()
        while not gamewon:
            game.print_grid_terminal()
            algorithms.queue_algorithm(game)
            algorithms.redcar_path_free(game)
            gamewon = algorithms.win(game)

        print(f"Done! It took {game.moves} moves to win the game")
        # game.save_plot("finished.png")

class Save_frames():
    """
        Solves the game and saves each frame of each move made. This function
        crashes very quickly when to many frames are saved.
    """
    def __init__(self):

        gridsize = 6
        # csvfile = "Rushhour6x6_easy.csv"
        game = Game(csvfile, gridsize)
        moves = 0

        # save plot initial grid setup
        game.save_plot("frame0.png")
        while not game.win_hiele():
            game.print_grid_terminal()
            game.random_move_max_steps()
            print()
            moves += 1

            file_name = "frame" + str(moves) + ".png"
            game.save_plot(file_name)

        # save final frame
        file_name = "frame" + str(moves + 1) + ".png"
        game.save_plot(file_name)

        print(f"Done! It took {moves} moves to win the game")


class Animation():
    """
        Solves the game and produces a live animation of each move.
    """
    def __init__(self):

        gridsize = 6
        # csvfile = "Rushhour6x6_easy.csv"
        game = Game(csvfile, gridsize)
        moves = 0

        # plot of the first move
        plt.figure()
        ax = plt.axes()
        game.frame(ax)
        while not game.win_hiele():
            game.random_move_max_steps()
            moves += 1
            game.frame(ax)

        # save final frame
        game.frame(ax)

if __name__ == "__main__":
    Play()
