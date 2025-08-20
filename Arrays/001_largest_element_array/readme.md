### 📝 Problem Statement

Given an array `arr[]`, the task is to find the largest element in the array and return it.

---

### 📊 Examples

**Example 1:**

- Input: `arr = [1, 8, 7, 56, 90]`
- Output: `90`
- Explanation: Among all elements, `90` is the largest.

**Example 2:**

- Input: `arr = [5, 5, 5, 5]`
- Output: `5`
- Explanation: All elements are the same, hence the largest is `5`.

**Example 3:**

- Input: `arr = [10]`
- Output: `10`
- Explanation: Only one element, so it is the largest.

---

### ⚙️ Constraints

- `1 <= arr.size() <= 10^6`
- `0 <= arr[i] <= 10^6`

---

## 🐢 Naïve Approach

### Idea

- Compare each element with all other elements.
- If an element is **not smaller than any other element**, declare it as the largest.

### Steps

1. Loop over each element `arr[i]`.
2. For each element, check if there exists another element greater than it.
3. If no greater element is found, return `arr[i]`.

### Debugging Example

Input: `arr = [1, 8, 7, 56, 90]`

- Check `1`: greater elements exist → not largest.
- Check `8`: greater elements exist → not largest.
- Check `7`: greater elements exist → not largest.
- Check `56`: greater element `90` exists → not largest.
- Check `90`: no greater element found → largest = `90`.

✅ Works correctly, but inefficient.

### ⏳ Time Complexity

- O(n²) because of two nested loops.

### 🐍 Python Code

```python
def largest_element_naive(arr):
    n = len(arr)
    for i in range(n):
        is_largest = True
        for j in range(n):
            if arr[j] > arr[i]:
                is_largest = False
                break
        if is_largest:
            return arr[i]

# Example usage
arr = [1, 8, 7, 56, 90]
print(largest_element_naive(arr))  # Output: 90

```

---

## 🚀 Efficient Approach

### Idea

- Keep track of the largest element while scanning the array once.
- Update the `max` whenever a larger element is found.

### Steps

1. Initialize `max` with the first element.
2. Traverse the array from left to right.
3. If `arr[i] > max`, update `max`.
4. At the end, return `max`.

### Debugging Example

Input: `arr = [1, 8, 7, 56, 90]`

- Start: `max = 1`
- Compare with `8`: update `max = 8`
- Compare with `7`: no update
- Compare with `56`: update `max = 56`
- Compare with `90`: update `max = 90`

Final Answer → `90`

### ⏳ Time Complexity

- O(n), only one traversal.

### 🐍 Python Code

```python
def largest_element_efficient(arr):
    n = len(arr)
    max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

# Example usage
arr = [1, 8, 7, 56, 90]
print(largest_element_efficient(arr))  # Output: 90

```