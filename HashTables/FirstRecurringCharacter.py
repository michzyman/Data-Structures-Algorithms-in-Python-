#Google Question 
#Given an array = [2,5,1,2,3,5,1,2,4]
#It should return 2 

#Given an array = [2,1,1,2,3,5,1,2,4]
#It should return 1

#Given an array = [2,3,4,5]
#It should return undefinied
"""
Input validation?  asumming we will always get an array of numbers 
This solution does not work 

def firstRecurringCharacter(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return None

print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))
"""

def hashSolution (nums):
    hash = dict()
    for i in range(len(nums)):
        if nums[i] in hash:
            return nums[i]
        else:
            hash[nums[i]] = i
        print(hash)
    return None
#Time Complexity improved by O(n) instead of )(n^2)
#Space Complexity increased by O(n) because we are creating a new object
print(hashSolution([2,5,1]))



