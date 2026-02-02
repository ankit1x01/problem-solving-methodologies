# Pattern 5: Binary Search (Standard)

## When to Use

- Search in sorted array
- Find boundary (first/last occurrence)

## Template

```javascript
// Standard search
function binarySearch(arr, target) {
  let left = 0,
    right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}

// Find leftmost (first occurrence)
function leftBound(arr, target) {
  let left = 0,
    right = arr.length;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] < target) left = mid + 1;
    else right = mid;
  }
  return left;
}

// Find rightmost (last occurrence)
function rightBound(arr, target) {
  let left = 0,
    right = arr.length;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] <= target) left = mid + 1;
    else right = mid;
  }
  return left - 1;
}
```
