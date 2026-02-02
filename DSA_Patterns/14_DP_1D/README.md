# Pattern 14: Dynamic Programming (1D)

## When to Use

- Optimization problems
- Counting problems
- Fibonacci-style recurrence

## Template

```javascript
// Bottom-up
function dp1D(n) {
    const dp = new Array(n + 1).fill(0);
    dp[0] = /* base case */;

    for (let i = 1; i <= n; i++) {
        dp[i] = /* transition from dp[i-1], dp[i-2], etc. */;
    }
    return dp[n];
}

// Space-optimized (when only using previous states)
function dp1DOptimized(n) {
    let prev2 = /* base for dp[0] */;
    let prev1 = /* base for dp[1] */;

    for (let i = 2; i <= n; i++) {
        const curr = prev1 + prev2;  // Example transition
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```
