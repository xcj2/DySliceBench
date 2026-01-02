from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
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
unionfind = UnionFind(n)
x_d = defaultdict(set)
y_d = defaultdict(set)
for i in range(n):
    x_d[data[i][0]].add(i)
    y_d[data[i][1]].add(i)

for i in range(n):
    x, y = data[i]
    if len(x_d[x]) > 1 and len(y_d[y]) > 1:
        for j in x_d[x]:
            unionfind.union(i, j)
        for j in y_d[y]:
            unionfind.union(i, j)

point = [[] for i in range(n)]
for i in range(n):
    if unionfind.size(i) <= 2:
        continue
    else:
        point[unionfind.find(i)].append(i)
ans = 0
for i in range(n):
    if len(point[i]) > 2 :
        x_s = set()
        y_s = set()
        for j in point[i]:
            x, y = data[j]
            x_s.add(x)
            y_s.add(y)
        ans += len(x_s) * len(y_s) - len(point[i])
print(ans)
