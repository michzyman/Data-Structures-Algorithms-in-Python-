def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less = [x for x in nums[1:] if x <= pivot]
        greater = [x for x in nums[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([5, 2, 8, 1, 9, 3]))