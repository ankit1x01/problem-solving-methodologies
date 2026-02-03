
# 🪟 Pattern 3: Sliding Window (Fixed Size)

## 🎯 Think Like a 5-Year-Old

Imagine you're at a toy store, and there's a long shelf with toys. You have a special box that can hold exactly 3 toys. You want to find which 3 toys next to each other cost the most money.

**The Slow Way (Wrong!):** Pick first 3 toys, add prices. Move to toy 2, 3, 4... add all 3 prices again from scratch. This is VERY slow! 😫

**The Smart Way (Sliding Window!):** 
- First, add prices of toy 1, 2, 3.
- Move box one step: Remove toy 1's price, add toy 4's price.
- Keep sliding until you reach the end!

This is SO MUCH FASTER! 🚀

---

## 🍬 Real Life Example 1: The Candy Store

You have a row of candies with "yumminess" points:

```
Index:  0   1    2   3   4
Value: | 5 | 2 | -1 | 0 | 3 |
```

**Mission:** Find the yummiest 3 candies in a row! (Window size = 3)

### Step-by-Step Animation

**Initial Window (indices 0, 1, 2):**
```
     👇 Window Start
    ┌───┬───┬───┐
    │ 5 │ 2 │-1 │ 0 │ 3 │
    └───┴───┴───┘
        └─────┘ Window
    
    Calculation: 5 + 2 + (-1) = 6
    Max so far: 6 ✨
```

**Slide Right (indices 1, 2, 3):**
```
         👇 Remove 5, Add 0
        ┌───┬───┬───┐
    │ 5 │ 2 │-1 │ 0 │ 3 │
        └───┴───┴───┘
    
    Old sum: 6
    Remove left (5): 6 - 5 = 1
    Add right (0): 1 + 0 = 1
    Max so far: 6 (unchanged)
```

**Slide Right Again (indices 2, 3, 4):**
```
             👇 Remove 2, Add 3
            ┌───┬───┬───┐
    │ 5 │ 2 │-1 │ 0 │ 3 │
            └───┴───┴───┘
    
    Old sum: 1
    Remove left (2): 1 - 2 = -1
    Add right (3): -1 + 3 = 2
    Max so far: 6 (unchanged)
```

**Answer: 6** 🎉

---

## 🚌 Real Life Example 2: The School Bus

A bus has 9 seats with happiness scores:

```
Seat:    1   2   3   4   5   6   7   8   9
Happy:  [3] [5] [2] [6] [1] [4] [1] [8] [2]
```

**Goal:** Find the happiest group of 4 kids sitting together (k = 4)

```
Window 1: [3][5][2][6]_ _ _ _ _  → Sum = 16
Window 2:  _[5][2][6][1]_ _ _ _  → Sum = 14
Window 3:  _ _[2][6][1][4]_ _ _  → Sum = 13
Window 4:  _ _ _[6][1][4][1]_ _  → Sum = 12
Window 5:  _ _ _ _[1][4][1][8]_  → Sum = 14
Window 6:  _ _ _ _ _[4][1][8][2] → Sum = 15

Maximum happiness: 16 in Window 1!
```

---

## 🎬 Animated Visualization

Think of it like a camera frame moving across a scene:

```
Frame (Window) of size 3:

Time 1:  [📷____] _ _ _ _    Looking at first 3
Time 2:  _ [📷____] _ _ _    Slide right by 1
Time 3:  _ _ [📷____] _ _    Slide right by 1
Time 4:  _ _ _ [📷____] _    Slide right by 1
Time 5:  _ _ _ _ [📷____]    Slide right by 1
```

Each time you slide, you only update 2 things:
- ➖ Remove what left the frame
- ➕ Add what entered the frame

---

## 🎯 Why Use Sliding Window?

### The Speed Difference

**Without Sliding Window (Slow Method):**
```
For window 1: Add 3 numbers → 3 operations
For window 2: Add 3 numbers → 3 operations  
For window 3: Add 3 numbers → 3 operations
...
Total: n × k operations 😰
```

**With Sliding Window (Fast Method):**
```
For window 1: Add 3 numbers → 3 operations
For window 2: Remove 1, Add 1 → 2 operations
For window 3: Remove 1, Add 1 → 2 operations
...
Total: k + 2(n-k) = 2n - k operations 🚀
```

### Benefits
- ⚡ **Super Fast:** Turns O(n×k) into O(n)
- 💾 **Saves Memory:** Only track current window
- 🎯 **Works For:**
  - Maximum/minimum sum of subarray of size K
  - Average of subarray of size K
  - Count/frequency in every window of size K
  - Any aggregate operation on fixed-size windows

