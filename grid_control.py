#functions that deal with the info inside the grid

#grid is a dictionary of tuple : colour (which is also a tuple)
def init_grid() -> dict:
    ret_dict = {}
    blockSize = 25 #Set the size of the grid block
    for x in range(100, 800, blockSize):
        for y in range(100, 650, blockSize):
            #store colour at the coordinates of the grid
            ret_dict[(x,y)] = None

    return ret_dict
