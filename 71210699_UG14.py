class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set() 

    def vertex(self): #mencetak seluruh vertex
        print("\nSeluruh Node = ",end = '')
        for key, value in self._data.items():
            print(key, end = ' ')

    def edge(self): #mencetak seluruh edge
        print("\nSeluruh Edge = ",end = '')
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge:
            print(item, end = ' ')  
  
    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y 
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)
                    
    # untuk pembacaan traversing bfs graph
    def bfs(self,node):
        print("\nTraversing BFS = ",end = '')
        visited = []
        queue = [] 
        visited.append(node)
        queue.append(node)
        while queue:
            x = queue.pop(0) 
            print (x, end = " ")

            for tetangga in self._data[x]:
                if tetangga not in visited:
                    visited.append(tetangga)
                    queue.append(tetangga)

graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('d', 'e')
graph.addEdge('c', 'e')
graph.addEdge('c', 'g')
graph.addEdge('e', 'f')

graph.vertex()
graph.edge()
graph.bfs('a')