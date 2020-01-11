import csv, os, random
import matplotlib.pyplot as plt

######################### Functions ############################
def print_grid_terminal(grid):
    grid_size = len(grid)

    for y in range(grid_size):
        for x in range(grid_size):
            print(grid[y][x], " ", end="")
        print()

def random_move(cars):
    """
    This algorithm moves a random car in a random direction if possible
    """
    # choose random car
    random_car = random.choice(list(cars.keys()))

    # check if there are empty spots next to the car
    move_x_negative = False
    move_x_positive = False
    move_y_negative = False
    move_y_positive = False
    x, y, orientation, length = cars[random_car]

    car_moved = False

    while not car_moved:
        if orientation == "H":
            if x - 1 >= 0:
                if grid[y][x - 1] == 0:
                    move_x_negative = True
            if x + 1 < grid_size:
                if grid[y][x + length] == 0:
                    move_x_positive = True

            if move_x_negative and move_x_positive:
                random_choice =  random.choice([0, 1])
                if random_choice == 1:
                    move_x_positive = False
                else:
                    move_x_negative = False

            if move_x_negative:
                cars[random_car][0] -= 1

            if move_x_positive:
                cars[random_car][0] += 1


        if orientation == "V":
            if y - 1 >= 0:
                if grid[y - 1][x] == 0:
                    move_y_negative = True
            if y + 1 < grid_size:
                if grid[y + length][x] == 0:
                    move_y_positive = True

            if move_y_negative and move_y_positive:
                random_choice =  random.choice([0, 1])
                if random_choice == 1:
                    move_y_positive = False
                else:
                    move_y_negative = False

            if move_y_negative:
                cars[random_car][1] -= 1

            if move_y_positive:
                cars[random_car][1] += 1

        if move_x_negative or move_x_positive or move_y_negative or move_y_positive:
            car_moved = True

    return cars

def update_grid(cars):

    # create empty grid
    grid_size = 6
    grid = []
    for i in range(grid_size):
        grid.append([])
        for j in range(grid_size):
            grid[i].append(0)

    # place the cars in the grid
    for car in cars:
        x = cars[car][0]
        y = cars[car][1]
        orientation = cars[car][2]
        length = cars[car][3]

        if orientation == "H":
            for i in range(length):
                grid[y][x] = car
                x += 1

        if orientation == "V":
            for i in range(length):
                grid[y][x] = car
                y += 1

    return(grid)

def save_plot(grid, file_name):
    """
    This function saves the plot of the given grid
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

    plt.figure()
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
    plt.savefig(file_name)
    plt.cla()
###########################################################



#################### Messy code #########################

# open file
csvfile = "Rushhour6x6_easy.csv"
file = open(csvfile)
reader = csv.reader(file, delimiter=',')

# create empty grid
grid_size = 6
grid = []
for i in range(grid_size):
    grid.append([])
    for j in range(grid_size):
        grid[i].append(0)

# list with all cars
cars = {}

# load all data from file
for car, orientation, coordinates, length in reader:

    # add data to dict cars
    coordinates = coordinates.split(",")
    x = int(coordinates[0])
    y = int(coordinates[1])
    cars[car] = [x-1, y-1, orientation, int(length)]


grid = update_grid(cars)
save_plot(grid, "frame1.png")
print_grid_terminal(grid)
cars = random_move(cars)
print()

grid = update_grid(cars)
save_plot(grid, "frame2.png")
print_grid_terminal(grid)
cars = random_move(cars)
print()

grid = update_grid(cars)
save_plot(grid, "frame3.png")
print_grid_terminal(grid)
cars = random_move(cars)
print()

grid = update_grid(cars)
save_plot(grid, "frame4.png")
print_grid_terminal(grid)
cars = random_move(cars)
print()

grid = update_grid(cars)
save_plot(grid, "frame5.png")
print_grid_terminal(grid)
cars = random_move(cars)
print()

grid = update_grid(cars)
save_plot(grid, "frame6.png")
print_grid_terminal(grid)
cars = random_move(cars)
print()
