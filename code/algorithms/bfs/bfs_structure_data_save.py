import structurecopy, bfs_algorithms, save_plots
import sys, timeit, time, xlsxwriter

class Node():
    """
    Creates a node item.
    """
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent



class Bfs_old():
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
            # print()
            # print(bfs_algorithms.print_grid_terminal(parent.grid))
            # print("you won")
            # print()
            win_path= bfs_algorithms.winning_path(self.game, parent)
            return win_path
        else:
            grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)


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
            if not any(node.grid == grid for node in self.explored):
                if not any(node.grid == grid for node in self.q):
                    temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))

    def search(self):

        parent = self.q.pop(0)
        self.explored.append(parent)

        if bfs_algorithms.game_won(self.game, parent.grid):
            # print()
            # print(bfs_algorithms.print_grid_terminal(parent.grid))
            # print("you won")
            # print()
            win_path= bfs_algorithms.winning_path(self.game, parent)
            return win_path
        else:
            grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

class Bfs_win_2():
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
            if not any(node.grid == grid for node in self.explored):
                if not any(node.grid == grid for node in self.q):
                    temp.append(grid)
        for grid in temp:
            self.q.append(Node(grid, parent))

    def search(self):

        parent = self.q.pop(0)
        self.explored.append(parent)

        if bfs_algorithms.game_won_2(self.game, parent.grid):
            # print()
            # print(bfs_algorithms.print_grid_terminal(parent.grid))
            # print("you won")
            # print()
            win_path= bfs_algorithms.winning_path(self.game, parent)
            return win_path
        else:
            grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
            self.add_nodes(grid_moves, parent)

class Bfs_post():
    """
    Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
    """
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))

    def search(self):

        parent = self.q.pop(0)
        if not any(node.grid == parent.grid for node in self.explored):
            self.explored.append(parent)

            if bfs_algorithms.game_won(self.game, parent.grid):
                # print()
                # print(bfs_algorithms.print_grid_terminal(parent.grid))
                # print("you won")
                # print()
                win_path= bfs_algorithms.winning_path(self.game, parent)
                return win_path
            else:
                grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
                for grid in grid_moves:
                    self.q.append(Node(grid, parent))

class Bfs_post_2():
    """
    Creates a tree containing nodes that can traverse all possible board states for a single puzzle.
    """
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))

    def search(self):

        parent = self.q.pop(0)
        if not any(node.grid == parent.grid for node in self.explored):
            self.explored.append(parent)

            if bfs_algorithms.game_won_2(self.game, parent.grid):
                # print()
                # print(bfs_algorithms.print_grid_terminal(parent.grid))
                # print("you won")
                # print()
                win_path= bfs_algorithms.winning_path(self.game, parent)
                return win_path
            else:
                grid_moves = bfs_algorithms.all_possible_max_moves(self.game, parent.grid)
                for grid in grid_moves:
                    self.q.append(Node(grid, parent))

def excelwriter(list, string):

    workbook = xlsxwriter.Workbook(string)
    sheet = workbook.add_worksheet()
    #declare data
    for item in range(len(list)):
        sheet.write(item, 0, list[item])

    workbook.close()

def Play_1():
    gridsize = 6
    csvfile = "Rushhour6x6_1.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_old(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)
    # print(list_of_moves)
    # print(len(list_of_moves))

def Play_2():

    gridsize = 6
    csvfile = "Rushhour6x6_1.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)
    # print(list_of_moves)
    # print(len(list_of_moves))

def Play_1_1_q():
    gridsize = 6
    csvfile = "Rushhour6x6_1.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_1_1_post():
    gridsize = 6
    csvfile = "Rushhour6x6_1.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_post(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)

def Play_1_2_q():
    gridsize = 6
    csvfile = "Rushhour6x6_1.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_win_2(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_1_2_post():
    gridsize = 6
    csvfile = "Rushhour6x6_1.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_post_2(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_2_1_q():
    gridsize = 6
    csvfile = "Rushhour6x6_2.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_2_1_post():
    gridsize = 6
    csvfile = "Rushhour6x6_2.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_post(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)

def Play_2_2_q():
    gridsize = 6
    csvfile = "Rushhour6x6_2.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_win_2(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_2_2_post():
    gridsize = 6
    csvfile = "Rushhour6x6_3.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_post_2(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_3_1_q():
    gridsize = 6
    csvfile = "Rushhour6x6_3.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_3_1_post():
    gridsize = 6
    csvfile = "Rushhour6x6_3.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_post(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)

def Play_3_2_q():
    gridsize = 6
    csvfile = "Rushhour6x6_3.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_win_2(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


def Play_3_2_post():
    gridsize = 6
    csvfile = "Rushhour6x6_3.csv"
    game = structurecopy.Game(csvfile, gridsize)
    grid = game.grid
    bfs = Bfs_post_2(grid, game)
    gamewon = False

    while not gamewon:
        gamewon = bfs.search()
    # list_of_moves = bfs_algorithms.moves_list(game, gamewon)


if __name__ == "__main__":
        list = []
        for i in range(1000):
            start = time.time()
            Play_1()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/1_old.xlsx")

        list = []
        for i in range(1000):
            start = time.time()
            Play_2()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/1_new.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_1_1_q()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/1_won1_q.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_1_1_post()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/1_won1_post.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_1_2_q()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/1_won2_q.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_1_2_post()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/1_won2_post_prune.xlsx")

        ###########################################################
        list = []
        for i in range(1000):
            start = time.time()
            Play_2_1_q()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/2_won1_q.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_2_1_post()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/2_won1_post.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_2_2_q()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/2_won2_q.xlsx")


        list = []
        for i in range(1000):
            start = time.time()
            Play_2_2_post()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/2_won2_post_prune.xlsx")


    ##############################################################
        list = []
        for i in range(200):
            start = time.time()
            Play_3_1_q()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/3_won1_q.xlsx")


        list = []
        for i in range(200):
            start = time.time()
            Play_3_1_post()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/3_won1_post_prune.xlsx")


        list = []
        for i in range(200):
            start = time.time()
            Play_3_2_q()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/3_won2_q.xlsx")


        list = []
        for i in range(200):
            start = time.time()
            Play_3_2_post()
            end = time.time()
            list.append(end - start)


        if len(list) > 0:
            excelwriter(list, "data/6x6/3_won2_post_prune.xlsx")
