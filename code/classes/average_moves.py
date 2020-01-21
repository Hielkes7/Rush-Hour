import csv
import matplotlib.pyplot as plt

file = open("6x6 game1 - max step - check path free.csv")
reader = csv.reader(file)

list_moves = []
for moves in reader:
    list_moves.append(int(moves[0]))


sum_moves = sum(list_moves)
average_moves = sum_moves/len(list_moves)

print("Average moves: ", average_moves)
