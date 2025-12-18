# 8-Puzzle-AI-Project
Solving 8-Puzzle problem using AI search algorithms

## Project Overview
This project addresses the classical 8-Puzzle Problem using fundamental Artificial Intelligence search algorithms.  
The objective of the project is to demonstrate how different search strategies operate and to compare their performance when solving the same problem.

The project is implemented in Python and organized in a clear and modular structure suitable for academic submission and GitHub hosting.

## Problem Description
The 8-Puzzle Problem consists of a 3×3 grid containing eight numbered tiles and one empty space, represented by 0.  
The empty space allows tiles to be moved up, down, left, or right. The goal is to transform an initial configuration into a predefined goal configuration.

### Initial State Example

1 2 3 4 0 6 7 5 8

### Goal State

1 2 3 4 5 6 7 8 0

## Algorithms Implemented
The following search algorithms are implemented in this project:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Uniform Cost Search (UCS)
- A* Search Algorithm using the Manhattan Distance heuristic

Each algorithm is implemented in a separate folder with its own source code and documentation.

## State Representation
Each puzzle state is represented as a tuple of nine elements, where the value 0 denotes the empty tile.  
Tuples are used because they are immutable and can be efficiently stored in visited sets.

Example:

(1, 2, 3, 4, 0, 6, 7, 5, 8)

## Allowed Moves
Depending on the position of the empty tile, the following moves are permitted:
- Move Up
- Move Down
- Move Left
- Move Right

## Technologies Used
- Programming Language: Python 3
- Standard Libraries:
  - collections
  - heapq

No external libraries are required.

## How to Run
Example usage:
```python
start_state = (1,2,3,4,0,6,7,5,8)
solution = astar(start_state)
print(solution)

Algorithm Comparison

Algorithm	Optimal Solution	Time Efficiency	Memory Usage

BFS	Yes	Medium	High
DFS	No	Fast	Low
UCS	Yes	Medium	Medium
A*	Yes	Fast	Medium

Conclusion

This project demonstrates the differences between classical artificial intelligence search algorithms when applied to the 8-Puzzle Problem.
Among the implemented approaches, the A* search algorithm achieved the best performance due to the use of heuristic guidance.
