def inpl(): return [int(i) for i in input().split()]
class UnionFind():
    def __init__(self, num):
        self.par = [-1 for _ in range(num)]
    
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
            if self.par[rx] > self.par[ry]:
                self.par[rx] = ry
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
        return

from collections import defaultdict
H = defaultdict(lambda: set([]))
H1 = defaultdict(lambda: set([]))
N, M = inpl()
p = inpl()
deer = UnionFind(N)
for _ in range(M):
    x, y = inpl()
    deer.union(x-1,y-1)

for i in range(N):
    H[deer.find(i)].add(i+1)
    H1[deer.find(i)].add(p[i])
    
ans =0
for i in H:
    ans += len(H[i] & H1[i])
print(ans)