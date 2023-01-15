""""
We will use two different stacks one for enqueue and anotherone for dequeue
"""
class Queue:
    def __init__(self):
        super().__init__()
        self.enqueue_stack = []
        self.dequeue_stack = []
    
    def enqueue(self, item):
        self.enqueue_stack.append(item)
    
    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
                if self.dequeue_stack:
                    return self.dequeue_stack.pop()
                else:
                    return None