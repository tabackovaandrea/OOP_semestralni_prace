
from robots import Robot, FastRobot, HeavyRobot

# Definition of the Tile class
class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x   # pozice sloupcová
        self.y = y   # pozice řádková
        self.tile_type = tile_type
        self.robot = None

# Definition of the Warehouse and Robot classes
class Warehouse:
    def __init__(self, columns, rows, robots):
        self.columns = columns
        self.rows = rows
        self.robots = robots
        self.tiles = []

        for y in range(rows):
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

    def move_robots(self, directions):
        for robot in self.robots:
            # Aquire the new position of the robot for collision detection and boundary checking
            new_x, new_y = robot.move(directions[robot][0], directions[robot][1]) # Accesses the first and second element of the direction list respectively for the specific robot thus two brackets (directions -> robot -> [0] or [1] element)
            
            # Check for potential collisions with warehouse boundaries before moving
            if new_x < 0 or new_x >= self.columns:
                directions[robot][0] = -directions[robot][0]
            if new_y < 0 or new_y >= self.rows:
                directions[robot][1] = -directions[robot][1]
            new_x, new_y = robot.move(directions[robot][0], directions[robot][1])

            # Check for potential collisions with shelves and other robots before moving
            collision = self.check_collisions(new_x, new_y, robot)  # Returns collision status (T/F) and coordinates of the collision
            
            # If no collision detected, update robot's position
            if not collision[0]:
                self.tiles[robot.position_y][robot.position_x].robot = None  # Remove robot from its current tile  
                robot.position_x = new_x
                robot.position_y = new_y
                self.tiles[robot.position_y][robot.position_x].robot = robot  # Place robot in its new tile

            else:
                # If collision detected, reverse the direction of movement for the robot
                directions[robot][0] = -directions[robot][0]
                directions[robot][1] = -directions[robot][1]
                print(f"Robot {robot.name} collided with shelf or another robot at ({collision[1]}, {collision[2]}) and reversed direction.")
                new_x, new_y = robot.move(directions[robot][0], directions[robot][1]) # New potential position after reversing direction
                # Check for potential collisions again after reversing direction
                collision = self.check_collisions(new_x, new_y, robot)
                if not collision[0]:  # If no collision detected after reversing direction, update robot 
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