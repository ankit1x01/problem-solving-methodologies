# Pattern 4: Sliding Window (Variable Size)

## When to Use

- Longest/shortest subarray with condition
- Minimum window substring

## Template

```javascript
function slidingWindowVariable(arr, condition) {
    let left = 0, result = 0;
    let windowState = /* hash map, count, etc. */;

    for (let right = 0; right < arr.length; right++) {
        // Expand window: add arr[right] to state

        while (/* window invalid */) {
            // Shrink window: remove arr[left] from state
            left++;
        }

        // Update result
        result = Math.max(result, right - left + 1);
    }
    return result;
}
```

## The Key Insight

- Expand right when window valid
- Shrink left when window invalid
- Update result at each valid state
