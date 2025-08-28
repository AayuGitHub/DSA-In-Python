# Move All Zeroes to End

---

### Problem Statement

You are given an array `arr[]` of non-negative integers.
The task is to **move all zeros** present in the array to the **right end**, while **maintaining the relative order** of non-zero elements.

The operation must be done **in-place** (without using extra space).

---

### Examples

**Example 1:**

* Input: `arr = [1, 2, 0, 4, 3, 0, 5, 0]`
* Output: `[1, 2, 4, 3, 5, 0, 0, 0]`
* Explanation: Three `0`s are moved to the end.

---

**Example 2:**

* Input: `arr = [10, 20, 30]`
* Output: `[10, 20, 30]`
* Explanation: No zero present, so no change.

---

**Example 3:**

* Input: `arr = [0, 0]`
* Output: `[0, 0]`
* Explanation: All elements are zero, so no change.

---

### Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^5`

---

## Naïve Approach

### Idea

* Traverse the array.
* Whenever you find a `0`, search for the next non-zero element and swap them.
* Continue this until the array is fully processed.

### Steps

1. Loop over array `i = 0 → n-1`.
2. If `arr[i] == 0`, search for next non-zero `arr[j]` (`j > i`).
3. Swap `arr[i]` and `arr[j]`.
4. Continue until all zeros are pushed back.

### Time & Space Complexity

* Time: **O(n²)** (due to nested loops in worst case).
* Space: **O(1)** (in-place).

### Python Code

```python
def move_zeroes_to_end_naive(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            for j in range(i + 1, n):
                if arr[j] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
    return arr

# Example usage
print(move_zeroes_to_end_naive([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
```


##  Efficient Approach

### Idea

* Use a **two-pointer approach**.
* `count` keeps track of where the next non-zero element should go.
* Traverse array:

  * If element is non-zero → place it at `arr[count]` and increment `count`.
* After traversal → fill remaining slots with zeros.

### Steps

1. Initialize `count = 0`.
2. Traverse array `i = 0 → n-1`:

   * If `arr[i] != 0`, swap with `arr[count]`, increment `count`.
3. After traversal, from `count → n-1`, fill with zeros (optional, but swap already does this implicitly).
4. Done 

### Debugging Example

Input: `arr = [1, 2, 0, 4, 3, 0, 5, 0]`

* `count=0` → arr\[0]=1 → place at index 0.
* `count=1` → arr\[1]=2 → place at index 1.
* arr\[2]=0 → skip.
* arr\[3]=4 → place at index 2.
* arr\[4]=3 → place at index 3.
* arr\[5]=0 → skip.
* arr\[6]=5 → place at index 4.
* arr\[7]=0 → skip.
* Fill rest with 0.
* Final: `[1, 2, 4, 3, 5, 0, 0, 0]`.

### Time & Space Complexity

* Time: **O(n)**
* Space: **O(1)**

### Python Code

```python
def move_zeroes_to_end_efficient(arr):
    n = len(arr)
    count = 0  # Position to place next non-zero
    
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    
    return arr

# Example usage
print(move_zeroes_to_end_efficient([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
```

---

## Naïve vs Efficient Comparison

| Approach  | Time Complexity | Space Complexity | In-place | Suitable for Large Input? |
| --------- | --------------- | ---------------- | -------- | ------------------------- |
| Naïve     | O(n²)           | O(1)             | ✅        | ❌ (too slow)              |
| Efficient | O(n)            | O(1)             | ✅        | ✅                         |

---