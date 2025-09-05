# Naive Approach

def get_water_naive(arr):
    n = len(arr)
    res = 0
    
    for i in range(1, n-1):
        
        lMax = arr[i]
        for j in range(0, i):
            lMax = max(lMax, arr[j])
            
        rMax = arr[i]
        for j in range(i+1, n):
            rMax = max(rMax, arr[j])
            
        res += min(lMax, rMax) - arr[i]
             
    return res

print(get_water_naive([3, 0, 1, 2, 5]))

# Efficient Approach

def get_water_efficient(arr):
    
    n = len(arr)
    res = 0
    
    lMax = [0]* n
    rMax = [0]* n
    
    lMax[0] = arr[0]
    for i in range(1, n):
        lMax[i] = max(arr[i], lMax[i-1])
        
    rMax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rMax[i] = max(arr[i], rMax[i+1])
        
    for i in range(1, n-1):
        res += min(lMax[i], rMax(i)) - arr[i]
    
    return res

print(get_water_efficient([3, 0, 1, 2, 5]))
