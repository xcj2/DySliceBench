import sys
input = sys.stdin.readline

# 組み合わせ　n_C_r
def comb(n,r):
    r = min(r,n-r)
    result = 1
    for i in range(n-r+1,n+1):
        result *= i
    for i in range(1,r+1):
        result //= i
    return result

class Unionfind:

    __slots__ = ['nodes','size']

    def __init__(self, n):
        self.nodes = list(range(n))
        self.size = [1]*n

    def root(self, x):
        if self.nodes[x] == x:
            return x
        else:
            root_x = self.root(self.nodes[x])
            self.nodes[x] = root_x
            return root_x

    def unite(self, x, y):
        x = self.root(x); y = self.root(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.nodes[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

N,M = map(int,input().split())
info = [[int(e)-1 for e in input().split()] for _ in range(M)]

uf = Unionfind(N)
out = []
ans = comb(N,2)
out.append(ans)
for A,B in info[::-1]:
    if not uf.same(A,B):
        ans -= uf.size[uf.root(A)] * uf.size[uf.root(B)]
    uf.unite(A,B)
    out.append(ans)

for q in out[-2::-1]:
    print(q)