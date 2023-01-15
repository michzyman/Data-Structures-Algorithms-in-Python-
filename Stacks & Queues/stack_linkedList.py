"""
Stacks 
Implementation: 
- Arrays
- Linked List

Both will work fairly well

ARRAYS allow something called cache locality, which makes them technically
faster when accessing its items in memory because they're right next to each other 
versus a linked list that has them scattered all over memory.
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top: 
            return self.top.data
        else:
            return None

    def push(self, data):
        newNode = Node(data)
        if self.top :
            newNode.next = self.top
            self.top = newNode 
        else: 
            self.top = newNode
            self.bottom = newNode
        self.length += 1
        return self.top.data
    def pop (self):
        if self.top:
            poppedNode = self.top 
            if self.top == self.bottom: 
                self.bottom = None
            self.top = self.top.next
            self.length -= 1
            return poppedNode.data
        else: 
            return None

myStack = Stack()
print(myStack.push('google'))
print(myStack.push('udemy'))
print(myStack.push('discord'))
print("PEEK")
print(myStack.peek())
print("POOP")
print(myStack.pop())
print("POOP")
print(myStack.pop())
print("POOP")
print(myStack.pop())