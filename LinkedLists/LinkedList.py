"""
Pointer are references 
A linked list is a data structure that consists of a sequence of nodes, where each node stores a data value and a reference to the next node in the sequence. Linked lists are often used to implement lists and queues because they can be modified efficiently by adding or removing elements from the beginning or end of the list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


#append adds a new node with the given data value to the end of the linked list
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            #Pointer of the tail 
            self.tail.next = newNode
            #New last item
            self.tail = newNode
            #increase the length of the list by one (newNode)
            self.length += 1
            return self

#prepend adds a new node with the given data value to the beginning of the linked list    def prepend(self, data):
    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def insert(self, index, data):
        #check params 
        if index < 0:
            print('Invalid position')
            return self

        #as long as the index is greater or equal add it to the end
        if index >= self.length:
            if index > self.length:
                print('Index of node is greater than length, inserting at end.')
                return self.append(data)

        if index == 0:
            self.prepend(data)
            print('prepend first')
            return self.print_list()

        elif index == self.length:
            self.append(data)
            print('append last')
            return self.print_list()

        else:
            ('here')
            newNode = Node(data)
            current_node = self.head
            current_index = 0
            while current_index < index - 1:
                current_node = current_node.next
                current_index += 1
                newNode.next = current_node.next
                current_node.next = newNode
                self.length += 1

        return self

    def delete(self, index):
        if index < 0 or index >= self.length:
            print('Invalid position')
            return self
        if index == 0:
            self.head = self.head.next
        elif index == self.length - 1:
            leader_node = self.head
            while leader_node.next != self.tail:
                leader_node = leader_node.next
            self.tail = leader_node
            leader_node.next = None
        else:
            leader_node = self.head
            current_index = 0
            while current_index < index - 1:
                leader_node = leader_node.next
                current_index += 1
            leader_node.next = leader_node.next.next
        self.length -= 1
        return self
    


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

    def reverse(self):
        if self.length == 1:
            return self.print_list()
     
        firstItem = self.head  #first item in the list
        self.tail = self.head
        secondItem = firstItem.next #second item in the list
        #as long as the second item exists
        while(secondItem):
            temp = secondItem.next #hold the 3rd value 
            secondItem.next = firstItem #change pointers 
            firstItem = secondItem #change variables
            secondItem = temp  #change variables
        self.head.next = None
        self.head = firstItem
        return self.print_list()





myLinkedList = LinkedList()
myLinkedList.append(10)
myLinkedList.append(20)
myLinkedList.append(30)
print('append 10,20,30')
myLinkedList.print_list()
myLinkedList.insert(2, 15)
print('insert 15 at index 2')
myLinkedList.print_list()
myLinkedList.delete(1)
print('delete index 1')
myLinkedList.print_list()
print('reverse')
myLinkedList.reverse()
