
from warehouse import Warehouse, Tile
from robots import Robot, FastRobot, HeavyRobot       

# Definition of robots, shelves and warehouse
robot1 = FastRobot("R1", 6, 14)
robot2 = HeavyRobot("R2", 6, 12)
robots = [robot1, robot2]

warehouse = Warehouse(10, 15, robots)

warehouse.add_shelf(0, 0, 10, 1) # Add a shelf at position (0, 0) with length 10 and width 1
warehouse.add_shelf(0, 1, 1, 12) # Add a shelf at position (0, 1) with length 1 and width 12
warehouse.add_shelf(9, 1, 1, 12) # Add a shelf at position (9, 1) with length 1 and width 12
warehouse.add_shelf(1, 4, 3, 1) # Add a shelf at position (1, 4) with length 3 and width 1
warehouse.add_shelf(7, 4, 2, 1) # Add a shelf at position (7, 4) with length 2 and width 1
warehouse.add_shelf(1, 8, 3, 1) # Add a shelf at position (1, 8) with length 3 and width 1
warehouse.add_shelf(7, 8, 2, 1) # Add a shelf at position (7, 8) with length 2 and width 1
warehouse.add_shelf(1, 12, 3, 1) # Add a shelf at position (1, 12) with length 3 and width 1
warehouse.add_shelf(7, 12, 2, 1) # Add a shelf at position (7, 12) with length 2 and width 1

dt = 1  # Time step for movement

directions = {robot1: [-1, 0], 
              robot2: [0, 1]}

print(f"Initial positions: {[(robot.name, robot.position_x, robot.position_y) for robot in warehouse.robots]}")
for time in range(20):
    warehouse.move_robots(directions)
    print(f"Time: {time}, Positions: {[(robot.name, robot.position_x, robot.position_y) for robot in warehouse.robots]}")
#print(f"Positions after moving: {[(robot.name, robot.position_x, robot.position_y) for robot in warehouse.robots]}")