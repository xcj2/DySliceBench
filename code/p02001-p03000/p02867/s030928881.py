N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for a,b in zip(sorted(A), sorted(B)):
    if a>b:
        print('No')
        exit()

BA = [(b,a) for a,b in zip(A,B)]
BA.sort()

AI = [(a,i) for i,(b,a) in enumerate(BA)]
AI.sort()

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
for j,(a,i) in enumerate(AI):
    uf.unite(i,j)
roots = set()
for i in range(N):
    roots.add(uf.root(i))
if(len(roots) > 1):
    print('Yes')
    exit()

for a,b in zip(list(sorted(A))[1:], sorted(B)):
    if a <= b:
        print('Yes')
        exit()
print('No')