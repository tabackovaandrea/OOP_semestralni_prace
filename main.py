
from warehouse import Warehouse, Tile
from robots import Robot, FastRobot, HeavyRobot 
import orders
import random      

# Definition of robots, shelves and warehouse
robot1 = FastRobot("F1", 0, 24)
robot2 = HeavyRobot("H1", 19, 24)
robot3 = FastRobot("F2", 1, 24)
robot4 = HeavyRobot("H2", 18, 24)
robot5 = HeavyRobot("H3", 17, 24)
robots = [robot1, robot2, robot3, robot4, robot5]

warehouse = Warehouse(20, 25, robots)

# Definition of shelves
warehouse.add_shelf(0, 0, 20, 1) # Add a shelf at position (0, 0) with length 20 and width 1
warehouse.add_shelf(0, 1, 1, 20) # Add a shelf at position (0, 1) with length 1 and width 20
warehouse.add_shelf(19, 1, 1, 20) # Add a shelf at position (19, 1) with length 1 and width 20
warehouse.add_shelf(1, 5, 6, 1) # Add a shelf at position (1, 5) with length 6 and width 1
warehouse.add_shelf(13, 5, 6, 1) # Add a shelf at position (13, 5) with length 6 and width 1
warehouse.add_shelf(1, 10, 6, 1) # Add a shelf at position (1, 10) with length 6 and width 1
warehouse.add_shelf(13, 10, 6, 1) # Add a shelf at position (13, 10) with length 6 and width 1
warehouse.add_shelf(1, 15, 6, 1) # Add a shelf at position (1, 15) with length 6 and width 1
warehouse.add_shelf(13, 15, 6, 1) # Add a shelf at position (13, 15) with length 6 and width 1
warehouse.add_shelf(1, 20, 6, 1) # Add a shelf at position (1, 20) with length 6 and width 1
warehouse.add_shelf(13, 20, 6, 1) # Add a shelf at position (13, 20) with length 6 and width 1

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
    "A9": {"shelf": (9, 0), "access": (9, 1)},
    "A10": {"shelf": (10, 0), "access": (10, 1)},
    "A11": {"shelf": (11, 0), "access": (11, 1)},
    "A12": {"shelf": (12, 0), "access": (12, 1)},
    "A13": {"shelf": (13, 0), "access": (13, 1)},
    "A14": {"shelf": (14, 0), "access": (14, 1)},
    "A15": {"shelf": (15, 0), "access": (15, 1)},
    "A16": {"shelf": (16, 0), "access": (16, 1)},
    "A17": {"shelf": (17, 0), "access": (17, 1)},
    "A18": {"shelf": (18, 0), "access": (18, 1)},

    # Row B
    "B1": {"shelf": (0, 1), "access": (1, 1)},
    "B2": {"shelf": (19, 1), "access": (18, 1)},

    # Row C
    "C1": {"shelf": (0, 2), "access": (1, 2)},
    "C2": {"shelf": (19, 2), "access": (18, 2)},

    # Row D
    "D1": {"shelf": (0, 3), "access": (1, 3)},
    "D2": {"shelf": (19, 3), "access": (18, 3)},

    # Row E
    "E1": {"shelf": (0, 4), "access": (1, 4)},
    "E2": {"shelf": (19, 4), "access": (18, 4)},

    # Row F
    "F1": {"shelf": (1, 5), "access": (1, 4)},
    "F2": {"shelf": (2, 5), "access": (2, 4)},
    "F3": {"shelf": (3, 5), "access": (3, 4)},
    "F4": {"shelf": (4, 5), "access": (4, 4)},
    "F5": {"shelf": (5, 5), "access": (5, 4)},
    "F6": {"shelf": (6, 5), "access": (6, 4)},
    "F7": {"shelf": (13, 5), "access": (13, 4)},
    "F8": {"shelf": (14, 5), "access": (14, 4)},
    "F9": {"shelf": (15, 5), "access": (15, 4)},
    "F10": {"shelf": (16, 5), "access": (16, 4)},
    "F11": {"shelf": (17, 5), "access": (17, 4)},
    "F12": {"shelf": (18, 5), "access": (18, 4)},

    # Row G
    "G1": {"shelf": (0, 6), "access": (1, 6)},
    "G2": {"shelf": (19, 6), "access": (18, 6)},

    # Row H
    "H1": {"shelf": (0, 7), "access": (1, 7)},
    "H2": {"shelf": (19, 7), "access": (18, 7)},

    # Row I
    "I1": {"shelf": (0, 8), "access": (1, 8)},
    "I2": {"shelf": (19, 8), "access": (18, 8)},

    # Row J
    "J1": {"shelf": (0, 9), "access": (1, 9)},
    "J2": {"shelf": (19, 9), "access": (18, 9)},

    # Row K
    "K1": {"shelf": (1, 10), "access": (1, 9)},
    "K2": {"shelf": (2, 10), "access": (2, 9)},
    "K3": {"shelf": (3, 10), "access": (3, 9)},
    "K4": {"shelf": (4, 10), "access": (4, 9)},
    "K5": {"shelf": (5, 10), "access": (5, 9)},
    "K6": {"shelf": (6, 10), "access": (6, 9)},
    "K7": {"shelf": (13, 10), "access": (13, 9)},
    "K8": {"shelf": (14, 10), "access": (14, 9)},
    "K9": {"shelf": (15, 10), "access": (15, 9)},
    "K10": {"shelf": (16, 10), "access": (16, 9)},
    "K11": {"shelf": (17, 10), "access": (17, 9)},
    "K12": {"shelf": (18, 10), "access": (18, 9)},

    # Row L
    "L1": {"shelf": (0, 11), "access": (1, 11)},
    "L2": {"shelf": (19, 11), "access": (18, 11)},

    # Row M
    "M1": {"shelf": (0, 12), "access": (1, 12)},
    "M2": {"shelf": (19, 12), "access": (18, 12)},

    # Row N
    "N1": {"shelf": (0, 13), "access": (1, 13)},
    "N2": {"shelf": (19, 13), "access": (18, 13)},

    # Row O
    "O1": {"shelf": (0, 14), "access": (1, 14)},
    "O2": {"shelf": (19, 14), "access": (18, 14)},

    # Row P
    "P1": {"shelf": (1, 15), "access": (1, 14)},
    "P2": {"shelf": (2, 15), "access": (2, 14)},
    "P3": {"shelf": (3, 15), "access": (3, 14)},
    "P4": {"shelf": (4, 15), "access": (4, 14)},
    "P5": {"shelf": (5, 15), "access": (5, 14)},
    "P6": {"shelf": (6, 15), "access": (6, 14)},
    "P7": {"shelf": (13, 15), "access": (13, 14)},
    "P8": {"shelf": (14, 15), "access": (14, 14)},
    "P9": {"shelf": (15, 15), "access": (15, 14)},
    "P10": {"shelf": (16, 15), "access": (16, 14)},
    "P11": {"shelf": (17, 15), "access": (17, 14)},
    "P12": {"shelf": (18, 15), "access": (18, 14)},

    # Row Q
    "Q1": {"shelf": (0, 16), "access": (1, 16)},
    "Q2": {"shelf": (19, 16), "access": (18, 16)},

    # Row R
    "R1": {"shelf": (0, 17), "access": (1, 17)},
    "R2": {"shelf": (19, 17), "access": (18, 17)},

    # Row S
    "S1": {"shelf": (0, 18), "access": (1, 18)},
    "S2": {"shelf": (19, 18), "access": (18, 18)},

    # Row T
    "T1": {"shelf": (0, 19), "access": (1, 19)},
    "T2": {"shelf": (19, 19), "access": (18, 19)},

    # Row U
    "U1": {"shelf": (1, 20), "access": (1, 19)},
    "U2": {"shelf": (2, 20), "access": (2, 19)},
    "U3": {"shelf": (3, 20), "access": (3, 19)},
    "U4": {"shelf": (4, 20), "access": (4, 19)},
    "U5": {"shelf": (5, 20), "access": (5, 19)},
    "U6": {"shelf": (6, 20), "access": (6, 19)},
    "U7": {"shelf": (13, 20), "access": (13, 19)},
    "U8": {"shelf": (14, 20), "access": (14, 19)},
    "U9": {"shelf": (15, 20), "access": (15, 19)},
    "U10": {"shelf": (16, 20), "access": (16, 19)},
    "U11": {"shelf": (17, 20), "access": (17, 19)},
    "U12": {"shelf": (18, 20), "access": (18, 19)}
   }


