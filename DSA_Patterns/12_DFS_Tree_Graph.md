# Pattern 12: DFS (Path Finding / Tree Traversal)

## When to Use

- Path exists?
- All paths
- Tree problems

## Template

```javascript
// Iterative DFS
function dfsIterative(graph, start) {
  const visited = new Set();
  const stack = [start];

  while (stack.length) {
    const node = stack.pop();
    if (visited.has(node)) continue;
    visited.add(node);

    // Process node

    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        stack.push(neighbor);
      }
    }
  }
}

// Recursive DFS (Tree)
function treeDfs(root) {
  if (!root) return;

  // Pre-order: process before children
  treeDfs(root.left);
  // In-order: process between children
  treeDfs(root.right);
  // Post-order: process after children
}
```
