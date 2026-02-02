# Pattern 11: BFS (Level-Order / Shortest Path)

## When to Use

- Shortest path in unweighted graph
- Level-order tree traversal
- Multi-source BFS

## Template

```javascript
function bfs(graph, start) {
  const visited = new Set([start]);
  const queue = [start];
  let level = 0;

  while (queue.length) {
    const levelSize = queue.length;

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();

      // Process node

      for (const neighbor of graph[node]) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
        }
      }
    }
    level++;
  }
  return level;
}
```
