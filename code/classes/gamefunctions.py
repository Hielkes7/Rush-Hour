"""
    This file contains functions that supporting the algorithms and games that can be played.
"""

import random

def win(game):
    """
        Check if game is won according to the coordinates of the red car.
    """
    if (game.redcar.x == game.gridsize - 1) and (game.redcar.y == game.gridexit):
        return True
    else:
        return False

def update(game, car, x, y):
    """
        Updates the coordinates of a car and the grid.
    """
    game.moves += 1
    size_move_x = x - car.x
    size_move_y = y - car.y

    # update new position in car object
    car.x = x
    car.y = y

    # removes the car from the grid
    for i in range(game.gridsize + 1):
        for j in range(game.gridsize + 1):
            if game.grid[i][j] == car.id:
                game.grid[i][j] = 0

    # places the car in its new position in the grid
    if car.orientation == "V":
        for i in range(car.length):
            game.grid[x][y] = car.id
            y += 1

    else:
        for i in range(car.length):
            game.grid[x][y] = car.id
            x += 1

    # write move to output.csv file
    if car.orientation == "V":
        size_move = size_move_y
    else:
        size_move = size_move_x
    car_id = car.id
    game.list_moves.append([str(car_id), " " + str(size_move)])

def movable_up(game, car):
    """
        Checks whether above the given car is an empty spot.
    """

    # check if car is not next to upper edge
    if car.y + car.length <= game.gridsize:

        # check above the car for an empty spot
        if game.grid[car.x][car.y + car.length] == 0:
            return True
    return False

def movable_down(game, car):
    """
        Checks whether below the given car is an empty spot.
    """
    # check if car is not next to lower edge
    if car.y - 1 >= 0:

        # check below the car for an empty spots
        if game.grid[car.x][car.y - 1] == 0:
            return True
    return False

def movable_left(game, car):
    """
        Checks whether left of the given car is an empty spot.
    """
    # check if car is not next to the left edge
    if car.x - 1 >= 0:

        # check left of the car for an empty spots
        if game.grid[car.x - 1][car.y] == 0:
            return True
    return False

def movable_right(game, car):
    """
        Checks whether right of the given car is an empty spot.
    """
    # check if car is not next to the right edge
    if car.x + car.length <= game.gridsize:

        # check right the car for an empty spot
        if game.grid[car.x + car.length][car.y] == 0:
            return True
    return False

def car_is_movable(game, car):
    """
        Checks if a car can move in to at least one direction.
    """

    if car.orientation == 'V':
         if movable_up(game, car) or movable_down(game, car):
             return True
    elif car.orientation == 'H':
        if movable_left(game, car) or movable_right(game, car):
            return True
    return False

def direction(game, car):
    """
        Returns a random direction that a car can move into.
    """

    move_y_positive = False
    move_y_negative = False
    move_x_positive = False
    move_x_negative = False

    # check if the car can move up or down
    if car.orientation == "V":
        move_y_positive = movable_up(game, car)
        move_y_negative = movable_down(game, car)

    # else car can only move left or right
    else:
        move_x_positive = movable_right(game, car)
        move_x_negative = movable_left(game, car)

    if move_y_positive or move_y_negative:

        # if the car can move both up and down, randomly pick one
        if move_y_positive and move_y_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        # keep moving the car up untill it is blocked
        if move_y_positive:
            return "y positive"

        # keep moving the car down untill it's blocked
        if move_y_negative:
            return "y negative"

    if move_x_negative or move_x_positive:

        # if the car can move both left and right, randomly pick one
        if move_x_positive and move_x_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_x_positive = False
            else:
                move_x_negative = False

        # keep moving the car right untill it's it blocked
        if move_x_positive:
            return "x positive"

        # keep moving the car left untill it's it blocked
        if move_x_negative:
            return "x negative"

    else:
        return False
