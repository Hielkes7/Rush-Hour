import structurecopy, algorithms
import sys

gridsize = 6
csvfile = "Rushhour6x6_test.csv"
game = structurecopy.Game(csvfile, gridsize)
# car =  game.cars[0]
# id = car.id
# grid = game.grid
# move = [id, 1]
grid = game.grid
# # print(grid)
# grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],['X', 'X', 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0],[0, 'K', 0, 0, 0, 'H'],[0, 'K', 0, 0, 0, 'H']]

# for x in range(game.gridsize + 1):
#     for y in range(game.gridsize + 1):
#         print(grid[x][y])

# y = 0
# for row in grid:
#     x = 0
#     for coordinate in row:
#         print(coordinate)
#         print(x, y)
#         print()
#         x += 1
#     y += 1


list = algorithms.all_possible_moves(game, grid)
print("list0", list[0])
print("list2", list[1])



class Node():
    """
    Stores info of node
    """
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent


class Bfs():
    """
    why is every color weird?
    """
    q = []
    explored = []

    def add_nodes(self, moves, parent):
        # parent = q[0]
        for move in moves:
            q.append(Node(move, parent))

        # append a null node as a divider ? so that you can remember the level?
        # q.append(Node(None, None))

    def search(self):

        parent = q.pop(0)
        explored.append(parent)

        if wincondition(parent):
            print("you won")
            return True
        else:
            moves = possible_moves(parent)
            add_nodes(moves, parent)



    # we willen checken of de lijst leeg is zodat er geen errors zijn, maar dit hoeft alleen bij het begin eigenlijk.
    def empty(self):
        if not q:
            parent = "first move"
            return parent






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
