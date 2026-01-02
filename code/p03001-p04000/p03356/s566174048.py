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

    def groups_num(self):
        if isinstance(self.parent,list):
            return len(list(filter(lambda x: x<0, self.parent)))
        else: # self.parent: defaultdict
            return len(list(filter(lambda x: x<0, self.parent.values())))

    def elements(self):
        if isinstance(self.parent,list):
            return range(len(self.parent))
        else:
            return self.parent.keys()

N, M = inpl()
p = inpl()
xy = [None]*M
for i in range(M):
    x, y = inpl()
    xy[i] = (x-1, y-1)

uf = UnionFind(2*N)
for i in range(N):
    uf.merge(i,(p[i]-1)+N)
for x, y in xy:
    uf.merge(x,y)
ans = 0
for i in range(N):
    if uf.connected(i,i+N):
        ans += 1
print(ans)