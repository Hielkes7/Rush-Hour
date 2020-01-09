grid = [["A", "B", "C", "D", "E", "F"],
        ["G", "H", "I", "J", "K", "L"],
        ["M", "N", "O", "P", "Q", "R"],
        ["S", "T", "U", "V", "W", "X"],
        ["Y", 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

def print_grid_terminal(grid):
    grid_size = len(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            print(grid[i][j], " ", end="")
        print()

print_grid_terminal(grid)
