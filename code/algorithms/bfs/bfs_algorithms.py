import random, copy, sys
import structurecopy


def all_possible_single_moves(game, grid):
    """
        Returns a list of all the possible single step moves of a board state
    """
    cars = game.cars
    grid = grid
    moves = []

    # append all possible moves on
    for car in cars:
        if car.orientation == 'V':
            move_y_positive = movable_up_single_bfs(game, grid, car)
            move_y_negative = movable_down_single_bfs(game, grid, car)

            if move_y_positive:
                moves.append(move_y_positive)
            if move_y_negative:
                moves.append(move_y_negative)

        else:
            move_x_positive = movable_right_single_bfs(game, grid, car)
            move_x_negative = movable_left_single_bfs(game, grid, car)

            if move_x_positive:
                moves.append(move_x_positive)
            if move_x_negative:
                moves.append(move_x_negative)

    return moves

def all_possible_max_moves(game, grid):
    """
        Returns a list of all the possible single step moves of a board state
    """

    cars = game.cars
    grid = grid
    moves = []
    for car in cars:
        if car.orientation == 'V':
            move_y_positive = movable_up_max_bfs(game, grid, car)
            move_y_negative = movable_down_max_bfs(game, grid, car)

            if move_y_positive:
                moves.append(move_y_positive)
            if move_y_negative:
                moves.append(move_y_negative)
        else:
            move_x_positive = movable_right_max_bfs(game, grid, car)
            move_x_negative = movable_left_max_bfs(game, grid, car)

            if move_x_positive:
                moves.append(move_x_positive)
            if move_x_negative:
                moves.append(move_x_negative)
    return moves

def movable_left_single_bfs(game, grid, car):
    """
        If spot left of car is empty, returns a single step move left.
    """
    y = car.y

    # loops over x-axis until car is found
    for x in range(game.gridsize):
        if grid[x][y] == car.id:

            # returns False if car is outside board
            if x - 1 >= 0:

                # returns updated grid if spot left of car is empty else returns false
                if grid[x - 1][y] == 0:
                    move = -1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_right_single_bfs(game, grid, car):
    """
        If spot right of car is empty, returns single step move right.
    """
    y = car.y

    # loops over x-axis until car is found
    for x in range(game.gridsize):
        if grid[x][y] == car.id:

            # checks if car is not outside of  board
            if x + car.length <= game.gridsize:

                # returns updated grid if spot right of car is empty else returns false
                if grid[x + car.length][y] == 0:
                    move = 1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_up_single_bfs(game, grid, car):
    """
        If spot above car is empty, returns a single step move up.
    """

    x = car.x

    # loops over y-axis until car is found
    for y in range(game.gridsize):
        if grid[x][y] == car.id:

            # returns False if car is outside board
            if y  + car.length <= game.gridsize:

                # returns updated grid if spot above car is empty else returns false
                if grid[x][y + car.length] == 0:
                    move = 1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_down_single_bfs(game, grid, car):
    """
        If spot below car is empty, returns a single step move.
    """
    x = car.x

    # loops over y-axis until car is found
    for y in range(game.gridsize):
        if grid[x][y] == car.id:

            # returns False if car is outside board
            if x - 1 <= game.gridsize:

                # returns updated grid if spot above car is empty else returns false
                if grid[x][y - 1] == 0:
                    move = -1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_left_max_bfs(game, grid, car):
    """
        If empty spots left of car, returns the maximum move possible.
    """
    y = car.y
    # loops over x-axis until car is found
    for x in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0

            # do while loop that keeps checking spots farther left
            while True:

                # breaks loop if car is outside board
                if x -1 + move < 0:
                    break

                # breaks loop if other car encountered
                if grid[x -1 + move][y] !=0:
                    break
                move -= 1

            # returns updated grid if move possible else False
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)


def movable_right_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    y = car.y

    # loops over x-axis until car is found
    for x in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0

            # do while loop that keeps checking spots farther right
            while True:

                # returns False if car is outside board
                if x + car.length + move > game.gridsize:
                    break

                # breaks loop if other car encountered
                if grid[x + car.length + move][y] != 0:
                    break
                move += 1

            # returns updated grid if move possible else False
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)

def movable_up_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    x = car.x

    # loops over y-axis until car is found
    for y in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0

            # do while loop that keeps checking spots farther up
            while True:

                # breaks loop if car is outside board
                if y + car.length + move > game.gridsize:
                    break

                # breaks loop if other car encountered
                if grid[x][y + car.length + move] !=0:
                    break
                move += 1

            # returns updated grid if move possible else False
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)

def movable_down_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    x = car.x

    # loops over y-axis until car is found
    for y in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0

            # do while loop that keeps checking spots farther down
            while True:

                # breaks loop if car is outside board
                if  y - 1 + move < 0:
                    break

                # breaks loop if other car encountered
                if grid[x][y - 1 + move] != 0:
                    break
                move -= 1

            # returns updated grid if move possible else False
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)

def update_bfs(game, grid, car, x, y, move):
    """
        Returns grid with updated configuration after the move
    """
    new_grid = copy.deepcopy(grid)


    if car.orientation == 'V':

        # removes car from grid
        for i in range(car.length):
            new_grid[x][y + i] = 0

        # places car in its new position into grid
        for i in range(car.length):
            new_grid[x][y + i + move] = car.id
    else:

        # removes car from grid
        for i in range(car.length):
            new_grid[x + i][y] = 0

        # places car in its new position into grid
        for i in range(car.length):
            new_grid[x + i + move][y] = car.id
    return new_grid

