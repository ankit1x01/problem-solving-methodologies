# 🐢 Pattern 2: Two Pointers (Same Direction)

## 🎯 Think Like a 5-Year-Old

Imagine a race between a **Tortoise (Slow)** and a **Hare (Fast)**! 🐢🐇

They both start at the same spot.

- The **Hare** runs very fast (jumping 2 steps at a time).
- The **Tortoise** walks slowly (taking 1 step at a time).

If they are running on a **straight** road, the Hare will reach the finish line first and the Tortoise will be left behind in the middle.

But if they are running on a **circular** track (a loop), the Hare will eventually catch up to the Tortoise from behind! 😲

**This helps us find two things:**

1.  **Middle of a line:** When the Hare finishes, the Tortoise is exactly in the middle!
2.  **Circles (Loops):** If they meet again, we know it's a circle!

---

## 🧹 Real Life Example 1: The Cleanup Crew

Imagine you have a row of toys, but some are broken (zeros) and you want to move all good toys to the front.

**The Team:**

- **The Scout (Fast Pointer):** Runs ahead to check every toy. "Is this one good? Is this one broken?"
- **The Builder (Slow Pointer):** Stays back and only accepts good toys from the Scout.

**Action:**

1.  Scout finds a good toy -> Tosses it to Builder -> Builder places it and moves one step.
2.  Scout finds a broken toy -> Ignores it and keeps running.

By the end, all good toys are packed tightly at the start!

---

## 🐢 Real Life Example 2: The Middle of the Train

You have a very long train and you want to find the middle carriage, but you can't count the total number first.

**Trick:**
Send two people walking down the train starting at the engine.

- Person A walks **1** carriage at a time.
- Person B runs **2** carriages at a time.

When Person B hits the end of the train, Person A will be magically standing in the **exact middle**! 🚂

---

## 🎬 Animated Visualization

### 1. Removing Duplicates (Sorted Array)

`[1, 1, 2, 3, 3, 4]`

```
Initial State:
Slow (S) 👇
Fast (F) 👇
        [1, 1, 2, 3, 3, 4]

Step 1 (F moves, checks overlap):
         👇 S
            👇 F (Same as S? Yes. Ignore.)
        [1, 1, 2, 3, 3, 4]

Step 2 (F finds new value):
         👇 S
               👇 F (Different! Copy 2 to S+1, move S)
        [1, 2, 2, 3, 3, 4]
            👆 (Changed)

Step 3 (F finds new value):
            👇 S
                  👇 F (Different! Copy 3 to S+1, move S)
        [1, 2, 3, 3, 3, 4]
               👆 (Changed)
```

### 2. Cycle Detection (The Chase)

Nodes: `1 -> 2 -> 3 -> 4 -> 5 -> 3 (Loop back)`

```
Start: T @ 1, H @ 1
Skip 1: T @ 2, H @ 3
Skip 2: T @ 3, H @ 5
Skip 3: T @ 4, H @ 2 (looped)
Skip 4: T @ 5, H @ 4
Skip 5: T @ 3, H @ 3 (CAUGHT UP! 💥)
```

---

## 🎯 Why Use This Pattern?

### The Speed Difference (Finding Middle)

**The Slow Way (Count First):**

1.  Walk to end to count N = 100.
2.  Walk back to start.
3.  Walk to N/2 = 50.
    **Total steps:** 150 (Too much walking!) 😓

**The Fast Way (Two Pointers):**

1.  Walk Fast and Slow together.
2.  Fast reaches end (100 steps). Slow is at 50.
    **Total steps:** 100 (Done in one pass!) 🚀

### Benefits

- ⚡ **Super Fast:** O(N) time complexity.
- 💾 **Saves Memory:** O(1) space (no extra lists or arrays needed).
- 🔄 **In-Place:** Modifies arrays without making copies.

---

## 🔢 Complexity Analysis (Explained Simply)

**Time Complexity: O(N)**

```
We walk through the list/array at most once or twice.
Even if Fast goes 2x speed, it's still linear time!
```

**Space Complexity: O(1)**

```
We only need two variables:
- slow
- fast
No matter how big the input is, we only need these 2 pointers!
```

---

## 📝 How Does It Work? (Algorithm Steps)

### Cycle Detection Strategy

```
1. 🏁 INITIALIZE
   - Set slow = head
   - Set fast = head

2. 🔄 LOOP while fast is not at end
   - Move slow 1 step (slow = slow.next)
   - Move fast 2 steps (fast = fast.next.next)

3. 🕵️ CHECK
   - If slow == fast: Cycle found! Return True.

4. 🔚 FINISH
   - If fast reaches null: No cycle. Return False.
```

---

## 💻 Code Templates

### JavaScript Template

```javascript
/* 1. Cycle Detection (Linked List) */
function hasCycle(head) {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next; // 1 step
    fast = fast.next.next; // 2 steps

    if (slow === fast) return true; // Collision!
  }
  return false; // Reached end
}

/* 2. Remove Duplicates (Array) */
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;

  let slow = 0;
  for (let fast = 1; fast < nums.length; fast++) {
    if (nums[fast] !== nums[slow]) {
      slow++;
      nums[slow] = nums[fast]; // Capture unique value
    }
  }
  return slow + 1; // Length of unique part
}
```

### Python Template

