import matplotlib.pyplot as plt

def string(grid):
    """
        Takes a grid (which is a list of lists) and changes it into a string.
    """

    # adds all components of the lists to an empty string
    grid_string = "".join(["".join([str(character) for character in elem]) for elem in grid])

    # returns the new string
    return grid_string

def save_plot(file_name, grid):

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
    plt.savefig("frames/" + file_name)
    plt.cla()
    plt.clf()

def frame(ax, grid):
    """
    This function returns a live plot of the given grid
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
