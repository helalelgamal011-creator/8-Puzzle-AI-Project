# 8-Puzzle A* Solution

## Initial State

1 2 3
4 0 6
7 5 8

- 0 is the blank tile.
- A* Search uses a **priority queue** based on `f(n) = g(n) + h(n)` where:
  - `g(n)` is the cost from start to current state
  - `h(n)` is the heuristic estimate to the goal
- We'll use **Manhattan Distance** as the heuristic.

---

## A* – Step by Step

### Step 1: Initial State

1 2 3
4 0 6
7 5 8

- g(n) = 0
- h(n) = 2 (tiles 5 and 8 are not in place)
- f(n) = 0 + 2 = 2
- Expand possible moves: Up, Down, Left, Right

Move Up → 1 0 3 / 4 2 6 / 7 5 8 → f(n) = 1 + 4 = 5  
Move Down → 1 2 3 / 4 5 6 / 7 0 8 → f(n) = 1 + 1 = 2  
Move Left → 0 2 3 / 1 4 6 / 7 5 8 → f(n) = 1 + 4 = 5  
Move Right → 1 2 3 / 4 6 0 / 7 5 8 → f(n) = 1 + 3 = 4

- Add all states to the priority queue ordered by f(n)

---

### Step 2: Expand lowest f(n) state

- State with f(n) = 2: 1 2 3 / 4 5 6 / 7 0 8

- Possible moves: Up, Down, Left, Right

Move Right → 1 2 3 / 4 5 6 / 7 8 0 → Goal reached

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

## A* Summary

- A* finds the **shortest path** using a heuristic.
- Solution = 2 Moves
- Explores states with the **lowest estimated total cost** first.

**Pros:**

- Optimal (finds shortest path if heuristic is admissible)
- Efficient with proper heuristic

**Cons:**

- Uses more memory than DFS
- Heuristic computation adds overhead
