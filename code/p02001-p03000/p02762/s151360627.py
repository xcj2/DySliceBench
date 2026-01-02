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
# sys.setrecursionlimit(100000)
# INF = 1001001001001
# MOD = 1000000007

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

    N, M, K = map(int, input().split())

    uf = UnionFind(N)
    friends = [set() for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        uf.union(a, b)
        friends[a] |= set([b])
        friends[b] |= set([a])

    blocks = [set() for _ in range(N)]
    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        if uf.same(c, d):
            blocks[c] |= set([d])
            blocks[d] |= set([c])

    # print(uf)
    # print(friends)
    # print(blocks)

    for i in range(N - 1):
        ans = uf.size(i) - 1 - len(friends[i]) - len(blocks[i])
        print(str(ans) + " ", end="")

    ans = uf.size(N - 1) - 1 - len(friends[N - 1]) - len(blocks[N - 1])
    print(ans)


if __name__ == '__main__':
    main()
