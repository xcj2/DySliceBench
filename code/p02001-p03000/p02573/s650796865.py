from collections import Counter

class union:
    def __init__(self,x):
        self.par = list(range(x))

    def root(self,x):
        S = set()
        S.add(x)
        y = x
        while True:
            if self.par[y] == y:
                for s in S:
                    self.par[s] = y
                return y
            S.add(y)
            y = self.par[y]

    def unite(self,x,y):
        rx = self.root(x)
        ry = self.root(y)
        self.par[rx] = ry

    def same(self,x,y):
        return self.root(x) == self.root(y)

N,M = map(int,input().split())
a,b = 0,0
U = union(N)
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    U.unite(a,b)

C = Counter([U.root(x) for x in range(N)])
print(max(C.values()))