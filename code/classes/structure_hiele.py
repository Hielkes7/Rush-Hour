import csv, os, random, time
import matplotlib.pyplot as plt

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
        for i in range(gridsize):
            gridrow = []
            for j in range(gridsize):
                gridrow.append(0)
            self.grid.append(gridrow)

        # open and read the start file
        file = open(csvfile)
        reader = csv.reader(file, delimiter=',')
        # close(csvfile)

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

    def win(self):
        """
            Returns True if the game is won, otherwise false.
        """
        if (self.redcar.x == self.gridsize - 1) and (self.redcar.y == self.gridexit):
            return True
        else:
            return False

    def win_hiele(self):
        """
            Returns True when the game is won. This happens when the path of
            the red car to the exit is free. When the game is won, this function
            also moves the red car to the exit
        """

        y_path = self.redcar.y
        for x_path in range(self.redcar.x + self.redcar.length, self.gridsize + 1):

            # check if any of the path blocks aren't 0
            if self.grid[x_path][y_path] != 0:
                return False

        # if path is free, remove red car from its original position
        self.grid[self.redcar.x][self.redcar.y] = 0
        self.grid[self.redcar.x + 1][self.redcar.y] = 0

        # add red car to exit position
        x_exit = self.gridsize - 1
        y_exit = int((self.gridsize + 1) / 2)
        self.grid[x_exit][y_exit] = "X"
        self.grid[x_exit + 1][y_exit] = "X"
        return True

    def update(self, car, x, y):
        """
            Updates the coordinates of a car and the grid.
        """
        car.x = x
        car.y = y

        # removes the car from the grid
        for i in range(self.gridsize + 1):
            for j in range(self.gridsize + 1):
                if self.grid[i][j] == car.id:
                    self.grid[i][j] = 0

        # places the car in its new position
        if car.orientation == "V":
            for i in range(car.length):
                self.grid[x][y] = car.id
                y += 1

        else:
            for i in range(car.length):
                self.grid[x][y] = car.id
                x += 1

    def movable_up(self, car):
        """
            Checks whether above the given car is an empty spot.
        """
        # check if car is not next to upper edge
        if car.y + car.length <= self.gridsize:

            # check above the car for an empty spot
            if self.grid[car.x][car.y + car.length] == 0:
                return True
            else:
                return False
        else:
            return False

    def movable_down(self, car):
        """
            Checks whether below the given car is an empty spot.
        """
        # check if car is not next to lower edge
        if car.y - 1 >= 0:

            # check below the car for an empty spots
            if self.grid[car.x][car.y - 1] == 0:
                return True
            else:
                return False
        else:
            return False

    def movable_left(self, car):
        """
            Checks whether left of the given car is an empty spot.
        """
        # check if car is not next to the left edge
        if car.x - 1 >= 0:

            # check left of the car for an empty spots
            if self.grid[car.x - 1][car.y] == 0:
                return True
            else:
                return False
        else:
            return False

    def movable_right(self, car):
        """
            Checks whether right of the given car is an empty spot.
        """
        # check if car is not next to the right edge
        if car.x + car.length <= self.gridsize:

            # check right the car for an empty spot
            if self.grid[car.x + car.length][car.y] == 0:
                return True
            else:
                return False
        else:
            return False

    def random_move_small_steps(self):

        car_possible = False
        while not car_possible:
            car = random.choice(self.cars)
            move_y_positive = False
            move_y_negative = False
            move_x_positive = False
            move_x_negative = False

            if car.orientation == 'V':
                if car.y + car.length <= self.gridsize:
                    if self.grid[car.x][car.y+car.length] == 0:
                        move_y_positive = True
                if car.y - 1 >= 0:
                    if self.grid[car.x][car.y-1] == 0:
                        move_y_negative = True

            if car.orientation == 'H':
                if car.x + car.length <= self.gridsize:
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
                y = car.y + 1
                self.update(car, x, y)

            else:
                y = car.y - 1
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
                x = car.x + 1
                self.update(car, x, y)

            else:
                x = car.x - 1
                self.update(car, x, y)

    def random_move_big_steps(self):
        """
            This function moves a random car as far as it can go.
        """

        # keep looping untill a randomly picked car is able to move
        car_movable = False
        while not car_movable:

            # pick random car
            car = random.choice(self.cars)
            print(car.id)
            move_y_positive = False
            move_y_negative = False
            move_x_positive = False
            move_x_negative = False

            # check if the car can move up or down
            if car.orientation == "V":

                # check if car can move up
                move_y_positive = self.movable_up(car)

                # check if car can move down
                move_y_negative = self.movable_down(car)

            # else car can only move left or right
            else:

                # check if car can move right
                move_x_positive = self.movable_right(car)

                # check if car can move left
                move_x_negative = self.movable_left(car)

            # if the car can move in any of the 4 directions, it's movable
            if move_y_positive or move_y_negative or move_x_positive or move_x_negative:
                car_movable = True

        print(True)

        # if the car can move both up and down, randomly pick one
        if move_y_positive and move_y_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        # if the car can move both left and right, randomly pick one
        if move_x_positive and move_x_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_x_positive = False
            else:
                move_x_negative = False

        # keep moving the car right untill it's it blocked
        if move_x_positive:
            while self.movable_right(car):
                self.update(car, car.x + 1, car.y)

        # keep moving the car left untill it's it blocked
        if move_x_negative:
            while self.movable_left(car):
                self.update(car, car.x - 1, car.y)

        # keep moving the car up untill it's it blocked
        if move_y_positive:
            while self.movable_up(car):
                self.update(car, car.x, car.y + 1)

        # keep moving the car down untill it's blocked
        if move_y_negative:
            while self.movable_down(car):
                self.update(car, car.x, car.y - 1)

    def random_move_non_recurrent(self):
        """
            This function moves a random car as far as it can go. It can't move
            the same car from the previous move. Returns the car it used
        """
        # keep looping untill a randomly picked car is able to move
        car_movable = False
        while not car_movable:

            # pick random car except previous car
            car = random.choice(self.cars)
            print(self.previous_car_id)
            print(car.id)
            time.sleep(1)
            while car.id == self.previous_car_id:
                print("change")
                car = random.choice(self.cars)

            print()
            # when found a new car, update previous_car_id
            self.previous_car_id = car.id

            move_y_positive = False
            move_y_negative = False
            move_x_positive = False
            move_x_negative = False

            # check if the car can move up or down
            if car.orientation == "V":

                # check if car can move up
                move_y_positive = self.movable_up(car)

                # check if car can move down
                move_y_negative = self.movable_down(car)

            # else car can only move left or right
            else:

                # check if car can move right
                move_x_positive = self.movable_right(car)

                # check if car can move left
                move_x_negative = self.movable_left(car)

            # if the car can move in any of the 4 directions, it's movable
            if move_y_positive or move_y_negative or move_x_positive or move_x_negative:
                car_movable = True

        # if the car can move both up and down, randomly pick one
        if move_y_positive and move_y_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        # if the car can move both left and right, randomly pick one
        if move_x_positive and move_x_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_x_positive = False
            else:
                move_x_negative = False

        # keep moving the car right untill it's it blocked
        if move_x_positive:
            while self.movable_right(car):
                self.update(car, car.x + 1, car.y)

        # keep moving the car left untill it's it blocked
        if move_x_negative:
            while self.movable_left(car):
                self.update(car, car.x - 1, car.y)

        # keep moving the car up untill it's it blocked
        if move_y_positive:
            while self.movable_up(car):
                self.update(car, car.x, car.y + 1)

        # keep moving the car down untill it's blocked
        if move_y_negative:
            while self.movable_down(car):
                self.update(car, car.x, car.y - 1)


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
        csvfile = "Rushhour6x6_super_easy.csv"
        game = Game(csvfile, gridsize)
        moves = 0
        gamewon = False


        while not gamewon:
            print(moves)
            game.random_move_small_steps()
            gamewon = game.win_hiele()
            moves += 1

        print(f"Done! It took {moves} moves to win the game")
        game.save_plot("finished.png")

class Save_frames():
    """
        Solves the game and saves each frame of each move made. This function
        crashes very quickly when to many frames are saved.
    """
    def __init__(self):

        gridsize = 6
        csvfile = "Rushhour6x6_1.csv"
        game = Game(csvfile, gridsize)
        moves = 0

        # save plot initial grid setup
        game.save_plot("frame0.png")
        while not game.win_hiele():
            game.print_grid_terminal()
            print(moves)
            game.random_move_big_steps()
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
        csvfile = "Rushhour6x6_1.csv"
        game = Game(csvfile, gridsize)
        moves = 0

        # plot of the first move
        plt.figure()
        ax = plt.axes()
        game.frame(ax)
        while not game.win_hiele():
            game.random_move_big_steps()
            moves += 1
            game.frame(ax)

        # save final frame
        game.frame(ax)

if __name__ == "__main__":
    # Play()
    Save_frames()
    # Animation()
