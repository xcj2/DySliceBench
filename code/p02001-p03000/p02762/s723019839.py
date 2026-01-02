import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m,k = map(int, input().split())
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
    
uf = UnionFindTree(n)
ns = [[] for _ in range(n)]
for i in range(m):
    a,b = map(lambda x: int(x)-1, input().split())
    uf.connect(a,b)
    ns[a].append(b)
    ns[b].append(a)

for i in range(k):
    c,d = map(lambda x: int(x)-1, input().split())
    ns[c].append(d)
    ns[d].append(c)
    
ans = [None]*n
for i in range(n):
    r = uf.root(i)
    s = uf.size[r]
    v = 0
    for j in ns[i]:
        if r==uf.root(j):
            v += 1
    ans[i] = s - v - 1
write(" ".join(map(str, ans)))