```python
# 1. Cycle Detection
def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next      # 1 step
        fast = fast.next.next # 2 steps

        if slow == fast:
            return True

    return False

# 2. Remove Duplicates
def remove_duplicates(nums):
    if not nums: return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

### C++ Template

```cpp
// 1. Cycle Detection
bool hasCycle(ListNode *head) {
    ListNode *slow = head;
    ListNode *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) return true;
    }
    return false;
}

// 2. Remove Duplicates
int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0;

    int slow = 0;
    for (int fast = 1; fast < nums.size(); fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    return slow + 1;
}
```

---

## 🌍 More Real-Life Analogies

### 🎨 The Painter and The Inspector

One person (Inspector/Fast) scans the wall for cracks. The second person (Painter/Slow) only comes over when a crack is found to fix it. This effectively compacts the "work" into a list of fixed spots.

### 🏃‍♂️ Running Track Laps

Often in long races, the leader "laps" the slower runners. If you are watching a race on a loop and see runner A pass runner B, you know runner A has completed a full extra cycle!

---

## 🎯 How to Identify These Problems?

### ✅ Look for These Clues

| Clue                | Example                                           |
| ------------------- | ------------------------------------------------- |
| Cycle/Loop          | "Determine if linked list has a cycle"            |
| Middle Element      | "Find middle node of linked list"                 |
| In-place Operations | "Remove duplicates in-place", "Move zeros to end" |
| Intersection        | "Find intersection of two linked lists"           |
| Duplicate Rejection | "Remove element equal to val"                     |

---

## ⚠️ Common Mistakes & How to Avoid Them

### Mistake 1: Not Checking Null for Fast Pointer ❌

```python
# WRONG!
while slow != fast:
    slow = slow.next
    fast = fast.next.next # Crash if fast is None!
```

**Fix:** Always check `fast` and `fast.next` boundaries.

```python
while fast and fast.next: ...
```

### Mistake 2: Returning Wrong Value (Array) ❌

```javascript
return slow; // Often returns index, but length is index + 1
```

**Fix:** Usually return `slow + 1` for length.

### Mistake 3: Infinite Loops ❌

If you don't advance the pointers correctly inside the loop, they might stay stuck forever. Make sure `fast` is actually moving faster than `slow`.

---

## 🧮 Detailed Problem Examples

### Problem 1: Linked List Cycle (LeetCode 141)

**Goal:** Return `true` if there is a cycle.

**Logic:**
If there is no cycle, `fast` will eventually hit `null` (the finish line).
If there is a cycle, `fast` will circle back and collide with `slow`.

### Problem 2: Middle of the Linked List (LeetCode 876)

**Goal:** Find the middle node.

**Logic:**
When `fast` reaches the end (`null`), `slow` has taken exactly half the number of steps.
Distance(Fast) = 2 _ Distance(Slow)
Total Length = 2 _ Distance(Slow)
Therefore, Slow is at Length / 2.

### Problem 3: Move Zeroes (LeetCode 283)

**Goal:** Move all 0s to end, keep order of non-zeros.

**Solution:**
`Slow` marks the position of the last "non-zero" found.
`Fast` scans for new non-zeros.
When `Fast` finds a non-zero, swap it with `Slow` and advance `Slow`.

```python
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

---

## 📚 Classic LeetCode Problems

| #   | Problem                                                                                                   | Difficulty | Key Concept              |
| --- | --------------------------------------------------------------------------------------------------------- | ---------- | ------------------------ |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)                                     | Easy       | Basic Fast/Slow          |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)                               | Medium     | Find start of cycle      |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)                     | Easy       | Runner technique         |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/)                                               | Easy       | Implicit cycle detection |
| 26  | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy       | In-place array mod       |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)                     | Medium     | Cycle detection in array |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                           | Easy       | Find middle + Reverse    |

---

## 💡 Pro Tips & Tricks

### Tip 1: Finding Cycle Start

If a cycle is found:

1. Reset `slow` to `head`.
2. Keep `fast` where they met.
3. Move both 1 step at a time.
4. The point where they meet again is the **Cycle Start Node**! 🤯

### Tip 2: Determine Cycle Length

Once they meet, keep `slow` stationary and move `fast` until it comes back to `slow`, counting the steps. That count is the cycle length.

---

## 🧠 Mental Model: The Elastic Band

Think of two beads on a string.

- Bead 1 (Slow) is heavy and moves 1 inch/sec.
- Bead 2 (Fast) is light and moves 2 inches/sec.
  If the string is straight, Bead 2 flies off the end.
  If the string is a necklace (loop), Bead 2 will lap Bead 1 eventually.

---

## 🎯 Quick Reference Cheat Sheet

```python
# TEMPLATE: LINKED LIST CYCLE
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

# TEMPLATE: ARRAY FILTERING
def filterArray(nums):
    slow = 0
    for fast in range(len(nums)):
        if condition(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1
    return slow # New length
```

---

## 🌟 Summary for Kids

### What We Learned:

1. 🐇 **Fast & Slow:** Uses two runners at different speeds.
2. 🔄 **Cycles:** Best way to find loops in a path.
3. 🧹 **Cleanup:** Great for removing bad items from a list.
4. ⚡ **Efficient:** Solves tricky problems in one pass!

### Remember This:

> "If you run in circles, the fast runner always catches the slow walker!" 🏃‍♂️🚶

---
