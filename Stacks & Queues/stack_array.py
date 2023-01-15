class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]
    
    def push(self, data):
        self.array.append(data)
        return self
    
    def pop (self):
        self.array.pop()
        return self

myStack = Stack()
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.pop()
myStack.peek()