import matplotlib.pyplot as plt

# all colors in grid
# grid = [["A", "B", "C", "D", "E", "F"],
#         ["G", "H", "I", "J", "K", "L"],
#         ["M", "N", "O", "P", "Q", "R"],
#         ["S", "T", "U", "V", "W", "X"],
#         ["Y", 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]]

grid = [['Q', 'Q', 'L', 'I', 'I', 'E',  0,  'B', 'B'],
        ['R',  0,  'L',  0,  'X', 'E',  0,   0,  'A'],
        ['R', 'N', 'N', 'N', 'X',  0,   0,   0,  'A'],
        ['R', 'O', 'O', 'J', 'J', 'F', 'F', 'F', 'A'],
        ['S', 'S', 'M',  0,   0,   0,   0,   0,   0],
        ['T',  0,  'M', 'K',  0,  'G', 'D', 'D', 'D'],
        ['T',  0,   0,  'K',  0,  'G',  0,  'C',  0],
        ['U',  0,   0,  'K',  0,  'G',  0,  'C',  0],
        ['U', 'P', 'P', 'P', 'H', 'H', 'H', 'C',  0]]


def frame(grid):
    """
    This function returns a plot of the given grid
    """
    colors = {'A': "#cc3399",
              'B': "#FFF000",
              'C': "#008000",
              'D': "#0000FF",
              'E': "#000000",
              'F': "#00FFFF",
              'G': "#FF00FF",
              'H': "#FFA500",
              'I': "#FFE455",
              'J': "#BC8F8F",
              'K': "#DA70D6",
              'L': "#00ff00",
              'M': "#0066ff",
              'N': "#663300",
              'O': "#003366",
              'P': "#660066",
              'Q': "#666699",
              'R': "#339966",
              'S': "#666633",
              'T': "#00cc00",
              'U': "#ff0066",
              'V': "#cc3300",
              'W': "#ff9999",
              'X': "#FF0000",
              'Y': "#99cc00"
            }
    grid_size = len(grid)

    # plt.figure()
    ax = plt.axes()
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] != 0:
                block = plt.Rectangle((x, y), 1, 1, fc=colors[grid[x][y]])
                ax.add_patch(block)

    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.grid()
    plt.draw()
    plt.pause(0.3)
    plt.cla()

def plot(grid):
    """
    This function returns a plot of the given grid
    """
    colors = {'A': "#cc3399",
              'B': "#FFF000",
              'C': "#008000",
              'D': "#0000FF",
              'E': "#000000",
              'F': "#00FFFF",
              'G': "#FF00FF",
              'H': "#FFA500",
              'I': "#FFE455",
              'J': "#BC8F8F",
              'K': "#DA70D6",
              'L': "#00ff00",
              'M': "#0066ff",
              'N': "#663300",
              'O': "#003366",
              'P': "#660066",
              'Q': "#666699",
              'R': "#339966",
              'S': "#666633",
              'T': "#00cc00",
              'U': "#ff0066",
              'V': "#cc3300",
              'W': "#ff9999",
              'X': "#FF0000",
              'Y': "#99cc00"
            }
    grid_size = len(grid)

    plt.figure()
    ax = plt.axes()
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] != 0:
                block = plt.Rectangle((x, y), 1, 1, fc=colors[grid[x][y]])
                ax.add_patch(block)

    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.grid()
    plt.show()
    plt.cla()

def print_grid_terminal(grid):
    grid_size = len(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            print(grid[i][j], " ", end="")
        print()

def save_plot(grid, file_name):
    """
    This function saves the plot of the given grid
    """
    colors = {'A': "#cc3399",
              'B': "#FFF000",
              'C': "#008000",
              'D': "#0000FF",
              'E': "#000000",
              'F': "#00FFFF",
              'G': "#FF00FF",
              'H': "#FFA500",
              'I': "#FFE455",
              'J': "#BC8F8F",
              'K': "#DA70D6",
              'L': "#00ff00",
              'M': "#0066ff",
              'N': "#663300",
              'O': "#003366",
              'P': "#660066",
              'Q': "#666699",
              'R': "#339966",
              'S': "#666633",
              'T': "#00cc00",
              'U': "#ff0066",
              'V': "#cc3300",
              'W': "#ff9999",
              'X': "#FF0000",
              'Y': "#99cc00"
            }
    grid_size = len(grid)

    plt.figure()
    ax = plt.axes()
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] != 0:
                block = plt.Rectangle((x, y), 1, 1, fc=colors[grid[x][y]])
                ax.add_patch(block)

    plt.axis('scaled')
    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.grid()
    plt.savefig(file_name)
    plt.cla()

def animation_test():
    """
    This function makes an animation of the grid changing
    """

    grid1 = [[0,  0, 'X', 0, 0],
             [0,  0, 'X', 0, 'C'],
             [0,  0, 'D', 'D', 'C'],
             [0,  'A', 'A', 0, 0],
             [0,  0, 'B', 'B', 0]]
    grid2 = [[0,  0, 'X', 0, 0],
             [0,  0, 'X', 0, 'C'],
             [0,  0, 'D', 'D', 'C'],
             ['A', 'A', 0, 0, 0],
             [0,  0, 'B', 'B', 0]]
    grid3 = [[0,  0, 'X', 0, 0],
             [0,  0, 'X', 0, 'C'],
             [0,  0, 'D', 'D', 'C'],
             ['A', 'A', 0, 0, 0],
             [0,  0, 0, 'B', 'B']]
    grid4 = [[0,  0, 'X', 0, 'C'],
             [0,  0, 'X', 0, 'C'],
             [0,  0, 'D', 'D', 0],
             ['A', 'A', 0, 0, 0],
             [0,  0, 0, 'B', 'B']]
    grid5 = [[0,  0, 'X', 0, 'C'],
             [0,  0, 'X', 0, 'C'],
             [0,  0, 0, 'D', 'D'],
             ['A', 'A', 0, 0, 0],
             [0,  0, 0, 'B', 'B']]
    grid6 = [[0,  0, 0, 0, 'C'],
             [0,  0, 0, 0, 'C'],
             [0,  0, 0, 'D', 'D'],
             ['A', 'A', 'X', 0, 0],
             [0,  0, 'X', 'B', 'B']]

    plt.figure()
    for i in range(5):
        frame(grid1)
        frame(grid2)
        frame(grid3)
        frame(grid4)
        frame(grid5)
        frame(grid6)

def animation():
    """
    This function makes an animation of the grid changing
    """
    plt.figure()

    while not game_won:
        grid = move(grid)
        frame(grid)

animation_test()
# plot(grid)
# save_plot(grid, "grid.png")
