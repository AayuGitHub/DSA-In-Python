# Naive approach:


def max_sub_array_sum_naive(arr):
    res = arr[0]
    n = len(arr)

    for i in range(0, n):
        curr = 0
        for j in range(i, n):
            curr += arr[j]
            res = max(res, curr)

    return res


# Efficient approach (Kadane's Algorithm)


def max_sub_array_sum_efficient(arr):
    res = 0
    n = len(arr)
    maxEnding = arr[0]
    for i in range(1, n):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)

    return res


print(max_sub_array_sum_naive([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array_sum_efficient([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
