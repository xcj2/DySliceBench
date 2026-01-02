# coding:utf-8

import sys
from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


# UnionFind
class UnionFind:
    # 負: ルートで値は木の深さを表す
    # 正: 子で値は次のノードを表す
    def __init__(self, size: int) -> None:
        self.nodes = [-1] * size  # 初期状態では全てのノードがルート

    def get_root(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.get_root(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> None:
        root_x, root_y = self.get_root(x), self.get_root(y)
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


H, W = LI()
B = [[1 if s == '#' else 0 for s in S()] for _ in range(H)]

uf = UnionFind(H * W)

for h in range(H):
    for w in range(W):
        if w < W - 1 and B[h][w] != B[h][w + 1]:
            uf.unite(h * W + w, h * W + w + 1)
        if h < H - 1 and B[h][w] != B[h + 1][w]:
            uf.unite(h * W + w, (h + 1) * W + w)

black = defaultdict(int)
white = defaultdict(int)
for h in range(H):
    for w in range(W):
        i = h * W + w
        if B[h][w] == 1:
            black[uf.get_root(i)] += 1
        else:
            white[uf.get_root(i)] += 1

ans = 0
for n in black.keys():
    ans += black[n] * white[n]

print(ans)
