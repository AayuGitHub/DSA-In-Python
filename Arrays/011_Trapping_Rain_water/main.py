# Naive Approach


def getWater(arr, n):
    res = 0

    # Loop through every element except first & last
    for i in range(1, n - 1):
        # Find max to the left
        lMax = arr[i]
        for j in range(i):
            lMax = max(lMax, arr[j])

        # Find max to the right
        rMax = arr[i]
        for j in range(i + 1, n):
            rMax = max(rMax, arr[j])

        # Water trapped at index i
        res += min(lMax, rMax) - arr[i]

    return res


# Driver Code
arr = [3, 0, 1, 2, 5]
n = len(arr)
print(getWater(arr, n))  # Output: 6

# Efficient Approach


def getWater(arr, n):
    res = 0

    # Arrays to store left max and right max
    lMax = [0] * n
    rMax = [0] * n

    # Fill lMax[]: max from left up to i
    lMax[0] = arr[0]
    for i in range(1, n):
        lMax[i] = max(arr[i], lMax[i - 1])

    # Fill rMax[]: max from right up to i
    rMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rMax[i] = max(arr[i], rMax[i + 1])

    # Calculate trapped water
    for i in range(1, n - 1):
        res += min(lMax[i], rMax[i]) - arr[i]

    return res


# Driver Code
arr = [5, 0, 6, 2, 3]
n = len(arr)
print(getWater(arr, n))  # Output: 6


def getWater_optimal(arr, n):
    res = 0
    left, right = 0, n - 1
    lMax, rMax = 0, 0

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= lMax:
                lMax = arr[left]
            else:
                res += lMax - arr[left]
            left += 1
        else:
            if arr[right] >= rMax:
                rMax = arr[right]
            else:
                res += rMax - arr[right]
            right -= 1

    return res


# Example
arr = [3, 0, 2, 0, 4]
print("Optimal Approach Output:", getWater_optimal(arr, len(arr)))  # 7
