#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict
INF = float("inf")


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


class UnionFind(object):

    def __init__(self, N):
        self.tree = list(range(N))

    def root(self, i):
        if self.tree[i] == i:
            return i
        else:
            self.tree[i] = self.root(self.tree[i])
            return self.tree[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.tree[x] = y


def main():

    N, M = map(int, input().split())
    L = [0]*N
    lang_leader = defaultdict(int)
    for i in range(N):
        K, *L[i] = list(map(int, input().split()))
    # 前Nは人
    uf = UnionFind(N+1)
    for i in range(N):
        for l in L[i]:
            if lang_leader[l] == 0:
                lang_leader[l] = i+1
            else:
                uf.unite(i, lang_leader[l]-1)

    # print(uf.tree)
    # 人はすべて同じグループであるか
    flag = True
    for i in range(N):
        if not uf.same(0, i):
            flag = False
            break
    if flag:
        yes()
    else:
        no()

    pass


if __name__ == '__main__':
    main()
