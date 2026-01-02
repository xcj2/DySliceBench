import sys
from collections import defaultdict
sys.setrecursionlimit(2*10**6)
class UF():
    def __init__(self, num):
        self.par = [-1]*num
        self.size = [1]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.size[rx] += self.size[ry] 
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.size[ry] += self.size[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.size[rx] += self.size[ry]
        return



N = int(input())

XY = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
X, Y = list(map(list, zip(*XY)))
G = UF(N)
checked = [False]*N

Xc = defaultdict(list)
Yc = defaultdict(list)
for i in range(N):
    Xc[X[i]].append(i)
    Yc[Y[i]].append(i)

for v in Xc.values():
    if len(v) == 1:
        continue
    vx = v[0]
    for x in v[1:]:
        G.union(vx, x)

for v in Yc.values():
    if len(v) == 1:
        continue
    vy = v[0]
    for y in v[1:]:
        G.union(vy, y)

ans = -N

Zx = defaultdict(set)
Zy = defaultdict(set)
for i in range(N):
    ri = G.find(i)
    Zx[ri].add(X[i])
    Zy[ri].add(Y[i])

for i in range(N):
    ri = G.find(i)
    if checked[ri] == True:
        continue
    checked[ri] = True
    ans += len(Zx[ri])*len(Zy[ri])
print(ans)