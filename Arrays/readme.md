> Your one-stop revision doc for Arrays in Python — from basics to advanced, with examples, pitfalls, and best practices.
> 

---

## 1️⃣ Introduction

**What is an array?**

An **array** is a collection of elements stored in a contiguous memory block, accessed by an index.

**In Python**, there are three main ways to work with arrays:

1. **List** — built-in, dynamic, most common in DSA.
2. **`array.array`** — type-restricted, memory-efficient.
3. **NumPy arrays (`numpy.ndarray`)** — for scientific computing.

---

## 2️⃣ Python Lists (Dynamic Arrays)

### Create

```python
arr = [10, 20, 30]  # literal
arr2 = list((1, 2, 3))  # from tuple

```

### Access

```python
arr[0]      # 10
arr[-1]     # last element

```

### Modify

```python
arr[1] = 99

```

### Add

```python
arr.append(40)      # add to end (O(1) amortized)
arr.insert(1, 15)   # add at index (O(n))

```

### Remove

```python
arr.pop()     # from end (O(1))
arr.pop(1)    # from index (O(n))
arr.remove(99) # remove first occurrence (O(n))

```

### Length

```python
len(arr)

```

---

## 3️⃣ Slicing & Copying

```python
arr = [10, 20, 30, 40, 50]
arr[1:4]    # [20, 30, 40] → copy
arr[::-1]   # reversed copy

```

⚠ **Note**: List slices always **create a copy** (O(k) time & space).

---

## 4️⃣ Iterating

```python
for x in arr:
    print(x)

for i, val in enumerate(arr):
    print(i, val)

```

---

## 5️⃣ Searching

```python
if 30 in arr:   # O(n)
    print("Found")

arr.index(30)   # returns first index or raises ValueError

```

---

## 6️⃣ Sorting

```python
arr.sort()                    # in-place
arr.sort(reverse=True)        # descending
arr.sort(key=lambda x: -x)    # custom

sorted_arr = sorted(arr)      # returns new list

```

---

## 7️⃣ Common Patterns

**Two Pointers**

```python
a = [1, 2, 3, 4, 5]
i, j = 0, len(a)-1
while i < j:
    print(a[i], a[j])
    i += 1
    j -= 1

```

**Sliding Window**

```python
def max_sum_subarray(arr, k):
    cur = sum(arr[:k])
    best = cur
    for i in range(k, len(arr)):
        cur += arr[i] - arr[i-k]
        best = max(best, cur)
    return best

```

---

## 8️⃣ `array.array` — Typed Arrays

```python
from array import array

nums = array('i', [1, 2, 3])  # 'i' = signed int
nums.append(4)
nums[0] = 10

```

**Type Codes**

- `'i'` → signed int
- `'f'` → float
- `'b'` → signed char

✅ **Benefits**: Less memory, faster for numeric scans.

---

## 9️⃣ NumPy Arrays (Quick Intro)

```python
import numpy as np

a = np.array([1, 2, 3], dtype=np.int32)
a + 10       # vectorized
a[1:3] += 5  # modifies view

```

⚠ **Slices are views** (no copy unless `.copy()` is called).

---

## 🔟 Pitfalls to Avoid

❌ **Shared row bug**

```python
# Wrong
grid = [[0]*3]*2
grid[0][1] = 9  # affects both rows

# Correct
grid = [[0]*3 for _ in range(2)]

```

❌ **pop(0) in a loop** → O(n²) time (use `collections.deque`).

❌ **Mixing types** in arrays → slower, less predictable.

---

## 1️⃣1️⃣ Complexity Cheat Sheet (List)

| Operation | Time Complexity |
| --- | --- |
| Indexing | O(1) |
| Append | O(1) amortized |
| Pop end | O(1) |
| Insert(i,x) | O(n) |
| Remove(x) | O(n) |
| Membership | O(n) |
| Sort | O(n log n) |

---

## 1️⃣2️⃣ Extra Tools for Arrays

### Binary Search

```python
import bisect
pos = bisect.bisect_left([10, 20, 30], 25)  # 2

```

### Heaps

```python
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappop(h)  # 1

```

---

## 1️⃣3️⃣ Summary Table

| Feature | list | array.array | numpy.ndarray |
| --- | --- | --- | --- |
| Type flexible | ✅ | ❌ | ❌ |
| Memory compact | ❌ | ✅ | ✅ |
| Math ops | ❌ | ❌ | ✅ |
| DSA friendly | ✅ | ⚠ | ⚠ |

---

✅ **Remember**:

- Use **list** for most DSA work.
- Use **array.array** when type-restricted + memory-sensitive.
- Use **NumPy** for large-scale numeric computations.