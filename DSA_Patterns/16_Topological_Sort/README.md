# Pattern 16: Topological Sort

## When to Use

- Task scheduling with dependencies
- Course prerequisites
- Build order

## Template (Kahn's Algorithm - BFS)

```javascript
function topologicalSort(n, edges) {
  const graph = Array.from({ length: n }, () => []);
  const inDegree = new Array(n).fill(0);

  for (const [from, to] of edges) {
    graph[from].push(to);
    inDegree[to]++;
  }

  const queue = [];
  for (let i = 0; i < n; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }

  const result = [];
  while (queue.length) {
    const node = queue.shift();
    result.push(node);

    for (const neighbor of graph[node]) {
      inDegree[neighbor]--;
      if (inDegree[neighbor] === 0) queue.push(neighbor);
    }
  }

  return result.length === n ? result : []; // Empty if cycle
}
```
