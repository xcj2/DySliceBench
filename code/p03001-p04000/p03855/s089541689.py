n, k, l = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(k)]
rs = [list(map(int, input().split())) for _ in range(l)]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

u1 = UnionFind(n)
for i in range(k):
    u1.union(pq[i][0], pq[i][1])

u2 = UnionFind(n)
for i in range(l):
    u2.union(rs[i][0], rs[i][1])

for i in range(n):
    a = u1.find(i + 1)
    b = u2.find(i + 1)

from collections import defaultdict
d = defaultdict(list)
for i in range(1, len(u1.par)):
    d[str(u1.par[i]) + ' ' + str(u2.par[i])].append(i)

ans = [0] * n
for k in d.keys():
    for v in d[k]:
        ans[v - 1] = len(d[k])

ans2 = ''
for i in range(len(ans)):
    ans2 += str(ans[i]) + ' '

print(ans2[:-1])
