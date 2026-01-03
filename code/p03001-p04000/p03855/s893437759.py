import sys
from collections import Counter

sys.setrecursionlimit(10 ** 5)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y

        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def check_same(self, x, y):
        return self.find(x) == self.find(y)


N, K, L = map(int, input().split())
r_union_find = UnionFind(N)
t_union_find = UnionFind(N)
for i in range(K):
    p, q = map(int, input().split())
    r_union_find.union(p, q)

for i in range(L):
    r, s = map(int, input().split())
    t_union_find.union(r, s)

pair = []

for i in range(1, N + 1):
    count = 0
    r_p = r_union_find.find(i)
    t_p = t_union_find.find(i)
    pair.append((r_p, t_p))

counter = Counter(pair)

answers = []
for p in pair:
    answers.append(counter[p])

answers = map(str, answers)
print(" ".join(answers))
