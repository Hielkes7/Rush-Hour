import csv
import matplotlib.pyplot as plt


def make_average_list(filename, amount_solutions_per_plot):
    file = open("data/game 2/" + filename)
    reader = csv.reader(file)

    list_moves = []
    for moves in reader:
        list_moves.append(int(moves[0]))

    list_average_moves = []
    solutions = []
    sum_moves = 0
    for i in range(len(list_moves)):
        sum_moves += list_moves[i]
        if i % number_solution_per_plot == 0:
            solutions.append(i)
            average_moves = sum_moves / (i + 1)
            list_average_moves.append(average_moves)

    return list_average_moves

number_solution_per_plot = 10

solutions = []
for i in range(int(5000/number_solution_per_plot)):
    solutions.append(i*number_solution_per_plot)

list_ave_1 = make_average_list("single step - win - 5k.csv", number_solution_per_plot)
list_ave_2 = make_average_list("single step - check path free - 5k.csv", number_solution_per_plot)
list_ave_3 = make_average_list("max step - check path free - 5k.csv", number_solution_per_plot)
list_ave_4 = make_average_list("queue - make path free - 5k.csv", number_solution_per_plot)
list_ave_5 = make_average_list("max step non recurring - check path free - 5k.csv", number_solution_per_plot)
list_ave_6 = make_average_list("max step non recurring - make path free - 5k.csv", number_solution_per_plot)


# print(len(solutions))
# print(len(list_ave_2))

plt.figure()
ax = plt.axes()
ax.set(xlim=(0, 5000), ylim=(0, 4000))
plt.title("Game 2 - Average moves per solution", fontsize = 30)
plt.xlabel("Solutions", fontsize = 25)
plt.ylabel("Average moves", fontsize = 25)
plt.plot(solutions, list_ave_1, 'r-', label="Single step - normal win")
plt.plot(solutions, list_ave_2, 'b-', label="Single step - check path free win")
plt.plot(solutions, list_ave_3, 'g-', label="Max step - check path free win")
plt.plot(solutions, list_ave_4, 'k-', label="Max step - always make path free")
plt.plot(solutions, list_ave_5, 'y-', label="Max step, non recurring - check path free")
plt.plot(solutions, list_ave_6, 'c-', label="Max step, non recurring - make path free")
plt.legend(loc=1, prop={'size': 15})
plt.show()
