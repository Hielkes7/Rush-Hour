import random, time
import game_functions

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
    game_functions.update(game, redcar, x, y)
    return True

def random_single_step(game):

    # keep looping untill a randomly picked car is able to move
    car_movable = False
    while not car_movable:
        # pick random car
        car = random.choice(game.cars)
        car_movable = game_functions.car_is_movable(game, car)

    direction = move(game, car)
    if direction == "y positive":
        x = car.x
        y = car.y + 1
        game_functions.update(game, car, x, y)

    elif direction == "y negative":
        x = car.x
        y = car.y - 1
        game_functions.update(game, car, x, y)

    elif direction == "x positive":
        y = car.y
        x = car.x + 1
        game_functions.update(game, car, x, y)

    elif direction == "x negative":
        y = car.y
        x = car.x - 1
        game_functions.update(game, car, x, y)

def random_max_step(game):
    """
        This function moves a random car as far as it can go.
    """

    # keep looping untill a randomly picked car is able to move
    car_movable = False
    while not car_movable:

        # pick random car
        car = random.choice(game.cars)
        car_movable = game_functions.car_is_movable(game, car)


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
        game_functions.update(game, car, car.x, new_y)
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
        game_functions.update(game, car, car.x, new_y)
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
        game_functions.update(game, car, new_x, car.y)
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
        game_functions.update(game, car, new_x, car.y)
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
        car_movable = game_functions.car_is_movable(game, car)

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
        game_functions.update(game, car, car.x, new_y)

    elif direction == "y negative":
        new_y = car.y

        # check for border
        while new_y > 0:

            # check if car can move down
            if game.grid[car.x][new_y -1] == 0:
                new_y -= 1
            else:
                break
        game_functions.update(game, car, car.x, new_y)

    elif direction == "x positive":
        new_x = car.x

        # check for border
        while new_x + car.length < game.gridsize + 1:

            # check if car can move right
            if game.grid[new_x + car.length][car.y] == 0:
                new_x += 1
            else:
                break
        game_functions.update(game, car, new_x, car.y)

    elif direction == "x negative":
        new_x = car.x

        # check for border
        while new_x > 0:

            # check if car can move left
            if game.grid[new_x - 1][car.y] == 0:
                new_x -= 1
            else:
                break
        game_functions.update(game, car, new_x, car.y)

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
        move_y_positive = game_functions.movable_up(game, car)
        move_y_negative = game_functions.movable_down(game, car)

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
            game_functions.update(game, car, car.x, new_y)

        # move red car to exit
        x = game.gridsize - 1
        y = game.gridexit
        game_functions.update(game, game.redcar, x, y)
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
            game_functions.update(game, car, car.x, new_y)
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
            game_functions.update(game, car, car.x, new_y)
            game.previous_car_id = car.id
            return True

    random_max_step_non_recurring(game)
    return False
