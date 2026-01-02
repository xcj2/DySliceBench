class Union_Find():
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]
        self.height = [0 for i in range(N)]
    def Find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.Find(self.par[x])
        return self.par[x]
    def Union(self, x, y):
        x, y = self.Find(x), self.Find(y)
        if self.height[x] < self.height[y]:
            self.par[x] = y
        else:
            self.par[y] = self.par[x]
            if self.height[x] == self.height[x]:
                self.height[x] += 1
    def Same(self, x, y):
        return Find(x) == Find(y)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(M):
    uf = Union_Find(N)
    for j in range(M):
        if i == j:
            continue
        uf.Union(edges[j][0] - 1, edges[j][1] - 1)
    cnt = 0
    for i in range(N):
        if uf.par[i] == i:
            cnt += 1
    if cnt > 1:
        ans += 1
print(ans)