# Pattern 2: Two Pointers (Same Direction / Fast-Slow)

## When to Use

- Remove duplicates in-place
- Linked list cycle detection
- Find middle of linked list

## Template

```javascript
// Remove duplicates
function removeDuplicates(arr) {
  let slow = 0;

  for (let fast = 1; fast < arr.length; fast++) {
    if (arr[fast] !== arr[slow]) {
      slow++;
      arr[slow] = arr[fast];
    }
  }
  return slow + 1;
}

// Cycle detection
function hasCycle(head) {
  let slow = head,
    fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```