---

## 🔢 Complexity Analysis (Explained Simply)

**Time Complexity: O(n)** where n = array length
```
Why? We visit each element exactly once!
👉 Element enters window → Process once
👉 Element leaves window → Process once
Total: 2n operations = O(n)
```

**Space Complexity: O(1)**
```
We only store:
- windowSum (or similar aggregate)
- maxSum (or result)
- A few index variables
No extra arrays needed!
```

---

## 📝 How Does It Work? (Algorithm Steps)

### Step-by-Step Process

```
1. 🏁 INITIALIZE
   - Set windowSum = 0
   - Set result = minimum/maximum possible value
   - Set start pointer = 0

2. 🔄 LOOP through array (let i = 0 to n-1)
   - Add arr[i] to windowSum
   
3. ✅ CHECK if window is complete (i >= k-1)
   - Update result if needed
   - Remove arr[i-k+1] from windowSum (slide left)
   
4. 🎉 RETURN result
```

---

## 💻 Code Templates

### JavaScript Template

```javascript
function slidingWindowFixed(arr, k) {
  let windowSum = 0, maxSum = -Infinity;
  
  for (let i = 0; i < arr.length; i++) {
    windowSum += arr[i]; // Add right element
    
    if (i >= k - 1) {
      maxSum = Math.max(maxSum, windowSum);
      windowSum -= arr[i - k + 1]; // Remove left element
    }
  }
  return maxSum;
}

// Example usage
console.log(slidingWindowFixed([5, 2, -1, 0, 3], 3)); // Output: 6
```

### Python Template

```python
def sliding_window_fixed(arr, k):
    """Find maximum sum of subarray of size k"""
    window_sum = 0
    max_sum = float('-inf')
    
    for i in range(len(arr)):
        window_sum += arr[i]  # Add right element
        
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - k + 1]  # Remove left element
    
    return max_sum

# Example usage
print(sliding_window_fixed([5, 2, -1, 0, 3], 3))  # Output: 6
```

### C++ Template

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int slidingWindowFixed(vector<int>& arr, int k) {
    int windowSum = 0;
    int maxSum = INT_MIN;
    
    for (int i = 0; i < arr.size(); i++) {
        windowSum += arr[i];  // Add right element
        
        if (i >= k - 1) {
            maxSum = max(maxSum, windowSum);
            windowSum -= arr[i - k + 1];  // Remove left element
        }
    }
    return maxSum;
}

int main() {
    vector<int> arr = {5, 2, -1, 0, 3};
    cout << slidingWindowFixed(arr, 3) << endl;  // Output: 6
    return 0;
}
```

### Java Template

```java
public class SlidingWindow {
    public static int slidingWindowFixed(int[] arr, int k) {
        int windowSum = 0;
        int maxSum = Integer.MIN_VALUE;
        
        for (int i = 0; i < arr.length; i++) {
            windowSum += arr[i];  // Add right element
            
            if (i >= k - 1) {
                maxSum = Math.max(maxSum, windowSum);
                windowSum -= arr[i - k + 1];  // Remove left element
            }
        }
        return maxSum;
    }
    
