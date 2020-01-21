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
    car.x = x
    car.y = y

    # removes the car from the grid
    for i in range(game.gridsize + 1):
        for j in range(game.gridsize + 1):
            if game.grid[i][j] == car.id:
                game.grid[i][j] = 0

    # places the car in its new position
    if car.orientation == "V":
        for i in range(car.length):
            game.grid[x][y] = car.id
            y += 1

    else:
        for i in range(car.length):
            game.grid[x][y] = car.id
            x += 1

def check_path_free(game):
    """
        Checks if path of the red car is free and updates it.
    """
    redcar = game.redcar

    y_path = redcar.y
    for x_path in range(redcar.x + redcar.length, game.gridsize + 1):

        # check if any of the path blocks are not 0
        if game.grid[x_path][y_path] != 0:
            return False

    # move redcar to exit
    x = game.gridsize - 1
    y = game.gridexit
    update(game, redcar, x, y)
    return True

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

def random_move_single_step(game):

    car_possible = False
    while not car_possible:
        car = random.choice(game.cars)
        move_y_positive = False
        move_y_negative = False
        move_x_positive = False
        move_x_negative = False

        if car.orientation == 'V':
            move_y_positive = movable_up(game, car)
            move_y_negative = movable_down(game, car)

        if car.orientation == 'H':
            move_x_positive = movable_right(game, car)
            move_x_negative = movable_left(game, car)

        if move_y_positive or move_y_negative or move_x_positive or move_x_negative:
            car_possible = True

    if move_y_positive or move_y_negative:
        x = car.x

        if move_y_positive and move_y_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        if move_y_positive:
            y = car.y + 1
            update(game, car, x, y)

        else:
            y = car.y - 1
            update(game, car, x, y)

    if move_x_positive or move_x_negative:
        y = car.y

        if move_x_positive and move_x_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_x_positive = False

            else:
                move_x_negative = False

        if move_x_positive:
            x = car.x + 1
            update(game, car, x, y)

        else:
            x = car.x - 1
            update(game, car, x, y)

def random_move_max_steps(game):
    """
        This function moves a random car as far as it can go.
    """

    # keep looping untill a randomly picked car is able to move
    car_movable = False
    while not car_movable:

        # pick random car
        car = random.choice(game.cars)
        move_y_positive = False
        move_y_negative = False
        move_x_positive = False
        move_x_negative = False

        # check if the car can move up or down
        if car.orientation == "V":

            # check if car can move up
            move_y_positive = movable_up(game, car)

            # check if car can move down
            move_y_negative = movable_down(game, car)

        # else car can only move left or right
        else:

            # check if car can move right
            move_x_positive = movable_right(game, car)

            # check if car can move left
            move_x_negative = movable_left(game, car)

        # if the car can move in any of the 4 directions, it's movable
        if move_y_positive or move_y_negative or move_x_positive or move_x_negative:
            car_movable = True

    if move_y_positive or move_y_negative:
        x = car.x

        # if the car can move both up and down, randomly pick one
        if move_y_positive and move_y_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        # keep moving the car up untill it is blocked
        if move_y_positive:
            while movable_up(game, car):
                y = car.y + 1
                update(game, car, x, y)

        # keep moving the car down untill it's blocked
        if move_y_negative:
            while movable_down(game, car):
                y = car.y - 1
                update(game, car, x, y)

    if move_x_negative or move_x_positive:
        y = car.y

        # if the car can move both left and right, randomly pick one
        if move_x_positive and move_x_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_x_positive = False
            else:
                move_x_negative = False

        # keep moving the car right untill it's it blocked
        if move_x_positive:
            while movable_right(game, car):
                x = car.x + 1
                update(game, car, x, y)

        # keep moving the car left untill it's it blocked
        if move_x_negative:
            while movable_left(game, car):
                x = car.x - 1
                update(game, car, x, y)

