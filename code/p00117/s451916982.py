# Aizu Problem 0117: A reward for a Carpenter
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

# -----------------------------------------------------------------------
# Defining directed graph class: 
# -----------------------------------------------------------------------

class DirectedGraph:
    """An DirectedGraph g contains a dictionary (g.neighbor_dict) which
    maps node identifiers (keys) to lists of neighboring nodes (values).
    g.neighbor_dict[node] returns a list [node2, node3, node4] of neighbors.
    Node identifiers can be any non-mutable Python type (e.g., integers,
    tuples, strings, but not lists)."""

    def __init__(self):
        """ UndirectedGraph() creates an empty graph g.
        g.neighbor_dict starts as an empty dictionary.  When nodes are
        added, the corresponding values need to be inserted into lists."""
        self.neighbor_dict = {}
        self.explored_dict = {}

 
    def HasNode(self, node):
        """Does not use the dict.keys() method, which would generate a 
        new list of all nodes each time this is called."""
        return node in self.neighbor_dict

    def AddNode(self, node):
        """ Uses HasNode(node) to determine if node has already been added.
            Optional argument position is for later drawing. Positions are
            in range [0.0, 1.0] and represent fractions of drawing window size.
            Color is also for drawing.
        """
        if( self.HasNode(node) ):
            return
        self.neighbor_dict[node] = []
        self.explored_dict[node] = False
        
    def AddEdge(self, node1, node2, length):
        """
    Add node1 and node2 to network first if necessary.
    Adds new edge node1 -> node2 with length 'length'
    """
        if( not self.HasNode(node1) ):
            self.AddNode(node1)
        if( not self.HasNode(node2) ):
            self.AddNode(node2)
        neighbors = self.neighbor_dict[node1]
        neighbors.append((node2, length))
        self.neighbor_dict[node1] = neighbors


    def GetExplored(self, node):
        """ Get explorationn status of node """
        return self.explored_dict[node]
        

    def GetNextUnexploredNeighbor(self, node):
        """ Get a neighbor node which is still unexplored. If none exists,
            return -1 """
        for neighbor in self.GetNeighbors(node):
            if( not self.GetExplored(neighbor) ):
                return neighbor
        return -1
        
    def SetExplored(self, node, value):
        """ Mark node as explored """
        self.explored_dict[node] = value
        
    def GetNodes(self):
        """g.GetNodes() returns all nodes (keys) in neighbor_dict"""
        return self.neighbor_dict.keys()

    def GetNeighbors(self, node):
        """g.GetNeighbors(node) returns a copy of the list of neighbors of
        the specified node.  A copy is returned (using the [:] operator) so
        that the user does not inadvertently change the neighbor list."""
        result = []
        for neighbor in self.neighbor_dict[node]:
            result.append(neighbor[0])
        return result


    def GetEdgeLength(self, node1, node2):
        """ Get length of edge from node1 to node2 """
        result = 9999999999999999
        neighbors = self.neighbor_dict[node1]
        #print neighbors
        for neighbor in neighbors:
            if( neighbor[0] == node2 ):
                return neighbor[1]
        return result

    
    def GetNumExploredNodes(self):
        """ Return number of explored nodes """
        num = 0
        for key, value in self.explored_dict.items():
            if( value ): num += 1
        return num

    
    #def GetPosition(self, node):
    #    """ Returns drawing position of node
    #    """
    #    return self.positions[node]
    
    #def SetColor(self, node, color):
    #    """ Returns color of node
    #    """
    #    self.colors[node] = color
    
    #def GetColor(self, node):
    #    """ Returns color of node
    #    """
    #    return self.colors[node]
    
    def GetDegree(self, node):
        """ Returns degree of node, i.e. number of edges connected to it
        """
        return len(self.GetNeighbors(node))
    
    def GetOrderedDegrees(self):
        """ Returns list of nodes, ordered by degree
        """
        result = []
        nodes = self.GetNodes()
        for node in nodes:
            result.append((node, self.GetDegree(node)))
        return sorted(result, key=lambda result: result[1], reverse=True)

    def GetAllEdges(self):
        """ Returns list of all edges
        """
        result = []
        nodes = self.GetNodes()
        for node in nodes:
            neighbors = self.GetNeighbors(node)
            for neighbor in neighbors:
                result.append((node, neighbor))
        return result


def dijkstra(graph, s):
    """ Implement 'naive' Dijktstra's algorithm (no heaps) for graph 'graph'
        and start vertex s """
    n = len(graph.GetNodes())
    #print "Dijkstra: # nodes =", n
    X = [s]      # vertices processed so far
    A = {}      # computed shortest path distances
    A[s] = 0    # distance of start vertex to itself

    # main loop:
    while( len(A) < n ):
        dijkstra_greedy = 999999999999999999999
        v_star = -1
        w_star = -1
        for v in X:
            for w in graph.GetNeighbors(v):
                if( w not in X ):
                    current_dist = A[v] + graph.GetEdgeLength(v, w)
                    if( current_dist < dijkstra_greedy ):
                        v_star = v
                        w_star = w
                        dijkstra_greedy = current_dist
        X.append(w_star)
        A[w_star] = dijkstra_greedy
    # set default distances for unvisited nodes:
    for node in graph.GetNodes():
        if( node not in A.keys() ):
            A[node] = 1000000
    return A                

G = DirectedGraph()
n = int(input())
for city in range(1, n + 1):
    G.AddNode(city)
m = int(input())
for road in range(m):
    city1, city2, cost1, cost2 = [int(_) for _ in input().split(',')]
    G.AddEdge(city1, city2, cost1)
    G.AddEdge(city2, city1, cost2)
source, target, money, price = [int(_) for _ in input().split(',')]
d = dijkstra(G, source)
cost1 = d[target]
d = dijkstra(G, target)
cost2 = d[source]
print(money - price - cost1 - cost2)