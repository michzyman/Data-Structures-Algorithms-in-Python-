def maxAreaBruteForce(height):
    maxArea = 0 
    for i in range(len(height)): 
        for j in range(i+1, len(height)):
            length = min(height[i], height[j])
            width = (j-i)
            newArea = length * width 
            if newArea >= maxArea:
                maxArea = newArea
    return maxArea

def maxAreaOptimalSolution(height):
    maxArea = 0 
    left = 0 
    right = len(height) - 1
    while left < right: 
        length = min(height[left], height[right])
        width = (right-left)
        newArea = length * width 
        if newArea >= maxArea:
            maxArea = newArea
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxArea