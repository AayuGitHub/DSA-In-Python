# Trapping Rain Water

## Problem Statement

You are given an array `arr[]` of non-negative integers where each element represents the height of bars. The task is to compute how much water can be trapped between these bars after it rains.

---

## Examples

**Input:**
`arr = [3, 0, 1, 2, 5]`
**Output:**
`6`
**Explanation:**

* Water trapped at index 1 = `min(3, 5) - 0 = 3`
* Water trapped at index 2 = `min(3, 5) - 1 = 2`
* Water trapped at index 3 = `min(3, 5) - 2 = 1`
* Total = `6`

---

**Input:**
`arr = [5, 0, 6, 2, 3]`
**Output:**
`6`

---

**Input:**
`arr = [3, 0, 2, 0, 4]`
**Output:**
`7`

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `0 ≤ arr[i] ≤ 10^6`

---

## Approaches

### 1. Naive Approach (Brute Force)

* For every element, find the **maximum height to the left** and the **maximum height to the right**.
* Water trapped at index `i` = `min(lMax, rMax) - arr[i]`.
* Sum up for all indices.

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

```python
def getWater_naive(arr, n):
    res = 0
    for i in range(1, n - 1):
        lMax = arr[i]
        for j in range(i):
            lMax = max(lMax, arr[j])

        rMax = arr[i]
        for j in range(i + 1, n):
            rMax = max(rMax, arr[j])

        res += min(lMax, rMax) - arr[i]

    return res
```

---

### 2. Efficient Approach (Using Precomputed Arrays)

* Precompute `lMax[i]` = max height to the **left** of `i`.
* Precompute `rMax[i]` = max height to the **right** of `i`.
* Water trapped at index `i` = `min(lMax[i], rMax[i]) - arr[i]`.

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def getWater_efficient(arr, n):
    res = 0
    lMax = [0] * n
    rMax = [0] * n

    lMax[0] = arr[0]
    for i in range(1, n):
        lMax[i] = max(arr[i], lMax[i - 1])

    rMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rMax[i] = max(arr[i], rMax[i + 1])

    for i in range(1, n - 1):
        res += min(lMax[i], rMax[i]) - arr[i]

    return res
```

---

### 3. Optimal Approach (Two Pointers)

* Use two pointers (`left`, `right`) and keep track of `lMax` and `rMax`.
* If `arr[left] <= arr[right]`:

  * If `arr[left] >= lMax`, update `lMax`. Else, add trapped water.
  * Move left pointer.
* Else:

  * If `arr[right] >= rMax`, update `rMax`. Else, add trapped water.
  * Move right pointer.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def getWater_optimal(arr, n):
    res = 0
    left, right = 0, n - 1
    lMax, rMax = 0, 0

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= lMax:
                lMax = arr[left]
            else:
                res += lMax - arr[left]
            left += 1
        else:
            if arr[right] >= rMax:
                rMax = arr[right]
            else:
                res += rMax - arr[right]
            right -= 1

    return res
```

---

## Comparison of Approaches

| Approach  | Time Complexity | Space Complexity | Notes                                     |
| --------- | --------------- | ---------------- | ----------------------------------------- |
| Naive     | O(n²)           | O(1)             | Simple but too slow for large input       |
| Efficient | O(n)            | O(n)             | Good balance, easy to understand          |
| Optimal   | O(n)            | O(1)             | Best solution for competitive programming |

---
