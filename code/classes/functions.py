

def string(grid):
    """
        Takes a grid (which is a list of lists) and changes it into a string.
    """

    # adds all components of the lists to an empty string
    grid_string = "".join(["".join([str(character) for character in elem]) for elem in grid])

    # returns the new string
    return grid_string
