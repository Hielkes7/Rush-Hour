grid = [['Q', 'Q', 'L', 'I', 'I', 'E', 0, 'B', 'B'],
        ['R', 0, 'L', 0, 'X', 'E', 0, 0, 'A'],
        ['R', 'N', 'N', 'N', 'X', 0, 0, 0, 'A'],
        ['R', 'O', 'O', 'J', 'J', 'F', 'F', 'F', 'A'],
        ['S', 'S', 'M', 0, 0, 0, 0, 0, 0],
        ['T', 0, 'M', 'K', 0, 'G', 'D', 'D', 'D'],
        ['T', 0, 0, 'K', 0, 'G', 0, 'C', 0],
        ['U', 0, 0, 'K', 0, 'G', 0, 'C', 0],
        ['U', 'P', 'P', 'P', 'H', 'H', 'H', 'C', 0]]

gridlength = 9
for i in range(gridlength):
    for j in range(gridlength):
        if grid[i][j] == 'A':
            grid[i][j] = 0
print(grid)
