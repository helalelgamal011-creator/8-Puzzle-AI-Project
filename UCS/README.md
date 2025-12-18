# 8-Puzzle UCS Solution

## Initial State

1 2 3
4 0 6
7 5 8

- 0 is the blank tile.
- UCS (Uniform Cost Search) starts from this state.
- UCS always expands the node with the **lowest path cost**.

---

## UCS – Step by Step

### Step 1: Initial State

1 2 3
4 0 6
7 5 8

- Path cost = 0
- Expand possible moves: Up, Down, Left, Right

**Move 1: Up**

1 0 3
4 2 6
7 5 8

- Path cost = 1

**Move 2: Down**

1 2 3
4 5 6
7 0 8

- Path cost = 1

**Move 3: Left**

1 2 3
0 4 6
7 5 8

- Path cost = 1

**Move 4: Right**

1 2 3
4 6 0
7 5 8

- Path cost = 1

UCS stores all these states in a priority queue based on path cost.

---

### Step 2: Expand lowest cost state

**State with path cost = 1**

1 2 3
4 5 6
7 0 8

- Expand possible moves:

Move Up → 1 2 3 / 4 0 6 / 7 5 8 (already visited)

Move Down → invalid (out of bounds)

Move Left → 1 2 3 / 4 5 6 / 0 7 8 (new state, path cost = 2)

Move Right → 1 2 3 / 4 5 6 / 7 8 0 (Goal reached, path cost = 2)

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

## UCS Summary

- UCS finds the **lowest-cost solution**.
- Solution = 2 Moves (minimum cost)
- UCS uses a **priority queue** to expand nodes with the lowest path cost first.

**Pros:**

- Optimal (finds lowest-cost solution)
- Can handle variable move costs

**Cons:**

- Higher memory usage than DFS
- Slightly slower than DFS for small problems

Run:
```python
ucs(start_state)
