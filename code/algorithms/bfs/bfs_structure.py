import structurecopy, bfs_algorithms
import sys

class Node():
    """
    Stores info of node
    """
    def __init__(self, grid, parent):
        # zorg dat dit een deepcopy is!!!!!
        self.grid = grid
        # dit zou ook met id kunnen en dan ook id in parent ipv pointer.
        self.parent = parent

class Bfs():
    """
    Bfs
    """
    # ik weet niet precies tot in welke hoogte ik alles hierin wil laten gebeuren of niet?
    # q = []
    def __init__(self, grid, game):
        self.q = []
        self.explored = []
        self.game = game
        self.q.append(Node(grid, "LUCA"))
        # print(queue)

    def add_nodes(self, moves, parent):
        temp = []
        for grid_move in moves:
            if self.duplicates(grid_move):
                temp.append(grid_move)

        for grid_move in temp:
            self.q.append(Node(grid_move, parent))

        # return self.q

        # append a null node as a divider ? so that you can remember the level?
        # q.append(Node(None, None))

    def duplicates(self, grid):

        for nodes in self.q:
            if nodes.grid == grid:
                return False

        for nodes in self.explored:
            if nodes.grid == grid:
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
            moves = bfs_algorithms.all_possible_moves(self.game, parent.grid)
            self.add_nodes(moves, parent)





if __name__ == "__main__":


        print("Hi! Let's wreck your memory with Rush-Hour!")
        gridsize = 6
        csvfile = "Rushhour6x6_1.csv"

        game = structurecopy.Game(csvfile, gridsize)
        grid = game.grid
        bfs = Bfs(grid, game)
        bfs_algorithms.print_grid_terminal(grid)
        # list = bfs.search()

        # print(list)
        # list_of_grids = Bfs.search(grid, game)

        #dit is voor het testen van de correctheid van de bordconfiguratie
        """
        werken de grids?
        """
        # bfs_algorithms.print_grid_terminal(grid)
        # print()
        # list = bfs_algorithms.all_possible_moves(game, grid)
        # # print(list)
        # for grid in list:
        #     bfs_algorithms.print_grid_terminal(grid)
        #     print()

        """
        wordt alles goed in de q gezet
        """

        # test1 = bfs.search()
        # for node in test1:
        #     bfs_algorithms.print_grid_terminal(node.grid)
        #     print()
        #
        # print()
        # test2 = bfs.search()
        #
        # for node in test2:
        #     bfs_algorithms.print_grid_terminal(node.grid)
        #     print()
        #
        # test3 = bfs.search()
        #
        # for node in test3:
        #     bfs_algorithms.print_grid_terminal(node.grid)
        #     print()

        """
        werkt de backtrack?
        """

        # gamewon = False
        #
        # while not gamewon:
        #     gamewon = bfs.search()
        #
        # print("moves made", len(gamewon))
        # for grid in gamewon:
        #     bfs_algorithms.print_grid_terminal(grid)
        #     print()
