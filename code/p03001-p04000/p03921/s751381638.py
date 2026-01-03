from collections import defaultdict
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
    
lang = defaultdict(lambda: [])
N, M = inpl()
for i in range(N):
    L = inpl()[1:]
    for j in L:
        lang[j].append(i)
CF = UnionFind(N)
for Li in lang.values():
    t = Li[0]
    for j in Li:
        CF.union(t, j)
uni = [i for i in CF.par if i< 0]
if len(uni) == 1:
    print('YES')
else:
    print('NO')