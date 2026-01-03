import sys
import numpy as np
read = sys.stdin.read


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


N, *xy = map(int, read().split())
xy = np.array(xy, np.int64).reshape(N, 2)
x = xy[:, 0]
y = xy[:, 1]

arg_x = np.argsort(x)
arg_y = np.argsort(y)

edges_x = x[arg_x[1:]] - x[arg_x[:-1]]
edges_y = y[arg_y[1:]] - y[arg_y[:-1]]

edges = np.concatenate([edges_x, edges_y])
towns_1 = np.concatenate([arg_x[:-1], arg_y[:-1]])
towns_2 = np.concatenate([arg_x[1:], arg_y[1:]])

arg_edges = np.argsort(edges)
graph = zip(edges[arg_edges].tolist(), towns_1[arg_edges].tolist(), towns_2[arg_edges].tolist())

tree = UnionFind(N)
answer = 0

for d, t1, t2 in graph:
    if tree.isSameGroup(t1, t2):
        continue

    tree.Unite(t1, t2)
    answer += d

print(answer)