---

### 📝 Problem Statement

Given a **sorted array** `arr[]` containing positive integers, remove all duplicate elements such that each element appears **only once**.

Return the modified array containing only the distinct elements in the same order.

---

### 📊 Examples

**Example 1:**

- Input: `arr = [2, 2, 2, 2, 2]`
- Output: `[2]`
- Explanation: All duplicates of `2` are removed, leaving only one instance.

---

**Example 2:**

- Input: `arr = [1, 2, 4]`
- Output: `[1, 2, 4]`
- Explanation: Array already has unique elements, so no change.

---

### ⚙️ Constraints

- `1 ≤ arr.size ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^6`

---

## 🐢 Naïve Approach

### Idea

- Create a **temporary array** to store unique elements.
- Traverse the array, and whenever you find a new element different from the last added, store it in the temporary array.
- Copy back the elements from the temporary array to the original one.

### Steps

1. Initialize `temp[0] = arr[0]`, and set `res = 1`.
2. Traverse from index `1` to `n-1`.
3. If `arr[i]` is different from the last added (`temp[res-1]`), add it.
4. Copy `temp[0..res-1]` back to `arr[0..res-1]`.

### ⏳ Time & Space Complexity

- Time: **O(n)**
- Space: **O(n)** (for temporary array)

### 🐍 Python Code

```python
def remove_duplicates_naive(nums, n):
    temp = [0] * n
    temp[0] = nums[0]
    res = 1

    for i in range(1, n):
        if temp[res - 1] != nums[i]:
            temp[res] = nums[i]
            res += 1

    # Copy unique elements back
    for i in range(res):
        nums[i] = temp[i]

    return nums[:res]

# Example usage
print(remove_duplicates_naive([2, 2, 2, 2, 2], 5))   # [2]
print(remove_duplicates_naive([1, 2, 2, 3, 3, 4], 6)) # [1, 2, 3, 4]

```

---

## 🚀 Efficient Approach

### Idea

- Since the array is sorted, duplicates will always be adjacent.
- Use a **two-pointer technique**:
    - `res` keeps track of the position of the next unique element.
    - Traverse the array, and whenever you find a new element, place it at `nums[res]`.

### Steps

1. Initialize `res = 1` (since first element is always unique).
2. Traverse from index `1` to `n-1`.
3. If `nums[i] != nums[res-1]`, store it at `nums[res]` and increment `res`.
4. Return `nums[0..res-1]`.

### Debugging Example

Input: `arr = [1, 1, 2, 2, 3]`

- `res=1`, check `arr[1]=1` → same as `arr[0]` → skip.
- `arr[2]=2` → different → place at `nums[1]`.
- `arr[3]=2` → same as last → skip.
- `arr[4]=3` → different → place at `nums[2]`.
- Final array: `[1, 2, 3]`.

### ⏳ Time & Space Complexity

- Time: **O(n)**
- Space: **O(1)** (in-place)

### 🐍 Python Code

```python
def remove_duplicates_efficient(nums, n):
    if n == 0:
        return []

    res = 1
    for i in range(1, n):
        if nums[i] != nums[res - 1]:
            nums[res] = nums[i]
            res += 1

    return nums[:res]

# Example usage
print(remove_duplicates_efficient([2, 2, 2, 2, 2], 5))   # [2]
print(remove_duplicates_efficient([1, 1, 2, 2, 3, 4], 6)) # [1, 2, 3, 4]

```

---

👉 Do you want me to also **add a quick Naïve vs Efficient comparison table** (like pros/cons, space usage) at the end for clarity, like we did with reverse array?