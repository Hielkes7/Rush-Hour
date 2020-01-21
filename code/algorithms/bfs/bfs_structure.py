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

    def __init__(self, grid):
        self.queue = []
        self.explored = []
        queue.append(Node(grid, "LUCA"))
        print(queue)

    def add_nodes(self, moves, parent):
        temp = []
        for grid_move in moves:
            # dit kost teveel onnodig rekenwerk dit moet beter!
            if grid_move not in self.queue or self.explored:
                temp.append(grid_move)

        for grid_move in temp:
            self.queue.append(Node(move, parent))

        # append a null node as a divider ? so that you can remember the level?
        # q.append(Node(None, None))

    def search(self):
        # pop return
        parent = queue.pop(0)
        explored.append(parent)

        if wincondition(parent):
            print("you won")
            backtrack = bfs_algorithms.back_track(game, grid)
            return backtrack
        else:
            moves = possible_moves(parent)
            add_nodes(moves, parent)


        game.save_plot("finished.png")

if __name__ == "__main__":


        print("Hi! Let's wreck your memory with Rush-Hour!")
        gridsize = 6
        csvfile = "Rushhour6x6_test.csv"

        game = structurecopy.Game(csvfile, gridsize)
        grid = game.grid
        # list_of_grids = Bfs.search(grid)

        #dit is voor het testen van de correctheid van de bordconfiguratie

        # game.print_grid_terminal()
        # list = bfs_algorithms.all_possible_moves(game, grid)
        # print(list)

        # bfs_algorithms.back_track(game, grid, moeder)


        print(f"Done! It took {game.moves} moves to win the game")


# 1  procedure BFS(G, start_v) is
# 2      let Q be a queue
# 3      label start_v as discovered
# 4      Q.enqueue(start_v)
# 5      while Q is not empty do
# 6          v := Q.dequeue()
# 7          if v is the goal then
# 8              return v
# 9          for all edges from v to w in G.adjacentEdges(v) do
# 10             if w is not labeled as discovered then
# 11                 label w as discovered
# 12                 w.parent := v
# 13                 Q.enqueue(w)


# x = "000000000000000000000000x4000000000000000000000000x4000000000000000000000000x4000000000000000000000000x4`000000000000000000000000x4"
# y = x*4
# print("length x =", len(x))
# print(grid)
# print("len")
# print("size of grid", sys.getsizeof(grid))
# print("size of string ", sys.getsizeof(x))
# class Play():
#     test = Bfs()
#
#     while not test.search():
#         search()
#
#
# if __name__ == "__main__":
#     Play()









# import queue, copy
#
# depth = 3
# queue = queue.Queue()
# queue.put("")
# while not queue.empty():
#     state = queue.get()
#     print(state)
#     if len(state) < depth:
#         for i in ['L', 'R']:
#             child = copy.deepcopy(state)
#             child += i
#             queue.put(child
#
#
# Pseudocode
#
# Class Queue():
#     sdf

# Voeg de wortel van de graaf toe aan de queue
# Als er een knoop in de queue zit, neem deze uit de queue en bekijk de knoop:
# Als dit een oplossing is: stop het zoeken en geef de oplossing
# Als dit geen oplossing is: voeg alle kinderen van deze knoop toe aan het einde van de FIFO queue
# Als de queue leeg is: alle knopen zijn bekeken dus stop het zoeken en geef aan dat er geen oplossing is
# Ga door naar stap 2
# #
#   procedure BFS(G, start_v) is
# 2      let Q be a queue
# 3      label start_v as discovered
# 4      Q.enqueue(start_v)
# 5      while Q is not empty do
# 6          v := Q.dequeue()
# 7          if v is the goal then
# 8              return v
# 9          for all edges from v to w in G.adjacentEdges(v) do
# 10             if w is not labeled as discovered then
# 11                 label w as discovered
# 12                 w.parent := v
# 13                 Q.enqueue(w)
# #
# # https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/
#
# procedure BFS(G, start_v) is
# 2      let Q be a queue
# 3      label start_v as discovered
# 4      Q.enqueue(start_v)
# 5      while Q is not empty do
# 6          v := Q.dequeue()
# 7          if v is the goal then
# 8              return v
# 9          for all edges from v to w in G.adjacentEdges(v) do
# 10             if w is not labeled as discovered then
# 11                 label w as discovered
# 12                 w.parent := v
# 13                 Q.enqueue(w)
