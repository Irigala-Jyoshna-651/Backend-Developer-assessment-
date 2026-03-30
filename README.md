# Backend-Developer-assessment-



# Mars Rover Problem Solver

## Overview

This project provides a Python implementation of the Mars Rover problem. It simulates the movement of robotic rovers on a rectangular grid based on a sequence of instructions.

Each rover maintains its position and orientation while executing commands to navigate within the defined boundaries.

---

## Problem Statement

A plateau is represented as a grid with defined upper-right coordinates. Rovers are deployed on this plateau with an initial position and direction.

Each rover receives a sequence of instructions:
- L : Turn left
- R : Turn right
- M : Move forward in the current direction

The rover must not move outside the grid boundaries.

---

## Features

- Supports multiple rover simulations
- Ensures boundary constraints are maintained
- Implements directional rotation and movement logic
- Clean and modular function design

---

## Project Structure

main.py    # Contains the core logic for rover navigation

---

## Input Format

1. The first line defines the grid size:
   max_x max_y

2. For each rover:
   - Initial position and direction:
     x y direction

   - Instruction string:
     sequence_of_commands

---

## Example Input

5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

---

## Example Output

1 3 N
5 1 E

---

## Implementation Details

- Directions are handled using an ordered list:
  directions = ["N", "E", "S", "W"]

- Movement vectors are defined as:
  moves = {
      "N": (0, 1),
      "E": (1, 0),
      "S": (0, -1),
      "W": (-1, 0)
  }

- Rotation is achieved using index manipulation with modulo arithmetic.
- Movement is validated against grid boundaries before updating position.

---

## How to Run

1. Clone the repository:
   git clone https://github.com/your-username/mars-rover.git

2. Navigate to the project directory:
   cd mars-rover

3. Run the script:
   python main.py

---

## Source Code

Refer to the implementation in main.py

---

## Future Enhancements

- Add obstacle detection
- Support dynamic grid sizes via user input
- Provide file-based or command-line input handling
- Extend to a web-based interface

---

## License

This project is open-source and available for use and modification.
