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

1 2 3  
4 0 6  
7 5 8

### Goal State

1 2 3  
4 5 6  
7 8 0

## BFS Solution

**Step 1: Initial State**

1 2 3  
4 0 6  
7 5 8

**Step 2: Move Down**

1 2 3  
4 5 6  
7 0 8

**Step 3: Move Right**

1 2 3  
4 5 6  
7 8 0

BFS finds the solution in the minimum number of moves.  
Solution = 2 Moves

## DFS Solution

**Step 1: Initial State**

1 2 3  
4 0 6  
7 5 8

**Step 2: Move Left (example path chosen by DFS)**

1 2 3  
0 4 6  
7 5 8

**Step 3: Continue exploring depth-wise until goal**  

1 2 3  
4 5 6  
7 8 0

DFS may not find the shortest path.  

## UCS Solution

**Step 1: Initial State**

1 2 3  
4 0 6  
7 5 8

**Step 2: Move Down**

1 2 3  
4 5 6  
7 0 8

**Step 3: Move Right**

1 2 3  
4 5 6  
7 8 0

UCS finds the optimal solution based on cost.  
Solution = 2 Moves

## IDS Solution

**Step 1: Initial State**

1 2 3  
4 0 6  
7 5 8

**Step 2: Iterative Deepening (Depth 1,2,...)**  

1 2 3  
4 5 6  
7 0 8

**Step 3: Goal State Reached**

1 2 3  
4 5 6  
7 8 0

IDS finds the optimal solution using limited depth searches.  

## A* Solution

**Step 1: Initial State**

1 2 3  
4 0 6  
7 5 8

**Step 2: Move Down (guided by Manhattan Distance)**

1 2 3  
4 5 6  
7 0 8

**Step 3: Move Right**

1 2 3  
4 5 6  
7 8 0

A* finds the shortest path using heuristic guidance.  
Solution = 2 Moves

## Allowed Moves
Depending on the position of the empty tile, the following moves are permitted:
- Move Up
- Move Down
- Move Left
- Move Right

## State Representation
Each puzzle state is represented as a 3x3 grid with 0 representing the empty tile.  

Example:

1 2 3  
4 0 6  
7 5 8

## Algorithms Comparison

| Algorithm | Optimal (Shortest Path) | Speed | Memory Usage |
|----------|-------------------------|-------|--------------|
| **DFS (Depth-First Search)** |  No | Fast (may go deep unnecessarily) | Very Low |
| **BFS (Breadth-First Search)** |  Yes | Slow | Very High |
| **IDS (Iterative Deepening Search)** |  Yes | Medium | Low |
| **UCS (Uniform Cost Search)** |  Yes | Slow | High |
| **A\* (A-Star Search)** |  Yes | Fastest | High |

## Notes

- DFS is memory efficient but not optimal.
- BFS and UCS guarantee optimal solutions but consume high memory.
- IDS provides a balance between memory usage and optimality.
- A* offers the best performance in terms of speed while maintaining optimality when using an admissible heuristic.

## How to Run
Example usage in Python:

```python
from bfs import bfs
from dfs import dfs
from ucs import ucs
from ids import ids
from astar import a_star
from common import print_puzzle

start_state = (1,2,3,4,0,6,7,5,8)

# Run BFS
solution = bfs(start_state)
print("BFS Solution:")
for step in solution:
    print_puzzle(step)

# Run DFS
solution = dfs(start_state)
print("DFS Solution:")
for step in solution:
    print_puzzle(step)

# Run UCS
solution = ucs(start_state)
print("UCS Solution:")
for step in solution:
    print_puzzle(step)

# Run IDS
solution = ids(start_state)
print("IDS Solution:")
for step in solution:
    print_puzzle(step)

# Run A*
solution = a_star(start_state)
print("A* Solution:")
for step in solution:
    print_puzzle(step)

Conclusion

This project demonstrates the differences between classical artificial intelligence search algorithms when applied to the 8-Puzzle Problem.
Among the implemented approaches, the A* search algorithm achieved the best performance due to the use of heuristic guidance.
BFS and UCS guarantee optimal solutions but require more memory, while DFS is faster but may not find the optimal path. IDS provides a memory-efficient complete search.
