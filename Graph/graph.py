#Edge List 
graph1 = [[0,2], [2,3], [2,1], [1,3]]
#Adjacent List 
graph2 =[[2],[2,3], [0,1,2], [1,2]]
    #The index of the array is the value of the actual Graph node

#adjacent Matric
graph = [
    [0, 0, 1, 0], #connected to node 2
    [0, 0, 1, 1], #connected to node 2 and 3
    [1, 1, 0, 1], #connected to node 0 1 and 3 
    [0, 1, 1, 0],#connected to node 2 and 1
]

class Graph: 
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
  
    def __str__(self):
        return str(self.__dict__)
    
    def add_vertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1
  

    def add_edge(self,node1,node2):
        #Undirected Graph
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
    
    def show_connections(self):
        for node in self.adjacentList:
            print(node, end= '-->')
            for vertex in self.adjacentList[node]:
                print(vertex, end =' ')
            print()


myGraph = Graph ()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
print(myGraph)
myGraph.add_edge('3', '1') 
myGraph.add_edge('3', '4') 
myGraph.add_edge('4', '2') 
myGraph.add_edge('4', '5') 
myGraph.add_edge('1', '2') 
myGraph.add_edge('1', '0') 
myGraph.add_edge('0', '2') 
myGraph.add_edge('6', '5')
myGraph.show_connections()
