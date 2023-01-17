"""
Given an array of integers,
return the indices of the two numbers 
that add up to a given targe

input: array of int & target value
Output: indices that add up to the target

Edge Cases:
input[1,3,7,9,2] t=11  output [3,4]
input[1,3,7,9,2] t=25  output None
input[] t=1  output None
input[5] t=5  output None
input[1,6] t=7  output [0,1]

Logic solution: 
try every possible pairs of numbers and see if the sum will add up to the target
    match = correct answer
    no match = None

numberToFind = target - nums[p1]
p2 will scan through the array and try to find numberToFind

"""

def twoSumBruteForceSolution(nums, target):
    for i in range(len(nums)): #Initializes a pointer to calculate the numToFind
        numToFind = target - nums[i] #compares the value 
        for j in range(i+1, len(nums)):
            if numToFind == nums[j]:
                return [i,j]
    return None
 #Time Complexity O(n^2) Space Complexity O(1)


def twoSumOptimalSolution(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        number = nums[i]
        numToFind = target - number
        if number in hashMap:
            return [hashMap[number], i]
        else:
            hashMap[numToFind]  = i 








