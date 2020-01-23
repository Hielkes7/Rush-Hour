import csv, os, random, statistics, xlsxwriter, algorithms, time
import matplotlib.pyplot as plt

class Game():
    """
        Creates a game.
    """

    def __init__(self, csvfile, gridsize):

        # variable for non recurrent algorithm, start with dummy value
        self.previous_car_id = None

        # gridsize and grid creation
        self.gridsize = gridsize - 1
        self.gridexit = int((gridsize / 2) + 1) - 1
        self.grid = []
        self.moves = 0
        for i in range(gridsize):
            gridrow = []
            for j in range(gridsize):
                gridrow.append(0)
            self.grid.append(gridrow)

        # open and read the start file
        file = open(csvfile)
        reader = csv.reader(file, delimiter=',')

        # empty list for the cars used in the game
        self.cars = []

        # creates car objects and adds to list
        for car, orientation, coordinates, length in reader:
            self.coordinates = coordinates.split(",")
            x = self.coordinates[0]
            y = self.coordinates[1]
            newcar = Car(car, orientation, x, y, length)
            self.cars.append(newcar)
            if car == 'X':
                self.redcar = newcar

        # fills grid with car id's
        for car in self.cars:
            x = car.x
            y = car.y
            if car.orientation == "V":
                for i in range(car.length):
                    self.grid[x][y] = car.id
                    y += 1
            else:
                for i in range(car.length):
                    self.grid[x][y] = car.id
                    x += 1

    def __str__(self):
        """
            Returns the grid of the game.
        """

        return self.grid

    def save_plot(self, file_name):

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

        ax = plt.axes()
        for x in range(self.gridsize + 1):
            for y in range(self.gridsize + 1):
                if self.grid[x][y] != 0:
                    block = plt.Rectangle((x, y), 1, 1, fc=colors[self.grid[x][y]])
                    ax.add_patch(block)

        plt.axis('scaled')
        plt.xlim(0, self.gridsize + 1)
        plt.ylim(0, self.gridsize + 1)
        plt.grid()
        plt.savefig("frames/" + file_name)
        plt.cla()
        plt.clf()

    def save_plot_extern_grid(self, file_name, grid):

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
        plt.savefig("frames/" + file_name)
        plt.cla()
        plt.clf()

    def frame(self, ax):
        """
        This function returns a live plot of the given grid
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

        for x in range(self.gridsize + 1):
            for y in range(self.gridsize + 1):
                if self.grid[x][y] != 0:
                    block = plt.Rectangle((x, y), 1, 1, fc=colors[self.grid[x][y]])
                    ax.add_patch(block)

        plt.xlim(0, self.gridsize + 1)
        plt.ylim(0, self.gridsize + 1)
        plt.grid()
        plt.draw()
        plt.pause(0.3)
        plt.cla()

    def print_grid_terminal(self):
        """
            This function prints the grid in the terminal
        """
        for y in range(self.gridsize + 1):
            for x in range(self.gridsize + 1):
                print(self.grid[y][x], " ", end="")
            print()





class Car():
    """
        Creates a car object that is used for a game.
    """
    def __init__(self, car, orientation, x, y, length):
        self.id = car
        self.orientation = orientation
        self.x = int(x) - 1
        self.y = int(y) - 1
        self.length = int(length)

    def __str__(self):
        """
            Returns the id of a car.
        """
        return self.id


class Test():
    """
        This function solves the game and then returns in how many moves it
        has done so.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_test.csv"
        game = Game(csvfile, gridsize)
        algorithms.breadth_first(game)


class Play():
    """
        This function solves the game and then returns in how many moves it
        has done so.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_2.csv"
        game = Game(csvfile, gridsize)
        gamewon = False
        while not gamewon:
            if algorithms.check_path_free(game):
                gamewon = True
                break
            algorithms.queue_algorithm_merge(game)

        print(f"Done! It took {game.moves} moves to win the game")

class Play_average():
    """
        This function solves the game and then returns in how many moves it
        has done so.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_2.csv"

        moves = []
        amount_of_games = 100
        for i in range(amount_of_games):
            game = Game(csvfile, gridsize)
            gamewon = False
            while not gamewon:
                if algorithms.check_path_free(game):
                    gamewon = True
                    break
                algorithms.queue_algorithm_merge(game)
            moves.append(game.moves)

        average = sum(moves)/amount_of_games
        print(f"Done! It took an average of ", average, " moves to win the game")

