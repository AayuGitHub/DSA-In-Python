# Naive Approach

def move_zeroes_to_end_naive(arr):
    
    n = len(arr)
    
    for i in range(0, n):
        if arr[i] == 0:
            for j in range(i+1, n):
                if arr[j] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
    
    return arr

# Efficient Approach:

def move_zeroes_to_end_efficient(arr):
    
    n = len(arr)
    
    count = 0  # Count of non-zero elements
    
    for i in range(0, n):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

    # Fill remaining positions with zeros
    for i in range(count, n):
        arr[i] = 0
    
    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]
move_zeroes_to_end_efficient(arr)