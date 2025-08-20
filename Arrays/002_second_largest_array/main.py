# Naive approach


def second_largest_naive(arr):
    n = len(arr)

    # Step 1: Find Largest element
    largest = arr[0]
    
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]
    
    # Step 2: Find Second largest element
    secondLargest = -1
    for i in range(n):
        if arr[i] != largest:
            if secondLargest == -1 or arr[i] > secondLargest:
                secondLargest = arr[i]
    return secondLargest

# Efficient Approach:

def second_largest_efficient(arr):
    n = len(arr)
    
    largest = arr[0]
    secondLargest = -1
    
    for i in range(1, n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] == largest:
            continue
        elif arr[i] > secondLargest or secondLargest == -1:
            secondLargest = arr[i]

    return secondLargest

# Example usage
arr = [12, 35, 1, 10, 34, 1]
print(second_largest_naive(arr))  # Output: 34
print(second_largest_efficient(arr))  # Output: 34
