import random, copy, sys
import structurecopy


def all_possible_moves(game, grid):

    cars = game.cars
    grid = grid
    moves = []

    for car in cars:
        move_y_positive = False
        move_y_negative = False
        move_x_positive = False
        move_x_negative = False

        if car.orientation == 'V':
            move_y_positive = movable_up_bfs(game, grid, car)
            move_y_negative = movable_down_bfs(game, grid, car)

        if car.orientation == 'H':
            move_x_positive = movable_right_bfs(game, grid, car)
            move_x_negative = movable_left_bfs(game, grid, car)
        if move_y_positive:
            moves.append(move_y_positive)
        if move_y_negative:
            moves.append(move_y_negative)
        if move_x_positive:
            moves.append(move_x_positive)
        if move_x_negative:
            moves.append(move_x_negative)
    return moves

def all_possible_max_moves(game, grid):
    cars = game.cars
    grid = grid
    moves = []
    for car in cars:

        move_y_positive = False
        move_y_negative = False
        move_x_positive = False
        move_x_negative = False

        if car.orientation == 'V':
            move_y_positive = movable_up_max_bfs(game, grid, car)
            move_y_negative = movable_down_max_bfs(game, grid, car)

        if car.orientation == 'H':
            move_x_positive = movable_right_max_bfs(game, grid, car)
            move_x_negative = movable_left_max_bfs(game, grid, car)

        if move_y_positive:
            moves.append(move_y_positive)
        if move_y_negative:
            moves.append(move_y_negative)
        if move_x_positive:
            moves.append(move_x_positive)
        if move_x_negative:
            moves.append(move_x_negative)
    return moves


def movable_left_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    y = car.y
    for x in range(game.gridsize):
        if grid[x][y] == car.id:
            if x - 1 >= 0:
                if grid[x - 1][y] == 0:
                    move = -1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_right_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """

    y = car.y
    for x in range(game.gridsize):
        if grid[x][y] == car.id:
            if x + car.length <= game.gridsize:
                if grid[x + car.length][y] == 0:
                    move = 1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_up_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """

    x = car.x
    for y in range(game.gridsize):
        if grid[x][y] == car.id:
            if y  + car.length <= game.gridsize:
                if grid[x][y + car.length] == 0:
                    move = 1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False


def movable_down_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    x = car.x
    for y in range(game.gridsize):
        if grid[x][y] == car.id:
            if x - 1 <= game.gridsize:
                if grid[x][y - 1] == 0:
                    move = -1
                    return update_bfs(game, grid, car, x, y, move)
            else:
                return False

def movable_left_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    y = car.y
    for x in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0
            while True:
                if x -1 + move < 0:
                    break
                if grid[x -1 + move][y] !=0:
                    break
                move -= 1
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)


def movable_right_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    y = car.y
    for x in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0
            while True:
                if x + car.length + move > game.gridsize:
                    break
                if grid[x + car.length + move][y] != 0:
                    break
                move += 1
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)

def movable_up_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    x = car.x
    for y in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0
            while True:
                if y + car.length + move > game.gridsize:
                    break
                if grid[x][y + car.length + move] !=0:
                    break
                move += 1
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)


def movable_down_max_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    x = car.x
    for y in range(game.gridsize):
        if grid[x][y] == car.id:
            move = 0
            while True:
                if  y - 1 + move < 0:
                    break
                if grid[x][y - 1 + move] != 0:
                    break
                move -= 1
            if move == 0:
                return False
            else:
                return update_bfs(game, grid, car, x, y, move)


def update_bfs(game, grid, car, x, y, move):

    new_grid = copy.deepcopy(grid)
    if car.orientation == 'V':
        for i in range(car.length):
            new_grid[x][y + i] = 0
        for i in range(car.length):
            new_grid[x][y + i + move] = car.id
    else:
        for i in range(car.length):
            new_grid[x + i][y] = 0
        for i in range(car.length):
            new_grid[x + i + move][y] = car.id
    return new_grid


def game_won(game, grid):
    """
    checks if game is won
    """
    y = game.redcar.y
    for i in range(game.gridsize + 1):
        # check if this range works
        if grid[game.gridsize - i][y] == 'X':
            return True
        if grid[game.gridsize - i][y] != 0:
            return False


def back_track(game, node):
    """backtrack"""
    node = node
    moves_list = []
    while node.parent != "LUCA":
        moves_list.append(node.grid)
        node = node.parent
    moves_list.append(node.grid)

    return moves_list


# def moves_list(game, backtrack):
#
#     for i in range(len(backtrack)):
#         for i in range(game.gridsize)



def print_grid_terminal(grid):
    """
        This function prints the grid in the terminal
    """
    for y in range(len(grid)):
        for x in range(len(grid)):
            print(grid[y][x], " ", end="")
        print()
