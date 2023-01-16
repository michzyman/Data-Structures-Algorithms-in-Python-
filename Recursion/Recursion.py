"""
Rules to build recursion functions 
1. Identify the base case 
2. Identify the recursive case 
3. Get closer and closer and return when nedded. 
    Usually you have 2 returns
"""

counter = 0
def inception(counter):
    if counter > 3:
        return 'Done'
    counter += 1
    return inception(counter)

counter = inception(counter)
print(counter)

