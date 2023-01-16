"""
Write down 2 functions that finds the factorial of any number. 
One should be recursive and the other should just use a loop.

Factorial 
5! = 5*4*3*2*1
base case = stop
recursive casa = multiply

"""
"""
factorial = 1
def findFactorialRecursive(number):
    if number > 1:
        factorial = number * number - 1
        print(factorial)
        return factorial
    print(findFactorialRecursive(factorial))
    return findFactorialRecursive(factorial)
"""

def findFactorialRecursive(number):
    #Base Case 
    if number == 2:
        return 2 
    #Recursive function 
    return number * findFactorialRecursive(number-1)
# O(n) time complexity

def findFactorialIterative(number):
    #code here
    factorial = 1

    if number == 2:
        factorial = 2

    for num in range(1, number + 1): 
        factorial *= num
    return factorial
# O(n) time complexity

print(findFactorialIterative(1)) # Output: 1
print(findFactorialIterative(5)) # Output: 120

print(findFactorialRecursive(5))
print(findFactorialRecursive(1))