# 3379. Transformed Array

## Problem Statement

You are given an integer array `nums` that represents a circular array. Your task is to create a new array `result` of the same size, following these rules:

For each index `i` (where `0 <= i < nums.length`), perform the following independent actions:

1.  If `nums[i] > 0`: Start at index `i` and move `nums[i]` steps to the right in the circular array. Set `result[i]` to the value of the index where you land.
2.  If `nums[i] < 0`: Start at index `i` and move `abs(nums[i])` steps to the left in the circular array. Set `result[i]` to the value of the index where you land.
3.  If `nums[i] == 0`: Set `result[i]` to `nums[i]`.

Return the new array `result`.

**Note:** Since `nums` is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

## Pattern Analysis

This problem follows the **Simulation** or **Array Transformation** pattern.

The core challenge is handling the **circular indexing**.

Given an array of size `n` and a current index `i`:

- Moving `k` steps to the right means the new index is `(i + k) % n`.
- Moving `k` steps to the left means the new index is `(i - k) % n`.

In this problem, `nums[i]` represents the steps.

- If `nums[i] > 0`, we move right by `nums[i]`. destination = `(i + nums[i]) % n`.
- If `nums[i] < 0`, we move left by `abs(nums[i])`. destination = `(i + nums[i]) % n` (since adding a negative number is moving left).

Thus, for any `i`, the target index is simply:
`target_index = (i + nums[i]) % n`

**Important Note for Languages:**

- In **Python**, the `%` operator handles negative numbers such that the result is always synonymous with the modulus in math (same sign as the divisor `n`). So `(i + nums[i]) % n` works correctly for negative `nums[i]`.
- In **Java/C++**, `%` can return a negative value if the dividend is negative. To handle this, the standard formula is `((i + nums[i]) % n + n) % n`.

## Solution

```python
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            # Calculate the target index
            # Python modulo handles negative wrapping correctly
            # Example: i=0, nums[i]=-2, n=5. (0 + -2) % 5 = -2 % 5 = 3.
            # Correct behavior: moving 2 left from 0 lands on 4 -> 3.
            # Wait, moving 1 left from 0 is 4. Moving 2 left is 3. Yes.

            target_index = (i + nums[i]) % n
            result[i] = nums[target_index]

        return result
```

## Complexity Analysis

- **Time Complexity:** O(N), where N is the length of `nums`. We iterate through the array once.
- **Space Complexity:** O(N) to store the `result` array. (or O(1) auxiliary space if we don't count the output).
