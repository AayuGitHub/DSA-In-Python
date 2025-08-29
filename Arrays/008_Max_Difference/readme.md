### Problem Statement

Given an array `arr[]` of integers, find the **maximum difference** between any two elements such that the **larger element appears after the smaller element**.

Return the maximum difference.

---

### Examples

**Example 1:**

- Input: `arr = [2, 3, 10, 6, 4, 8, 1]`
- Output: `8`
- Explanation: Maximum difference is `10 - 2 = 8`.

---

**Example 2:**

- Input: `arr = [7, 9, 5, 6, 3, 2]`
- Output: `2`
- Explanation: Maximum difference is `9 - 7 = 2`.

---

### Constraints

- `2 <= arr.size() <= 10^5`
- `10^6 <= arr[i] <= 10^6`

---

## Naïve Approach

### Idea

- Compare every pair `(arr[i], arr[j])` where `j > i`.
- Keep track of the maximum difference.

### Steps

1. Initialize `max_diff = arr[1] - arr[0]`.
2. For each element `i`, check all elements to its right (`j > i`).
3. Update `max_diff` if `(arr[j] - arr[i])` is greater.
4. Return `max_diff`.

### Time & Space Complexity

- Time: **O(n²)** (nested loops).
- Space: **O(1)**.

### Python Code

```python
def max_difference_naive(arr):
    max_diff = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]
    return max_diff

# Example usage
print(max_difference_naive([2, 3, 10, 6, 4, 8, 1]))  # 8

```

---

## Efficient Approach

### Idea

- Keep track of the **minimum element so far** while traversing.
- At each step:
    - Calculate difference = `arr[i] - min_element`.
    - Update `max_diff` if this difference is larger.
    - Update `min_element` if `arr[i]` is smaller.

### Steps

1. Initialize `max_diff = arr[1] - arr[0]`, `min_element = arr[0]`.
2. Traverse from index `1 → n-1`.
3. For each element:
    - Update `max_diff = max(max_diff, arr[i] - min_element)`.
    - Update `min_element = min(min_element, arr[i])`.
4. Return `max_diff`.

### Debugging Example

Input: `arr = [2, 3, 10, 6, 4, 8, 1]`

- min_element = 2, max_diff = 1
- i=1 → arr[1]=3 → diff=1 → max_diff=1
- i=2 → arr[2]=10 → diff=8 → max_diff=8
- i=3 → arr[3]=6 → diff=4 → max_diff=8
- i=4 → arr[4]=4 → diff=2 → max_diff=8
- i=5 → arr[5]=8 → diff=6 → max_diff=8
- i=6 → arr[6]=1 → update min_element=1

Final Answer = 8.

### Time & Space Complexity

- Time: **O(n)**.
- Space: **O(1)**.

### Python Code

```python
def max_difference_efficient(arr):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff

# Example usage
print(max_difference_efficient([2, 3, 10, 6, 4, 8, 1]))  # 8

```

---

## Naïve vs Efficient Comparison

| Approach | Time Complexity | Space Complexity | Suitable for Large n |
| --- | --- | --- | --- |
| Naïve | O(n²) | O(1) | No |
| Efficient | O(n) | O(1) | Yes |