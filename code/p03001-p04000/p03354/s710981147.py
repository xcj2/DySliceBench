import sys
from operator import itemgetter
from itertools import groupby
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, M = map(int, readline().split())
p = list(map(int, readline().split()))
xy = map(int, read().split())


class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if x == y:
            return
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]


tree = UnionFind(N)
for x, y in zip(xy, xy):
    tree.Unite(x, y)

group = tree.root[1:]
number = list(range(1, N + 1))
answer = 0

for i in range(N):
    if tree.isSameGroup(number[i], p[i]):
        answer += 1

print(answer)