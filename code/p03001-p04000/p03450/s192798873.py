# coding:utf-8

import sys


input = sys.stdin.readline


def inpl(): return list(map(int, input().split()))


# ---
class UnionFind:
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
    # def unite(self, x: int, y: int, w: int) -> bool:
    #     root_x = self.find(x)
    #     root_y = self.find(y)
    #     if root_x == root_y:
    #         return False
    #     else:
    #         rank_x = -self.nodes[root_x]
    #         rank_y = -self.nodes[root_y]
    #         if rank_x < rank_y:
    #             self.nodes[root_x] = root_y
    #             self.weight[root_x] = w - self.weight[y] - self.weight[x]
    #         else:
    #             self.nodes[root_y] = root_x
    #             self.weight[root_y] = w - self.weight[x] - self.weight[y]
    #
    #             if rank_x == rank_y:
    #                 self.nodes[root_x] += -1
    #
    #         return True

    # xとyのルートが等しい時: 入力された重みwが正しいかどうかを判定
    # xとyのルートが異なる時: xとyを併合する
    # True: 併合，False: 何もしない，ValueError: 入力された重みに矛盾がある
    def relate(self, x: int, y: int, w: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # 入力された重みwに矛盾がないか判定
            if self.weight[x] - self.weight[y] == w:
                return False
            raise ValueError
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

    # UnionFind木の一覧を返す
    # def get_tree(self) -> dict:
    #     tree = {}
    #     for i, node in enumerate(self.nodes):
    #         if node < 0:
    #             if i not in tree.keys():
    #                 tree[i] = []
    #         else:
    #             if self.find(node) in tree.keys():
    #                 tree[self.find(node)].append(i)
    #             else:
    #                 tree[self.find(node)] = [i]
    # 
    #     return tree


N, M = inpl()
uf = UnionFind(N)
relate = uf.relate
try:
    for i in range(M):
        l, r, d = inpl()
        relate(l - 1, r - 1, d)
    else:
        print('Yes')
except ValueError:
    print('No')
