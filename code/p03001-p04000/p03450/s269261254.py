# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


class WeightedUnionFind:
    __slots__ = ['nodes', 'weight']

    def __init__(self, size: int) -> None:
        self.nodes = [-1] * size  # ノードの値が負の場合ルートを表し、値は木のランクを表す
        self.weight = [0] * size  # ノードx -> ルート(ノードx)への重みを表す

    # 検索
    def find(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            parent = self.find(self.nodes[x])
            self.weight[x] += self.weight[self.nodes[x]]
            self.nodes[x] = parent
            return parent

    # 併合
    def unite(self, x: int, y: int, w: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return self.diff_weight(x, y, w)
        else:
            rank_x = -self.nodes[root_x]
            rank_y = -self.nodes[root_y]
            if rank_x < rank_y:
                self.nodes[root_x] = root_y
                self.weight[root_x] = w + self.weight[y] - self.weight[x]
            else:
                self.nodes[root_y] = root_x
                self.weight[root_y] = -w + self.weight[x] - self.weight[y]

                if rank_x == rank_y:
                    self.nodes[root_x] += -1

            return True

    # def is_same(self, x: int, y: int) -> bool:
    #     return self.find(x) == self.find(y)

    def diff_weight(self, x: int, y: int, w: int) -> int:
        return self.weight[x] - self.weight[y] == w


n, m = LI()
uf = WeightedUnionFind(n)
for _ in range(m):
    l, r, d = LI()
    l -= 1
    r -= 1
    if not uf.unite(l, r, d):
        print('No')
        exit()
print('Yes')
