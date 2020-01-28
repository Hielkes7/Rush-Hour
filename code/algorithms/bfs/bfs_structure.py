import structurecopy, bfs_algorithms, save_plots
import sys, timeit, time, xlsxwriter

class Node():
    """
    Creates a node item.
    """
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent

class Bfs_win_1():
    """
    Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
    this version uses pre-pruning and the first win-condition
    """

    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))


    def add_nodes(self, grid_moves, parent):
        """
            Creates new children nodes for grids not already in q or explored, and appends them to end of q
        """
        temp = []
        for grid in grid_moves:
            if self.duplicates(grid):
                temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))


    def duplicates(self, grid):
        """
            Checks if grids already exist in q or explored
        """

        for node in self.explored:
            if node.grid == grid:
                return False

        for node in self.q:
            if node.grid == grid:
                return False
        return True

    def search(self):
        """
            Goes through q until node with winning configuration is found, after inspection nodes are removed from the list and children are added to end of q.
        """

        parent = self.q.pop(0)
        self.explored.append(parent)

        if bfs_algorithms.game_won_1(self.game, parent.grid):
            win_path= bfs_algorithms.winning_path_1(self.game, parent)
            return win_path
        else:
            grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

class Bfs_win_2():
    """
        Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
        This version uses pre-pruning and the second win-condition
    """

    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))


    def add_nodes(self, grid_moves, parent):
        """
            Creates new children nodes for grids not already in q or explored, and appends them to end of q.
        """
        temp = []
        for grid in grid_moves:
            if self.duplicates(grid):
                temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))


    def duplicates(self, grid):
        """
            Checks if grid is already in q or explored
        """

        for node in self.explored:
            if node.grid == grid:
                return False

        for node in self.q:
            if node.grid == grid:
                return False
        return True

    def search(self):
        """
            Goes through q until node with winning configuration is found, after inspection nodes are removed from the list and children are added to end of q.
        """

        parent = self.q.pop(0)
        self.explored.append(parent)

        final_move = bfs_algorithms.game_won_2(self.game, parent.grid)
        if final_move:
            win_path = bfs_algorithms.winning_path_2(self.game, parent, final_move)
            return win_path
        else:
            grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

class Bfs_post_1():
    """
    Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
    This version uses post-pruning and the first win condition
    """
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))

    def duplicates(self, grid):
        """
            Checks if grid is already in q or explored
        """
        for node in self.explored:
            if node.grid == grid:
                return False
        return True

    def search(self):
        """
            Goes through q until node with winning configuration is found, after inspection nodes are removed from the list and children are added to end of q.
        """
        parent = self.q.pop(0)
        if self.duplicates(parent.grid):
            self.explored.append(parent)

            if bfs_algorithms.game_won_1(self.game, parent.grid):
                win_path= bfs_algorithms.winning_path_1(self.game, parent)
                return win_path
            else:
                grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
                for grid in grid_moves:
                    self.q.append(Node(grid, parent))

class Bfs_post_2():
    """
        Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
        This version uses post_pruning and the second win-condition.
    """
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))

    def duplicates(self, grid):
        """
            Checks if grid is already in  explored.
        """
        for node in self.explored:
            if node.grid == grid:
                return False
        return True

    def search(self):
        """
            Goes through q until node with winning configuration is found, after inspection nodes are removed from the list and children are added to end of q.
        """

        parent = self.q.pop(0)

        if duplicates(parent):
            self.explored.append(parent)

            if bfs_algorithms.game_won_2(self.game, parent.grid):
                win_path= bfs_algorithms.winning_path_2(self.game, parent)
                return win_path
            else:
                grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
                for grid in grid_moves:
                    self.q.append(Node(grid, parent))

def Play():
    gridsize = 6
    csvfile = "boards/Rushhour6x6_1.csv"

    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_win_1(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()

    print("moves made", len(gamewon))
    save_plots.save_all_plots(gamewon)
    list_of_moves = bfs_algorithms.moves_list(game, gamewon)
    print(list_of_moves)
    print(len(list_of_moves))


if __name__ == "__main__":

    start = time.time()
    Play()
    end = time.time()

    print("time it took", end - start)
