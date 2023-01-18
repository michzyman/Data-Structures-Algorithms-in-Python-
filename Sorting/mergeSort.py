def mergeSort(nums):
    if len(nums) > 1:
        # Split the list in half
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Recursively sort each half
        mergeSort(left_half)
        mergeSort(right_half)

        # Merge the sorted halves back together
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Add any remaining elements
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1

    return nums
print(mergeSort([5, 2, 8, 1, 9, 3]))