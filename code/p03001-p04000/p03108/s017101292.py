import sys

class UnionFind():
    def __init__(self, num):
        self.par = [-1]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        prx = self.par[rx]
        pry = self.par[ry]
        if rx != ry:
            if prx <= pry:
                self.par[ry] = rx 
                self.par[rx] += pry
            else:
                self.par[rx] = ry
                self.par[ry] += prx
        return

def inpl(): return list(map(int, input().split()))
input = sys.stdin.readline

N, M = inpl()
Edge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

UF = UnionFind(N)
ic = N*(N-1)//2
Ans = []
for i, (a, b) in enumerate(Edge[::-1]):
    Ans.append(ic)
    ra = UF.find(a)
    rb = UF.find(b)
    if ra != rb:
        ic -= UF.par[ra]*UF.par[rb]
        UF.union(a, b)
for a in Ans[::-1]:
    print(a)
