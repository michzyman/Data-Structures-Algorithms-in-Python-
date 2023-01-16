"""
Given anumber N return the index value of the Fibonacci sequence, where the sequence is:

0,1,1,2,3,5,8,13,21,34,55,89,144 ....

the pattern of the sequence is that each value is the sum of the 2 previous values that means that for N=5 -> 2+3

"""

def fibonacciIterative(n):
    array = [0,1] #inital items of the sequence
    for i in range(2, n):
        #append the sum of the previous 2 items
        array.append(array[i-2] + array[i-1])
    return array[n-1]

def fibonacciRecursive(n):
    #Base case
    if n < 2:
        return n
    #Recursive Solution 
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
"""
Even though the recursive solution is more readable is not ideally because the time complexity is O(2^n)
"""
print(fibonacciRecursive(0)) #Output: 0 
print(fibonacciRecursive(1)) #Output: 1
print(fibonacciRecursive(2)) #Output: 1 
print(fibonacciRecursive(8)) #Output: 21 

print(fibonacciIterative(8)) #Output: 21 

