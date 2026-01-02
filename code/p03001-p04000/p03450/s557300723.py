import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class UnionFindWeighted:
    # Reference: https://note.nkmk.me/python-union-find/
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.weight = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            root = self.find(self.parents[x])
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = root
            return root

    def union(self, x, y, w):
        w += -self.weight[x] + self.weight[y]

        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y, w = y, x, -w

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.weight[y] = -w

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


def main():
    N, M, *LRD = map(int, read().split())

    uf = UnionFindWeighted(N)
    for l, r, d in zip(*[iter(LRD)] * 3):
        l -= 1
        r -= 1
        if uf.same(l, r) and uf.diff(l, r) != d:
            print('No')
            return
        else:
            uf.union(l, r, d)

    print('Yes')
    return


if __name__ == '__main__':
    main()
