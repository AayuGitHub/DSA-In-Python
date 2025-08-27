# Reverse an Array

### 📝 Problem Statement

Given an array `arr[]`, reverse it **in place** (without using extra space for another array).

### 📊 Examples

**Example 1:**

* Input: `arr = [1, 4, 3, 2, 6, 5]`
* Output: `[5, 6, 2, 3, 4, 1]`
* Explanation: First element `1` goes to the last position, second element `4` goes to the second last, and so on.

---

**Example 2:**

* Input: `arr = [4, 5, 2]`
* Output: `[2, 5, 4]`
* Explanation: After reversing, elements are swapped symmetrically from ends.

---

**Example 3:**

* Input: `arr = [1]`
* Output: `[1]`
* Explanation: Single element remains unchanged.

---

### ⚙️ Constraints

* `1 ≤ arr.size ≤ 10^6`
* `-10^9 ≤ arr[i] ≤ 10^9`

---

## 🐢 Naïve Approach

#### Idea

* Create a **new array** and copy elements from the original array in reverse order.
* Return the new array.

#### Steps

1. Start from the **last index** of the array.
2. Append elements one by one into a new array.
3. Return the new array.

#### ⏳ Time & Space Complexity

* Time: **O(n)**
* Space: **O(n)** (extra array needed)

#### 🐍 Python Code

```python
def reverse_array_naive(arr):
    return arr[::-1]   # Using Python slicing

# Example usage
print(reverse_array_naive([1, 4, 3, 2, 6, 5]))  # [5, 6, 2, 3, 4, 1]
print(reverse_array_naive([4, 5, 2]))           # [2, 5, 4]
print(reverse_array_naive([1]))                 # [1]
```

---

## 🚀 Efficient Approach (In-place)

#### Idea

* Use **two pointers** – one at the start (`low`) and one at the end (`high`).
* Swap elements at `low` and `high`.
* Move `low` forward and `high` backward until they meet.

#### Steps

1. Initialize `low = 0`, `high = n-1`.
2. While `low < high`:

   * Swap `arr[low]` and `arr[high]`.
   * Increment `low`, decrement `high`.
3. Return the modified array.

#### Debugging Example

Input: `arr = [10, 20, 30, 40]`

* Swap `10` ↔ `40` → `[40, 20, 30, 10]`
* Swap `20` ↔ `30` → `[40, 30, 20, 10]`
* Done ✅

#### ⏳ Time & Space Complexity

* Time: **O(n)**
* Space: **O(1)** (in-place, no extra array used)

#### 🐍 Python Code

```python
def reverse_array_inplace(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]  # swap
        low += 1
        high -= 1
    return arr

# Example usage
print(reverse_array_inplace([1, 4, 3, 2, 6, 5]))  # [5, 6, 2, 3, 4, 1]
print(reverse_array_inplace([4, 5, 2]))           # [2, 5, 4]
print(reverse_array_inplace([1]))                 # [1]
```