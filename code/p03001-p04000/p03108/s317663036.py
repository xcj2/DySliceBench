import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


class UnionFindTree:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, i):
        inter = set()
        while self.parent[i]!=i:
            inter.add(i)
            i = self.parent[i]
        r = i
        for i in inter:
            self.parent[i] = r
        return r

    def connect(self, i, j):
        if i==j:
            return
        ri = self.root(i)
        rj = self.root(j)
        if ri==rj:
            return
        if self.size[ri]<self.size[rj]:
            self.parent[ri] = rj
            self.size[rj] += self.size[ri]
        else:
            self.parent[rj] = ri
            self.size[ri] += self.size[rj]
    
n,m = map(int, input().split())
uf = UnionFindTree(n)
ans = [None] * m
val = n * (n-1) // 2
ab = [None] * m
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    ab[i] = (a,b)
i = 0
for a,b in ab[::-1]:
    ans[m-1-i] = val
    i += 1
    ra = uf.root(a)
    rb = uf.root(b)
    if ra==rb:
        pass
    else:
        val -= uf.size[ra] * uf.size[rb]
    uf.connect(a,b)
write("\n".join(map(str, ans)))
