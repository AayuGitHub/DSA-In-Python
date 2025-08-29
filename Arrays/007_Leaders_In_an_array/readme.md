# Array Leaders

---

### Problem Statement

You are given an array `arr` of positive integers.
An element is considered a **leader** if it is greater than or equal to all elements to its right.
The **rightmost element is always a leader**.

Return all the leaders in the array.

---

### Examples

**Example 1:**

* Input: `arr = [16, 17, 4, 3, 5, 2]`
* Output: `[17, 5, 2]`
* Explanation: Leaders are `17`, `5`, and `2` since no greater element exists to their right.

---

**Example 2:**

* Input: `arr = [10, 4, 2, 4, 1]`
* Output: `[10, 4, 4, 1]`
* Explanation: Equal values are also allowed; hence both `4`s are leaders.

---

**Example 3:**

* Input: `arr = [5, 10, 20, 40]`
* Output: `[40]`
* Explanation: For a strictly increasing array, only the last element is a leader.

---

**Example 4:**

* Input: `arr = [30, 10, 10, 5]`
* Output: `[30, 10, 10, 5]`
* Explanation: For a non-increasing array, all elements are leaders.

---

### Constraints

* `1 <= arr.size() <= 10^6`
* `0 <= arr[i] <= 10^6`

---

## Naïve Approach

### Idea

* For each element, check all elements to its right.
* If no element is greater, mark it as a leader.

### Steps

1. Loop `i` from `0 → n-1`.
2. For each element `arr[i]`, check if there exists any `arr[j] > arr[i]` (`j > i`).
3. If none found, `arr[i]` is a leader.

### Time & Space Complexity

* Time: **O(n²)** (nested loops).
* Space: **O(1)**.

### Python Code

```python
def leaders_in_array_naive(arr):
    result = []
    for i in range(len(arr)):
        flag = False
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                flag = True
                break
        if not flag:
            result.append(arr[i])
    return result

# Example usage
print(leaders_in_array_naive([16, 17, 4, 3, 5, 2]))  # [17, 5, 2]
```

---

## Efficient Approach

### Idea

* Traverse from **right to left**.
* Keep track of the maximum element seen so far (`max_from_right`).
* An element is a leader if it is greater than or equal to `max_from_right`.

### Steps

1. Start with `max_from_right = arr[n-1]` (last element).
2. Move leftwards:

   * If `arr[i] >= max_from_right`, it is a leader.
   * Update `max_from_right`.
3. Reverse the collected leaders (since we traverse from right to left).

### Time & Space Complexity

* Time: **O(n)**.
* Space: **O(1)** (if printing directly) or **O(k)** (to store leaders).

### Python Code

```python
def leaders_in_array_efficient(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[n-1]
    leaders.append(max_from_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
    
    leaders.reverse()
    return leaders

# Example usage
print(leaders_in_array_efficient([16, 17, 4, 3, 5, 2]))  # [17, 5, 2]
```

---

## Naïve vs Efficient Comparison

| Approach  | Time Complexity | Space Complexity | Suitable for Large n |
| --------- | --------------- | ---------------- | -------------------- |
| Naïve     | O(n²)           | O(1)             | No                   |
| Efficient | O(n)            | O(1)             | Yes                  |

---