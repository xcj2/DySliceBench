from collections import defaultdict
from copy import deepcopy
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


class UnionFind():
    def __init__(self, n):
        self.n = n
        # 各要素の親要素 親は -(その集合の要素数)
        self.parents = [-1] * n

    def find(self, x):
        '''要素 x の親要素の番号を返す'''
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        '''要素 x が属する集合と要素 y が属する集合を併合する'''
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        '''要素 x が属する集合の要素数を返す'''
        return -self.parents[self.find(x)]

    def same(self, x, y):
        '''要素 x と要素 y が同じ集合に属するかを返す'''
        return self.find(x) == self.find(y)

    def members(self, x):
        '''要素 x が属する集合の要素をリストを返す'''
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
    n, m = LI()
    edges = [LI() for _ in range(m)]
    ans = 0
    for remove_u, remove_v in edges:
        uf = UnionFind(n)
        for u, v in edges:
            if u == remove_u and v == remove_v:
                continue
            u, v = u - 1, v - 1
            uf.union(u, v)
        if len(uf.roots()) > 1:
            ans += 1
    print(ans)


main()
