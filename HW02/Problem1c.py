def modifiedBinarySearch(A, low, high, searchKey):
    m = 0
    while (low <= high):
        m = (high + low) // 2
        if (A[m] < searchKey and A[m+1] > searchKey):
            return m
        elif (A[m] < searchKey):
            low = m + 1
        else:
            high = m - 1
    return 0

# sort the array
quickSort(Array, 0, arr_size-1) # O(nlogn)

closestSum = 0
closestPair = [] 
for i in range(0, arr_size-1): # O(n)
    target = sum-Array[i]
    # O(logn)
    index = modifiedBinarySearch(Array, i+1, arr_size-1, target)
    if(index):
        pairSum = Array[i] + Array[index]
        if ( sum-pairSum < sum-closestSum ):
            closestSum = pairSum
            closestPair = [Array[i], Array[index]]
        
