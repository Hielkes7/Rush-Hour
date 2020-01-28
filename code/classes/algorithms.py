import random, time

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

def random_single_step(game):

    # keep looping untill a randomly picked car is able to move
    car_movable = False
    while not car_movable:
        # pick random car
        car = random.choice(game.cars)
        car_movable = car_is_movable(game, car)

    direction = move(game, car)
    if direction == "y positive":
        x = car.x
        y = car.y + 1
        update(game, car, x, y)

    elif direction == "y negative":
        x = car.x
        y = car.y - 1
        update(game, car, x, y)

    elif direction == "x positive":
        y = car.y
        x = car.x + 1
        update(game, car, x, y)

    elif direction == "x negative":
        y = car.y
        x = car.x - 1
        update(game, car, x, y)

def random_max_step(game):
    """
        This function moves a random car as far as it can go.
    """

    # keep looping untill a randomly picked car is able to move
    car_movable = False
    while not car_movable:

        # pick random car
        car = random.choice(game.cars)
        car_movable = car_is_movable(game, car)


    direction = move(game, car)
    if direction == "y positive":
        new_y = car.y

        # check for border
        while new_y + car.length < game.gridsize + 1:

            # check if car can move up
            if game.grid[car.x][new_y + car.length] == 0:
                new_y += 1
            else:
                break
        update(game, car, car.x, new_y)
        return car, car.x, new_y

    elif direction == "y negative":
        new_y = car.y

        # check for border
        while new_y > 0:

            # check if car can move down
            if game.grid[car.x][new_y -1] == 0:
                new_y -= 1
            else:
                break
        update(game, car, car.x, new_y)
        return car, car.x, new_y

    elif direction == "x positive":
        new_x = car.x

        # check for border
        while new_x + car.length < game.gridsize + 1:

            # check if car can move right
            if game.grid[new_x + car.length][car.y] == 0:
                new_x += 1
            else:
                break
        update(game, car, new_x, car.y)
        return car, new_x, car.y


    else:
        new_x = car.x

        # check for border
        while new_x > 0:

            # check if car can move left
            if game.grid[new_x - 1][car.y] == 0:
                new_x -= 1
            else:
                break
        update(game, car, new_x, car.y)
        return car, new_x, car.y

def random_max_step_non_recurring(game):
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
        car_movable = car_is_movable(game, car)

    direction = move(game, car)
    if direction == "y positive":
        new_y = car.y

        # check for border
        while new_y + car.length < game.gridsize + 1:

            # check if car can move up
            if game.grid[car.x][new_y + car.length] == 0:
                new_y += 1

            else:
                break
        update(game, car, car.x, new_y)

    elif direction == "y negative":
        new_y = car.y

        # check for border
        while new_y > 0:

            # check if car can move down
            if game.grid[car.x][new_y -1] == 0:
                new_y -= 1
            else:
                break
        update(game, car, car.x, new_y)

    elif direction == "x positive":
        new_x = car.x

        # check for border
        while new_x + car.length < game.gridsize + 1:

            # check if car can move right
            if game.grid[new_x + car.length][car.y] == 0:
                new_x += 1
            else:
                break
        update(game, car, new_x, car.y)

    elif direction == "x negative":
        new_x = car.x

        # check for border
        while new_x > 0:

            # check if car can move left
            if game.grid[new_x - 1][car.y] == 0:
                new_x -= 1
            else:
                break
        update(game, car, new_x, car.y)

    game.previous_car_id = car.id
    return [car, car.x, car.y]

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

        # if both up and down are possible, randomly choose one
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

        # move all cars off the path
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
    cars_in_path = []

    # look for cars in the exit path of the red car, only look to the right
    for x in range(game.redcar.x + game.redcar.length, game.gridsize + 1):
         spot = game.grid[x][game.gridexit]
         if spot != 0:
             for car in game.cars:
                 if car.id == spot:
                     cars_in_path.append(car)
                     break

    if len(cars_in_path) > 0:

        # choose a random car in the queue
        car = random.choice(cars_in_path)
        if car.id == game.previous_car_id:
            random_max_step_non_recurring(game)
            return False

        x = car.x
        direction = move(game, car)
        if direction == "y positive":
            new_y = car.y

            # check for border
            while new_y + car.length < game.gridsize + 1:

                # check if car can move up
                if game.grid[car.x][new_y + car.length] == 0:
                    new_y += 1
                else:
                    break
            update(game, car, car.x, new_y)
            game.previous_car_id = car.id
            return True

        elif direction == "y negative":
            new_y = car.y

            # check for border
            while new_y > 0:

                # check if car can move down
                if game.grid[car.x][new_y -1] == 0:
                    new_y -= 1
                else:
                    break
            update(game, car, car.x, new_y)
            game.previous_car_id = car.id
            return True

    random_max_step_non_recurring(game)
    return False

def move(game, car):

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
