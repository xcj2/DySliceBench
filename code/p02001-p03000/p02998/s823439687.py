import sys
input = sys.stdin.readline
inpl = lambda: list(map(int,input().split()))
from collections import defaultdict

class UnionFind:
    def __init__(self, N=None):
        if N is None or N < 1:
            self.parent = defaultdict(lambda: -1)
        else:
            self.parent = [-1]*int(N)

    def root(self, n):
        if self.parent[n] < 0:
            return n
        else:
            m = self.root(self.parent[n])
            self.parent[n] = m
            return m

    def merge(self, m, n):
        rm = self.root(m)
        rn = self.root(n)
        if rm != rn:
            if -self.parent[rm] < -self.parent[rn]:
                rm, rn = rn, rm
            self.parent[rm] += self.parent[rn]
            self.parent[rn] = rm

    def size(self, n):
        return -self.parent[self.root(n)]
    
    def connected(self, m, n):
        return self.root(m) == self.root(n)
    
    def groups(self):
        if isinstance(self.parent,list):
            return list(map(lambda x: x<0, self.parent)).count(True)
        else: # self.parent: defaultdict
            return list(map(lambda x: x<0, self.parent.values())).count(True) 

class CountUp:
    def __init__(self, start=0):
        self.index = start-1

    def __call__(self):
        self.index += 1
        return self.index

Xi = defaultdict(CountUp())
Yi = defaultdict(CountUp())
N = int(input())
xy = []
for _ in range(N):
    x, y = inpl()
    xi = Xi[x]
    yi = Yi[y]
    xy.append((xi,yi))
Nx = len(Xi)
Ny = len(Yi)
Nxy = Nx + Ny
uf = UnionFind(Nx+Ny)
for xi, yi in xy:
    uf.merge(xi,yi+Nx)

gi = defaultdict(CountUp())
Ng = uf.groups()
edges = [0]*Ng
nx = [0]*Ng
ny = [0]*Ng
for i in range(Nx):
    nx[gi[uf.root(i)]] += 1
for i in range(Nx,Nxy):
    ny[gi[uf.root(i)]] += 1
for xi, yi in xy:
    edges[gi[uf.root(xi)]] += 1

ans = 0
for g in range(Ng):
    ans += nx[g]*ny[g] - edges[g]
print(ans)