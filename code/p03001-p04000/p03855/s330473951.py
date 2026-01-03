from collections import defaultdict

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
    
N, K, L = map(int, input().split())
uf_road = UnionFind(N)
uf_rail = UnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    uf_road.union(p-1, q-1)
for _ in range(L):
    r, s = map(int, input().split())
    uf_rail.union(r-1, s-1)
    
d = defaultdict(int)
comp = [(uf_road.find(i), uf_rail.find(i)) for i in range(N)]
for c in comp:
    d[c] += 1
    
print(*[d[c] for c in comp], sep=' ')