"""
In Binary Trees each node can have either 0,1 or 2 nodes
and each child can have only one parent
each node represent a certain state

Full Tree = No Gaps in the tree
Perfect Binary Tree: All the leaf nodes are full and there is no node that only has one child (either 0 or 2)
This is really efficient 
    - Number of total nodes dobles as we move one lvel down the tree
    - Number of nodes in the last level is = to the sum of the rest of the nodes + 1
        4 bottom 
        3 + 1 = 4

     0
   /   \ 
  2     3
 / \    /\ 
4   5  4  6

Full Binary Tree: a node has either 2 or 0 children but NEVER 1 
     0
   /   \ 
  2     3
 / \   
4    5  
     /\ 
    3 2

lookUp, Insert and Delete O(Log N)
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
(log n) Explained 

Level 0: 2^0 = 1
Level 1: 2^1 = 2
Level 2: 2^2 = 4
Level 3: 2^3 = 8 //8 nodes we need to check
We can find out the number of nodes in a tree by doing 2^height
# of Nodes = 2^h - 1
log of nodes = steps (log 100 = 2 bc 10^2 = 100)

"""
