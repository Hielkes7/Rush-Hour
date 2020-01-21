import csv
import matplotlib.pyplot as plt

file = open("1mln small_steps, win_hiele.csv")
reader = csv.reader(file)

list_moves = []
for moves in reader:
    list_moves.append(int(moves[0]))

# create dictionary with N items and all values 0
dict_moves = {}
for i in range(list_moves[-1] + 1):
    dict_moves[i] = 0

for moves in list_moves:
    dict_moves[moves] += 1

categorized = []
width_bar = 5

# the current domain looked at
lower_lim = 0
upper_lim = width_bar
bar_count = 0
for key in dict_moves:
    if key > upper_lim:
        categorized.append(bar_count)
        upper_lim += width_bar
        bar_count = 0

    bar_count += dict_moves[key]

# add last items, because key didnt get above the last upper_lim
categorized.append(bar_count)



# making x-axis of number of moves
number_of_bars = int(list_moves[-1]/width_bar) + 1
moves = width_bar / 2
moves_axis = []
for i in range(number_of_bars):
    moves_axis.append(moves)
    moves += width_bar



plt.figure()
plt.bar(moves_axis, categorized, width=width_bar, bottom=None, align='center', data=None)
plt.show()
