# coding:utf-8

import sys
from collections import deque, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


# UnionFind
class UnionFind:
    # 負: ルートで値は木のサイズを表す
    # 正: 子で値は次のノードを表す
    def __init__(self, size: int) -> None:
        self.nodes = [-1] * size  # 初期状態では全てのノードがルート

    def find(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size(x) < self.size(y):
            rx, ry = ry, rx

        self.nodes[rx] += self.nodes[ry]
        self.nodes[ry] = rx

        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return - self.nodes[self.find(x)]


def main():
    n, m = LI()

    uf = UnionFind(n)
    res = deque()
    res.append(n * (n - 1) // 2)
    AB = [LI_() for _ in range(m)]
    AB.reverse()
    for a, b in AB:
        if uf.same(a, b):
            res.append(res[-1])
            continue

        tmp = res[-1] - uf.size(a) * uf.size(b)
        if tmp < 0:
            tmp = 0
        res.append(tmp)
        uf.unite(a, b)

    res.reverse()
    res.popleft()
    print(*res, sep='\n')


main()
