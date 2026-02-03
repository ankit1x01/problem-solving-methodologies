# Trionic Array

## Problem Statement

You are given an integer array `nums` of length `n`.

An array is **trionic** if there exist indices `0 < p < q < n − 1` such that:

1.  `nums[0...p]` is strictly increasing.
2.  `nums[p...q]` is strictly decreasing.
3.  `nums[q...n − 1]` is strictly increasing.

Return `true` if `nums` is trionic, otherwise return `false`.

### Examples

**Example 1:**

```text
Input: nums = [1,3,5,4,2,6]
Output: true
Explanation:
Pick p = 2, q = 4:
nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
```

**Example 2:**

```text
Input: nums = [2,1,3]
Output: false
Explanation:
There is no way to pick p and q to form the required three segments.
```

### Constraints

- `3 <= n <= 100`
- `-1000 <= nums[i] <= 1000`

## Pattern Analysis

This problem follows the **Two Pointers (Same Direction)** or **Linear Scan** pattern.

We are essentially looking for two specific "turning points" or "peaks/valleys" in the array:

1.  A **Peak** at index `p` (where the array stops increasing and starts decreasing).
2.  A **Valley** at index `q` (where the array stops decreasing and starts increasing).

We can simulate this by traversing the array with a single pointer (index `i`) and checking for the three required phases sequentially.

**Phases:**

1.  **Phase 1 (Increasing):** Move `i` forward as long as `nums[i] < nums[i+1]`.
2.  **Phase 2 (Decreasing):** From the point `p`, move `i` forward as long as `nums[i] > nums[i+1]`.
3.  **Phase 3 (Increasing):** From the point `q`, move `i` forward as long as `nums[i] < nums[i+1]`.

If we successfully complete all three phases and reach the end of the array, the array is trionic.

## Solution

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
             # Minimum length must be 4 to satisfy 0 < p < q < n-1?
             # Let's check indices:
             # If n=3, indices are 0, 1, 2.
             # 0 < p < q < 2 implies p=1. Then 1 < q < 2 implies no integer q.
             # So minimum length is indeed 4?
             # Wait, strict inequalities:
             # 0 < p (min p=1)
             # p < q (min q=2)
             # q < n-1 (min n-1 = 3 => n=4)
             # So yes, n must be at least 4.
             # Actually let's re-read constraints. 0 < p < q < n-1.
             # Smallest valid indices: p=1, q=2, n-1=3 => n=4.
             # Example: [1, 2, 1, 2] -> p=1, q=2. Valid.
             return False

        i = 0

        # Phase 1: Strictly increasing
        # We must take at least one step, so we track start.
        start_p = i
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        p = i

        # Check if we actually ascended and didn't reach the end or stop immediately
        if p == start_p or p == n - 1:
            return False

        # Phase 2: Strictly decreasing
        start_q = i
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
        q = i

        # Check if we actually descended
        if q == start_q or q == n - 1:
            return False

        # Phase 3: Strictly increasing
        start_end = i
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1

        # Check if we successfully increased to the end
        # We must have increased at least once
        if i == start_end:
            return False

        # Must reach the end of the array
        return i == n - 1

```

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of `nums`. We traverse the array exactly once.
- **Space Complexity:** O(1), as we only use a few variables for indices.
