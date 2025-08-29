# Naive Approach:

def max_difference_naive(arr):
    max_diff = arr[1] - arr[0]
    
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]
    return max_diff

# Efficient Approach


def max_difference_efficient(arr):
    max_difference  = arr[1] - arr[0]
    min_element = arr[0]
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] - min_element > max_difference:
            max_difference = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]
    return max_difference

print("Max Difference output:", end=" ")
print(max_difference_naive([2, 4, 8, 7, 7, 9, 3]))
print("\nMax Difference output:", end=" ")
print(max_difference_efficient([2, 4, 8, 7, 7, 9, 3]))