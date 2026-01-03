import bisect
import collections
import sys
import heapq

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 32


class UnionFind(object):
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

    def members_dict(self):
        pass

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def lmi():
    return list(map(int, input().split()))


def llmi_index(n):
    return [[i] + lmi() for i in range(n)]


N = int(input())
XY = llmi_index(N)
x_sorted = sorted(XY, key=lambda v: v[1])
y_sorted = sorted(XY, key=lambda v: v[2])
# print(x_sorted)
# # print(y_sorted)

uf = UnionFind(N)
cost_hq = []  # cost , index,index
for i in range(N - 1):
    cost = x_sorted[i + 1][1] - x_sorted[i][1]
    heapq.heappush(cost_hq, (cost, x_sorted[i][0], x_sorted[i + 1][0]))
for i in range(N - 1):
    cost = y_sorted[i + 1][2] - y_sorted[i][2]
    heapq.heappush(cost_hq, (cost, y_sorted[i][0], y_sorted[i + 1][0]))

ans = 0
while cost_hq:
    cost, index1, index2 = heapq.heappop(cost_hq)
    # print(cost, index1, index2)
    if uf.same(index1, index2):
        continue
    # print('join {},{}'.format(index1,index2))
    uf.union(index1, index2)
    ans += cost

print(ans)
