def twoSum(nums, target):
  for i in range(len(nums)):
    #O(n)
    for j in range(i+1, len(nums)):
      #O(n)
      sum = nums[i] + nums[j]
      if sum == target:
        print([i,j])
#Time Complexity O(n*n)

print('result from twoSum()')       
twoSum(nums=[2,3,4] , target=5)

#search the array for the complement
#store the comlement in a map or dictionary
def twoSum2(nums, target):
  complementMap = dict() # {}
  for i in range(len(nums)):
    num = nums[i] # num = 3
    complement = target - num # 5 - 3 = 2
    if num in complementMap:
      return [complementMap[num] , i] #{0,1}
    else:
      complementMap[complement] = i #{2,0}

print('result from twoSum2()')    
print(twoSum2(nums=[2,3,4] , target=5))