# Pattern 6: Binary Search on Answer

## When to Use

- "Minimum/maximum value that satisfies condition"
- Optimization problems with monotonic property

## Template

```javascript
function binarySearchOnAnswer(lo, hi, condition) {
  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2);

    if (condition(mid)) {
      hi = mid; // For minimum satisfying
      // lo = mid + 1; // For maximum satisfying
    } else {
      lo = mid + 1; // For minimum satisfying
      // hi = mid;     // For maximum satisfying
    }
  }
  return lo;
}

// Example: Koko Eating Bananas
function minEatingSpeed(piles, h) {
  let lo = 1,
    hi = Math.max(...piles);

  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2);
    const hours = piles.reduce((sum, pile) => sum + Math.ceil(pile / mid), 0);

    if (hours <= h) hi = mid;
    else lo = mid + 1;
  }
  return lo;
}
```
