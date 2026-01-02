# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


# UnionFind
class UnionFind:
    # 負: ルートで値は木の深さを表す
    # 正: 子で値は次のノードを表す
    def __init__(self, size: int) -> None:
        self.nodes = [-1] * size  # 初期状態では全てのノードがルート

    def root(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.root(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> None:
        root_x, root_y = self.root(x), self.root(y)
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


n, q = LI()
query = [LI() for _ in range(q)]

uf = UnionFind(n)
for com, x, y in query:
    if com == 0:  # 連結クエリ
        uf.unite(x, y)
    else:  # 判定クエリ
        if uf.root(x) == uf.root(y):
            print(1)
        else:
            print(0)

