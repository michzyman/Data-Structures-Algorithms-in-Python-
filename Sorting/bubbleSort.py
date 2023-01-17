numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    length = len(array)
    # Traverse through all array elements
    for i in range(len(array)):

        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                #Swap Numbers
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

bubbleSort(numbers)
print(numbers)

#Space complexity O(1)
#Time complexity O(n^2)

