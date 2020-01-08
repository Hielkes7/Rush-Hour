import csv


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
        print("car created")



class Grid():
    def __init__(self, M, N):
        self.grid = []
        for i in range(M):
            self.row = []
            for j in range(N):
                self.row.append(0)
            self.grid.append(self.row)


class Move():

    def print_grid_terminal(self):
        """
        This function prints the grid.
        """
        grid = Grid(7, 7)
        for row in grid.grid:
            for item in row:
                print(item, " ", end = '')
            print()

if __name__ == "__main__":
    car1 = Car('A', 'H', 0, 0, 2)
    car2 = Car('B', 'V', 0, 4, 3)
    move = Move()
    move.print_grid_terminal()



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
