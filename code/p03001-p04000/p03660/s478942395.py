import heapq
class Graph:
    def __init__(self,v,edgelist,w_v = None,directed = False):
        super().__init__()
        self.v = v
        self.w_e = [{} for _ in [0]*self.v]
        self.neighbor = [[] for _ in [0]*self.v]
        self.w_v = w_v
        self.directed = directed

        for i,j,w in edgelist:
            self.w_e[i][j] = w
            self.neighbor[i].append(j)

    def dijkstra(self,v_n):
        d = [float('inf')]*self.v
        d[v_n] = 0
        prev = [-1]*self.v

        queue = []
        for i,d_i in enumerate(d): heapq.heappush(queue,(d_i,i))
        
        while len(queue)>0:
            d_u,u = queue.pop()
            if d[u]<d_u :continue
            for v in self.neighbor[u]:
                alt = d[u]+self.w_e[u][v]
                if d[v]>alt:
                    d[v] = alt
                    prev[v] = u
                    heapq.heappush(queue,(alt,v))

        return d,prev

    def warshallFloyd(self):
        d = [[10**18]*self.v for _ in [0]*self.v]
        for i in range(self.v):
            d[i][i] = 0
            
        for i in range(self.v):
            for j in self.neighbor[i]:
                d[i][j] = self.w_e[i][j]
            
        for i in range(self.v):
            for j in self.neighbor[i]:
                d[i][j] = self.w_e[i][j]
        
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    check = d[i][k] + d[k][j]
                    if d[i][j] > check:
                        d[i][j] = check
        return d

    def prim(self):
        gb = GraphBuilder(self.v,self.directed)

        queue = []
        for i,w in self.w_e[0].items(): heapq.heappush(queue,(w,0,i))
        rest = [True]*self.v
        rest[0] = False

        while len(queue)>0:
            w,i,j = heapq.heappop(queue)
            if rest[j]:
                gb.addEdge(i,j,w)
                rest[j] = False
                for k,w in self.w_e[j].items():
                    if rest[k]:
                        heapq.heappush(queue,(w,j,k))

        return gb


class Tree():
    def __init__(self,v,e):
        pass

class GraphBuilder():
    def __init__(self,v,directed = False):
        self.v = v
        self.directed = directed
        self.edge = []

    def addEdge(self,i,j,w=1):
        if not self.directed:
            self.edge.append((j,i,w))
        self.edge.append((i,j,w))

    def addEdges(self,edgelist,weight = True):
        if weight:
            if self.directed:
                for i,j,w in edgelist:
                    self.edge.append((i,j,w))
            else:
                for i,j,w in edgelist:
                    self.edge.append((i,j,w))
                    self.edge.append((j,i,w))
        else:
            if self.directed:
                for i,j in edgelist:
                    self.edge.append((i,j,1))
            else:
                for i,j in edgelist:
                    self.edge.append((i,j,1))
                    self.edge.append((j,i,1))
            

    def addAdjMat(self, mat):
        for i,mat_i in enumerate(mat):
            for j,w in enumerate(mat_i):
                self.edge.append((i,j,w))

    def buildTree(self):
        pass

    def buildGraph(self):
        return Graph(self.v,self.edge,directed=self.directed)

def main():
    n = int(input())
    
    edge = [tuple([int(t)-1 for t in input().split()])for _ in [0]*(n-1)]

    gb = GraphBuilder(n)
    gb.addEdges(edge,False)

    g = gb.buildGraph()

    node = [0]*n

    head = [0]
    tail = [n-1]
    
    while len(head)>0 or len(tail)>0:
        t = []
        while len(head)>0:
            h = head.pop()
            for i in g.neighbor[h]:
                if node[i]==0:
                    t.append(i)
                    node[i] = 1
        head = t

        t = []
        while len(tail)>0:
            h = tail.pop()
            for i in g.neighbor[h]:
                if node[i]==0:
                    t.append(i)
                    node[i] = -1
        tail = t

    ans = sum(node)
    if ans>0:
        print("Fennec")
    else:
        print("Snuke")

if __name__ == "__main__":
    main()