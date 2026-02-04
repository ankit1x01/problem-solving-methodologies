# Max Trionic Subarray Sum

## Problem Statement

You are given an integer array `nums` of length `n`.

A **trionic subarray** is a contiguous subarray `nums[l...r]` (with `0 <= l < r < n`) for which there exist indices `l < p < q < r` such that:

1. `nums[l...p]` is strictly increasing.
2. `nums[p...q]` is strictly decreasing.
3. `nums[q...r]` is strictly increasing.

Return the _maximum sum_ of any trionic subarray in `nums`.

### Example 1

**Input:** `nums = [0,-2,-1,-3,0,2,-1]`
**Output:** `-4`
**Explanation:**
Pick `l = 1, p = 2, q = 3, r = 5`:

- `nums[l...p] = [-2, -1]` is strictly increasing.
- `nums[p...q] = [-1, -3]` is strictly decreasing.
- `nums[q...r] = [-3, 0, 2]` is strictly increasing.
  Sum = `(-2) + (-1) + (-3) + 0 + 2 = -4`.

### Example 2

**Input:** `nums = [1,4,2,7]`
**Output:** `14`
**Explanation:**
Pick `l = 0, p = 1, q = 2, r = 3`:

- `nums[l...p] = [1, 4]` (inc)
- `nums[p...q] = [4, 2]` (dec)
- `nums[q...r] = [2, 7]` (inc)
  Sum = `1 + 4 + 2 + 7 = 14`.

### Constraints

- `4 <= n <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- It is guaranteed that at least one trionic subarray exists.

---

## Pattern Analysis

This problem is a variation of the **Maximum Subarray Sum** problem (Kadane’s Algorithm), combined with structural constraints. It belongs to the **Dynamic Programming (1D)** pattern, specifically involving **Multi-pass DP** or **State Decompostion**.

The structure is **Increase** $\to$ **Decrease** $\to$ **Increase**.
This creates a "W" shape (or "N" shape with an extra leg).
The shape is defined by two pivots, $p$ (peak) and $q$ (valley).

### Approach

We can think of this as connecting three components at indices $p$ and $q$.
To maximize the total sum efficiently, we can precompute the best "arms" for each potential pivot point.

1.  **L[p]**: Max sum of a strictly increasing subarray ending at index `p` (with length $\ge 2$).
2.  **R[q]**: Max sum of a strictly increasing subarray starting at index `q` (with length $\ge 2$).
3.  **M[q]**: Max sum of a combined shape (strictly increasing ending at some $p$ + strictly decreasing from $p$ to $q$) ending at $q$.

The answer will be $\max_q (M[q] + R[q] - \text{nums}[q])$.
_(We subtract `nums[q]` because it's included in both `M[q]` and `R[q]`)_.

### Algorithm Steps

1.  **Compute `L` array**:
    - Iterate `i` from 0 to `n-1`.
    - Track `inc[i]` (max sum increasing ending at `i`).
    - If `nums[i] > nums[i-1]`, extend `inc`. Else reset.
    - `L[i]` is valid only if `nums[i] > nums[i-1]` (ensures length $\ge 2$).

2.  **Compute `R` array**:
    - Iterate `i` from `n-1` down to 0.
    - Track `dec_rev[i]` (max sum increasing starting at `i`).
    - `R[i]` is valid only if `nums[i] < nums[i+1]` (ensures length $\ge 2$).

3.  **Compute `M` array**:
    - Iterate `i` from 0 to `n-1`.
    - If `nums[i] < nums[i-1]` (decreasing step):
      - We can extend an existing `M[i-1]`.
      - OR we can start the decreasing phase from a valid `L[i-1]`.
      - `M[i] = nums[i] + max(L[i-1], M[i-1])` (ignoring invalid components).
    - Else, `M[i]` is invalid (-infinity).

4.  **Compute Result**:
    - Iterate `q` from 0 to `n-1`.
    - If both `M[q]` and `R[q]` are valid, update global max with `M[q] + R[q] - nums[q]`.

## Code Implementation (Python)

```python
def maxTrionicSubarray(nums):
    n = len(nums)
    if n < 4:
        return 0 # Should not happen based on constraints

    INF = float('inf')

    # 1. Compute L[i]: Max strictly increasing subarray ending at i (len >= 2)
    # Helper: best_inc[i] is max increasing ending at i (len >= 1)
    best_inc = [0] * n
    L = [-INF] * n

    best_inc[0] = nums[0]
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            # Extend previous if positive contributions
            best_inc[i] = nums[i] + max(0, best_inc[i - 1])
            # To be a valid p (end of inc part), we need length >= 2
            # This is guaranteed if we extended (nums[i] > nums[i-1])
            # The sum is best_inc[i-1] + nums[i].
            # Note: best_inc[i-1] already maximizes strict inc ending at i-1.
            L[i] = best_inc[i - 1] + nums[i]
        else:
            best_inc[i] = nums[i]
            L[i] = -INF

    # 2. Compute R[i]: Max strictly increasing subarray starting at i (len >= 2)
    # Helper: best_inc_start[i] is max increasing starting at i (len >= 1)
    best_inc_start = [0] * n
    R = [-INF] * n

    best_inc_start[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            best_inc_start[i] = nums[i] + max(0, best_inc_start[i + 1])
            R[i] = nums[i] + best_inc_start[i + 1]
        else:
            best_inc_start[i] = nums[i]
            R[i] = -INF

    # 3. Compute M[i]: Inc (len>=2) + Dec (len>=2) ending at i
    # This represents the peak p and the descent to valley q=i
    M = [-INF] * n

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            # We are in a decreasing descent
            # Option 1: Continue descent from M[i-1]
            cand1 = M[i - 1] + nums[i] if M[i - 1] != -INF else -INF

            # Option 2: Start descent from a valid peak L[i-1]
            cand2 = L[i - 1] + nums[i] if L[i - 1] != -INF else -INF

            M[i] = max(cand1, cand2)
        else:
            M[i] = -INF

    # 4. Combine M[q] + R[q]
    max_sum = -INF
    for i in range(n):
        if M[i] != -INF and R[i] != -INF:
            # nums[i] is the valley, included in both M and R
            val = M[i] + R[i] - nums[i]
            if val > max_sum:
                max_sum = val

    return max_sum

# Example Usage
print(maxTrionicSubarray([0, -2, -1, -3, 0, 2, -1])) # Output: -4
print(maxTrionicSubarray([1, 4, 2, 7]))             # Output: 14
```
