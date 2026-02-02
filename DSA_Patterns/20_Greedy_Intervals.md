# Pattern 20: Greedy (Interval Problems)

## When to Use

- Interval scheduling
- Task assignment
- Activity selection

## Template

```javascript
// Merge Intervals
function merge(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const result = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const last = result[result.length - 1];
    const curr = intervals[i];

    if (curr[0] <= last[1]) {
      last[1] = Math.max(last[1], curr[1]);
    } else {
      result.push(curr);
    }
  }
  return result;
}

// Meeting Rooms (check overlap)
function canAttend(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < intervals[i - 1][1]) {
      return false;
    }
  }
  return true;
}

// Meeting Rooms II (min rooms needed)
function minMeetingRooms(intervals) {
  const starts = intervals.map((i) => i[0]).sort((a, b) => a - b);
  const ends = intervals.map((i) => i[1]).sort((a, b) => a - b);

  let rooms = 0,
    endPtr = 0;
  for (const start of starts) {
    if (start < ends[endPtr]) {
      rooms++;
    } else {
      endPtr++;
    }
  }
  return rooms;
}
```
