import sys

# import math
# import bisect

# import copy
# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
# INF = sys.maxsize
# MOD = 10 ** 9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()


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

    n, m = map(int, input().split())

    d = []
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d.append((a, b))

    d.reverse()
    ans = []
    a = n*(n-1)//2
    que = UnionFind(n)

    for i in range(m):
        ans.append(a)
        x,y = d[i]
        if not que.same(x,y):
            a -= que.size(x)*que.size(y)
            que.union(x,y)

    ans.reverse()
    for tmp_a in ans:
        print(tmp_a)


if __name__ == '__main__':
    main()
