"""
Binary Tree
- Binary Search Tree
    - great for searching 
    - preserves relationship
Rules:
1. All child nodes in the tree to the right of the root node must be greater than the current node
2. All child nodes in the tree to the left < root node 
    LEFT < ROOT < RIGHT
3. A node can only have up to 2 children 

Advantage: Searching and LookUp is really fast
Disatvantage: It can become really unbalance that will look like a linked list
            BALANCE         UNBALANCED
LookUp      O(log n)          O(n)
Insert      O(log n)          O(n)
Delete      O(log n)          O(n)

This is the reason why an unbalanced BST is bad. Ideally we wanto to balance our search tree in order to have performanze optimization

We have built in algorightms that will help us balance our BST

Pros: 
1. Better than O(n) - assuming that is balanced
2. Ordered
3. Flexible Size

Cons: 
1. No O(1) operations
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        #check if root node is None 
        if not self.root:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    #Left
                    if not currentNode.left:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                else:
                    #Right
                    if not currentNode.right:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right
                      
    def lookup(self,value):
        #Room is empty? 
        if not self.root: 
            return False 
        #instanciate the current node
        currentNode = self.root
        while currentNode: 
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right 
            elif currentNode.value == value:
                return currentNode
        return False
    
    def remove(self, value): 
        if not self.root:
            return False
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:
                #Left
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                #right 
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode.value == value:
                #we have a match get to work
                # Option 1 no right child 
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    #if parent > current value , make current left child a child of parent
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.left
                    #if parent < current value , make current left child a right child of parent
                    elif currentNode.value > parentNode.value:
                        parentNode.right = currentNode.left

                #Option 2: right child which doesnt have a left child
                elif currentNode.right.left == None: 
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        currentNode.right.left = currentNode.left
                    #if parent > current, make right child of the left the parent
                    if currentNode.value < parentNode.value:
                        parentNode.left = currentNode.right
                    #if parent < current, make right child a right child of the parent
                    elif currentNode.value > parentNode.value:
                        parentNode.right = currentNode.right

                
                #Option 3: right child that has left child
                else: 
                    leftmost = currentNode.right.left
                    leftmostparent = currentNode.right
                    while leftmost.left != None:
                        leftmostparent = leftmost
                        leftmost = leftmost.left
                    
                    #Parent's left subtree is now leftmost's right subtree
                    leftmostparent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                return True

    def print_tree(self):
        if not self.root:
            return None
        return self._print_tree_preorder(self.root)

    def _print_tree_preorder(self, current):
        if not current:
            return
        print(current.value)
        self._print_tree_preorder(current.left)
        self._print_tree_preorder(current.right)


myBST = BinarySearchTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(20)
myBST.insert(170)
myBST.insert(15)
print(myBST.remove(15))


"""
AVL and Red/Black Tree are 2 different algorithms that will work in order to balance out BST
"""