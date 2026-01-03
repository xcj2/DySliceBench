import bisect
import collections
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 32


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


N, K, L = lmi()
pq = llmi(K)
rs = llmi(L)


class _UnionFind(object):
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


class UnionFind(_UnionFind):
    pass


uf_road = UnionFind(N)
for p, q in pq:
    uf_road.union(p - 1, q - 1)
uf_train = UnionFind(N)
for p, q in rs:
    uf_train.union(p - 1, q - 1)
# road_dict = collections.defaultdict(set)  # parent node -> set of member
# train_dict = collections.defaultdict(set)
# for i in range(N):
#     road_dict[uf_road.find(i)].add(i)
#     train_dict[uf_train.find(i)].add(i)
#
# print(' '.join(str(len(road_dict[uf_road.find(i)]&train_dict[uf_train.find(i)])) for i in range(N)))

d = collections.defaultdict(int)
for i in range(N):
    key = uf_road.find(i), uf_train.find(i)
    d[key] += 1

print(' '.join(str(d[(uf_road.find(i), uf_train.find(i))]) for i in range(N)))
