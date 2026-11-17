# Definition of robot classes

class Robot:
    def __init__(self, name, position_x, position_y):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.path = []
        self.current_order = None
        self.status = "available"

    # # Calculate the robot's new position based on the specified direction
    # Direction values should be -1, 0, or 1 to indicate movement along the x and y axes
    def move(self, direction_x, direction_y):
        new_x = self.position_x + direction_x
        new_y = self.position_y + direction_y
        return new_x, new_y

# Class robot has two subclasses: FastRobot and HeavyRobot with different speeds
class FastRobot(Robot):
    def __init__(self, name, position_x, position_y):
        super().__init__(name, position_x, position_y)
        self.move_interval = 1  # Number of simulation steps after which the robot can move again (moves once every step)
        self.min_load = 0
        self.max_load = 10
        self.battery = 100

    def charge_battery(self):
        self.battery += 5
        print("Robot ", self.name, "is charging.")

class HeavyRobot(Robot):
    def __init__(self, name, position_x, position_y):
        super().__init__(name, position_x, position_y)
        self.move_interval = 3    # Number of simulation steps after which the robot can move again (moves once every three steps)
        self.min_load = 10
        self.max_load = 20
        self.battery = 100

    def charge_battery(self):
        self.battery += 2
        print("Robot ", self.name, "is charging.")