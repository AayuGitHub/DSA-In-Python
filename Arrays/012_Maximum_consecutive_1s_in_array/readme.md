## Problem Statement

Given a binary array `arr[]` consisting of only `0`s and `1`s, the task is to find the maximum number of consecutive `1`s present in the array.

---

## Examples

**Example 1:**

- Input: `arr = [0, 1, 1, 0, 1, 1, 1]`
- Output: `3`
- Explanation: The maximum sequence of consecutive 1s is `[1, 1, 1]`.

**Example 2:**

- Input: `arr = [1, 1, 1, 1]`
- Output: `4`
- Explanation: The entire array is made of 1s.

**Example 3:**

- Input: `arr = [0, 0, 0]`
- Output: `0`
- Explanation: There are no 1s in the array.

---

## Constraints

- `1 ≤ arr.size() ≤ 10^6`
- `arr[i]` is either `0` or `1`

---

## Approaches

### 1. Naive Approach

- Start from each index `i` and count consecutive `1`s until a `0` is found.
- Keep track of the maximum count found so far.

**Steps:**

1. Initialize `res = 0`.
2. For each index `i`, check consecutive 1s starting from `i`.
3. Update `res` with the maximum count.

**Time Complexity:** O(n²)

**Space Complexity:** O(1)

```python
def max_consecutive_ones_naive(arr):
    res = 0
    n = len(arr)

    for i in range(n):
        current_max = 0
        for j in range(i, n):
            if arr[j] == 1:
                current_max += 1
            else:
                break
        res = max(res, current_max)

    return res

# Example usage
print(max_consecutive_ones_naive([0, 1, 1, 0, 1, 1, 1]))  # Output: 3

```

---

### 2. Efficient Approach

- Traverse the array once.
- Maintain a counter `current_max` to track the length of the current sequence of consecutive `1`s.
- Reset `current_max = 0` whenever a `0` is encountered.
- Update `res` with the maximum value of `current_max`.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

```python
def max_consecutive_ones_efficient(arr):
    res = 0
    current_max = 0

    for num in arr:
        if num == 0:
            current_max = 0
        else:
            current_max += 1
            res = max(res, current_max)

    return res

# Example usage
print(max_consecutive_ones_efficient([0, 1, 1, 0, 1, 1, 1]))  # Output: 3

```

---

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Notes |
| --- | --- | --- | --- |
| Naive | O(n²) | O(1) | Simple, but too slow for large arrays |
| Efficient | O(n) | O(1) | Best choice, works in one pass |

---