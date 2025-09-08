# Naive Approach


def max_consecutive_ones_naive(arr):
    res = 0
    n = len(arr)

    for i in range(0, n):
        current_max = 0

        for j in range(i, n):
            if arr[j] == 1:
                current_max += 1
            else:
                break

        res = max(res, current_max)

    return res


print(max_consecutive_ones_naive([0, 1, 1, 0, 1, 1, 1]))


def max_consecutive_ones_efficient(arr):

    res = 0
    n = len(arr)
    current_max = 0

    for i in range(0, n):
        if arr[i] == 0:
            current_max = 0
        else:
            current_max += 1
            res = max(res, current_max)

    return res


print(max_consecutive_ones_efficient([0, 1, 1, 0, 1, 1, 1]))
