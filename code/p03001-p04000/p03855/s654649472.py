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
    
from collections import defaultdict
import sys
sdin = sys.stdin.readline    

# 入力
n, k, l = map(int, sdin().split())

pq = []
for i in range(k):
    p, q = map(int, sdin().split())
    pq.append(tuple([p-1, q-1]))

rs = []
for i in range(l):
    r, s = map(int, sdin().split())
    rs.append(tuple([r-1, s-1]))

# 道路、鉄道についてそれぞれunion find
path = UnionFind(n)
for p, q in pq:
    path.unite(p, q)

rail = UnionFind(n)
for r, s in rs:
    rail.unite(r, s)

# (path.root, rail.root)の辞書作る
path_rail = defaultdict(int)
    
for i in range(n):
    path_rail[(path.find(i), rail.find(i))] += 1

# 表示する
ans = [path_rail[(path.find(i), rail.find(i))] for i in range(n)]
print(*ans)
