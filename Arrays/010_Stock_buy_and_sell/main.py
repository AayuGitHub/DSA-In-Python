# Naive Approach:

def max_profit_naive(arr, start, end):

    if end <= start:
        return 0
    
    profit = 0
    
    for i in range(start, end):
        for j in range(i+1, end):
            if arr[j] > arr[i]:
                curr_profit = arr[j] - arr[i] + max_profit_naive(arr, start, i-1) + max_profit_naive(arr, j+1, end)
                profit = max(profit, curr_profit)
    return profit

max_profit = max_profit_naive([1, 5, 3, 8, 12], 0, 5)
print(max_profit)