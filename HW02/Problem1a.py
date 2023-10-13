# sort the array
quickSort(Array, 0, arr_size-1) # O(nlogn)
leftIndex = 0
rightIndex = arr_size-1
# Search Array for a pair that sums to sum
while leftIndex < rightIndex: # O(n)
  if (Array[leftIndex] + Array[rightIndex] == sum):
    print (Array[leftIndex], Array[rightIndex])
  elif (Array[leftIndex] + Array[rightIndex] < sum):
    leftIndex += 1
  else:
    rightIndex -= 1