# Positions of pick-up and delivery of each order (at the bottom of the map)
pickup_point = (7, 24)
delivery_point = (10, 24)

resting_point = (0, 23)

charging_point1 = (0, 24)
charging_point2 = (1, 24)
charging_point3 = (19, 24)
charging_point4 = (18, 24)

# Generating and assigning orders to robots
order_list = []

for i in range(10):
    order_list.append(orders.generate_order(i + 1, storage_locations))  # i+1 so that numbers of orders start from one
for order in order_list:
    print(order.id, order.location, order.status)

next_order_id = 11


# Main working cycle
for time in range(200):
    
    # If there are less than 10 unfinished orders, new orders are generated
    unfinished_orders_count = 0
    for order in order_list:
        if order.status != "completed":
            unfinished_orders_count +=1
    while unfinished_orders_count < 10:
        order_list.append(orders.generate_order(next_order_id, storage_locations))
        next_order_id += 1
        unfinished_orders_count += 1

    print(f"Time: {time}, Unfinished orders: {unfinished_orders_count}")
    print([(order.id, order.status, order.weight) for order in order_list])

    for robot in robots:
        if time > 0 and time % robot.move_interval == 0:

            # If robot is not charged enough and is available, it moves to charging station
            if robot.battery < 30 and robot.status == "available":
                robot.status = "to_charging_station"
            elif robot.status == "to_charging_station":
                if warehouse.tiles[charging_point1[1]][charging_point1[0]].robot is None:
                    warehouse.move_robot(robot, charging_point1)
                elif warehouse.tiles[charging_point2[1]][charging_point2[0]].robot is None:
                    warehouse.move_robot(robot, charging_point2)
                elif warehouse.tiles[charging_point3[1]][charging_point3[0]].robot is None:
                    warehouse.move_robot(robot, charging_point3)
                elif warehouse.tiles[charging_point4[1]][charging_point4[0]].robot is None:
                    warehouse.move_robot(robot, charging_point4)

                # If robot is at one of the charging points, it changes status to charging and charges up to 90 then changes status back to available
                # Due to the palcement of the charging condition inside the time condition, the heavy robot charges only at its move interval 
                if ((robot.position_x, robot.position_y) == charging_point1 or (robot.position_x, robot.position_y) == charging_point2
                    or (robot.position_x, robot.position_y) == charging_point3 or (robot.position_x, robot.position_y) == charging_point4):
                    robot.status = "charging"
                    if robot.battery < 90:
                        robot.charge_battery()
            elif robot.status == "charging":
                if robot.battery >= 90:
                    robot.status = "available"
                else:
                    robot.charge_battery()

            # If robot is charged enough, it works on delivering orders
            else:
                robot.battery -= 1

                if robot.status == "available":         # If robot is available, goes to pickup point and if at pickup point asks for an order
                    warehouse.move_robot(robot, pickup_point)
                    if robot.position_x == pickup_point[0] and robot.position_y == pickup_point[1]:
                        orders.assign_order(robot, order_list)
                        if robot.current_order is not None:     # If order is available, robot status changes to to_storage
                            robot.status = "to_storage"
                            robot.current_order.status = "acquiring"
                            print("Order", robot.current_order.id, "in progress.")
                        else:
                            robot.status = "waiting"     # Robot couldn't find order in its load range -> moves to the side and back so the pickup point is free for other robots

                elif robot.status == "waiting":
                    warehouse.move_robot(robot, resting_point)
                    if robot.position_x == resting_point[0] and robot.position_y == resting_point[1]:
                        robot.status = "available"
                        print("Robot got to resting point")

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
