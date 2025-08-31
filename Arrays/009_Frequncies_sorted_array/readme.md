---

### Problem Statement

Given a **sorted array** `arr[]` of size `N`, the task is to find the **frequency of each distinct element** in the array.

---

### Examples

**Example 1:**

- Input: `arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]`
- Output:
    
    ```
    Frequency of 1 is: 3
    Frequency of 2 is: 1
    Frequency of 3 is: 2
    Frequency of 5 is: 2
    Frequency of 8 is: 3
    Frequency of 9 is: 2
    Frequency of 10 is: 1
    
    ```
    

---

**Example 2:**

- Input: `arr = [2, 2, 6, 6, 7, 7, 7, 11]`
- Output:
    
    ```
    Frequency of 2 is: 2
    Frequency of 6 is: 2
    Frequency of 7 is: 3
    Frequency of 11 is: 1
    
    ```
    

---

### Constraints

- `1 ≤ arr.size ≤ 10^5`
- `10^6 ≤ arr[i] ≤ 10^6`
- Array is **sorted**

---

## Naïve Approach

### Idea

- Use a **hash map (dictionary in Python)** to count occurrences of each element.
- Traverse array once to fill the dictionary.
- Traverse dictionary to print frequencies.

### Time & Space Complexity

- Time: **O(n)**
- Space: **O(n)** (extra space for dictionary)

### Python Code

```python
def frequencies_naive(arr):
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    for key, val in freq_map.items():
        print(f"Frequency of {key} is: {val}")

# Example usage
frequencies_naive([1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10])

```

---

## Efficient Approach

### Idea

Since the array is **sorted**, equal elements are always consecutive.

We can directly count their frequency during traversal without using extra space.

### Steps

1. Initialize `freq = 1`.
2. Traverse array from index `1` to `n-1`.
    - If `arr[i] == arr[i-1]`, increment `freq`.
    - Else → print frequency of `arr[i-1]`, reset `freq = 1`.
3. After loop ends, print frequency of the last element.

### Time & Space Complexity

- Time: **O(n)**
- Space: **O(1)**

### Python Code

```python
def frequencies_efficient(arr):
    n = len(arr)
    freq = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            freq += 1
        else:
            print(f"Frequency of {arr[i - 1]} is: {freq}")
            freq = 1

    # Print frequency for the last element
    print(f"Frequency of {arr[n - 1]} is: {freq}")

# Example usage
frequencies_efficient([1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10])

```

---

## Naïve vs Efficient Comparison

| Approach | Time Complexity | Space Complexity | Suitable for Large n |
| --- | --- | --- | --- |
| Naïve | O(n) | O(n) | Yes, but extra memory used |
| Efficient | O(n) | O(1) | Best choice |