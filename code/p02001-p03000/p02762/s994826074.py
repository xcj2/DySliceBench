class UnionFind:
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.size = [1] * (n + 1)

    def root(self, x: int) -> int:
        if self.par[x] == x: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x: int, y: int):
        root_x, root_y = self.root(x), self.root(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.size[root_x] += self.size[root_y]
            self.par[root_y] = root_x

    def check(self, x: int, y: int) -> bool:
        root_x, root_y = self.root(x), self.root(y)
        return root_x == root_y


from collections import defaultdict
N, M, K = map(int, input().split())

u = UnionFind(N)

ABm = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    ABm[a].append(b)
    ABm[b].append(a)
    u.unite(a, b)

CDk = defaultdict(list)
for _ in range(K):
    c, d = map(int, input().split())
    CDk[c].append(d)
    CDk[d].append(c)

ans = []
for i in range(1, N + 1):
    size = u.size[u.root(i)]
    block = 0
    for x in CDk[i]:
        if u.check(x, i): block += 1

    friends = len(ABm[i])
    res = size - block - friends - 1
    ans.append(str(res))

print(" ".join(ans))