# Pattern 8: Hash Map (Frequency Count)

## When to Use

- Two Sum
- Anagrams
- Frequency problems

## Template

```javascript
// Two Sum
function twoSum(nums, target) {
  const seen = new Map();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }
    seen.set(nums[i], i);
  }
  return [-1, -1];
}

// Character frequency
function charFrequency(str) {
  const freq = new Map();
  for (const char of str) {
    freq.set(char, (freq.get(char) || 0) + 1);
  }
  return freq;
}
```
