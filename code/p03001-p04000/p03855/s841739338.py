# coding:utf-8

import sys
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, k, l = LI()

# UnionFind
class UnionFind:
    # 負: ルートで値は木の深さを表す
    # 正: 子で値は次のノードを表す
    def __init__(self, size: int) -> None:
        self.nodes = [-1] * size  # 初期状態では全てのノードがルート

    def find(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.nodes[root_x] != self.nodes[root_y]:  # グラフの高さが異なる場合
                # 木のランクが高い方のルートに併合させる
                # 併合後にランクの変動はない
                if self.nodes[root_x] < self.nodes[root_y]:
                    self.nodes[root_y] = root_x
                else:
                    self.nodes[root_x] = root_y
            else:
                # ランクが等しい木同士を併合させるので
                # 併合後は木のランクが1つ上がる
                self.nodes[root_x] += -1
                self.nodes[root_y] = root_x


ufa = UnionFind(n)
ufb = UnionFind(n)

for _ in range(k):
    a, b = LI_()
    ufa.unite(a, b)
for _ in range(l):
    a, b = LI_()
    ufb.unite(a, b)

cnt = defaultdict(int)
keys = []
for i in range(n):
    key = (ufa.find(i), ufb.find(i))
    cnt[key] += 1
    keys.append(key)

print(*[cnt[key] for key in keys])
