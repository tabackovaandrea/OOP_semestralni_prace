
## Warehouse Robot Simulation

This repository contains files regarding a simulation of an automated warehouse with a grid layout and different types of mobile robots.

## Current Features

- Grid-based warehouse environment
- Configurable warehouse dimensions
- Shelves and storage locations with access points
- Different robot types with individual properties
- Acquirement of the shortest path by Breadth-First Search (BFS) 
- Robot movement along the calculated path
- Basic collision detection
- Random order generation
- Assignment of orders to robots based on their load capacities

## Project Structure

- `main.py` – Main program and simulation setup
- `warehouse.py` – Warehouse grid, tiles, acquirement of path and collision detection
- `robots.py` – Robot classes, their properties and movement logic
- `orders.py` – Order class, random order generation and assignment

## Technologies

- Python 3

## Status

The project is currently under development. More features, such as warehouse visualization or simulation statistics, may be added in future versions.