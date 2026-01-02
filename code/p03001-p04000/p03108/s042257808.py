import sys

class UnionFind():
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
        ic -= UF.size[ra]*UF.size[rb]
        UF.union(a, b)
for a in Ans[::-1]:
    print(a)
