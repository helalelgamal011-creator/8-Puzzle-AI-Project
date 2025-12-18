# 8-Puzzle IDS Solution

## Initial State

1 2 3
4 0 6
7 5 8

- 0 is the blank tile.
- IDS (Iterative Deepening Search) starts from this state.
- IDS combines DFS depth-limited search with BFS completeness.

---

## IDS – Step by Step

IDS explores paths with increasing depth limits until the goal is found.

### Depth Limit = 0

- Only initial state is examined:

1 2 3
4 0 6
7 5 8

- Goal not reached → Increase depth limit

---

### Depth Limit = 1

Possible moves from initial state: Up, Down, Left, Right

Move Up

1 0 3
4 2 6
7 5 8

Not the Goal

Move Down

1 2 3
4 5 6
7 0 8

Not the Goal

Move Left

0 2 3
1 4 6
7 5 8

Not the Goal

Move Right

1 2 3
4 6 0
7 5 8

Not the Goal → Increase depth limit

---

### Depth Limit = 2

From state:

1 2 3
4 5 6
7 0 8

Move Right

1 2 3
4 5 6
7 8 0

Goal Reached

---

## Solution Path (Final Path)

Step 1: Initial State

1 2 3
4 0 6
7 5 8

Step 2 (Down)

1 2 3
4 5 6
7 0 8

Step 3 (Right)

1 2 3
4 5 6
7 8 0

---

## IDS Summary

- IDS is complete like BFS and memory-efficient like DFS.
- Solution = 2 Moves (minimum moves)
- Explores increasing depth limits iteratively.

**Pros:**

- Optimal (finds shortest path)
- Low memory usage compared to BFS

**Cons:**

- Repeated exploration of states increases runtime
- Slightly slower than BFS for shallow solutions
