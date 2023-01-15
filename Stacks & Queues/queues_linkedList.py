"""
Queues 
- Arrays: Never build it with an array bc we will need 
- Linked List: remove the head f
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0 

    def peek(self):
        if self.first:
            return self.first.data
        else:
            return None
        
        
    
    def enqueue(self,data):
        newNode = Node(data)
        if self.length == 0:
            self.first = newNode
            self.last = newNode 
            self.length += 1
        else:
            self.last.next = newNode
            self.last = newNode
            self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            return None
        if self.first == self.last:
            self.last = None
        holdingPointer = self.first
        self.first = self.first.next
        self.length -=1
        return holdingPointer.data


myQueue = Queue()
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samit')
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
