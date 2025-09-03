# Stock Buy and Sell Problem

**Problem Statement:**
Given an array `arr[]` denoting the cost of stock on each day, the task is to find the **maximum total profit** if we can buy and sell the stock **any number of times**.

⚠️ Rules:

* You can only sell a stock after buying it.
* You cannot hold multiple stocks at once.

---

## Example

### Input:

```
arr = [100, 180, 260, 310, 40, 535, 695]
```

### Output:

```
865
```

### Explanation:

* Buy on day 0 (100) and sell on day 3 (310) → Profit = 210
* Buy on day 4 (40) and sell on day 6 (695) → Profit = 655
* **Total Profit = 210 + 655 = 865**

---

## 🔹 Naive Approach

* Generate **all possible pairs** of buy/sell transactions.
* Recursively calculate maximum profit for every subarray before and after the chosen transaction.
* Time Complexity → **O(n²)** (very slow for large arrays).
* Space Complexity → **O(n)** (recursion stack).

### Python Code

```python
# Naive Recursive Approach
def max_profit_naive(arr, start, end):
    if end <= start:
        return 0

    profit = 0
    
    for i in range(start, end):
        for j in range(i+1, end+1):
            if arr[j] > arr[i]:
                # Calculate current profit and recurse for remaining days
                curr_profit = (arr[j] - arr[i] +
                               max_profit_naive(arr, start, i-1) +
                               max_profit_naive(arr, j+1, end))
                profit = max(profit, curr_profit)
    
    return profit


# Example Run
arr = [100, 180, 260, 310, 40, 535, 695]
print("Naive Max Profit:", max_profit_naive(arr, 0, len(arr)-1))
```

---

## 🔹 Efficient Approach

💡 Observation:
Whenever the price today is **higher** than yesterday, it’s profitable to buy yesterday and sell today.

So, we just sum up all **positive differences** between consecutive days.

* Time Complexity → **O(n)**
* Space Complexity → **O(1)**

### Python Code

```python
# Efficient Greedy Approach
def max_profit_efficient(arr):
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit


# Example Run
arr = [100, 180, 260, 310, 40, 535, 695]
print("Efficient Max Profit:", max_profit_efficient(arr))
```

---

## ✅ Sample Runs

```
Input: [100, 180, 260, 310, 40, 535, 695]
Output (Naive): 865
Output (Efficient): 865

Input: [4, 2, 2, 2, 4]
Output: 2

Input: [4, 2]
Output: 0
```

---

👉 This way, you now have **both approaches explained, coded, and compared** (same style as before).

Do you want me to also add **dry-run step-by-step walkthrough** (like we did earlier) for the **efficient solution** with an example? That way, it will be crystal clear for interviews.