    public static void main(String[] args) {
        int[] arr = {5, 2, -1, 0, 3};
        System.out.println(slidingWindowFixed(arr, 3));  // Output: 6
    }
}
```

---

## 🌍 More Real-Life Analogies

### 🔍 The Magnifying Glass
You're reading a book with a magnifying glass that shows exactly 5 words at a time. To read the whole page, you slide it along, always seeing 5 words.

### 🚂 The Train Inspector
A train has 20 carriages. You need to inspect every group of 4 consecutive carriages. Instead of counting weight for each group from scratch, you slide your inspection window: remove the carriage that left, add the new one that entered.

### 🎮 Video Game Health Bar
In a game, your health is the average of your last 10 actions. Every new action, you remove the oldest action's effect and add the newest one.

### 📺 TV Screen Scrolling
Imagine scrolling through a photo gallery where you see exactly 3 photos at once on screen. As you scroll right, one photo leaves the left, one enters from the right.

### 🏃‍♂️ Running Marathon Time
You're tracking the fastest 5-kilometer split in a marathon. Each kilometer, you update by removing the oldest km time and adding the newest.

---

## 🎯 How to Identify Sliding Window Problems?

### ✅ Look for These Clues

| Clue | Example |
|------|---------|
| Fixed size mentioned | "subarray of size K" |
| Contiguous elements | "consecutive numbers" |
| Max/Min/Average asked | "maximum sum", "minimum average" |
| Can be solved with nested loops | But would be too slow! |
| Array/String/List input | Linear data structure |
| Constraints: n ≤ 10⁵ | Need O(n) solution |

### 🔴 Red Flags (NOT Sliding Window)

- ❌ Need to find ALL subarrays (not fixed size)
- ❌ Elements can be picked non-consecutively
- ❌ Need to sort or rearrange elements
- ❌ Problem involves tree or graph structure

---

## ⚠️ Common Mistakes & How to Avoid Them

### Mistake 1: Starting Window Too Early ❌
```javascript
// WRONG!
if (i >= k) {  // Should be k-1
    maxSum = Math.max(maxSum, windowSum);
}
```
**Why:** When i=k, we've actually seen k+1 elements (index 0 to k)!

**Fix:** Use `i >= k - 1` ✅

---

### Mistake 2: Wrong Element Removal ❌
```javascript
// WRONG!
windowSum -= arr[i - k];  // Off by one!
```
**Why:** If i=5 and k=3, window is [3,4,5]. We should remove arr[3], not arr[2]!

**Fix:** Use `arr[i - k + 1]` ✅

---

### Mistake 3: Not Handling Edge Cases ❌
```python
# WRONG! What if k > len(arr)?
def sliding_window(arr, k):
    # No validation!
```

**Fix:** Add validation ✅
```python
def sliding_window(arr, k):
    if k > len(arr) or k <= 0:
        return None  # or raise exception
```

---

### Mistake 4: Forgetting to Update Result ❌
```javascript
// WRONG!
if (i >= k - 1) {
    windowSum -= arr[i - k + 1];  // Forgot to check max!
}
```

**Fix:** Always update result before sliding ✅

---

## 🧮 Detailed Problem Examples with Solutions

### Problem 1: Maximum Sum Subarray of Size K

**Problem:** Given array `[1, 4, 2, 10, 23, 3, 1, 0, 20]` and k=4, find maximum sum of any 4 consecutive numbers.

**Thought Process:**
```
Window 1: [1, 4, 2, 10]    → 17
Window 2: [4, 2, 10, 23]   → 39 ✨ (Maximum!)
Window 3: [2, 10, 23, 3]   → 38
Window 4: [10, 23, 3, 1]   → 37
Window 5: [23, 3, 1, 0]    → 27
Window 6: [3, 1, 0, 20]    → 24
```

**Solution:**
```python
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    # Calculate first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Test
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(max_sum_subarray(arr, 4))  # Output: 39
```

---

### Problem 2: Average of Subarrays of Size K

**Problem:** Given array `[1, 3, 2, 6, -1, 4, 1, 8, 2]` and k=5, find all averages.

**Solution:**
```python
def find_averages(arr, k):
    result = []
    window_sum = 0.0
    
    for i in range(len(arr)):
        window_sum += arr[i]  # Add next element
        
        if i >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[i - k + 1]  # Remove first element
    
    return result

# Test
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(find_averages(arr, 5))  
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]
```

**Visualization:**
```
Window 1: [1, 3, 2, 6, -1] → avg = 11/5 = 2.2
Window 2: [3, 2, 6, -1, 4] → avg = 14/5 = 2.8
Window 3: [2, 6, -1, 4, 1] → avg = 12/5 = 2.4
Window 4: [6, -1, 4, 1, 8] → avg = 18/5 = 3.6
Window 5: [-1, 4, 1, 8, 2] → avg = 14/5 = 2.8
```

---

### Problem 3: Maximum of All Subarrays of Size K

**Problem:** Given array `[1, 3, -1, -3, 5, 3, 6, 7]` and k=3, find maximum in each window.

**Solution (Using Deque for O(n) time):**
```python
from collections import deque

