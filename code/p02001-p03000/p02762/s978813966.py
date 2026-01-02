class UnionFind:
    def __init__(self, N):
        # Union find with component size
        # Negative means is a root where value is component size
        # Otherwise is index to parent
        self.p = [-1 for i in range(N)]

    def find(self, i):
        # Find root with path compression
        if self.p[i] >= 0:
            self.p[i] = self.find(self.p[i])
            return self.p[i]
        else:
            return i

    def union(self, i, j):
        # Union by size
        root1 = self.find(j)
        root2 = self.find(i)
        if root1 == root2:
            return
        size1 = -self.p[root1]
        size2 = -self.p[root2]
        if size1 < size2:
            self.p[root1] = root2
            self.p[root2] = -(size1 + size2)
        else:
            self.p[root2] = root1
            self.p[root1] = -(size1 + size2)

    def getComponentSize(self, i):
        return -self.p[self.find(i)]


from collections import defaultdict

N, M, K = list(map(int, input().split()))
friend = defaultdict(set)
for i in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    friend[a].add(b)
    friend[b].add(a)
block = defaultdict(set)
for i in range(K):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    block[c].add(d)
    block[d].add(c)

uf = UnionFind(N)
for a, friends in friend.items():
    for b in friends:
        uf.union(a, b)

out = []
for a in range(N):
    count = uf.getComponentSize(a) - 1 - len(friend[a])
    for b in block[a]:
        if uf.find(a) == uf.find(b):
            count -= 1
    out.append(str(count))
print(" ".join(out))

