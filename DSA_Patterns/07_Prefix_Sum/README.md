# Pattern 7: Prefix Sum

## When to Use

- Range sum queries
- Subarray sum equals K

## Template

```javascript
// Build prefix sum
function buildPrefixSum(arr) {
  const prefix = [0];
  for (const num of arr) {
    prefix.push(prefix[prefix.length - 1] + num);
  }
  return prefix;
}

// Range sum [i, j] inclusive
function rangeSum(prefix, i, j) {
  return prefix[j + 1] - prefix[i];
}

// Subarray Sum Equals K
function subarraySum(nums, k) {
  const prefixCount = new Map([[0, 1]]);
  let sum = 0,
    count = 0;

  for (const num of nums) {
    sum += num;
    if (prefixCount.has(sum - k)) {
      count += prefixCount.get(sum - k);
    }
    prefixCount.set(sum, (prefixCount.get(sum) || 0) + 1);
  }
  return count;
}
```
