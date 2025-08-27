# Naive Approach


def remove_duplicates_naive(nums, n):

    temp = [0] * n
    temp[0] = nums[0]
    res = 1

    for i in range(1, n):
        if temp[res - 1] != nums[i]:
            temp[res] = nums[i]
            res += 1

    for i in range(res):
        nums[i] = temp[i]

    return res


# Efficient Approach


def remove_duplicates_efficient(nums, n):

    res = 1

    for i in range(1, n):
        if nums[i] != nums[i]:
            nums[res] = nums[i]
            res += 1

    return res