def max_sliding_window(arr, k):
    result = []
    dq = deque()  # Store indices
    
    for i in range(len(arr)):
        # Remove elements outside window
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (they're useless)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

# Test
arr = [1, 3, -1, -3, 5, 3, 6, 7]
print(max_sliding_window(arr, 3))
# Output: [3, 3, 5, 5, 6, 7]
```

---

### Problem 4: Count Vowels in Substrings of Length K

**Problem:** Find maximum number of vowels in any substring of length k=3
String: "abciiidef"

**Solution:**
```python
def max_vowels(s, k):
    vowels = set('aeiouAEIOU')
    max_count = count = 0
    
    for i in range(len(s)):
        # Add new character
        if s[i] in vowels:
            count += 1
        
        # Window complete
        if i >= k - 1:
            max_count = max(max_count, count)
            # Remove left character
            if s[i - k + 1] in vowels:
                count -= 1
    
    return max_count

# Test
print(max_vowels("abciiidef", 3))  # Output: 3 (substring "iii")
```

**Visualization:**
```
"abciiidef", k=3

Window "abc" → vowels: a=1    → count = 1
Window "bci" → vowels: i=1    → count = 1
Window "cii" → vowels: i,i=2  → count = 2
Window "iii" → vowels: i,i,i=3 → count = 3 ✨
Window "iid" → vowels: i,i=2  → count = 2
Window "ide" → vowels: i,e=2  → count = 2
Window "def" → vowels: e=1    → count = 1
```

---

## 📚 Classic LeetCode Problems (With Difficulty)

| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Basic sliding window |
| 1343 | [Number of Sub-arrays of Size K and Average ≥ Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Medium | Count windows |
| 1456 | [Maximum Number of Vowels in Substring of Length K](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium | Character counting |
| 1052 | [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/) | Medium | Window optimization |
| 1423 | [Maximum Points from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Medium | Bidirectional window |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Anagram detection |
| 438 | [Find All Anagrams in String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | Multiple anagrams |
| 1151 | [Minimum Swaps to Group All 1's Together](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/) | Medium | Count zeros |
| 2090 | [K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) | Medium | Center-based window |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Deque optimization |

---

## 🎓 Practice Strategy

### Beginner Level (Start Here!)
1. **Maximum Average Subarray I** - Learn basic template
2. **Number of Subarrays of Size K** - Practice counting
3. **Maximum Vowels in Substring** - Character tracking

### Intermediate Level
4. **Find All Anagrams** - Frequency maps
5. **Permutation in String** - Pattern matching
6. **Grumpy Bookstore Owner** - Real-world application

### Advanced Level
7. **Sliding Window Maximum** - Deque data structure
8. **Maximum Points from Cards** - Bidirectional thinking
9. **Minimum Swaps** - Optimization problems

---

## 💡 Pro Tips & Tricks

### Tip 1: Use Two-Pointer Approach
```python
left = 0
for right in range(len(arr)):
    # Add arr[right]
    if right >= k - 1:
        # Process window
        # Remove arr[left]
        left += 1
```

### Tip 2: Track Frequency with HashMap
```python
from collections import Counter

freq = Counter()
for i in range(len(s)):
    freq[s[i]] += 1
    
    if i >= k - 1:
        # Check freq
        freq[s[i - k + 1]] -= 1
        if freq[s[i - k + 1]] == 0:
            del freq[s[i - k + 1]]
```

### Tip 3: Handle Edge Cases First
```python
if not arr or k <= 0 or k > len(arr):
    return None  # Or appropriate default
```

### Tip 4: Use Prefix Sum for Fast Queries
```python
# Precompute prefix sums
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Window sum = prefix[i+1] - prefix[i-k+1]
```

---

## 🧠 Mental Model: The "Add-Remove" Dance

```
Think of it as a dance with 2 moves:

Step 1: 👉 ADD new element (expand right)
Step 2: 👈 REMOVE old element (shrink left)

Repeat until you reach the end!

        ADD →
    [■ ■ ■ □] □ □ □
        ← REMOVE
    □ [■ ■ ■ □] □ □
        ← REMOVE
    □ □ [■ ■ ■ □] □
```

---

## 🎪 Interactive Visualization Exercise

**Try this yourself on paper!**

Array: `[2, 1, 5, 1, 3, 2]`, k = 3

1. Draw 6 boxes for the array
2. Draw a bracket [ ] under first 3 boxes
3. Write the sum inside the bracket
4. Move bracket one step right, update sum
5. Keep going until the end!

```
Try it here:
┌───┬───┬───┬───┬───┬───┐
│ 2 │ 1 │ 5 │ 1 │ 3 │ 2 │
└───┴───┴───┴───┴───┴───┘
 └─────────┘ Sum = ?
     └─────────┘ Sum = ?
         └─────────┘ Sum = ?
             └─────────┘ Sum = ?
```

**Answers:**
- Window 1: 2+1+5 = 8
- Window 2: 1+5+1 = 7
- Window 3: 5+1+3 = 9 ✨
- Window 4: 1+3+2 = 6

Maximum = 9!

---

## 🎯 Quick Reference Cheat Sheet

```python
# TEMPLATE FOR FIXED WINDOW
def sliding_window_fixed(arr, k):
    # Edge case
    if len(arr) < k:
        return result_for_invalid_case
    
    # Initialize
    window_sum = 0
    result = initial_value
    
    # Main loop
    for i in range(len(arr)):
        window_sum += arr[i]  # Expand window
        
        if i >= k - 1:
            result = update_result(result, window_sum)
            window_sum -= arr[i - k + 1]  # Shrink window
    
    return result
```

**Key Variables:**
- `window_sum`: Current window aggregate
- `result`: Best answer so far
- `i - k + 1`: Left edge of window
- `i >= k - 1`: Window is ready

---

## 🌟 Summary for Kids

### What We Learned:
1. 🪟 **Sliding Window** = Moving a box along a row
2. ➕➖ **Two Operations** = Add new, Remove old
3. 🚀 **Super Fast** = O(n) instead of O(n×k)
4. 🎯 **Fixed Size** = Window always has K elements
5. 💪 **Many Uses** = Sum, average, max, count, anything!

### The Secret Formula:
```
1. Add the right element
2. If window is full:
   - Do something with the window
   - Remove the left element
3. Repeat!
```

### Remember This:
> "Don't start from scratch each time.
> Just update what changed!" 🎓

---

## 🎮 Practice Challenge: Try It Yourself!

**Challenge 1:** Find minimum sum of size k=3
```
Array: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
Your answer: __________
```

**Challenge 2:** Find all windows with sum > 10, k=3
```
Array: [1, 4, 6, 2, 8, 3]
Your answer: __________
```

**Challenge 3:** Count vowels in each window, k=4
```
String: "weallloveyou"
Your answer: __________
```

<details>
<summary>Click for Answers</summary>

**Challenge 1:** Minimum = 2 (window: [1, 2, -1] or [1, 0, 1])
**Challenge 2:** Windows [4,6,2]=12, [6,2,8]=16, [2,8,3]=13
**Challenge 3:** [2, 3, 3, 3, 3, 3, 2, 2, 3]

</details>

---

## 📖 Additional Resources

### Online Platforms
- 🔗 [LeetCode Sliding Window Problems](https://leetcode.com/problem-list/sliding-window/)
- 🔗 [GeeksforGeeks Sliding Window Tutorial](https://www.geeksforgeeks.org/window-sliding-technique/)
- 🔗 [HackerRank Practice Problems](https://www.hackerrank.com/domains/algorithms)
- 🔗 [AlgoExpert Video Explanations](https://www.algoexpert.io/)

### Video Tutorials
- 📺 [NeetCode: Sliding Window Playlist](https://www.youtube.com/c/NeetCode)
- 📺 [Abdul Bari: Algorithm Tutorials](https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw)

### Books
- 📚 "Grokking Algorithms" by Aditya Bhargava
- 📚 "Introduction to Algorithms" (CLRS)
- 📚 "Cracking the Coding Interview" by Gayle Laakmann McDowell

---

## 🏆 Mastery Checklist

Track your progress:

- [ ] ✅ Understand the concept with real-life examples
- [ ] ✅ Write the basic template from memory
- [ ] ✅ Solve 3 easy problems
- [ ] ✅ Solve 5 medium problems
- [ ] ✅ Understand time/space complexity
- [ ] ✅ Handle edge cases correctly
- [ ] ✅ Solve 1 hard problem
- [ ] ✅ Explain the technique to someone else
- [ ] ✅ Create your own problem
- [ ] ✅ Master variations (max, min, average, count)

---

## 🎉 Final Words

Remember:
> **"A window that slides is better than a loop that grinds!"** 

### You've Got This! 💪

Sliding Window is one of the most elegant and useful patterns in programming. Once you master it, you'll find it everywhere!

Keep practicing, stay curious, and happy coding! 🚀

---

**Last Updated:** 2026
**Pattern Difficulty:** ⭐⭐ (Medium)
**Frequency in Interviews:** ⭐⭐⭐⭐⭐ (Very High)

---

### Quick Navigation
- [📁 Back to DSA Patterns Index](../00_Pattern_Index.md)
- [⬅️ Previous: Two Pointers Same Direction](../02_Two_Pointers_Same_Direction/README.md)
- [➡️ Next: Sliding Window Variable](../04_Sliding_Window_Variable/README.md)

---

Made with ❤️ for learners who think visually!
