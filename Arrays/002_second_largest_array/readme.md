### 📝 Problem Statement

Given an array `arr[]`, the task is to find the **second largest distinct element** in the array.

If no such element exists (all elements are equal), return `-1`.

---

### 📊 Examples

**Example 1:**

- Input: `arr = [12, 35, 1, 10, 34, 1]`
- Output: `34`
- Explanation: Largest = `35`, second largest = `34`.

**Example 2:**

- Input: `arr = [10, 5, 10]`
- Output: `5`
- Explanation: Largest = `10`, second largest = `5`.

**Example 3:**

- Input: `arr = [10, 10, 10]`
- Output: `1`
- Explanation: All elements are same, so no second largest.

---

### ⚙️ Constraints

- `1 <= arr.size() <= 10^6`
- `0 <= arr[i] <= 10^6`

---

## 🐢 Naïve Approach

### Idea

1. First, find the **largest element** using the efficient `largest_element` approach.
2. Then, traverse the array again to find the **largest element smaller than this maximum**.
3. This will be the second largest.

### Steps

1. Compute `largest = max(arr)`.
2. Initialize `second_largest = -1`.
3. Traverse the array again → if an element is smaller than `largest` but greater than `second_largest`, update it.
4. Return `second_largest`.

### Debugging Example

Input: `arr = [12, 35, 1, 10, 34, 1]`

- First pass → largest = `35`
- Second pass:
    - Compare `12`: `12 > -1` → second_largest = `12`
    - Compare `35`: ignore (equal to largest)
    - Compare `1`: ignore
    - Compare `10`: ignore
    - Compare `34`: `34 > 12` → second_largest = `34`
    - Compare `1`: ignore

✅ Answer = `34`

### ⏳ Time Complexity

- O(n) for finding largest + O(n) for second largest = **O(n)**
    
    (but with two passes)
    

### 🐍 Python Code

```python
def second_largest_naive(arr):
    n = len(arr)
    # Step 1: Find largest
    largest = arr[0]
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    # Step 2: Find second largest
    second_largest = -1
    for i in range(n):
        if arr[i] != largest:
            if second_largest == -1 or arr[i] > second_largest:
                second_largest = arr[i]

    return second_largest

# Example usage
arr = [12, 35, 1, 10, 34, 1]
print(second_largest_naive(arr))  # Output: 34

```

---

## 🚀 Efficient Approach

### Idea

- Track both **largest** and **second largest** in a single traversal.
- While iterating:
    - If `arr[i] > largest`, then update → `second_largest = largest`, `largest = arr[i]`.
    - Else if `arr[i] < largest` and (`second_largest == -1` OR `arr[i] > second_largest`), update `second_largest`.
- Ignore duplicates of largest and second largest.

### Steps

1. Initialize `largest = arr[0]`, `second_largest = -1`.
2. Traverse the array from index `1`.
3. Update `largest` and `second_largest` accordingly.
4. Return `second_largest`.

### Debugging Example

Input: `arr = [12, 35, 1, 10, 34, 1]`

- Start: largest = `12`, second_largest = -1
- Compare `35`: new largest → largest = `35`, second_largest = `12`
- Compare `1`: ignore
- Compare `10`: update second_largest = `12 → 10`? (no, because 10 < 12)
- Compare `34`: update second_largest = `34`
- Compare `1`: ignore

✅ Answer = `34`

### ⏳ Time Complexity

- **O(n)** (single traversal)

### 🐍 Python Code

```python
def second_largest_efficient(arr):
    n = len(arr)
    largest = arr[0]
    second_largest = -1

    for i in range(1, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest:
            if second_largest == -1 or arr[i] > second_largest:
                second_largest = arr[i]

    return second_largest

# Example usage
arr = [12, 35, 1, 10, 34, 1]
print(second_largest_efficient(arr))  # Output: 34

```

---