class PlayData1():
    """
        This function runs the game 200 times and then saves the data to a excel file.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_1.csv"
        repeats = 5000
        export_excel = True
        movelist = []

        for i in range(repeats):
            game = Game(csvfile, gridsize)
            moves = 0
            gamewon = False

            while not gamewon:
                if algorithms.check_path_free(game):
                    gamewon = True
                    break
                algorithms.random_move_max_steps(game)

            # give update on how many measurements have been calculate
            movelist.append(game.moves)
            if i % (repeats/100) == 0:
                print(i*100/repeats,"%,  ", game.moves, " moves")


        if export_excel:

            #create excel file
            workbook = xlsxwriter.Workbook("data/game1/output1.xlsx")
            sheet = workbook.add_worksheet()

            #declare data
            for item in range(len(movelist)):
                sheet.write(item, 0, movelist[item])

            workbook.close()
class PlayData2():
    """
        This function runs the game 200 times and then saves the data to a excel file.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_1.csv"
        repeats = 5000
        export_excel = True
        movelist = []

        for i in range(repeats):
            game = Game(csvfile, gridsize)
            moves = 0
            gamewon = False

            while not gamewon:
                if algorithms.check_path_free(game):
                    gamewon = True
                    break
                algorithms.random_move_max_steps_non_recurrent(game)

            # give update on how many measurements have been calculate
            movelist.append(game.moves)
            if i % (repeats/100) == 0:
                print(i*100/repeats,"%,  ", game.moves, " moves")


        if export_excel:

            #create excel file
            workbook = xlsxwriter.Workbook("data/game1/output2.xlsx")
            sheet = workbook.add_worksheet()

            #declare data
            for item in range(len(movelist)):
                sheet.write(item, 0, movelist[item])

            workbook.close()
class PlayData3():
    """
        This function runs the game 200 times and then saves the data to a excel file.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_1.csv"
        repeats = 5000
        export_excel = True
        movelist = []

        for i in range(repeats):
            game = Game(csvfile, gridsize)
            moves = 0
            gamewon = False

            while not gamewon:
                if algorithms.make_path_free(game):
                    gamewon = True
                    break
                algorithms.random_move_max_steps_non_recurrent(game)

            # give update on how many measurements have been calculate
            movelist.append(game.moves)
            if i % (repeats/100) == 0:
                print(i*100/repeats,"%,  ", game.moves, " moves")


        if export_excel:

            #create excel file
            workbook = xlsxwriter.Workbook("data/game1/output3.xlsx")
            sheet = workbook.add_worksheet()

            #declare data
            for item in range(len(movelist)):
                sheet.write(item, 0, movelist[item])

            workbook.close()
class PlayData4():
    """
        This function runs the game 200 times and then saves the data to a excel file.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_1.csv"
        repeats = 5000
        export_excel = True
        movelist = []

        for i in range(repeats):
            game = Game(csvfile, gridsize)
            moves = 0
            gamewon = False

            while not gamewon:
                if algorithms.make_path_free(game):
                    gamewon = True
                    break
                algorithms.queue_algorithm(game)

            # give update on how many measurements have been calculate
            movelist.append(game.moves)
            if i % (repeats/100) == 0:
                print(i*100/repeats,"%,  ", game.moves, " moves")


        if export_excel:

            #create excel file
            workbook = xlsxwriter.Workbook("data/game1/output4.xlsx")
            sheet = workbook.add_worksheet()

            #declare data
            for item in range(len(movelist)):
                sheet.write(item, 0, movelist[item])

            workbook.close()
