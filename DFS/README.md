# 8-Puzzle DFS Solution

## Initial State

1 2 3
4 0 6
7 5 8

- 0 is the blank tile.
- DFS (Depth-First Search) starts from this state.

---

## DFS – Step by Step

DFS explores **one path as deep as possible** before backtracking.

### Step 1: Move Up

1 0 3
4 2 6
7 5 8

Not the Goal. DFS goes deeper.

#### Step 2: From previous state, move Up (invalid) / Down / Left / Right

- Up: invalid (out of bounds)
- Down:

1 2 3
4 0 6
7 5 8

(same as initial state → DFS backtracks)

- Left:

0 2 3
1 4 6
7 5 8

Not the Goal. DFS continues deeper.

- Right:

1 2 3
4 6 0
7 5 8

Not the Goal. DFS continues deeper.

---

### Step 3: Backtrack and explore other moves

DFS backtracks whenever a path reaches a dead-end or repeats a state. Eventually, it reaches:

1 2 3
4 5 6
7 0 8

Then moves Right:

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

## DFS Summary

- DFS may **not find the shortest path**.
- Solution found depends on the order of moves explored.
- DFS uses **less memory** than BFS but can get stuck in deep paths.

**Pros:**

- Low memory usage
- Simple implementation

**Cons:**

- Not guaranteed to be optimal (may not find shortest path)
- Can get stuck in deep paths or loops
