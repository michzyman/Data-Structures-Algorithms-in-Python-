class Node(): 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 1

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            newNode.previous = self.tail
            #Pointer of the tail 
            self.tail.next = newNode
            #New last item
            self.tail = newNode
            #increase the length of the list by one (newNode)
            self.length += 1
            return self

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
        self.length += 1
        return self
    
    def insert(self, index, data):
        if index >= self.length:
            return self.append(data)
        newNode = Node(data)
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = newNode
        newNode.previous = leader
        newNode.next = follower
        follower.previous = newNode
        self.length += 1
        print(self)
        return self.print_list()

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while(counter != index):
            currentNode = currentNode.next
            counter += 1
        return currentNode



    def print_list(self):
        array = []
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                array.append(current_node.data)
                current_node = current_node.next
            print(array)

    def remove(self, index):
        leader = self.traverseToIndex(index -1)
        unwanted_node = leader.next
        follower = unwanted_node.next
        leader.next = follower
        follower.previous = leader
        self.length -= 1

        return self.print_list()

myDoublyLinkedList = DoublyLinkedList()
myDoublyLinkedList.append(10)
myDoublyLinkedList.append(5)
myDoublyLinkedList.append(16)
print(myDoublyLinkedList)
myDoublyLinkedList.prepend(1)
myDoublyLinkedList.print_list()
myDoublyLinkedList.insert(1,99)
myDoublyLinkedList.remove(1)
