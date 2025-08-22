# 📘 Check if Array is Sorted

### 📝 Problem Statement

Given an array `arr[]`, check whether it is sorted in **non-decreasing order**.
Return `True` if it is sorted, otherwise `False`.

### 📊 Examples

**Example 1:**

* Input: `arr = [10, 20, 30, 40, 50]`
* Output: `True`
* Explanation: Every element is greater than or equal to the previous element.

**Example 2:**

* Input: `arr = [90, 80, 100, 70, 40, 30]`
* Output: `False`
* Explanation: Since `80 < 90` and later `70 < 100`, the array is not sorted.

**Example 3:**

* Input: `arr = [5, 5, 5, 5]`
* Output: `True`
* Explanation: Equal elements are allowed in non-decreasing order.

### ⚙️ Constraints

* `1 ≤ arr.size ≤ 10^6`
* `-10^9 ≤ arr[i] ≤ 10^9`

## 🐢 Naïve Approach

#### Idea

* Compare **every pair of elements** `(arr[i], arr[j])` where `j > i`.
* If **any element before is greater than an element after it**, then array is not sorted.
* Otherwise, it is sorted.

#### Steps

1. Loop `i` from `0` to `n-1`.
2. For each `i`, loop `j` from `i+1` to `n-1`.
3. If `arr[j] < arr[i]`, return `False`.
4. If no such case is found, return `True`.

#### Debugging Example

Input: `arr = [10, 20, 30]`

* Compare `10` with `20`, `30` → fine
* Compare `20` with `30` → fine
* No violations → return `True`

Input: `arr = [3, 1, 2]`

* Compare `3` with `1` → violation (`1 < 3`) → return `False`

#### ⏳ Time Complexity

* O(n²) (two nested loops)

#### 🐍 Python Code

```python
def is_sorted_naive(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                return False
    return True

# Example usage
print(is_sorted_naive([10, 20, 30, 40, 50]))   # True
print(is_sorted_naive([90, 80, 100, 70, 40]))  # False
```

---

## 🚀 Efficient Approach

#### Idea

* Traverse array once, comparing each element with its **previous one**.
* If any element is **smaller than the previous**, array is not sorted.
* Otherwise, it is sorted.

#### Steps

1. Start from index `1`.
2. Compare `arr[i]` with `arr[i-1]`.
3. If `arr[i] < arr[i-1]`, return `False`.
4. If no such violation, return `True`.

#### Debugging Example

Input: `arr = [10, 20, 30, 40, 50]`

* Compare `20 >= 10` ✅
* Compare `30 >= 20` ✅
* Compare `40 >= 30` ✅
* Compare `50 >= 40` ✅
* No violations → return `True`

Input: `arr = [90, 80, 100]`

* Compare `80 < 90` ❌ → return `False`

#### ⏳ Time Complexity

* **O(n)** (single traversal)

#### 🐍 Python Code

```python
def is_sorted_efficient(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

# Example usage
print(is_sorted_efficient([10, 20, 30, 40, 50]))   # True
print(is_sorted_efficient([90, 80, 100, 70, 40]))  # False
print(is_sorted_efficient([5, 5, 5, 5]))           # True
```
