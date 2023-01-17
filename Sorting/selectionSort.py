numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(arr):
    #iterates through all the elements of the array
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(numbers)
print(selectionSort(numbers))
