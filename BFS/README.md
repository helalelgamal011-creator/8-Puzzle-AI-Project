Solution

## 1️⃣ Initial State

1 2 3 4 0 6 7 5 8

- `0` is the blank tile.
- BFS (Breadth-First Search) starts from this state.

---

## 2️⃣ BFS – Level 1 (All possible moves)

The blank tile is in the middle → it can move **Up / Down / Left / Right**.

**Move 1: Up**

1 0 3 4 2 6 7 5 8

**Move 2: Down**

1 2 3 4 5 6 7 0 8

**Move 3: Left**

1 2 3 0 4 6 7 5 8

**Move 4: Right**

1 2 3 4 6 0 7 5 8

> BFS stores all these states in a queue in the same order.

---

## 3️⃣ BFS – Level 2

BFS examines the states one by one in order.

**First state checked:**

1 0 3 4 2 6 7 5 8

❌ Not the Goal

**Next state:**

1 2 3 4 5 6 7 0 8

Compare with the Goal:

1 2 3 4 5 6 7 8 0

Still one move away.

---

## 4️⃣ Expansion from this state

**Move: Right**

1 2 3 4 5 6 7 8 0

🎯 Goal Reached

---

## 5️⃣ Solution Path (Final Path)

**Step 1: Initial State**

1 2 3 4 0 6 7 5 8

**Step 2 (Down)**

1 2 3 4 5 6 7 0 8

**Step 3 (Right)**

1 2 3 4 5 6 7 8 0

---

## 6️⃣ BFS Summary

- BFS finds the solution in the **minimum number of moves**.
- **Solution = 2 Moves**
- BFS explores all states **level by level**.

**Pros:**
- ✔️ Optimal (finds the shortest path)

**Cons:**
- ❌ High memory usage