def game_won_1(game, grid):
    """
        Returns true if the spots in front of the red car are free
    """
    y = game.redcar.y
    for i in range(game.gridsize + 1):
        if grid[game.gridsize - i][y] == 'X':
            return True
        if grid[game.gridsize - i][y] != 0:
            return False

def game_won_2(game, grid):
    """
        Returns true if there is only one removable car blocking the path of the red car
    """
    y = game.redcar.y
    blocking_cars = []

    # iterates over x axis and checks for cars blocking path
    for i in range(game.gridsize + 1):

        if grid[game.gridsize - i][y] == 'X':
            break
        if grid[game.gridsize - i][y] != 0:
            blocking_cars.append(game.gridsize - i)

    # if 1 car is blocking path create car variable else return False
    if len(blocking_cars) == 1:
        blocking_car = blocking_cars[0]
        blocking_car_id = grid[blocking_car][y]
        for car in game.cars:
            if car.id == blocking_car_id:
                blocking_car = car
    else:
        return False

    move_up = True
    move_down = True
    x = blocking_car.x

    # checks if there is are enough spots above car to free path
    for i in range(blocking_car.length):

        # breaks loop if car is outside board
        if y + 1 + i > game.gridsize:
            move_up = False
            break

        # breaks loop if other car is encountered
        if grid[x][y + 1 + i] != 0 and grid[x][y + 1 + i] != blocking_car.id:
            move_up = False
            break

    # checks if there is are enough spots above car to free path
    for i in range(blocking_car.length):

        # breaks loop if car is outside board
        if y - 1 - i < 0:
            move_down = False
            break

        # breaks loop if other car is encountered
        if grid[x][y - 1 - i] != 0 and grid[x][y - 1 - i] != blocking_car.id:
            move_down = False
            break

    # if move is possible return the corresponding grid
    if move_up:
        return movable_up_max_bfs(game, grid, blocking_car)
    if move_down:
        return movable_down_max_bfs(game,grid, blocking_car)
    else:
        return False

def winning_path(game, node, final_grid):
    """
        Returns a list containing the traversed grids of the fastest path to the exit for gamewon_1.
    """
    node = node
    moves_list = []

    while node.parent != "LUCA":
        moves_list.insert(0, node.grid)
        node = node.parent
    moves_list.insert(0, node.grid)

def winning_path_2(game, node, final_grid):
    """
        Returns a list containing the traversed grids of the fastest path to the exit for gamewon_2.
    """
    node = node
    moves_list = []
    moves_list.append(final_grid)
    while node.parent != "LUCA":
        moves_list.insert(0, node.grid)
        node = node.parent
    moves_list.insert(0, node.grid)

    return moves_list

    return moves_list

def moves_list(game, win_path):
    """
        Uses a list of all traversed board configurations to return a list of all moves used to get to the fastest exit.
    """
    moves_list = []

    # loops over all grids in win_path except for the last
    for i in range(len(win_path)-1):
        grid = win_path[i]
        next_grid = win_path[i + 1]
        car_id = None
        move_car = None

        # finds the car that has been moved between grids
        for x in range(game.gridsize + 1):
            for y in range(game.gridsize + 1):
                if grid[x][y] == 0 and next_grid[x][y] != 0:
                    car_id = next_grid[x][y]
                    break

        for car in game.cars:
            if car.id == car_id:
                move_car = car

        if move_car.orientation == 'V':
            old_y = []
            new_y = []
            x = move_car.x

            # calculates movement by substracting average coordinate of new
            # grid with the old_grid
            for y in range(game.gridsize + 1):
                if grid[x][y] == move_car.id:
                    old_y.append(y)
                if next_grid[x][y] == move_car.id:
                    new_y.append(y)
            movement = (sum(new_y) - sum(old_y))/len(new_y)
            moves_list.append([move_car.id, movement])
        else:
            old_x = []
            new_x = []
            y = move_car.y

            # calculates movement by substracting average coordinate of new
            # grid with the old_grid
            for x in range(game.gridsize + 1):
                if grid[x][y] == move_car.id:
                    old_x.append(x)
                if next_grid[x][y] == move_car.id:
                    new_x.append(x)

            movement = (sum(new_x) - sum(old_x))/len(new_x)
            moves_list.append([move_car.id, movement])

    grid = win_path[-1]
    print_grid_terminal(grid)
    red_car = game.redcar
    y = red_car.y
    min_move = red_car.length

    # adds the move that takes red car to exit
    for i in range(game.gridsize + 1):
        if grid[game.gridsize - i][y] == red_car.id:
                moves_list.append([red_car.id, i + min_move])
                break
    return moves_list



def print_grid_terminal(grid):
    """
        Prints the grid in the terminal
    """
    for y in range(len(grid)):
        for x in range(len(grid)):
            print(grid[y][x], " ", end="")
        print()

def excelwriter(list, string):
    """
        Writes list of data into an excel sheet
    """

    workbook = xlsxwriter.Workbook(string)
    sheet = workbook.add_worksheet()

    # declare data
    for item in range(len(list)):
        sheet.write(item, 0, list[item])

    workbook.close()
