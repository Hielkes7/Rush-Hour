import matplotlib.pyplot as plt

grids = [[[0,0,0,0,0],
          [0,0,0,0,0],
          ["A","A",0,0,0],
          [0,0,0,0,0],
          [0,0,"B","B",0]],

         [[0,0,0,0,"A"],
          ["C",0,0,0,"A"],
          ["C",0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]]

def save_single_plot(grid, file_name):
    gridsize = len(grid)
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

    ax = plt.axes()
    for x in range(gridsize):
        for y in range(gridsize):
            if grid[x][y] != 0:
                block = plt.Rectangle((x, y), 1, 1, fc=colors[grid[x][y]])
                ax.add_patch(block)

    plt.axis('scaled')
    plt.xlim(0, gridsize)
    plt.ylim(0, gridsize)
    plt.grid()
    plt.savefig("frames/" + file_name)
    plt.cla()
    plt.clf()


def save_all_plots(grids):
    number_of_grids = len(grids)
    plt.figure()

    for i in range(number_of_grids):
        file_name = "frame" + str(i) + ".png"
        grid = grids[i]
        save_single_plot(grid, file_name)

save_all_plots(grids)
