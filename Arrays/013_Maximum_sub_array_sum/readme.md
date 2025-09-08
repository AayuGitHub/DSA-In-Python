---

## Problem Statement

Given an array `arr[]` of integers (can include positive, negative, or zero), find the **maximum sum of any contiguous subarray**.

---

## Examples

**Example 1:**

- Input: `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6`
- Explanation: The subarray `[4, -1, 2, 1]` has the maximum sum `6`.

**Example 2:**

- Input: `arr = [1, 2, 3, -2, 5]`
- Output: `9`
- Explanation: The subarray `[1, 2, 3, -2, 5]` gives sum `9`.

**Example 3:**

- Input: `arr = [-1, -2, -3, -4]`
- Output: `1`
- Explanation: The subarray `[ -1 ]` has the maximum sum (since all elements are negative).

---

## Constraints

- `1 ≤ arr.size() ≤ 10^6`
- `10^9 ≤ arr[i] ≤ 10^9`

---

## Approaches

### 1. Naive Approach (Brute Force)

- Generate all subarrays and calculate their sums.
- Track the maximum among them.

**Steps:**

1. Initialize `res = arr[0]`.
2. For every starting index `i`, compute sum of subarray `[i…j]`.
3. Update `res` with the maximum sum found.

**Time Complexity:** O(n²)

**Space Complexity:** O(1)

```python
def max_sub_array_sum_naive(arr):
    res = arr[0]
    n = len(arr)

    for i in range(n):
        curr = 0
        for j in range(i, n):
            curr += arr[j]
            res = max(res, curr)

    return res

# Example
print(max_sub_array_sum_naive([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6

```

---

### 2. Efficient Approach (Kadane’s Algorithm)

- Idea: Instead of recalculating subarray sums, build them as you traverse.
- Maintain:
    - `maxEnding` → Maximum sum of subarray ending at current index.
    - `res` → Overall maximum sum so far.

**Steps:**

1. Initialize `maxEnding = arr[0]`, `res = arr[0]`.
2. For each element `arr[i]` from index `1`:
    - Update `maxEnding = max(arr[i], maxEnding + arr[i])`.
    - Update `res = max(res, maxEnding)`.
3. Return `res`.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

```python
def max_sub_array_sum_efficient(arr):
    n = len(arr)
    maxEnding = arr[0]
    res = arr[0]

    for i in range(1, n):
        maxEnding = max(arr[i], maxEnding + arr[i])
        res = max(res, maxEnding)

    return res

# Example
print(max_sub_array_sum_efficient([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6

```

---

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Notes |
| --- | --- | --- | --- |
| Naive | O(n²) | O(1) | Too slow for large arrays |
| Kadane’s | O(n) | O(1) | Optimal, works even with negatives |

---

⚡ Fun Fact: Kadane’s Algorithm is one of the most **famous dynamic programming problems** and is often asked in interviews as a gateway problem to DP.