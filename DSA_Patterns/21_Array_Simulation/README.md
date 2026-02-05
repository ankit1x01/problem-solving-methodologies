# 🔄 Pattern 21: Array Simulation & Matrix Traversal

## 🎯 Think Like a 5-Year-Old

Imagine you are playing a board game like **Monopoly** or **Snakes and Ladders**.

1.  **Follow the Rules:** You roll a dice and move your piece exactly that many steps. You don't teleport, and you don't calculate the final winner instantly used advanced math. You just **move step-by-step**.
2.  **The Board:**
    - Sometimes the board is a **straight line** (like a race track).
    - Sometimes it's a **circle** (like Monopoly - you pass "GO" and start again).
    - Sometimes it's a **grid** (like Chess or a maze).

**Array Simulation** just means "Writing code that plays the game exactly as the rules say."

---

## ⏰ Real Life Example 1: The Kitchen Clock

Imagine a standard 12-hour clock.

- It's currently **10:00**.
- You want to know what time it will be in **5 hours**.
- simple math: `10 + 5 = 15`.
- But there is no "15:00" on the clock face!
- You wrap around: `15 - 12 = 3:00`.

**This is Simulation using Modulo Arithmetic (`%`).** In programming, we simulate circular movement (wrapping around array ends) using this exact logic.

---

## 🤖 Real Life Example 2: The Roomba Vacuum

Imagine a robot vacuum cleaner in a rectangular room (a Grid).

1.  It moves **Right** until it hits a wall.
2.  It turns **Down** and moves a bit.
3.  It moves **Left** until it hits a wall.
4.  It turns **Down** again.

To code this, you don't use a complex graph algorithm. You literally write loop instructions: "If hitting wall, turn 90 degrees."

---

## 🎬 Animated Visualization

### 1. Wrapped Movement (The Clock)

Array length `N = 5`: `[A, B, C, D, E]`
Current Index `i = 4` (Value 'E')
Move `+2` steps.

```
Start:  [ A, B, C, D, E ]
                      👆 (i=4)

Step 1: Move to 5? No! Wrap to 0.
        [ A, B, C, D, E ]
          � (i=0)

Step 2: Move to 1.
        [ A, B, C, D, E ]
             � (i=1) -> Value 'B'
```

Math: `(4 + 2) % 5 = 6 % 5 = 1`.

### 2. Spiral Matrix (The Snail)

Grid `3x3`.

```
START -> [ 1, 2, 3 ] -> Turn Down
           8, 9, 4
           7, 6, 5 <- Turn Left
           ^
       Turn Up
```

---

## 🎯 Why Use This Pattern?

Sometimes, there is **no clever shortcut**.

- **Algorithmic Optimization:** Not needed.
- **Trickery:** Not needed.
- **Implementation Skills:** CRITICAL.

These problems test if you can translate **complex English instructions** into **precise code** without making "Off-by-One" errors. They are very common in interviews to filter out candidates who know theory but can't code clearly.

---

## 🛠 Key Tools for Simulation

### 1. The Modulo Operator (`%`)

Used for circular arrays.

- **Move Forward:** `(i + steps) % n`
- **Move Backward:** `(i - steps + n) % n` (Be careful with negative results in Java/C++!)

### 2. Direction Arrays (For Grids)

Instead of writing 4 `if` statements, use a list of directions.

```python
# Order: Right, Down, Left, Up
dr = [0, 1, 0, -1]  # Change in Row
dc = [1, 0, -1, 0]  # Change in Col

# Move in direction 'd'
new_r = r + dr[d]
new_c = c + dc[d]
```

---

## 💻 Code Templates

### 1. Circular Array Movement

```python
def move_circular(nums, start_index, steps):
    n = len(nums)
    # The % n handles wrapping automatically
    target_index = (start_index + steps) % n
    return nums[target_index]
```

### 2. Grid Traversal (4 Directions)

```python
def traverse_grid(grid):
    rows, cols = len(grid), len(grid[0])
    # Directions: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    r, c = 0, 0 # Start position
    seen = set([(0, 0)])

    for _ in range(steps):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # Valid move
                print(f"Visiting {grid[nr][nc]}")
```

### 3. Spiral Matrix Template

```python
def spiralOrder(matrix):
    res = []
    if not matrix: return res

    # Define boundaries
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        # 1. Traverse Right (Top row)
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1 # Shrink top boundary

        # 2. Traverse Down (Right col)
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1 # Shrink right boundary

        if top <= bottom:
            # 3. Traverse Left (Bottom row)
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1 # Shrink bottom boundary

        if left <= right:
            # 4. Traverse Up (Left col)
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 # Shrink left boundary

    return res
```

---

## ⚠️ Common Mistakes & How to Avoid Them

### Mistake 1: The "Negative Modulo" Trap ❌

In Python, `-2 % 5 == 3`. This is good!
In Java/C++, `-2 % 5 == -2`. This is bad! It crashes your array index.

**Fix:** In Java/C++, always use: `((a % n) + n) % n`.

### Mistake 2: Boundary Confusion ❌

Mixing up `rows` (y-axis usually) and `cols` (x-axis usually), or swapping `top/bottom` logic.

**Fix:** explicitly name your variables `r` (row) and `c` (col) instead of `x` and `y` to avoid coordinate confusion. Rows correspond to "Y" (vertical), Cols correspond to "X" (horizontal).

---

## � Classic LeetCode Problems

| #    | Problem                                                               | Difficulty | Key Concept           |
| ---- | --------------------------------------------------------------------- | ---------- | --------------------- |
| 54   | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)         | Medium     | Matrix Boundaries     |
| 59   | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)   | Medium     | Matrix Generation     |
| 189  | [Rotate Array](https://leetcode.com/problems/rotate-array/)           | Medium     | Circular Wrapping     |
| 48   | [Rotate Image](https://leetcode.com/problems/rotate-image/)           | Medium     | In-place Matrix Manip |
| 73   | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium     | State Marking         |
| 498  | [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/) | Medium     | Complex Indexing      |
| 289  | [Game of Life](https://leetcode.com/problems/game-of-life/)           | Medium     | Neighbor Interaction  |
| 3379 | [Transformed Array](https://leetcode.com/problems/transformed-array/) | Easy       | Circular Indexing     |

---

## 🌟 Summary for Kids

### What We Learned:

1.  **Imitate Life:** Sometimes code just mimics a real-world process like a clock or a robot.
2.  **Boundaries:** Be careful not to fall off the edge of the board!
3.  **Wrapping:** The world might be round! If you go off the right side, you might appear on the left.

### Remember This:

> "Don't look for a magic formula. Just follow the instructions one step at a time!" 👣