def random_move_max_steps_non_recurrent(game):
    """
        This function moves a random car as far as it can go. It can't move
        the same car from the previous move. Returns the car it used
    """

    # keep looping untill a randomly picked car is able to move
    car_movable = False
    while not car_movable:

        # pick random car except previous car
        car = random.choice(game.cars)
        while car.id == game.previous_car_id:
            car = random.choice(game.cars)

        # when found a new car, update previous_car_id
        game.previous_car_id = car.id

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

        # if the car can move in any of the 4 directions, it's movable
        if move_y_positive or move_y_negative or move_x_positive or move_x_negative:
            car_movable = True

    if move_y_positive or move_y_negative:
        x = car.x

        # if the car can move both up and down, randomly pick one
        if move_y_positive and move_y_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        # keep moving the car up untill it is blocked
        if move_y_positive:
            while movable_up(game, car):
                y = car.y + 1
                update(game, car, x, y)

        # keep moving the car down untill it's blocked
        if move_y_negative:
            while movable_down(game, car):
                y = car.y - 1
                update(game, car, x, y)

    if move_x_negative or move_x_positive:
        y = car.y

        # if the car can move both left and right, randomly pick one
        if move_x_positive and move_x_negative:
            random_choice =  random.choice([0, 1])
            if random_choice == 1:
                move_x_positive = False
            else:
                move_x_negative = False

        # keep moving the car right untill it's it blocked
        if move_x_positive:
            while movable_right(game, car):
                x = car.x + 1
                update(game, car, x, y)

        # keep moving the car left untill it's it blocked
        if move_x_negative:
            while movable_left(game, car):
                x = car.x - 1
                update(game, car, x, y)

def queue_algorithm_hiele(game):
    """
        Ik schrijf mijn eigen versie om jouw algoritme te snappen en te debuggen
    """
    cars_in_path = []

    # look for cars in the exit path of the red car, only look to the right
    for x in range(game.redcar.x + game.redcar.length, game.gridsize + 1):
         spot = game.grid[x][game.gridexit]
         if spot != 0:
             for car in game.cars:
                 if car.id == spot:
                     cars_in_path.append(car)
                     break


    # check if cars are able to move
    # when they are able to move, check if they can be moved off the path
    for car in cars_in_path:

        # all cars on the path are vertical orientated
        move_y_positive = movable_up(game, car)
        move_y_negative = movable_down(game, car)

        # if the car is able to move up or down and completely of the path:
        move_up = False
        move_down = False

        # check how far the car can go up
        if move_y_positive:
            new_y_up = car.y

            # keep checking the spot above the previous spot to see if it's 0
            # do this untill hitting a car or the upper edge
            while new_y_up + car.length < 6:
                if game.grid[car.x][new_y_up + car.length] == 0:
                    new_y_up += 1
                else:
                    break

            # check if the new position is completely off the path
            if new_y_up > game.gridexit:
                move_up = True
            else:
                move_up = False

        # check how far the car can go down
        if move_y_negative:
            new_y_down = car.y

            # keep checking the spot below the previous spot to see if it's 0
            # do this untill hitting a car or the lower edge
            while new_y_down > 0:
                if game.grid[car.x][new_y_down - 1] == 0:
                    new_y_down -= 1
                else:
                    break

            # check if the new position is completely off the path
            if new_y_down + car.length - 1 < game.gridexit:
                move_down = True
            else:
                move_down = False

        if move_down and move_up:
            random_choice = random.choice([0, 1])
            if random_choice == 1:
                move_down = False
            else:
                move_up = False

        if move_down:
            update(game, car, car.x, new_y_down)
            return True

        elif move_up:
            update(game, car, car.x, new_y_up)
            return True

    # When no path freeing move was able to be made, make a rnao
    random_move_max_steps_non_recurrent(game)
    # TODO: dont use random_move. Pick a random car that won't go
    # back to the path
    return False

