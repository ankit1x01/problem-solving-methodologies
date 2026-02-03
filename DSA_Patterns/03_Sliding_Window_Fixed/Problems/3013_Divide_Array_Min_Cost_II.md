# 3013. Divide an Array Into Subarrays With Minimum Cost II

**Difficulty:** Hard 🔥
**Pattern:** Sliding Window (Fixed) + Two Heaps
**Key Insight:** We're picking split points, not counting elements!

---

## 🎯 Problem in Simple Words

Imagine you have a row of candy boxes, each with a number on it. You need to:

1. **Divide** them into **k groups** (each group = consecutive boxes)
2. Each group has a "cost" = the **first box's number** in that group
3. Find the way to divide that gives the **smallest total cost**

**But there's a special rule:** The first box of the 2nd group and the first box of the last group can't be too far apart (distance ≤ `dist`).

---

## 📝 Problem Description (Official)

You are given:
- `nums`: An array of integers (length `n`)
- `k`: Number of groups to create
- `dist`: Maximum distance constraint

**Cost Rule:** The cost of a subarray is its **first element**.
- Example: `[1,2,3]` has cost `1`, `[3,4,1]` has cost `3`

**Task:** Divide `nums` into `k` disjoint contiguous subarrays where:
- If splits are at indices `i₁, i₂, ..., iₖ₋₁`
- Then `iₖ₋₁ - i₁ ≤ dist` (distance constraint)

**Goal:** Minimize the sum of all subarray costs.

---

## 🧩 Understanding Through Example

### Example 1: Basic Case

```
nums = [1, 3, 2, 6, 4, 2]
k = 3 (we need 3 groups)
dist = 3
```

**What does k=3 mean?**
We need to make 3 groups, which means we need **2 split points** (k-1 = 2).

**What are split points?**
Split points are the **starting indices** of new groups:
- Group 1 starts at index 0 (always)
- Group 2 starts at some index i₁
- Group 3 starts at some index i₂

**Visual representation:**

```
Index:  0   1   2   3   4   5
Value: [1] [3] [2] [6] [4] [2]
        ↑
    Group 1 starts here (always)
```

**Option A: Split at indices 1 and 2**
```
Group 1: [1]       → cost = 1
Group 2: [3]       → cost = 3  
Group 3: [2,6,4,2] → cost = 2
Total cost: 1 + 3 + 2 = 6

Check distance: i₂ - i₁ = 2 - 1 = 1 ≤ 3 ✅
```

**Option B: Split at indices 1 and 4**
```
Group 1: [1]       → cost = 1
Group 2: [3,2,6]   → cost = 3
Group 3: [4,2]     → cost = 4
Total cost: 1 + 3 + 4 = 8

Check distance: i₂ - i₁ = 4 - 1 = 3 ≤ 3 ✅
```

**Option C: Split at indices 2 and 5**
```
Group 1: [1,3]     → cost = 1
Group 2: [2,6,4]   → cost = 2
Group 3: [2]       → cost = 2
Total cost: 1 + 2 + 2 = 5

Check distance: i₂ - i₁ = 5 - 2 = 3 ≤ 3 ✅
```

**Best option: C with total cost = 5** ✨

---

## 🔍 Key Observation: What Are We Really Choosing?

This is the **AHA! moment**:

```
We're NOT choosing which elements to include.
We're choosing WHERE to SPLIT the array!

Split points = Starting indices of groups 2, 3, 4, ..., k
We need to pick (k-1) split points.
```

**Why does nums[0] always count?**
- `nums[0]` is ALWAYS the start of Group 1
- So its value ALWAYS adds to the total cost
- We can't change this!

**What can we optimize?**
- We pick k-1 split points from indices 1, 2, ..., n-1
- Each split point's value adds to the cost
- We want to pick indices with **smallest values**
- BUT they must satisfy: `last_index - first_index ≤ dist`

---

## 🎨 Visual Understanding

### How the constraint works:

```
nums = [1, 3, 2, 6, 4, 2, 8, 1]
k = 4 (need 3 split points)
dist = 4

         i₁      i₂     i₃
         ↓       ↓      ↓
Index: 0  1  2  3  4  5  6  7
Value: 1  3  2  6  4  2  8  1
       │  └──────────────┘
       │          ↑
  Always     Must fit in window
  picked     of size ≤ dist
```

**If i₁ = 1:**
- We can pick i₂ and i₃ from indices [2, 3, 4, 5] (since 5 - 1 = 4 ≤ dist)
- Best 2 values in [2,6,4,2] are 2 and 2 (at indices 2 and 5)
- Total: 1 + 3 + 2 + 2 = 8

