def frequencies_naive(arr):
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    for key, val in freq_map.items():
        print(f"Frequency of {key} is: {val}")


# Example usage
frequencies_naive([1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10])


def frequencies_efficient(arr):
    n = len(arr)
    freq = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            freq += 1
        else:
            print(f"Frequency of {arr[i - 1]} is: {freq}")
            freq = 1

    # Print frequency for the last element
    print(f"Frequency of {arr[n - 1]} is: {freq}")


# Example usage
frequencies_efficient([1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10])
