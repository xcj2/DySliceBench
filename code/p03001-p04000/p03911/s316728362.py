from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for _ in range(N)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def connectedNum(self, x):
        return self.size[self.find(x)]


N, M = map(int, input().split())
Un = UnionFind(N)  # 会話できる人をつなげる
D = defaultdict(lambda: [])
for i in range(N):
    _, *L = map(lambda x: int(x)-1, input().split())
    for l in L:
        D[l].append(i)
for i in range(M):
    if len(D[i]) > 1:
        t = D[i]
        for d in t[1:]:
            Un.union(t[0], d)
print("YES" if Un.connectedNum(0) == N else "NO")
