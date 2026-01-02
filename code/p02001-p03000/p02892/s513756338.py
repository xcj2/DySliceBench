from collections import deque

class UnionFind:
    def __init__(self, n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)



n = int(input())
s = [input() for _ in range(n)]

min_i = 0
min_count = n + 1
for i in range(n):
    count = 0
    for j in range(n):
        if s[i][j]:
            count += 1
    if count < min_count:
        min_count = count
        min_i = i

uf = UnionFind(n)

INF = 1001001001
ans = 0

for min_i in range(n):
    dist = [INF] * n
    dist[min_i] = 0
    q = deque([(min_i, 0, -1)])

    while q:
        v, d, p = q.popleft()
        box = []
        for nv in range(n):
            if s[v][nv] == '1':
                if nv == p:
                    continue
                if uf.same(v, nv):
                    print(-1)
                    exit()
                if d + 1 < dist[nv]:
                    dist[nv] = d + 1
                    q.append((nv, d + 1, v))
                    box.append(nv)
        for i in range(len(box) - 1):
            uf.merge(box[i], box[i + 1])
    ans = max(ans, max(dist) + 1)

print(ans)
