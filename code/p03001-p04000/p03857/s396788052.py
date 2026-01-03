import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

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
    
from collections import defaultdict
    
n,k,l = li()
pq = []
rs = []

for _ in range(k):
    pq.append(tuple(li_()))
    
for _ in range(l):
    rs.append(tuple(li_()))

road = UnionFind(n)
rail = UnionFind(n)

for p,q in pq:
    road.unite(p,q)
    
for r,s in rs:
    rail.unite(r,s)
    
for i in range(n):
    road.find(i)
    
for i in range(n):
    rail.find(i)
    
road_dic = {i:set() for i in range(n)}
rail_dic = {i:set() for i in range(n)}

for i in range(n):
    road_dic[road.par[i]].add(i)
    rail_dic[rail.par[i]].add(i)
    
ans_dic = defaultdict(int)
for i in range(n):
    if ans_dic[(road.par[i], rail.par[i])] == 0:
        ans_dic[(road.par[i], rail.par[i])] = len(road_dic[road.par[i]] & rail_dic[rail.par[i]])
    
ans = []
for i in range(n):
    ans.append(ans_dic[(road.par[i], rail.par[i])])
    
print(*ans)