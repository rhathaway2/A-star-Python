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

    @property
    def goal_pos(self):
        #goal is the bottom right hand corner of grid
        return (self._width-1, self._height-1)

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
        return [(x_coord-1, y_coord),
                (x_coord+1, y_coord),
                (x_coord, y_coord-1),
                (x_coord, y_coord+1),
            ]
    
    def within_bounds(self, x_coord, y_coord):
        return (x_coord >= 0 and y_coord >= 0 and x_coord < self._width and y_coord < self._height)

    def get_cost(self, x, y):
        if self.within_bounds(x,y):
            terrain = self._grid[y][x]
            return Grid.terrain_costs[terrain]
        else:
            return -1

'''
Search heuristic: Manhattan distance
'''
def manhattan_distance_heauristic(start_x, start_y, goal_x, goal_y):
    return abs(goal_x - start_x) + abs(goal_y - start_y)

'''
Get coordinates of lowest fscore from grid
only searches coordinates in open_set
'''
def get_lowest_fscore_pos(search_grid, open_set):
    sorted_set = sorted(open_set, key=lambda pos : search_grid.fscore[pos[0]][pos[1]])
    return sorted_set[0]

'''
Prints grid with path once found
'''
def print_path(search_grid, found_path):
    pass

'''
A star search algorithm
'''
def search(search_space, start=(0,0), goal=(0,0)):
    #set to hold positions
    already_visited_positions = []
    positions_to_visit = [start,]
    
    #dictionary containing where each node is reached from
    came_from = {}

    start_x, start_y = start
    #cost from going from start to start is 0
    search_space.gscore[start_x][start_y] = 0

    goal_x, goal_y = goal

    search_space.fscore[start_x][start_y] = manhattan_distance_heauristic(*start, *goal)

    while len(positions_to_visit) != 0:
        #get position with lowest fscore from positions_to_visit
        current = get_lowest_fscore_pos(search_space, positions_to_visit)
        if current == goal:
            print_path(search_space, came_from)
            return True
        
        positions_to_visit.remove(current)
        already_visited_positions.append(current)
        
        cur_x, cur_y = current
        for neighbor in search_space.get_adjacent_coordinates(cur_x, cur_y):
            if not search_space.within_bounds(*neighbor) or neighbor in already_visited_positions:
                pass
            else:
                score = search_space.gscore[cur_x][cur_y] + search_space.get_cost(*neighbor) 
                
                neighbor_x, neighbor_y = neighbor

                if not neighbor in positions_to_visit:
                    positions_to_visit.append(neighbor)
                elif score >= search_space.gscore[neighbor_x][neighbor_y]:
                    pass

                came_from[neighbor] = current
                search_space.gscore[neighbor_x][neighbor_y] = score
                search_space.fscore[neighbor_x][neighbor_y] = search_space.gscore[neighbor_x][neighbor_y] + manhattan_distance_heauristic(*neighbor, *goal)


    
    


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

goal_pos = search_grid.goal_pos
status = search(search_grid, start=(0,0), goal=goal_pos)

print(status)


