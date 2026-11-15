
import random

# Definition of order class

class Order:
    def __init__(self, order_id, location, weight):
        self.id = order_id
        self.location = location
        self.weight = weight
        self.status = "waiting"
        self.robot = None

# Generation of orders
def generate_order(order_id, storage_locations):
    order_position = random.choice(list(storage_locations.keys())) # Storage_locations is transformed into list for easier work
    order_weight = random.randint(1, 20)  # Generates random integer from 1 to 20
    order = Order(order_id, order_position, order_weight)
    return order

# Assigning orders to robots
def assign_order(robot, orders):
    if robot.current_order is None:
        for order in orders:
            if order.status == "waiting" and (robot.min_load < order.weight <= robot.max_load):  # Checks if order status is waiting and the order weight is within robot's limit
                order.status = "assigned"
                robot.status = "to_storage"
                order.robot = robot
                robot.current_order = order
                break

