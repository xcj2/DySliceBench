import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

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
    
    
# edgesは(cost, prev_node, nex_node)をE本格納しているリスト
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

n = ni()
city = []

for i in range(n):
    city.append([i] + list(li()))

# x,y順にソートして2(N-1)本の辺の候補を出す (cost, from, to)
edges = []

city.sort(key=lambda x:x[1])
for i in range(n-1):
    edges.append((city[i+1][1] - city[i][1], city[i][0], city[i+1][0]))

city.sort(key=lambda x:x[2])
for i in range(n-1):
    edges.append((city[i+1][2] - city[i][2], city[i][0], city[i+1][0]))

# クラスカル法
ans = kruskal(edges, n)

print(ans)