from collections import deque, defaultdict
import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

N = int(input())
S = [input().rstrip() for _ in range(N)]
uf = UnionFind(N)
for i in range(N):
    for j in range(i):
        if S[i][j] == '1':
            uf.unite(i, j)
depth = defaultdict(int)
for i in range(N):
    color = [-1] * N
    queue = deque()
    queue.append((i, 1))
    color[i] = 0
    max_d = 1
    while queue:
        j, d = queue.popleft()
        max_d = max(max_d, d)
        for k in range(N):
            if k == j or S[j][k] == '0':
                continue
            if color[k] == -1:
                color[k] = 1 - color[j]
                queue.append((k, d+1))
            elif color[k] == color[j]:
                print(-1)
                exit()
    depth[uf.find(i)] = max(depth[uf.find(i)], max_d)
ans = sum(depth[i] for i in range(N))
print(ans)