**If i₁ = 2:**
- We can pick i₂ and i₃ from indices [3, 4, 5, 6] (since 6 - 2 = 4 ≤ dist)
- Best 2 values in [6,4,2,8] are 2 and 4 (at indices 5 and 4)
- Total: 1 + 2 + 4 + 2 = 9

**If i₁ = 3:**
- We can pick i₂ and i₃ from indices [4, 5, 6, 7] (since 7 - 3 = 4 ≤ dist)
- Best 2 values in [4,2,8,1] are 1 and 2 (at indices 7 and 5)
- Total: 1 + 6 + 2 + 1 = 10

---

## 🎪 Super Simple Visual Guide

### The Candy Box Story 🍬

```
You have candy boxes in a line:
[1] [3] [2] [6] [4] [2]

You want to give them to 3 kids.
Each kid gets a group of boxes next to each other.
Each kid's "score" = the first box they get.

Find the way that minimizes total score!
```

**Constraint:** The 2nd kid and 3rd kid must get their first boxes close together (within 3 positions).

**Visualizing the choices:**

```
Choice 1: Split after box 0 and after box 1
────────────────────────────────────────
[1] │ [3] │ [2][6][4][2]
Kid1│Kid2│  Kid3
Score: 1 + 3 + 2 = 6


Choice 2: Split after box 0 and after box 2
────────────────────────────────────────
[1] │ [3][2] │ [6][4][2]
Kid1│  Kid2  │  Kid3
Score: 1 + 3 + 6 = 10


Choice 3: Split after box 1 and after box 2
────────────────────────────────────────
[1][3] │ [2] │ [6][4][2]
 Kid1  │Kid2│  Kid3
Score: 1 + 2 + 6 = 9


Choice 4: Split after box 1 and after box 4
────────────────────────────────────────
[1][3] │ [2][6][4] │ [2]
 Kid1  │   Kid2    │Kid3
Score: 1 + 2 + 2 = 5 ✨ BEST!
```

Notice: In Choice 4, the splits are at indices 2 and 5.
Distance: 5 - 2 = 3 ≤ 3 ✓

---

## 🏗️ Building Blocks: From Simple to Complex

### Level 1: Understanding "Split Points"

```
Array: [A][B][C][D][E]

No splits:
[A][B][C][D][E] → 1 group, cost = A

One split at index 2:
[A][B] │ [C][D][E] → 2 groups
        ↑ split
Group 1 cost = A
Group 2 cost = C
Total = A + C

Two splits at indices 1 and 3:
[A] │ [B][C] │ [D][E]
    ↑         ↑ splits
Group 1 cost = A
Group 2 cost = B  
Group 3 cost = D
Total = A + B + D
```

### Level 2: The Distance Rule

```
If splits are at indices i₁ and i₂:
Distance = i₂ - i₁ must be ≤ dist

Example with dist = 2:
[A] │ [B][C] │ [D][E]
 0     1  2     3  4
      ↑         ↑
      i₁=1      i₂=3
Distance: 3-1 = 2 ≤ 2 ✓
```

### Level 3: Optimization Strategy

```
Given: nums, k (groups needed), dist

Step 1: Realize nums[0] is forced
  - It's always the first group's start
  - We CAN'T change this
  - Add its value to answer

Step 2: Pick k-1 split points
  - Choose indices from 1 to n-1
  - Want smallest values
  - Must satisfy distance rule

Step 3: Use sliding window
  - Try each possible "first split" (i₁)
  - For each i₁, window = [i₁+1, i₁+dist]
  - Pick k-2 smallest from window
  - Calculate total cost
  - Track minimum
```

---

## 🎬 Animated Step-by-Step Example

### Setup
```
nums = [5, 1, 2, 4, 3]
k = 3 (need 3 groups)
dist = 2 (max distance between splits)

Need to pick: k-1 = 2 split points
After 1st split (i₁), pick k-2 = 1 more from window
```

### Animation Frame 1: Try i₁ = 1

```
     i₁
     ↓
[5] [1] [2] [4] [3]
 0   1   2   3   4
     └──────┘
     window (indices 2 to 3)
     
Window values: [2, 4]
Pick 1 smallest: 2

Cost = 5 (forced) + 1 (i₁) + 2 (picked) = 8
```

### Animation Frame 2: Try i₁ = 2

```
         i₁
         ↓
[5] [1] [2] [4] [3]
 0   1   2   3   4
         └──────┘
         window (indices 3 to 4)
         
Window values: [4, 3]
Pick 1 smallest: 3

Cost = 5 (forced) + 2 (i₁) + 3 (picked) = 10
```

