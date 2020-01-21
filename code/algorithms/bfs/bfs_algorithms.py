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
        print("left move", move_x_negative)
        print("right move", move_x_positive)
        if move_y_positive:
            moves.append(move_y_positive)
        if move_y_negative:
            moves.append(move_y_negative)
        if move_x_positive:
            moves.append(move_x_positive)
        if move_x_negative:
            moves.append(move_x_negative)

        # deze is er puur en alleen voor als je terug wilt naar de moves overzichtelijker
        #bekijken (voor tests)
        # if move_y_positive:
        #     moves.append((car.id,1))
        # if move_y_negative:
        #     moves.append((car.id,-1))
        # if move_x_positive:
        #     moves.append((car.id,1))
        # if move_x_negative:
        #     moves.append((car.id,-1))
    return moves

def all_possible_moves_only(game, grid):

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
            moves.append((car.id,1))
        if move_y_negative:
            moves.append((car.id,-1))
        if move_x_positive:
            moves.append((car.id,1))
        if move_x_negative:
            moves.append((car.id,-1))
    return moves

# used to be up ish
def movable_left_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """
    for coordinate in grid[0]:
        if coordinate == car.id:
            print("hello there")
            print(coordinate)
            return False
    x = 0
    for column in grid:
        y = 0
        for coordinate in column:
            if coordinate == car.id:
                if x - 1 >= 0:
                    if grid[x - 1][y] == 0:
                        move = -1
                        new_grid = update_bfs(game, grid, car, x, y, move)
                        return new_grid
                    else:
                        return False
            y += 1
        x += 1

#used to be down ish
def movable_right_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """

    # check if car is not next to upper edge
    # gridsize = game.gridsize
    for coordinate in grid[game.gridsize]:
        if coordinate == car.id:
            return False
    x = 0
    for column in grid:
        y = 0
        for coordinate in column:
            if coordinate == car.id:
                if x + car.length <= game.gridsize:
                    if grid[x + car.length][y] == 0:
                        move = 1
                        new_grid = update_bfs(game, grid, car, x, y, move)
                        return new_grid
                    else:
                        return False
            y += 1
        x += 1

#used to be right
def movable_up_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """

    for row in grid:
        # print("row is", row)
        if row[game.gridsize] == car.id:
            return False
    x = 0
    for column in grid:
        y = 0
        for coordinate in column:
            if coordinate == car.id:
                if y + car.length <= game.gridsize:
                    if grid[x][y + car.length] == 0:
                        move = 1
                        new_grid = update_bfs(game, grid, car, x, y, move)
                        return new_grid
                    else:
                        return False
            y += 1
        x += 1

#used to be left
def movable_down_bfs(game, grid, car):
    """
        Checks whether above the given car is an empty spot.
    """

    for row in grid:
        if row[0] == car.id:
            return False
    x = 0
    for column in grid:
        y = 0
        for coordinate in column:
            if coordinate == car.id:
                if x - 1 >= 0:
                    if grid[x][y - 1] == 0:
                        move = -1
                        new_grid = update_bfs(game, grid, car, x, y, move)
                        return new_grid
                    else:
                        return False
            y += 1
        x += 1


def update_bfs(game, grid, car, x, y, move):
    print("grid entered")
    # return grid
    new_grid = copy.deepcopy(grid)
    print("grid before", grid)
    for i in range(game.gridsize + 1):
        for j in range(game.gridsize + 1):
            if new_grid[i][j] == car.id:
                new_grid[i][j] = 0
    print("grid after remove", grid)
    # this requires finding the starting space, otherwise it wont work.
    # so remember to always send the starting space of the car towards update_bfs
    if car.orientation == "V":
        for i in range(car.length):
            new_grid[x][y + move] = car.id
            y += 1

    else:
        for i in range(car.length):
            new_grid[x + move][y] = car.id
            x += 1
    print("grid after adding new car", grid)
    print("grid saved")

    return new_grid