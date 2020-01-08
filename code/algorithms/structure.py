import csv

class Game():
    """
        Creates a game.
    """

    def __init__(self, csvfile, gridsize):

        # gridsize and grid creation
        self.gridsize = gridsize
        self.grid = (self.gridsize) * [((self.gridsize) * [0])]

        # open and read the start file
        file = open(csvfile)
        reader = csv.reader(file)
        print(reader)

        # empty list for the cars used in the game
        self.cars = []

        # creates car objects and adds to list
        for car, orientation, coordinates, length in reader:
            self.coordinates = coordinates.split(",")
            x = self.coordinates[0]
            y = self.coordinates[1]
            newcar = Car(car, orientation, x, y, length)
            self.cars.append(newcar)

        # fills grid with car id's
        for car in self.cars:
            x = car.x - 1
            y = car.y - 1
            if car.orientation == "V":
                for block in range(car.length - 1):
                    self.grid[x][y] = car.id
                    y += 1
            else:
                for block in range(car.length - 1):
                    self.grid[x][y] = car.id
                    x += 1
            print(self.grid)

class Car():
    """
        Creates a car object that is used for a game.
    """

    def __init__(self, car, orientation, x, y, length):
        self.id = car
        self.orientation = orientation
        self.x = x
        self.y = y
        self.length = length

if __name__ == "__main__":
    Game("Rushhour6x6_1.csv", 6)