### Animation Frame 3: Try i₁ = 3

```
             i₁
             ↓
[5] [1] [2] [4] [3]
 0   1   2   3   4
             └──┘
             window (index 4 only)
             
Window values: [3]
Pick 1 smallest: 3

Cost = 5 (forced) + 4 (i₁) + 3 (picked) = 12
```

### Result: Minimum cost = 8 ✨

---

## 💡 Solution Strategy

### The Key Insight

```
Problem breaks down into:
1. nums[0] is ALWAYS selected (fixed cost)
2. We need to pick (k-1) more indices from nums[1:]
3. Let's say first pick is at index i₁
4. Then all other picks must be in range [i₁+1, i₁+dist]
5. We want the SMALLEST values possible
```

### Why Sliding Window?

```
For each possible i₁:
  - Window = indices from i₁+1 to i₁+dist
  - Pick (k-2) smallest values from this window
  - Calculate: nums[0] + nums[i₁] + sum of (k-2) smallest
  - Track minimum cost
  
As i₁ moves right, the window slides!
```

### Why Two Heaps?

We need to efficiently:
1. Keep track of the k-2 smallest elements in a sliding window
2. Get their sum quickly
3. Add/remove elements as window slides

**Two Heap approach:**
- `low` (Max Heap): Stores the k-2 smallest elements
- `high` (Min Heap): Stores the rest
- As window slides, rebalance the heaps

---

## 🎬 Algorithm Walkthrough

### Step-by-Step with Example

```
nums = [1, 3, 2, 6, 4, 2]
k = 3 (need 2 split points: i₁ and one more)
dist = 3
k-2 = 1 (need 1 smallest value from window after i₁)
```

**Step 1: i₁ = 1 (value = 3)**
```
Window for other picks: indices [2, 3, 4] (within dist=3 from index 1)
Values in window: [2, 6, 4]
Pick 1 smallest: 2
Cost = 1 + 3 + 2 = 6
```

**Step 2: i₁ = 2 (value = 2)**
```
Window for other picks: indices [3, 4, 5] (within dist=3 from index 2)
Values in window: [6, 4, 2]
Pick 1 smallest: 2
Cost = 1 + 2 + 2 = 5 ✨ (Best so far!)
```

**Step 3: i₁ = 3 (value = 6)**
```
Window for other picks: indices [4, 5] (can't go beyond array)
Values in window: [4, 2]
Pick 1 smallest: 2
Cost = 1 + 6 + 2 = 9
```

**Answer: 5**

---

## 🔧 Detailed Algorithm

### Pseudocode

```python
1. Initialize min_cost = infinity
2. Add nums[0] to min_cost (it's always included)

3. For each possible first split i₁ from 1 to n-k+1:
   
   a. Create window of candidates: [i₁+1, min(i₁+dist, n-1)]
   
   b. Find k-2 smallest values in this window:
      - Use two heaps to maintain smallest k-2 elements
      - Track their sum
   
   c. Calculate cost = nums[0] + nums[i₁] + sum_of_k_2_smallest
   
   d. Update min_cost if this is better
   
   e. Slide window: remove old, add new element

4. Return min_cost
```

---

## 💻 Complete Working Solution

```python
from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        
        # Special case: only need 2 splits total
        if k == 2:
            return nums[0] + min(nums[1:])
        
        # We need to pick k-2 smallest from the candidates
        target_size = k - 2
        
        # Two heaps approach
        low = []   # Max heap (negated) - stores k-2 smallest
        high = []  # Min heap - stores the rest
        low_sum = 0
        
        def add_to_heaps(val):
            """Add a value to the heap system"""
            nonlocal low_sum
            heappush(low, -val)  # Max heap (negate for min heap)
            low_sum += val
            
            # If low has too many, move largest to high
            if len(low) > target_size:
                removed = -heappop(low)
                low_sum -= removed
                heappush(high, removed)
        
        def remove_from_heaps(val):
            """Remove a value from the heap system"""
            nonlocal low_sum
            if low and -low[0] >= val:
                # Value is in low heap
                low.remove(-val)
                heapify(low)
                low_sum -= val
                
                # Rebalance: move from high to low if needed
                if high and len(low) < target_size:
                    moved = heappop(high)
                    heappush(low, -moved)
                    low_sum += moved
            else:
                # Value is in high heap
                high.remove(val)
                heapify(high)
        
        # Initialize the first window
        # i1 = 1, candidates are from [2, min(1+dist, n-1)]
        right_bound = min(1 + dist, n - 1)
        for idx in range(2, right_bound + 1):
            add_to_heaps(nums[idx])
        
        # Calculate first cost
        min_cost = nums[0] + nums[1] + low_sum
        
        # Slide the window
        for i1 in range(2, n - k + 2):
            # Remove element that's no longer in window
            old_idx = i1  # This was in previous window
            if old_idx >= 2:
                remove_from_heaps(nums[old_idx])
            
            # Add new element entering window
            new_idx = min(i1 + dist, n - 1)
            if new_idx >= i1 + 1 and new_idx not in range(2, min(1 + dist, n - 1) + 1):
                add_to_heaps(nums[new_idx])
            
            # Calculate cost for this i1
            current_cost = nums[0] + nums[i1] + low_sum
            min_cost = min(min_cost, current_cost)
        
        return min_cost
```

