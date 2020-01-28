from code.algorithms.breadthfirst import breadthfirst_algorithm
from code.classes.structure import Game
import sys, timeit, time, csv

class Node():
    """
        Creates a node item.
    """

    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent

class Bfs_max_pre_win1():
    """
        Creates a tree containing nodes that can traverse all possible board
        states for a single puzzle. This version uses pre-pruning and the first
        win-condition, while one move consists of the maxium possible distance.
    """

    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "start_board"))


    def add_nodes(self, grid_moves, parent):
        """
            Creates new children nodes for grids not already in q or explored,
            and appends them to end of q.
        """

        temp = []
        for grid in grid_moves:
            if self.duplicates(grid):
                temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))


    def duplicates(self, grid):
        """
            Checks if grids already exist in q or explored.
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
            Goes through q until node with winning configuration is found,
            after inspection nodes are removed from the list and children are
            added to end of q.
        """

        parent = self.q.pop(0)
        self.explored.append(parent)

        if breadthfirst_algorithm.game_won_1(self.game, parent.grid):
            win_path= breadthfirst_algorithm.winning_path_1(self.game, parent)
            return win_path
        else:
            grid_moves = breadthfirst_algorithm.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

class Bfs_max_pre_win2():
    """
        Creates a tree containing nodes that can traverse all possible board
        states for a single puzzle. This version uses pre-pruning and the second
        win-condition,while one move consists of the maxium possible distance.
    """

    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "start_board"))


    def add_nodes(self, grid_moves, parent):
        """
            Creates new children nodes for grids not already in q or explored,
            and appends them to end of q.
        """

        temp = []
        for grid in grid_moves:
            if self.duplicates(grid):
                temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))


    def duplicates(self, grid):
        """
            Checks if grid is already in q or explored.
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
            Goes through q until node with winning configuration is found,
            after inspection nodes are removed from the list and children are
            added to end of q.
        """

        parent = self.q.pop(0)
        self.explored.append(parent)

        final_move = breadthfirst_algorithm.game_won_2(self.game, parent.grid)
        if final_move:
            win_path = breadthfirst_algorithm.winning_path_2(self.game, parent, final_move)
            return win_path
        else:
            grid_moves = breadthfirst_algorithm.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

class Bfs_max_post_win1():
    """
        Creates a tree containing nodes that can traverse all possible board
        states for a single puzzle. This version uses post-pruning and the first
        win condition, while one move consists of the maxium possible distance.
    """

    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "start_board"))

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
            Goes through q until node with winning configuration is found,
            after inspection nodes are removed from the list and children are
            added to end of q.
        """

        parent = self.q.pop(0)
        if self.duplicates(parent.grid):
            self.explored.append(parent)

            if breadthfirst_algorithm.game_won_1(self.game, parent.grid):
                win_path= breadthfirst_algorithm.winning_path_1(self.game, parent)
                return win_path
            else:
                grid_moves = breadthfirst_algorithm.all_possible_max_moves(self.game, parent.grid)
                for grid in grid_moves:
                    self.q.append(Node(grid, parent))

class Bfs_max_post_win2():
    """
        Creates a tree containing nodes that can traverse all possible board
        states for a single puzzle. This version uses post-pruning and the second
        win condition, while one move consists of the maxium possible distance.
    """
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "start_board"))

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
            Goes through q until node with winning configuration is found,
            after inspection nodes are removed from the list and children are
            added to end of q.
        """
        parent = self.q.pop(0)
        if self.duplicates(parent.grid):
            self.explored.append(parent)

            final_move = breadthfirst_algorithm.game_won_2(self.game, parent.grid)
            if final_move:
                win_path = breadthfirst_algorithm.winning_path_2(self.game, parent, final_move)
                return win_path
            else:
                grid_moves = breadthfirst_algorithm.all_possible_max_moves(self.game, parent.grid)
                for grid in grid_moves:
                    self.q.append(Node(grid, parent))

class Breadthfirst():

    def __init__(self, gridsize, csvfile, win_condition, pruning):

        game = Game(csvfile, gridsize)
        grid = game.grid


        if win_condition == "path_free":
            if pruning == "pre":
                bfs = Bfs_max_pre_win1(grid, game)
            else:
                bfs = Bfs_max_post_win1(grid, game)
        else:
            if pruning == "pre":
                bfs = Bfs_max_pre_win2(grid, game)
            else:
                bfs = Bfs_max_post_win2(grid, game)

        gamewon = False
        while not gamewon:
            gamewon = bfs.search()


        list_of_moves = breadthfirst_algorithm.moves_list(game, gamewon)


        with open('output.csv', mode='w') as output_file:
            output_writer = csv.writer(output_file, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['car', ' move'])

            for move in list_of_moves:
                output_writer.writerow([move[0], int(move[1])])

        self.moves = len(list_of_moves)

    def __str__(self):
        return str(self.moves)
