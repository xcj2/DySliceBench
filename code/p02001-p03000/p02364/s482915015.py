class UnionFind:
    def __init__(self, N):
        # negative value: represents the root of a tree; its absolute value is the size of the tree
        # positive value: the parent's index
        self.vertices = [-1 for _ in range(N)]
        self.rank = [0] * N
        
    def find(self, v):
        if self.vertices[v] < 0: # v is a root
            return v
        else:
            # path compression: reconnect v to the root
            self.vertices[v] = self.find(self.vertices[v])
            return self.vertices[v]
        
    def union(self, u, v):
        s1 = self.find(u) # the root of the tree including vertex u
        s2 = self.find(v) # the root of the tree including vertex v
        
        if s1 == s2: # u and v is in the same tree
            return False
        
        if self.rank[s1] > self.rank[s2]: # the tree including u is taller
            self.vertices[s1] += self.vertices[s2] # update the size of the bigger tree
            self.vertices[s2] = s1
        else: # the tree including v is taller
            self.vertices[s2] += self.vertices[s1] # update the size of the bigger tree
            self.vertices[s1] = s2
            if self.rank[s1] == self.rank[s2]:
                self.rank[s2] += 1
        return True
        
    def is_connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def size(self, v):
        return -self.vertices[self.find(v)]
        
    def is_connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def size(self, v):
        return -self.vertices[self.find(v)]

class Kruskal:
    def __init__(self, N):
        self.N = N # #vertices
        self.E = []

    def add_edge(self, init, end, weight):
        self.E.append((weight, init, end))
        
    def min_spanning_tree(self):
        N, E = self.N, self.E
        weight = 0; edges = []
        n_edges = 0
        uf = UnionFind(N) # for judging connectivity
        E = sorted(E)
        for w, a, b in E:
            if uf.union(a, b):
                edges.append((a, b))
                n_edges += 1; weight += w
            if n_edges == N - 1: break
        return edges, weight

N, M = map(int, input().split())
kr = Kruskal(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    kr.add_edge(a, b, c)
_, ans = kr.min_spanning_tree()
print(ans)