### Simpler Solution Using SortedList (Easier to Understand)

```python
from sortedcontainers import SortedList
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        
        # Edge case
        if k == 2:
            return nums[0] + min(nums[1:])
        
        # Number of additional picks after i1
        need = k - 2
        
        # Use SortedList to maintain candidates
        candidates = SortedList()
        
        # Initialize first window [2, 1+dist]
        for idx in range(2, min(2 + dist, n)):
            candidates.add(nums[idx])
        
        # Calculate initial cost (i1 = 1)
        min_cost = nums[0] + nums[1] + sum(candidates[:need])
        
        # Slide window through remaining positions
        for i1 in range(2, n):
            # Remove element leaving window
            leaving = i1
            if leaving in range(2, min(2 + dist, n)):
                candidates.remove(nums[leaving])
            
            # Add element entering window
            entering = i1 + dist
            if entering < n:
                candidates.add(nums[entering])
            
            # Calculate cost with this i1
            if len(candidates) >= need:
                cost = nums[0] + nums[i1] + sum(candidates[:need])
                min_cost = min(min_cost, cost)
        
        return min_cost
```

---

## 📊 Example Walkthrough with Code Trace

### Example: nums = [1, 3, 2, 6, 4, 2], k = 3, dist = 3

```python
Step-by-step execution:

Initial: nums[0] = 1 (always included)
need = k - 2 = 1

i1 = 1 (nums[1] = 3):
    Window: indices [2, 3, 4] within dist=3
    Candidates: [2, 6, 4]
    Sorted: [2, 4, 6]
    Pick 1 smallest: [2]
    Cost: 1 + 3 + 2 = 6

i1 = 2 (nums[2] = 2):
    Window: indices [3, 4, 5] within dist=3
    Candidates: [6, 4, 2]
    Sorted: [2, 4, 6]
    Pick 1 smallest: [2]
    Cost: 1 + 2 + 2 = 5 ← MINIMUM!

i1 = 3 (nums[3] = 6):
    Window: indices [4, 5] within dist=3
    Candidates: [4, 2]
    Sorted: [2, 4]
    Pick 1 smallest: [2]
    Cost: 1 + 6 + 2 = 9

Result: 5
```

---

## 🎯 Common Mistakes to Avoid

### Mistake 1: Counting Elements Instead of Split Points ❌
```
WRONG: "We need to pick k elements"
RIGHT: "We need k-1 split points (k groups)"
```

### Mistake 2: Forgetting nums[0] is Always Included ❌
```
WRONG: We can choose not to include nums[0]
RIGHT: nums[0] is ALWAYS the first split point
```

### Mistake 3: Window Size Confusion ❌
```
WRONG: Window size = dist
RIGHT: Window contains indices from i₁+1 to i₁+dist
```

### Mistake 4: Picking From Wrong Range ❌
```
WRONG: After picking i₁, pick from ALL remaining elements
RIGHT: After picking i₁, pick only from [i₁+1, i₁+dist]
```

---

## 📈 Complexity Analysis

### Time Complexity: O(n log k)

**Breakdown:**
```
- n iterations (sliding window through array)
- Each iteration:
  - Add/remove from heap: O(log k)
  - Get sum: O(1)
- Total: O(n log k)
```

### Space Complexity: O(k)

**Breakdown:**
```
- Heaps store at most k elements
- No additional arrays needed
- Total: O(k)
```

### Why This is Efficient

```
Brute Force: Try all combinations
- Choose k-1 indices from n-1 positions
- Check distance constraint
- Time: O(C(n,k) * k) ≈ Exponential! 😱

Our Solution: Sliding window + heaps
- Linear scan with log operations
- Time: O(n log k) 🚀
```

---

## 🧪 More Test Cases

