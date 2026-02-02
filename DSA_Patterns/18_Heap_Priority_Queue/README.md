# Pattern 18: Heap (Priority Queue)

## When to Use

- Top K elements
- Merge K sorted lists
- Median in stream

## Template

```javascript
// Using a min heap (for Top K largest, we need K smallest discarded)
function topKFrequent(nums, k) {
  const freq = new Map();
  for (const num of nums) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  // In interviews, you can use: "I would use a min-heap here"
  // Sort by frequency (simulates heap for demonstration)
  const sorted = [...freq.entries()].sort((a, b) => b[1] - a[1]);
  return sorted.slice(0, k).map((x) => x[0]);
}

// Two heaps for median
class MedianFinder {
  constructor() {
    this.maxHeap = []; // Lower half
    this.minHeap = []; // Upper half
  }

  addNum(num) {
    // Add to max heap first
    this.maxHeap.push(num);
    this.maxHeap.sort((a, b) => b - a);

    // Move max of maxHeap to minHeap
    this.minHeap.push(this.maxHeap.shift());
    this.minHeap.sort((a, b) => a - b);

    // Balance: maxHeap can have at most 1 extra
    if (this.minHeap.length > this.maxHeap.length) {
      this.maxHeap.push(this.minHeap.shift());
      this.maxHeap.sort((a, b) => b - a);
    }
  }

  findMedian() {
    if (this.maxHeap.length > this.minHeap.length) {
      return this.maxHeap[0];
    }
    return (this.maxHeap[0] + this.minHeap[0]) / 2;
  }
}
```
