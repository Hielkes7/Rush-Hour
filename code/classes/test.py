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
