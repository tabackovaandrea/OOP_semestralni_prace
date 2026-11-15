
from warehouse import Warehouse, Tile
from robots import Robot, FastRobot, HeavyRobot 
import orders
import random      

# Definition of robots, shelves and warehouse
robot1 = FastRobot("R1", 1, 2)
robot2 = HeavyRobot("R2", 4, 8)
robots = [robot1, robot2]

warehouse = Warehouse(10, 15, robots)

# Definition of shelves
warehouse.add_shelf(0, 0, 10, 1) # Add a shelf at position (0, 0) with length 10 and width 1
warehouse.add_shelf(0, 1, 1, 12) # Add a shelf at position (0, 1) with length 1 and width 12
warehouse.add_shelf(9, 1, 1, 12) # Add a shelf at position (9, 1) with length 1 and width 12
warehouse.add_shelf(1, 4, 2, 1) # Add a shelf at position (1, 4) with length 2 and width 1
warehouse.add_shelf(7, 4, 2, 1) # Add a shelf at position (7, 4) with length 2 and width 1
warehouse.add_shelf(1, 8, 2, 1) # Add a shelf at position (1, 8) with length 2 and width 1
warehouse.add_shelf(7, 8, 2, 1) # Add a shelf at position (7, 8) with length 2 and width 1
warehouse.add_shelf(1, 12, 2, 1) # Add a shelf at position (1, 12) with length 2 and width 1
warehouse.add_shelf(7, 12, 2, 1) # Add a shelf at position (7, 12) with length 2 and width 1

# Definition of access points for each storage location (using nested dictionaries)
storage_locations = {
    # Row A
    "A1": {"shelf": (1, 0), "access": (1, 1)},
    "A2": {"shelf": (2, 0), "access": (2, 1)},
    "A3": {"shelf": (3, 0), "access": (3, 1)},
    "A4": {"shelf": (4, 0), "access": (4, 1)},
    "A5": {"shelf": (5, 0), "access": (5, 1)},
    "A6": {"shelf": (6, 0), "access": (6, 1)},
    "A7": {"shelf": (7, 0), "access": (7, 1)},
    "A8": {"shelf": (8, 0), "access": (8, 1)},

    # Row B
    "B1": {"shelf": (0, 1), "access": (1, 1)},
    "B2": {"shelf": (9, 1), "access": (8, 1)},

    # Row C
    "C1": {"shelf": (0, 2), "access": (1, 2)},
    "C2": {"shelf": (9, 2), "access": (8, 2)},

    # Row D
    "D1": {"shelf": (0, 3), "access": (1, 3)},
    "D2": {"shelf": (9, 3), "access": (8, 3)},

    # Row E
    "E1": {"shelf": (1, 4), "access": (1, 3)},
    "E2": {"shelf": (2, 4), "access": (2, 3)},
    "E3": {"shelf": (7, 4), "access": (7, 3)},
    "E4": {"shelf": (8, 4), "access": (8, 3)},

    # Row F
    "F1": {"shelf": (0, 5), "access": (1, 5)},
    "F2": {"shelf": (9, 5), "access": (8, 5)},

    # Row G
    "G1": {"shelf": (0, 6), "access": (1, 6)},
    "G2": {"shelf": (9, 6), "access": (8, 6)},

    # Row H
    "H1": {"shelf": (0, 7), "access": (1, 7)},
    "H2": {"shelf": (9, 7), "access": (8, 7)},

    # Row I
    "I1": {"shelf": (1, 8), "access": (1, 7)},
    "I2": {"shelf": (2, 8), "access": (2, 7)},
    "I3": {"shelf": (7, 8), "access": (7, 7)},
    "I4": {"shelf": (8, 8), "access": (8, 7)},
 
    # Row J
    "J1": {"shelf": (0, 9), "access": (1, 9)},
    "J2": {"shelf": (9, 9), "access": (8, 9)},

    # Row K
    "K1": {"shelf": (0, 10), "access": (1, 10)},
    "K2": {"shelf": (9, 10), "access": (8, 10)},

    # Row L
    "L1": {"shelf": (0, 11), "access": (1, 11)},
    "L2": {"shelf": (9, 11), "access": (8, 11)},

    # Row M
    "M1": {"shelf": (1, 12), "access": (1, 11)},
    "M2": {"shelf": (2, 12), "access": (2, 11)},
    "M3": {"shelf": (7, 12), "access": (7, 11)},
    "M4": {"shelf": (8, 12), "access": (8, 11)},
   }

# Positions of pick-up and delivery of each order (at the bottom of the map)
pickup_point = (3, 14)
delivery_point = (5, 14)

# Generating and assigning orders to robots
order_list = []

for i in range(7):
    order_list.append(orders.generate_order(i + 1, storage_locations))  # i+1 so that numbers of orders start from one
for order in order_list:
    print(order.id, order.location, order.status)

next_order_id = 8


# Main working cycle
for time in range(100):

    # If there are less than 7 unfinished orders, new orders are generated
    unfinished_orders_count = 0
    for order in order_list:
        if order.status != "completed":
            unfinished_orders_count +=1
    while unfinished_orders_count < 7:
        order_list.append(orders.generate_order(next_order_id, storage_locations))
        next_order_id += 1
        unfinished_orders_count += 1

    print(f"Time: {time}, Unfinished orders: {unfinished_orders_count}")
    print([(order.id, order.status, order.weight) for order in order_list])

    for robot in robots:

        if robot.status == "available":         # If robot is available, goes to pickup point and if at pickup point asks for an order
            warehouse.move_robot(robot, pickup_point)
            if robot.position_x == pickup_point[0] and robot.position_y == pickup_point[1]:
                orders.assign_order(robot, order_list)
                if robot.current_order is not None:     # If order is available, robot status changes to to_storage
                    robot.status = "to_storage"
                    robot.current_order.status = "acquiring"
                    print("Order", robot.current_order.id, "in progress.")

        elif robot.status == "to_storage":  # Robot goes to storage to order's access point, when at the access point, robot status changes to to_delivery and order status changes to delivering
            go_to_storage = storage_locations[robot.current_order.location]["access"]
            warehouse.move_robot(robot, go_to_storage)
            if robot.position_x == go_to_storage[0] and robot.position_y == go_to_storage[1]:
                robot.status = "to_delivery"
                robot.current_order.status = "delivering"

        elif robot.status == "to_delivery":   # Robot goes to delivery point, when at delivery point, robot status changes to available and order status changes to is completed
            warehouse.move_robot(robot, delivery_point)
            if robot.position_x == delivery_point[0] and robot.position_y == delivery_point[1]:
                robot.current_order.status = "completed"
                print("Order", robot.current_order.id, "is completed.")
                robot.current_order = None
                robot.status = "available"

