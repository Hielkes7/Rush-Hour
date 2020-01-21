# import sys
#
# grid = [['Q', 'Q', 'L', 'I', 'I', 'E', 0, 'B', 'B'],
#         ['R', 0, 'L', 0, 'X', 'E', 0, 0, 'A'],
#         ['R', 'N', 'N', 'N', 'X', 0, 0, 0, 'A'],
#         ['R', 'O', 'O', 'J', 'J', 'F', 'F', 'F', 'A'],
#         ['S', 'S', 'M', 0, 0, 0, 0, 0, 0],
#         ['T', 0, 'M', 'K', 0, 'G', 'D', 'D', 'D'],
#         ['T', 0, 0, 'K', 0, 'G', 0, 'C', 0],
#         ['U', 0, 0, 'K', 0, 'G', 0, 'C', 0],
#         ['U', 'P', 'P', 'P', 'H', 'H', 'H', 'C', 0]]
#
# gridstring = "QQLIIE0BBR0L0XE00ARNNNX000AROOJJFFFASSM000000T0MK0GDDDT00K0G0C0U00K0G0C0UPPPHHHC0"
# moves = "A12B43C42D34A12X43B32D32"
# print(len(gridstring))
# print(sys.getsizeof(grid))
# print(sys.getsizeof(gridstring))
# print(sys.getsizeof(moves))

for i in range(4):
    list.append([i,2*i])

for [i,j] in list:
    print(i,j)
