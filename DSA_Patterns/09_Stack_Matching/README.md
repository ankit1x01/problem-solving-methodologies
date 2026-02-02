# Pattern 9: Stack (Matching/Nesting)

## When to Use

- Parentheses matching
- Expression evaluation
- Nested structures

## Template

```javascript
function validParentheses(s) {
  const stack = [];
  const pairs = { ")": "(", "]": "[", "}": "{" };

  for (const char of s) {
    if ("([{".includes(char)) {
      stack.push(char);
    } else {
      if (stack.pop() !== pairs[char]) return false;
    }
  }
  return stack.length === 0;
}
```
