# Pattern 1: Two Pointers (Opposite Direction)

## When to Use

- Sorted array + find pairs
- Palindrome check
- Container with most water

## Template

```javascript
function twoPointers(arr) {
    let left = 0, right = arr.length - 1;

    while (left < right) {
        // Process current pair
        const sum = arr[left] + arr[right];

        if (/* condition met */) {
            return [left, right];
        } else if (/* need bigger */) {
            left++;
        } else {
            right--;
        }
    }
    return -1;
}
```

## Sample Problems

- Two Sum II (sorted)
- 3Sum
- Container With Most Water
- Trapping Rain Water
