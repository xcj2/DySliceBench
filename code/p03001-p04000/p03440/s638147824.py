from collections import defaultdict
import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

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
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

N, M = map(int, input().split())
a = list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(x, y)
group = defaultdict(list)
for i in range(N):
    group[uf.find(i)].append(a[i])
if len(group) == 1:
    print(0)
    exit()
ans = 0
rem = []
for k, v in group.items():
    v.sort()
    ans += v[0]
    rem += v[1:]
if len(rem) < len(group) - 2:
    print('Impossible')
else:
    rem.sort()
    ans += sum(rem[:len(group) - 2])
    print(ans)