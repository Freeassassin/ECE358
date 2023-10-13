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
    Array = Array[:j]
A = [1, 2, 2, 2, 6,  6,  7,  8,  8,  10]
B = [2, 2, 6, 8, 10, 10, 10, 16, 18, 20]
A = removeDuplicates(A, len(A)) # O(n)
B = removeDuplicates(B, len(B)) # O(n)
union = []
j = 0
print(A, B)
if (len(A) > len(B)):
    for i in range(0,len(A)): # O(n)
        if(A[i] == B[j]):
            union.append(A[i])
            if (j < len(B)-1):
                j += 1
        else:
            union.append(A[i])
            union.append(B[j])
            if (j < len(B)-1):
                j += 1
else:
    for i in range(0,len(B)): # O(n)
        if(A[i] == B[j]):
            union.append(B[i])
            if (j < len(A)-1):
                j += 1
        else:
            union.append(A[i])
            union.append(B[j])
            if (j < len(A)-1):
                j += 1        