# Pattern 3: Sliding Window (Fixed Size)

## When to Use

- Maximum/minimum of subarray of size K
- Average of subarray of size K

## Template

```javascript
function slidingWindowFixed(arr, k) {
  let windowSum = 0,
    maxSum = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    windowSum += arr[i]; // Add right element

    if (i >= k - 1) {
      maxSum = Math.max(maxSum, windowSum);
      windowSum -= arr[i - k + 1]; // Remove left element
    }
  }
  return maxSum;
}
```
