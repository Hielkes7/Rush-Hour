import csv, os, random
import matplotlib.pyplot as plt


class Game():
    """
        Creates a game.
    """

    def __init__(self, csvfile, gridsize):

        # gridsize and grid creation
        self.gridsize = gridsize
        self.gridexit = int((gridsize / 2) + 1)
        self.grid = []
        for i in range(self.gridsize):
            gridrow = []
            for j in range(self.gridsize):
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

    def win(self):
        """
            Returns True if the game is won, otherwise false.
        """

        if (self.redcar.x == self.gridsize - 1) and (self.redcar.y == self.gridexit):
            return True
        else:
            return False


    def update(self, car, x, y):
        """
            Updates the coordinates of a car and the grid.
        """

        car.x = x
        car.y = y
        for i in range(self.gridsize):
            for j in range(self.gridsize):
                if self.grid[i][j] == car.id:
                    self.grid[i][j] = 0

        if car.orientation == "V":
            for i in range(car.length):
                self.grid[x-1][y-1] = car.id
                y += 1
        else:
            for i in range(car.length):
                self.grid[x-1][y-1] = car.id
                x += 1

    def random_move(self):

        car_possible = False
        while not car_possible:
            car = random.choice(self.cars)
            move_y_positive = False
            move_y_negative = False
            move_x_positive = False
            move_x_negative = False

            #onderstaande code geeft nog een foutmelding
            # print(car.x, car.y, car.orientation, car.length)
            if car.orientation == 'V':
                if car.y + car.length < self.gridsize:
                    if self.grid[car.x][car.y+car.length] == 0:
                        move_y_positive = True
                if car.y - 1 >= 0:
                    if self.grid[car.x][car.y-1] == 0:
                        move_y_negative = True

            if car.orientation == 'H':
                if car.x + car.length < self.gridsize:
                    if self.grid[car.x+car.length][car.y] == 0:
                        move_x_positive = True
                if car.x - 1 >= 0:
                    if self.grid[car.x-1][car.y] == 0:
                        move_x_negative = True

            if move_y_positive or move_y_negative or move_x_positive or move_x_negative:
                car_possible = True

        if move_y_positive or move_y_negative:
            x = car.x

            if move_y_positive and move_y_negative:
                random_choice =  random.choice([0, 1])
                if random_choice == 1:
                    move_y_positive = False
                else:
                    move_y_negative = False

            if move_y_positive:
                y = car.y + car.length
                self.update(car, x, y)

            elif move_y_negative:
                y = car.y
                self.update(car, x, y)

        if move_x_positive or move_x_negative:
            y = car.y

            if move_x_positive and move_x_negative:
                random_choice =  random.choice([0, 1])
                if random_choice == 1:
                    move_x_positive = False

                else:
                    move_x_negative = False

            if move_x_positive:
                x = car.x + car.length
                self.update(car, x, y)

            elif move_x_negative:
                x = car.x
                self.update(car, x, y)

        # print(f"go {car.x}, {car.y}, {car.orientation}" )

    def print_grid_terminal(self, grid):
        """
        puur voor visualising grid
        """
        grid_size = len(grid)

        for i in range(grid_size):
            for j in range(grid_size):
                print(grid[i][j], " ", end="")
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

def save_plot(grid, file_name):
    """
    This function saves the plot of the given grid
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
    grid_size = len(grid)

    plt.figure()
    ax = plt.axes()
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] != 0:
                block = plt.Rectangle((x, y), 1, 1, fc=colors[grid[x][y]])
                ax.add_patch(block)

    plt.axis('scaled')
    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.grid()
    plt.savefig(file_name)
    plt.cla()

gridsize = 6
csvfile = "Rushhour6x6_1.csv"

game = Game(csvfile, gridsize)
moves = 0
gamewon = False

save_plot(game.grid, "frame1.png")
game.random_move()

save_plot(game.grid, "frame2.png")
game.random_move()

save_plot(game.grid, "frame3.png")
game.random_move()

save_plot(game.grid, "frame4.png")
game.random_move()

save_plot(game.grid, "frame5.png")
game.random_move()

save_plot(game.grid, "frame6.png")
game.random_move()

# class Play():
#     """
#         Plays the game.
#     """
#     def __init__(self):
#         print("Hi! Let's play Rush-Hour!")
#         gridsize = 6
#         csvfile = "Rushhour6x6_1.csv"
        # gridsize = cs50.get_int("What is the gridsize?")
        # csvfile = cs50.get_string("Which CSV file should we use?")
        # correctfile = False
        # while correctfile == False:
        #     if (os.path.exists(csvfile)):
        #         game = Game(csvfile, gridsize)
        #         correctfile = True
        #     else:
        #         csvfile = cs50.get_string("CSV file does not exist. Which CSV file should we use?")
        # print("OK, let's go!")

        # dit moet aangepast worden
#         game = Game(csvfile, gridsize)
#         moves = 0
#         gamewon = False
#
#         while gamewon == False:
#             game.random_move()
#             gamewon = game.win()
#             moves += 1
#             print(moves)
#             if moves % 100 == 0:
#                 game.print_grid_terminal(game.grid)
#         print(f"Done! It took {moves} moves to win the game")
#
# if __name__ == "__main__":
#     Play()
