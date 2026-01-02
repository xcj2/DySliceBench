import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

class UnionFind:
    def __init__(self,n):
        self.ps = [-1]*(n+1)
    def find(self,x):
        if self.ps[x]<0:
            return x
        else:
            self.ps[x]=self.find(self.ps[x])
            return self.ps[x]
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return False
        if self.ps[x]>self.ps[y]:
            x,y = y,x
        self.ps[x] += self.ps[y]
        self.ps[y] = x
        return True
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def size(self,x):
        x = self.find(x)
        return -self.ps[x]

n,m,k = nm()
ed = [nl() for _ in range(m)]
bl = [nl() for _ in range(k)]
al = [0]*n
uf = UnionFind(n)
for a,b in ed:
    uf.unite(a,b)
    al[a-1] += 1
    al[b-1] += 1
ans = [uf.size(x)-1-al[x-1] for x in range(1,n+1)]
for a,b in bl:
    if uf.same(a,b):
        ans[a-1] -= 1
        ans[b-1] -= 1
print(*ans)
