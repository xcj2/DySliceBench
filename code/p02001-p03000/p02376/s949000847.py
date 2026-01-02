from collections import deque

class Edge:
    def __init__(self, fromNode, toNode, cap, rev=None):
        self.fromNode = fromNode
        self.toNode = toNode
        self.cap = cap
        self.rev = rev

class MaxFlow:
    def __init__(self, V):
        self.v = V
        self.edges = [[] for _ in range(V)]

    def addEdge(self, fromNode, toNode, cap):
        forEdge = Edge(fromNode, toNode, cap)
        backEdge = Edge(toNode, fromNode, 0)
        forEdge.rev = backEdge
        backEdge.rev = forEdge
        self.edges[fromNode].append(forEdge)
        self.edges[toNode].append(backEdge)
    
    def bfs(self, source, sink):
        self.level = [None] * self.v
        self.level[source] = 0
        que = deque()
        que.append(source)
        while que:
            node = que.popleft()
            newLevel = self.level[node] + 1
            for edge in self.edges[node]:
                if edge.cap and self.level[edge.toNode] is None:
                    self.level[edge.toNode] = newLevel
                    que.append(edge.toNode)

        return self.level[sink] is not None

    def dfs(self, node, sink, f):
        if node == sink: return f

        for edge in self.edges[node]:
            if edge.cap and self.level[edge.fromNode] < self.level[edge.toNode]:
                newFlow = self.dfs(edge.toNode, sink, min(f, edge.cap))
                if newFlow:
                    edge.cap -= newFlow
                    edge.rev.cap += newFlow
                    return newFlow

        return 0
    
    def run(self, source, sink):
        flow = 0
        INF = 10 ** 10
        while self.bfs(source, sink):
            addFlow = INF
            while addFlow:
                addFlow = self.dfs(source, sink, INF)
                flow += addFlow

        return flow

V, E = map(int, input().split())
net = MaxFlow(V)
for _ in range(E):
    u, v, c = map(int, input().split())
    net.addEdge(u, v, c)
print(net.run(0, V - 1))
