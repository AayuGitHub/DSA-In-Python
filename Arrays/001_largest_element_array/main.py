# Naive approach to find the largest element in an array


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


# Efficient approach to find the largest element in an array


def largest_element_efficient(arr):
    n = len(arr)
    if n == 0:
        return None

    largest = arr[0]
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]
    return largest


# Example usage
arr = [1, 8, 7, 56, 90]
print(largest_element_naive(arr))  # Output: 90
print(largest_element_efficient(arr))  # Output: 90
