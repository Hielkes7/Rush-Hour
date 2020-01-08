import csv

class Game():
    """
        Creates a game.
    """

    def __init__(self, csvfile, gridsize):

        # gridsize and grid creation

        self.gridsize = gridsize
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

        # fills grid with car id's
        for car in self.cars:
            x = car.x - 1
            y = car.y - 1
            if car.orientation == "V":
                for i in range(car.length):
                    self.grid[x][y] = car.id
                    y += 1
            else:
                for i in range(car.length):
                    self.grid[x][y] = car.id
                    x += 1
        print(self.grid)

        #
        # def manual(self):
        #     sd


    def random(self):

        car = random.choice(self.cars)
        carlist = []
        carlist.append(car)
        print(carlist)
        print("hoi")
        return carlist

    def updatecar(self):
        """
        liz doet dit
        """

    def move(self, car, direction):
        """
        de input hier is een keuze in auto en een keuze van - of +
        """

        """
        For moving the board, check Orientation,
        If Orientation is H only alteration of X is allowed, ergo only Y alteration is allowed if orientation is V

        - Start with steps of 1.

        - Prompt user for input (find the number game)
        - ask which car they want to move (A/Z)
        - Direction? (- or +)
        - All grids with identity of car, check if block next to them is either 0 or the same identity.
        - If not cancel move and return INVALID MOVE!
        - otherwise change the grid
        - change the coordinates in the item car.
        -random is basically, a loop that just selects a car at random,
        selects movement at random
        TADAAA
        - Next step is if the road to the exit is empty finish the game!
        """


class Car():
    """
        Creates a car object that is used for a game.
    """

    def __init__(self, car, orientation, x, y, length):
        self.id = car
        self.orientation = orientation
        self.x = int(x)
        self.y = int(y)
        self.length = int(length)

if __name__ == "__main__":
    game = Game("Rushhour9x9_1.csv", 9)
    item = game.random()
