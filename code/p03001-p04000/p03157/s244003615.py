class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

H,W = map(int,input().split())
N = H*W
def num(i,j):
    return i*W+j
def coo(num):
    i = num // W
    j = num % W
    return(i,j)

uf = UnionFind(N)
color = [-1]*N
grid = []
for i in range(H):
    grid.append(list(input()))
for i in range(H):
    for j in range(W):
        color[num(i,j)]= grid[i][j]
for i in range(H):
    for j in range(W-1):
        if grid[i][j] != grid[i][j+1]:
            uf.union(num(i,j),num(i,j+1))
for i in range(H-1):
    for j in range(W):
        if grid[i][j] != grid[i+1][j]:
            uf.union(num(i,j),num(i+1,j))
ans = 0
BW = [[0,0] for _ in range(N)]
for i in range(N):
    root = uf.find(i)
    if color[i] == "#":
        BW[root][0] += 1
    else:
        BW[root][1] += 1
for root in uf.roots():
    ans += BW[root][0]*BW[root][1]
print(ans)