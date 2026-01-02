import sys
import queue
sys.setrecursionlimit(10 ** 6)


class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n  # 各ノードの親を保存する。 idx 番号がノードに相当する
        self.rank = [0] * n  # 各ノードのrank　を保存する。 idx 番号がノードに相当する

    def root(self, x):  # ノードの一番上の親を返す。
        if self.parents[x] == -1:  # self.parents が変化していないならば根である。
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        x_root = self.root(x)
        y_root = self.root(y)

        if x_root == y_root:  # すでに同一の木に属している場合
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parents[x_root] = y_root  # 大きい木に小さい木を接続する。　self.root の処理が軽くなるから。
        elif self.rank[x_root] == self.rank[y_root]:
            self.parents[x_root] = y_root
            self.rank[y_root] += 1
        else:
            self.parents[y_root] = x_root
        return

    def is_in_same(self, x, y):  # 同じ木に属しているか確認する。
        if self.root(x) == self.root(y):
            return True
        else:
            return False


def main():
    v, e = map(int, sys.stdin.readline().strip().split())

    edges = []
    for _ in range(e):
        s, t, w = map(int, sys.stdin.readline().strip().split())
        edges.append((s, t, w))

    edges = sorted(edges, key=lambda x: x[2])  # 辺の重みで昇順ソート

    ans = 0  # 最小全域木の辺の重みの総和

    unionfind = UnionFind(v)
    for s, t, w in edges:
        if unionfind.is_in_same(s, t):
            continue
        else:
            unionfind.unite(s, t)
            ans += w

    print(ans)


if __name__ == '__main__':
    main()

