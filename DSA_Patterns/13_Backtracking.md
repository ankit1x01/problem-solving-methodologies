# Pattern 13: Backtracking

## When to Use

- Generate all possibilities
- Subsets, permutations, combinations
- Constraint satisfaction

## Template

```javascript
function backtrack(result, current, choices, start) {
    // Base case: found a valid solution
    if (/* solution complete */) {
        result.push([...current]);
        return;
    }

    for (let i = start; i < choices.length; i++) {
        // Skip duplicates (if needed)
        if (i > start && choices[i] === choices[i - 1]) continue;

        // Make choice
        current.push(choices[i]);

        // Recurse
        backtrack(result, current, choices, i + 1);  // i+1 for combinations
        // backtrack(result, current, choices, i);   // i for unlimited use
        // backtrack(result, current, remaining, 0); // For permutations

        // Undo choice
        current.pop();
    }
}
```

## Subsets

```javascript
function subsets(nums) {
  const result = [];

  function backtrack(start, current) {
    result.push([...current]);

    for (let i = start; i < nums.length; i++) {
      current.push(nums[i]);
      backtrack(i + 1, current);
      current.pop();
    }
  }

  backtrack(0, []);
  return result;
}
```

## Permutations

```javascript
function permute(nums) {
  const result = [];

  function backtrack(current, remaining) {
    if (remaining.length === 0) {
      result.push([...current]);
      return;
    }

    for (let i = 0; i < remaining.length; i++) {
      current.push(remaining[i]);
      backtrack(current, [...remaining.slice(0, i), ...remaining.slice(i + 1)]);
      current.pop();
    }
  }

  backtrack([], nums);
  return result;
}
```
