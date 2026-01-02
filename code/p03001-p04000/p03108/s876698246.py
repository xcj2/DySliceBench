# import sys
# import math
# import itertools
# from collections import deque
# from collections import defaultdict
# import heapq
# import copy
# import bisect
# import numpy as np
# from scipy.special import comb

# def my_input(): return sys.stdin.readline().rstrip()

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


def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M

    for i in range(M):
        A[i], B[i] = map(int, input().split())

    iland = [0] * M
    uf = UnionFind(N)
    for i in range(M-1, -1, -1):
        a = A[i] - 1
        b = B[i] - 1

        if uf.same(a, b):
            iland[i] = 0
        else:
            iland[i] = uf.size(a) * uf.size(b)

        uf.union(a, b)

    ans = [0] * M
    ans[0] = iland[0]
    for i in range(1, M):
        ans[i] = ans[i-1] + iland[i]

    for i in range(M):
        print(ans[i])


if __name__ == '__main__':
    main()
