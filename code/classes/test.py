# gridsize = 6
# grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# print(grid)
# x = 3
# y = 4
# print(grid[x][y])
# row = grid[0]
# print(row)
# row[0] = 'A'
# print(row)
#
# print(grid)

gridsize = 6
grid = []
for spot in range(gridsize):
    gridplace = []
    for spot in range(gridsize):
        gridplace.append(0)
    grid.append(gridplace)
print(grid)
x = 3
y = 4
grid[x][y] = 'A'
print(grid)