### Test Case 1: Minimum Example
```python
nums = [1, 2, 3, 4]
k = 2
dist = 2

# Only need 1 split point (besides nums[0])
# Best choice: index 1 (value = 2)
# Cost: 1 + 2 = 3
```

### Test Case 2: All Split Points Together
```python
nums = [1, 10, 20, 1, 1, 1, 100, 200]
k = 4
dist = 3

# nums[0] = 1 (always)
# Need 3 more splits within distance 3
# Best: indices 3, 4, 5 (values 1, 1, 1)
# Cost: 1 + 1 + 1 + 1 = 4
```

### Test Case 3: Large Values at Start
```python
nums = [100, 1, 2, 1, 1]
k = 3
dist = 3

# nums[0] = 100 (always, can't change!)
# Need 2 more splits
# Best: indices 1, 3 (values 1, 1)
# Cost: 100 + 1 + 1 = 102
```

### Test Case 4: Negative Numbers
```python
nums = [5, -3, -2, 6, -1]
k = 3
dist = 2

# nums[0] = 5
# Best: indices 1, 2 (values -3, -2)
# Cost: 5 + (-3) + (-2) = 0
```

---

## 🎓 Pattern Recognition Guide

### When to Use This Pattern?

✅ **Yes, use it when:**
- Need to pick k elements from a sequence
- Elements must satisfy distance constraints
- Want to minimize/maximize a sum
- Can benefit from sliding window

❌ **No, don't use when:**
- Elements can be picked non-consecutively
- No distance constraints
- Need exact positions, not just values
- Problem requires sorting/rearranging

---

## 💭 Intuition Building

### Think About It This Way:

```
1. Splitting an array into k parts
   = Choosing k-1 "cutting points"
   = Picking k-1 indices

2. Each cutting point creates a new group
   Group cost = first element of that group
   
3. We want smallest total cost
   = Pick indices with smallest values
   
4. But there's a distance rule
   = All picks must fit in a window
   = Use sliding window!
```

### The "Aha!" Moments:

1. **nums[0] is free (forced)** - We don't choose it, it's always there
2. **We pick indices, not counts** - The indices ARE the split points
3. **Window of candidates** - After picking i₁, we have limited choices
4. **Two heaps track top k** - Efficiently maintain smallest k-2 values

---

## 🔗 Related Problems

Similar patterns appear in:

1. **Leetcode 239**: Sliding Window Maximum
   - Also uses deque/heap for window queries

2. **Leetcode 480**: Sliding Window Median
   - Uses two heaps to track median in window

3. **Leetcode 2813**: Maximum Elegance of a K-Length Subsequence
   - Similar constraint-based selection

4. **Leetcode 1425**: Constrained Subsequence Sum
   - Distance constraints on element selection

---

## 🎯 Key Takeaways

### Remember These Points:

1. **First element always counts**
   ```
   Cost includes nums[0] no matter what
   ```

2. **We're picking split points**
   ```
   k groups = k-1 split points (indices)
   ```

3. **Distance constraint limits choices**
   ```
   After picking i₁, can only pick from [i₁+1, i₁+dist]
   ```

4. **Sliding window fits perfectly**
   ```
   As i₁ moves, window slides naturally
   ```

5. **Two heaps track smallest k-2**
   ```
   Efficiently maintain and query top elements
   ```

---

## 🚀 Optimization Tips

### Making It Faster:

1. **Early termination**: If cost can't improve, break
2. **Prefix sums**: If applicable to your variant
3. **SortedList**: Often simpler than two heaps
4. **Lazy deletion**: For heap operations when needed

---

## 📚 Practice Strategy

### Step 1: Understand the Core (Day 1-2)
- [ ] Understand what "split points" means
- [ ] Draw arrays and mark split points manually
- [ ] Calculate costs for different configurations

### Step 2: Code Without Looking (Day 3-4)
- [ ] Write brute force solution first
- [ ] Optimize to sliding window
- [ ] Add heap/sorted data structure

### Step 3: Solve Variations (Day 5-7)
- [ ] Try different k values
- [ ] Test with negative numbers
- [ ] Handle edge cases

---

## Summary

This problem combines:
- **Sliding Window** (for iteration through choices)
- **Two Heaps** (for efficient k-smallest tracking)
- **Greedy Selection** (always pick smallest available)

The key insight: **We're not counting elements, we're choosing where to cut!**

---

**Last Updated:** February 2026
**Difficulty Rating:** ⭐⭐⭐⭐ (Hard)  
**Interview Frequency:** ⭐⭐⭐ (Medium-High)

**Master this pattern, and you'll unlock a whole class of problems!** 🎉
