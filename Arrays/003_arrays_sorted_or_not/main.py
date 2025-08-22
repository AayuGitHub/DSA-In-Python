#   Naive Approach

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

# Efficient Approach:

def is_sorted_efficient(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

