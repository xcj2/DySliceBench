# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

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

dic = defaultdict(list)

n,m = li()

# 各言語を話せる人を登録
for i in range(n):
    l_list = li()
    for l in l_list[1:]:
        dic[l].append(i)
        
# union-findでマージしていく
uf = UnionFind(n)
for key in dic.keys():
    val = dic[key]
    for i in range(len(val)-1):
        if not uf.isSame(val[i], val[i+1]):
            uf.unite(val[i], val[i+1])
            
root = uf.find(0)
for i in range(n):
    if uf.find(i) != root:
        print("NO")
        break
    
    if i == n-1:
        print("YES")