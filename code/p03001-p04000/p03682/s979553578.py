import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, node:int) -> None:
        self.n = node
        self.par = [i for i in range(self.n)]
        self.rank = [0 for i in range(self.n)]
        
    def find(self, x:int) -> int:
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def unite(self, x:int, y:int) -> bool:
        if self.isSame(x,y):
            #print("x and y has already united")
            return False
        
        rx = self.find(x)
        ry = self.find(y)
        
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = self.par[ry]
        else:
            self.par[ry] = self.par[rx]
            
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
                
        return True
                
    
    def isSame(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
    
    
def kruskal(edges: list, node_num: int) -> int:
    edges.sort(key=lambda x:x[0])
    
    uf = UnionFind(node_num)
    rem = node_num-1
    ans = 0
    
    for cost, prev, nex in edges:
        if uf.find(prev) != uf.find(nex):
            uf.unite(prev, nex)
            ans += cost
            rem -= 1
            
        if rem == 0:
            break
        
    return ans


N = int(input().rstrip())

town = []
for i in range(N):
    x,y = map(int, input().split())
    town.append(tuple([i,x,y]))


edges = []
for xy in [1,2]:
    town.sort(key=lambda x: x[xy])
    
    for i in range(N-1):
        edges.append(tuple([town[i+1][xy] - town[i][xy],town[i+1][0], town[i][0]]))
        
        
ans = kruskal(edges, N)
print(ans)
