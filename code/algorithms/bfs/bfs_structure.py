import structurecopy, bfs_algorithms, save_plots
import sys, timeit, time

class Node():
    """
    Creates a node item.
    """
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent

        # def __eq__(self, other)


class Bfs():
    """
    Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
    """
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))


    def add_nodes(self, grid_moves, parent):
        """

        """
        temp = []
        for grid in grid_moves:
            if self.duplicates(grid):
                temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))


    def duplicates(self, grid):

        for node in self.explored:
            if node.grid == grid:
                return False

        for node in self.q:
            if node.grid == grid:
                return False
        return True

    def search(self):

        parent = self.q.pop(0)
        self.explored.append(parent)

        if bfs_algorithms.game_won(self.game, parent.grid):
            print()
            print(bfs_algorithms.print_grid_terminal(parent.grid))
            print("you won")
            print()
            backtrack = bfs_algorithms.back_track(self.game, parent)
            return backtrack
        else:
            grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

def Play():
    gridsize = 6
    csvfile = "Rushhour6x6_2.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs(grid, game)
    gamewon = False

    # bfs_algorithms.print_grid_terminal(grid)
    # print()
    # print()

    # moves = bfs_algorithms.all_possible_max_moves(game, grid)
    # for grid in moves:
    #     bfs_algorithms.print_grid_terminal(grid)
    #     print()

    while not gamewon:
        gamewon = bfs.search()


    print("moves made", len(gamewon))
    # save_plots.save_all_plots(gamewon)

if __name__ == "__main__":
        start = time.time()
        Play()
        end = time.time()
        print("total time", end-start)
