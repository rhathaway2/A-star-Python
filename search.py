import sys
import math

'''
Ryan Hathaway
A* search - Python
Jun 11, 2020
'''

'''
Class representing search space for A* algorithm
n by m grid containing char that represent different
terrain each with a specific cost to travel over
'''
class Grid:
    
    valid_terrain = [".", "*", "o", "~", "x" ]
    terrain_costs = {
        "." : 1,
        "*" : 3,
        "o" : 5,
        "~" : 7,
        "x" : math.inf
    }

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = [[0] * width for _ in range(height)]
        self.gscore = [[math.inf] * width for _ in range(height)]
        self.fscore = [[math.inf] * width for _ in range(height)]

    def __repr__(self):
        return "Grid({}, {})".format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    def read_in_grid(self):
        try:
            for i in range(self._height):
                row = input().strip()
                for j, char in enumerate(row):
                    if char in Grid.valid_terrain:
                        self._grid[i][j] = char
                    else:
                        raise Exception("Invalid terrain entered")
        except Exception as e:
            print("Exception Occurred: {}".format(e))
            return None

    def print(self):
        for i in range(self._height):
            for j in range(self._width):
                print(self._grid[i][j], end='')
            print()

    def get_adjacent_coordinates(self, x_coord, y_coord):
        return [(xcoord-1, y_coord),
                (xcoord+1, y_coord),
                (x_coord, y_coord-1),
                (x_coord, y_coord+1),
            ]
    
    def within_bounds(self, x_coord, y_coord):
        return (x_coord >= 0 and y_coord >= 0 and x_coord < self._width and y_coord < self._height)

    def get_cost(self, x, y):
        if within_bounds(x,y):
            terrain = self._grid[y][x]
            return Grid.terrain_costs[terrain]
        else:
            return -1

'''
Search heuristic: Manhattan distance
'''
def manhattan_distance_heauristic():
    pass

'''
A star search algorithm
'''
def search(search_space, start=(0,0)):
    already_visited_positions = {}
    positions_to_visit = {start,}
    
    came_from = {}

    start_x, start_y = start
    search_space.gscore[start_x][start_y] = 0
    
    


def Usage():
    print("USAGE: python search.py GRID_WIDTH(int) GRID_HEIGHT(int)")

grid_width = 0
grid_height = 0
#handle command line arguments
try:
    if len(sys.argv) != 3:
        raise Exception("Invalid number of command line arguments")
    try:
        grid_width = int(sys.argv[1])
    except:
        raise Exception("GRID_WIDTH must be an integer")
    try:
        grid_height = int(sys.argv[2])
    except:
        raise Exception("GRID_HEIGHT must be an integer")

except Exception as e:
    print("Exception Occurred: {}".format(e))
    Usage()


search_grid = Grid(grid_width, grid_height)
search_grid.read_in_grid()

search(search_grid)

