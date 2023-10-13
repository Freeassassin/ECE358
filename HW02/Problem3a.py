def removeDuplicates(Array, n):
    temp = list(range(n))
    j = 0
    for i in range(0, n-1):
        if Array[i] != Array[i+1]:
            temp[j] = Array[i]
            j += 1
    temp[j] = Array[n-1]
    j += 1
    for i in range(0, j):
        Array[i] = temp[i]
    return temp[:j]
A = [1, 2, 2, 2, 6,  6,  7,  8,  10, 10]
B = [2, 2, 6, 8, 10, 10, 10, 10, 10, 10]
B = removeDuplicates(B, len(B)) # O(n)
print(B)
intersection = []
j = 0
for i in range(0,len(A)): # O(n)
    if(A[i] == B[j]):
        intersection.append(A[i])
        j += 1
    elif(A[i] < B[j]):
        continue
    else:
        while(A[i] > B[j]):
            j += 1
            if(A[i] == B[j]):
                intersection.append(A[i])
                j += 1
                break