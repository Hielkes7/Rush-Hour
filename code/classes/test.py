move_list = [['A', 1, 2], ['B', 2, 1], ['C', 4, 5]]
move_grids = ["grid1", "grid2", "grid3"]
grid = "grid3"
dict = {}
dict[move_grids[2]] = []
dict[move_grids[2]].append(move_list[2])
dict[move_grids[2]].append(move_list[1])
print(dict)
if grid in dict.keys():
        print("yes!")
print(len(dict[move_grids[2]]))
