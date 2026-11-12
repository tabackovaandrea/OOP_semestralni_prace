
from robots import Robot, FastRobot, HeavyRobot

# Definition of the Tile class
class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x   # pozice sloupcová
        self.y = y   # pozice řádková
        self.tile_type = tile_type
        self.robot = None

# Definition of the Warehouse class
class Warehouse:
    def __init__(self, columns, rows, robots):
        self.columns = columns
        self.rows = rows
        self.robots = robots
        self.tiles = []

        for y in range(rows):  # This order of for cycles means that array will be accessed in [y][x] style where y is for rows and x is for columns (the order everywhere else is x,y - columns then rows)
            row = []
            for x in range(columns):
                row.append(Tile(x, y, "floor"))
            self.tiles.append(row)

        for robot in robots:                     # Assigns each robot to its corresponding tile in the warehouse based on its initial position
            self.tiles[robot.position_y][robot.position_x].robot = robot

    def add_shelf(self, x, y, length, width):    # Specify tile type as shelf at the given position with the given dimensions of the shelf
        for row in range(y, y + width):
            for column in range(x, x + length):
                self.tiles[row][column].tile_type = "shelf"

    def move_robots(self, destination):
        for robot in self.robots:
            robot.path = self.find_shortest_path((robot.position_x, robot.position_y), destination)
            if robot.path is None or len(robot.path) <=1:  # Cases where path does not exist or robot is already at destination - skips the following calculations
                continue
            next_position = robot.path[1]
            direction_x = next_position[0]-robot.position_x
            direction_y = next_position[1]-robot.position_y
            
            # Aquire the new position of the robot for collision detection and boundary checking
            new_x, new_y = robot.move(direction_x, direction_y) # Accesses the first and second element of the direction list respectively for the specific robot thus two brackets (directions -> robot -> [0] or [1] element)

            # Check for potential collisions with shelves and other robots before moving
            collision = self.check_collisions(new_x, new_y, robot)  # Returns collision status (T/F) and coordinates of the collision
            
            # If no collision detected, update robot's position
            if not collision[0]:
                self.tiles[robot.position_y][robot.position_x].robot = None  # Remove robot from its current tile  
                robot.position_x = new_x
                robot.position_y = new_y
                self.tiles[robot.position_y][robot.position_x].robot = robot  # Place robot in its new tile

    def check_collisions(self, new_x, new_y, robot):
        if self.tiles[new_y][new_x].tile_type == "shelf":
            return(True, new_x, new_y)  # Collision detected with a shelf tile, returns position of collision
        if self.tiles[new_y][new_x].robot is not None and self.tiles[new_y][new_x].robot is not robot:    # Tile is occupied by a robot AND the robot in that tile is not the same as the one trying to move there
            return(True, new_x, new_y)  # Collision detected with another robot, returns position of collision
        return(False, None, None)   # No collision detected

    # Method for finding the shortest path from current robot's position to it's destination (basically Breadth-First Search = prohledávání do šířky)
    def find_shortest_path(self, start, destination):
        queue = [start]
        possible_directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # left, right, down, up
        already_visited = [start]  # Needs new list for checking the position because elements are taken out of queue (cannot be checked with queue)
        remembered_path = {start: None}   # Dictionary for storing the previous position for each visited position -> final path

        while queue:
            current = queue.pop(0)      # Takes first position from queue
            if current == destination:
                path = []
                position = destination
                path.append(position)   # Path starts at destination and works its way back to start

                while position != start:
                    position = remembered_path[position]
                    path.append(position)

                path.reverse()  # Reorders the path from start to destination 
                return path
            
            x, y = current                  # Extract x and y coordinates from the current position (it's a tuple)
            for dx, dy in possible_directions:
                neighbor = (x + dx, y + dy)
                # Check if new position is inside warehouse and is not shelf then check if new position was not already visited
                if 0 <= neighbor[0] < self.columns and 0 <= neighbor[1] < self.rows and self.tiles[neighbor[1]][neighbor[0]].tile_type == "floor":
                    if neighbor not in already_visited:
                        queue.append(neighbor)
                        already_visited.append(neighbor)
                        remembered_path[neighbor] = current

        return None  # Returns None if the destination is not reachable