def make_path_free(game):
    """
        This algorithm checks the path can be freed
    """
    cars_in_path = []

    # look for cars in the exit path of the red car, only look to the right
    for x in range(game.redcar.x + game.redcar.length, game.gridsize + 1):
         spot = game.grid[x][game.gridexit]
         if spot != 0:
             for car in game.cars:
                 if car.id == spot:
                     cars_in_path.append(car)
                     break

    # check if cars are able to completely move off the path
    cars_movable = []
    for car in cars_in_path:

        # all cars on the path are vertical orientated
        move_y_positive = movable_up(game, car)
        move_y_negative = movable_down(game, car)

        # if the car is able to move up or down and completely of the path:
        move_up = False
        move_down = False

        # check how far the car can go up
        if move_y_positive:
            new_y_up = car.y

            # keep checking the spot above the previous spot to see if it's 0
            # do this untill hitting a car or the upper edge
            while new_y_up + car.length < 6:
                if game.grid[car.x][new_y_up + car.length] == 0:
                    new_y_up += 1
                else:
                    break

            # check if the new position is completely off the path
            if new_y_up > game.gridexit:
                move_up = True
            else:
                move_up = False

        # check how far the car can go down
        if move_y_negative:
            new_y_down = car.y

            # keep checking the spot below the previous spot to see if it's 0
            # do this untill hitting a car or the lower edge
            while new_y_down > 0:
                if game.grid[car.x][new_y_down - 1] == 0:
                    new_y_down -= 1
                else:
                    break

            # check if the new position is completely off the path
            if new_y_down + car.length - 1 < game.gridexit:
                move_down = True
            else:
                move_down = False

        if move_down and move_up:
            random_choice = random.choice([0, 1])
            if random_choice == 1:
                move_down = False
            else:
                move_up = False

        if move_down:
            cars_movable.append([car, new_y_down])

        elif move_up:
            cars_movable.append([car, new_y_up])

    # check if the path will be completely free when all the movable cars are moved
    if len(cars_in_path) == len(cars_movable):

        # move all movable cars
        for [car, new_y] in cars_movable:
            update(game, car, car.x, new_y)

        # move red car to exit
        x = game.gridsize - 1
        y = game.gridexit
        update(game, game.redcar, x, y)
        return True
    return False

def queue_algorithm(game):
    """
        Checks which cars are in the way of the red car and moves these cars first.
    """
    car_queue = []
    queue_count = 0
    for i in range(game.gridsize):
        spot = game.grid[i][game.gridexit]
        if (spot is not 0) and (spot is not 'X'):
            for car in game.cars:
                if car.id == spot:
                    car_queue.append(car)
                    queue_count += 1

    if queue_count > 0:

        print(car_queue)
        # choose a random car in the queue
        car =  random.choice(car_queue)
        if car.id == game.previous_car_id:
            random_move_max_steps_non_recurrent(game)

        # check if car can move up
        move_y_positive = movable_up(game, car)

        # check if car can move down
        move_y_negative = movable_down(game, car)

        x = car.x

        # if the car can move both up and down, randomly pick one
        if move_y_positive and move_y_negative:
            random_choice = random.choice([0, 1])
            if random_choice == 1:
                move_y_positive = False
            else:
                move_y_negative = False

        # keep moving the car up untill it is blocked
        if move_y_positive:
            while movable_up(game, car):
                y = car.y + 1
                update(game, car, x, y)
                return True

        # keep moving the car down untill it's blocked
        if move_y_negative:
            while movable_down(game, car):
                y = car.y - 1
                update(game, car, x, y)
                return True

    random_move_max_steps_non_recurrent(game)
    return False

def breadth_first(game):
    """
        This function moves a random car as far as it can go.
    """
    queue = []

    for car in game.cars:

        # check if the car can move up or down
        if car.orientation == "V":
            if movable_up(game, car):
                
            move_y_negative = movable_down(game, car)

        # else car can only move left or right
        else:
            move_x_positive = movable_right(game, car)
            move_x_negative = movable_left(game, car)

        if move_y_positive










def score(game):
    """
        This function calculates the score of a
        current grid.
    """
    score = 0

    # a score is when a car moves of the win_path

    # a score point is when a vertical car is moved to the side of the grid
    # it is allowed to be. The other side is impossible

    pass
