inpl = lambda: list(map(int,input().split()))
import numpy as np
class ParityTree:
    def __init__(self,N):
        self.parent = [-1]*int(N)
        self.parity = [0]*int(N)

    def root(self, n):
        if self.parent[n] < 0:
            return n, 0
        else:
            m, p = self.root(self.parent[n])
            self.parent[n] = m
            self.parity[n] = (p + self.parity[n]) % 2
            return m, self.parity[n]

    def merge(self, m, n, parity):
        rm, pm = self.root(m)
        rn, pn = self.root(n)
        if rm != rn:
            if -self.parent[rm] < -self.parent[rn]:
                rm, rn = rn, rm
            self.parent[rm] += self.parent[rn]
            self.parent[rn] = rm
            self.parity[rn] = (pm + pn + parity) % 2

    def size(self, n):
        return -self.parent[self.root(n)]
    
    def aresame(self, m, n):
        return self.root(m) == self.root(n)

N, M = inpl()
pt = ParityTree(N)
for i in range(M):
    X, Y, Z = inpl()
    pt.merge(X-1,Y-1,Z)

print(len(np.where(np.array(pt.parent)<0)[0]))