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

    def same(self, x, y):
        return self.find(x) == self.find(y)



def main():
    n, m = LI()

    uf = UnionFind(n)
    res = deque()
    res.append(n * (n - 1) // 2)
    cnt = [1] * n
    AB = [LI_() for _ in range(m)]
    AB.reverse()
    for a, b in AB:
        if uf.same(a, b):
            res.append(res[-1])
            continue
        ca = cnt[uf.find(a)]
        cb = cnt[uf.find(b)]
        tmp = res[-1] - ca * cb
        # print(a+1, b+1, res[-1], ca, cb)
        if tmp < 0:
            tmp = 0
        res.append(tmp)
        uf.unite(a, b)
        cnt[uf.find(a)] = ca + cb
        # print(cnt[uf.find(a)], cnt[uf.find(b)])

    res.reverse()
    res.popleft()
    print(*res, sep='\n')


main()
