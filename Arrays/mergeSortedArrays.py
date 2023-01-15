def mergeSortedArrays(arr1, arr2):
  newArr = []
  newArray = arr1 + arr2
  newArr.sort()
  return newArray

def mergeSortedArrays2 (arr1, arr2):
#If either array is empty
  if len(arr1) == 0 or len(arr2) == 0:
    return arr1 + arr2

  mergedArray = []
  i= 0
  j=0
  while i < len(arr1) and j < len(arr2): 
    if arr1[i] <= arr2[j]:
      mergedArray.append(a[i])
      i += 1
    if arr2[j] < arr1[i]:
      mergedArray.append(b[j])
      j += 1
  return mergedArray+arr1[i:]+b[j:]
    

a = [1,2,6]
b = [4,5,3]
c = []
print(mergeSortedArrays(a,b))
print(mergeSortedArrays2(a,b))
    
    