from collections import defaultdict as dd
n, m = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))

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

uf = UnionFind(n)
#print(P)
for i in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    uf.union(x, y)

#dic[root] -> [i1, i2, ...]
dic_idx = dd(set)
#dic[root] -> [p1, p2, ...]
dic_p = dd(set)
visited_root = set()

for i, p in enumerate(P):
    root = uf.find(i)
    visited_root.add(root)
    dic_idx[root].add(i)
    dic_p[root].add(p)

#print(dic_idx)
#print(dic_p)
#print(visited_root)

ans = 0
for root in list(visited_root):
    #print(root, dic_idx[root] & dic_p[root])
    ans += len(dic_idx[root] & dic_p[root])
print(ans)