class PlayData5():
    """
        This function runs the game 200 times and then saves the data to a excel file.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_1.csv"
        repeats = 5000
        export_excel = True
        movelist = []

        for i in range(repeats):
            game = Game(csvfile, gridsize)
            moves = 0
            gamewon = False

            while not gamewon:
                if algorithms.check_path_free(game):
                    gamewon = True
                    break
                algorithms.random_move_single_step(game)

            # give update on how many measurements have been calculate
            movelist.append(game.moves)
            if i % (repeats/100) == 0:
                print(i*100/repeats,"%,  ", game.moves, " moves")


        if export_excel:

            #create excel file
            workbook = xlsxwriter.Workbook("data/game1/output5.xlsx")
            sheet = workbook.add_worksheet()

            #declare data
            for item in range(len(movelist)):
                sheet.write(item, 0, movelist[item])

            workbook.close()
class PlayData6():
    """
        This function runs the game 200 times and then saves the data to a excel file.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_1.csv"
        repeats = 5000
        export_excel = True
        movelist = []

        for i in range(repeats):
            game = Game(csvfile, gridsize)
            moves = 0
            gamewon = False

            while not gamewon:
                if algorithms.win(game):
                    gamewon = True
                    break
                algorithms.random_move_single_step(game)

            # give update on how many measurements have been calculate
            movelist.append(game.moves)
            if i % (repeats/100) == 0:
                print(i*100/repeats,"%,  ", game.moves, " moves")


        if export_excel:

            #create excel file
            workbook = xlsxwriter.Workbook("data/game1/output6.xlsx")
            sheet = workbook.add_worksheet()

            #declare data
            for item in range(len(movelist)):
                sheet.write(item, 0, movelist[item])

            workbook.close()





class Save_frames():
    """
        Solves the game and saves each frame of each move made. This function
        crashes very quickly when to many frames are saved.
    """
    def __init__(self):

        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboards/Rushhour6x6_2.csv"
        game = Game(csvfile, gridsize)
        gamewon = False

        # save plot initial grid setup
        plt.figure()
        game.save_plot("frame0.png")
        while not gamewon:
            algorithms.queue_algorithm_hiele(game)
            file_name = "frame" + str(game.moves) + ".png"
            game.save_plot(file_name)
            algorithms.make_path_free(game)
            algorithms.check_path_free(game)
            gamewon = algorithms.win(game)


        # save final frame
        file_name = "frame" + str(game.moves) + ".png"
        game.save_plot(file_name)

        print(f"Done! It took {game.moves} moves to win the game")


class Save_frames_buffer():
    """
        Solves the game and saves each frame of each move made. This function
        crashes very quickly when to many frames are saved.
    """
    def __init__(self):

        def extract_grid(grid):
            grid_size = len(grid)

            # create grid_copy with all 0's
            grid_copy = []
            for i in range(grid_size):
                row = []
                for j in range(grid_size):
                    row.append(0)
                grid_copy.append(row)

            # copy given grid into grid_copy
            for x in range(grid_size):
                for y in range(grid_size):
                    grid_copy[x][y] = grid[x][y]

            return grid_copy


        print("Hi! Let's play Rush-Hour!")
        gridsize = 6
        csvfile = "gameboard/Rushhour6x6_3.csv"
        save_frames = True

        max_moves = 400

        # dummy begin value
        moves = max_moves + 1

        game = Game(csvfile, gridsize)
        gamewon = False
        list_grids = []
        list_grids.append(extract_grid(game.grid))

        while not gamewon:
            if game.moves > max_moves:
                game = Game(csvfile, gridsize)
                gamewon = False
                list_grids = []
                list_grids.append(extract_grid(game.grid))
            algorithms.random_move_max_steps_non_recurrent(game)
            list_grids.append(extract_grid(game.grid))
            algorithms.check_path_free(game)
            gamewon = algorithms.win(game)
            moves = game.moves

        # save final grid
        list_grids.append(game.grid)
        print(f"Done! It took {game.moves} moves to win the game")

        # save all frames
        if save_frames:
            for i in range(len(list_grids)):
                file_name = "frame" + str(i) + ".png"
                game.save_plot_extern_grid(file_name, list_grids[i])
        game.save_plot_extern_grid("final_frame.png", list_grids[-1])


class Animation():
    """
        Solves the game and produces a live animation of each move.
    """
    def __init__(self):

        gridsize = 6
        csvfile = "gameboard/Rushhour6x6_1.csv"
        game = Game(csvfile, gridsize)

        # plot of the first move
        plt.figure()
        ax = plt.axes()
        game.frame(ax)
        while not game.win_hiele():
            game.random_move_max_steps()
            game.frame(ax)

        # save final frame
        game.frame(ax)



if __name__ == "__main__":
    # Play_average()
    # Test()
    # PlayData_nacht1()
    # PlayData_nacht2()
    # PlayData_nacht3()
    PlayData1()
    PlayData2()
    PlayData3()
    PlayData4()
    PlayData5()
    PlayData6()
    # Save_frames_buffer()
    # Save_frames()
