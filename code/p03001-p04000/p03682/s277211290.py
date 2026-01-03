import sys
import copy
import heapq
from collections import deque
import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize


# ===CODE===
def main():
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

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    n = int(input())
    tree = UnionFind(n)

    edges_x = []
    edges_y = []
    for i in range(n):
        x, y = map(int, input().split())
        edges_x.append((x, i))
        edges_y.append((y, i))

    edges_x.sort()
    edges_y.sort()

    edges = []
    for i in range(n - 1):
        tmp = abs(edges_x[i][0] - edges_x[i + 1][0])
        edges.append((tmp, edges_x[i][1], edges_x[i + 1][1]))
        tmp = abs(edges_y[i][0] - edges_y[i + 1][0])
        edges.append((tmp, edges_y[i][1], edges_y[i + 1][1]))

    edges.sort()

    ans = 0
    for d, s, t in edges:
        if not tree.same(s, t):
            tree.union(s, t)
            ans += d

    print(ans)


# ===main===
if __name__ == '__main__':
    main()
