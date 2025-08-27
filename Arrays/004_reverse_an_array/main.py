# Naive Approachh
def reverse_array_naive(arr):
    return arr[::-1]  # Using Python slicing


# Example usage
print(reverse_array_naive([1, 4, 3, 2, 6, 5]))  # [5, 6, 2, 3, 4, 1]
print(reverse_array_naive([4, 5, 2]))  # [2, 5, 4]
print(reverse_array_naive([1]))  # [1]

# Efficient Approach


def reverse_array_inplace(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low += 1
        high -= 1

    return arr


# Example usage
print(reverse_array_inplace([1, 4, 3, 2, 6, 5]))  # [5, 6, 2, 3, 4, 1]
print(reverse_array_inplace([4, 5, 2]))  # [2, 5, 4]
print(reverse_array_inplace([1]))  # [1]
