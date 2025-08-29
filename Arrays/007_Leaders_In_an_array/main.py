# Naive Approach

def leaders_in_array_naive(arr):
    
    for i in range(len(arr)):
        flag = False
        for j in range(i+1, len(arr)):
            if arr[j] >= arr[i]:
                flag = True
                break
        if not flag:
            print(arr[i], end=" ")

# Efficient Approach:

def leaders_in_array_efficient(arr):
    n = len(arr)-1
    max_from_right = arr[n]
    print(max_from_right, end=" ")
    for i in range(n-1, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            print(max_from_right, end=" ")
            

print("Naive approach output:", end=" ")
leaders_in_array_naive([16, 17, 4, 3, 5, 2])
print("\nEfficient approach output:", end=" ")
leaders_in_array_efficient([16, 17, 4, 3, 5, 2])