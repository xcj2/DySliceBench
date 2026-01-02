import itertools
import sys
import math
import numpy as np
from collections import deque
from itertools import combinations
from functools import reduce
from functools import lru_cache
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans


def main():
    N, M, K = map(int,input().split())
    friend = {}
    block = {}
    tree = UnionFind(N)

    for _ in range(M):
        a,b = map(lambda x:int(x)-1,input().split())
        tree.unite(a,b)
        for _ in range(2):
            if not a in friend.keys():
                friend[a] = [b]
            else:
                friend[a].append(b)
            a,b = b,a

    for _ in range(K):
        c,d = map(lambda x:int(x)-1,input().split())
        for _ in range(2):
            if not c in block.keys():
                block[c] = [d]
            else:
                block[c].append(d)
            c,d = d,c

    def solve(x):
        res = 0
        res += tree.get_size(x)

        if x in friend.keys():
            res -= len(friend[x])

        if x in block.keys():
            res -= len(list(filter(lambda y: tree.is_same_group(x,y),block[x])))

        return res - 1

    ans = []
    for i in range(N):
        ans.append(str(solve(i)))

    print(" ".join(ans))


if __name__ == "__main__":
  main()
