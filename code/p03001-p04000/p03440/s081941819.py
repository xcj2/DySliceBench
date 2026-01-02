import sys
input = sys.stdin.readline
from collections import defaultdict
 
class Unionfind:
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [1]*n
    
    def root(self, x):
        p = x
        
        while not self.par[p]<0:
            p = self.par[p]
        
        while x!=p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p
        
        return p
    
    def unite(self, x, y):
        rx, ry = self.root(x), self.root(y)
        
        if rx==ry: return False
        
        if self.rank[rx]<self.rank[ry]:
            rx, ry = ry, rx
        
        self.par[rx] += self.par[ry]
        self.par[ry] = rx
    
        if self.rank[rx]==self.rank[ry]:
            self.rank[rx] += 1
    
    def is_same(self, x, y):
        return self.root(x)==self.root(y)
    
    def count(self, x):
        return -self.par[self.root(x)]

N, M = map(int, input().split())
a = list(map(int, input().split()))
uf = Unionfind(N)

for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(x, y)

d = defaultdict(list)

for i in range(N):
    d[uf.root(i)].append(a[i])

keys = list(d.keys())

if len(keys)==1:
    print(0)
    exit()

if N<2*(len(keys)-1):
    print('Impossible')
    exit()
    
for k in keys:
    d[k].sort()

ans = 0
l = []

for k in keys:
    ans += d[k][0]
    l += d[k][1:]

l.sort()
ans += sum(l[:len(keys)-2])

print(ans)