nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

N, M = nl()


edges = []
for i in range(M):
    A, B = nl()
    edges.append((A, B))

class UnionFind(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.sizes[x] < self.sizes[y]:
            self.parents[x] = y
            self.sizes[y] += self.sizes[x]
        else:
            self.parents[y] = x
            self.sizes[x] += self.sizes[y]

uf = UnionFind(N)
res = [N*(N-1)//2]
for a, b in edges[::-1]:
    ra = uf.find(a-1)
    rb = uf.find(b-1)
    if ra != rb:
        new_res = res[-1] - uf.sizes[ra] * uf.sizes[rb]
    else:
        new_res = res[-1]
    uf.union(a-1, b-1)
    res.append(new_res)

res = res[::-1]
for r in res[1:]:
    print(r)

