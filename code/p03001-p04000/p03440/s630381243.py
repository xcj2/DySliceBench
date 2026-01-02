N,M = map(int,input().split())
A = list(map(int,input().split()))
XY = [tuple(map(int,input().split())) for i in range(M)]

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1
uf = UnionFind(N)

for x,y in XY:
    if uf.is_same(x,y): continue
    uf.unite(x,y)

re = N - uf.count
if re==1:
    print(0)
    exit()
v = (re-1)*2
if v > N:
    print('Impossible')
    exit()

for i in range(N):
    uf.root(i)
ans = 0
used = [0]*N
d = {}
for i in range(N):
    r = uf.root(i)
    if r in d:
        if d[r][0] > A[i]:
            d[r] = (A[i], i)
    else:
        d[r] = (A[i], i)

for a,b in d.values():
    ans += a
    used[b] = 1
rem = v-re
notused = []
for i in range(N):
    if used[i]: continue
    notused.append(A[i])
notused.sort()
ans += sum(notused[:rem])
print(ans)