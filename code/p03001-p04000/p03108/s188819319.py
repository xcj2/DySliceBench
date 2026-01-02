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
        self.elem = [1 for i in range(self.n)]
        
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
            self.elem[ry] += self.elem[rx]
            self.elem[rx] = 0
        else:
            self.par[ry] = self.par[rx]
            self.elem[rx] += self.elem[ry]
            self.elem[ry] = 0
            
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
                
        return True
                
    def isSame(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
    
n,m = li()
ab = []

uf = UnionFind(n)
ans = [n*(n-1)//2]
cur = n*(n-1)//2

for _ in range(m):
    ab.append(list(li_()))
    
for _ in range(m):
    a,b = ab.pop()
    if uf.find(a) == uf.find(b):
        ans.append(cur)
        
    else:
        ra = uf.find(a)
        rb = uf.find(b)
        cur -= uf.elem[ra]*uf.elem[rb]
        
        ans.append(cur)
        
        uf.unite(ra, rb)
        
for ansi in ans[-2::-1]:
    print(ansi)