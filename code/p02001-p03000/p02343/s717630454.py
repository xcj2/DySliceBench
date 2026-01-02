# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A


class UnionFind:

    def __init__(self, size: int):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.size = size
        self.parent = [-1] * size

    def find(self, x: int) -> int:
        """
        xを含む集合の代表を求める
        """
        if self.parent[x] < 0:
            return x
        # 集合の代表にリンクを繋ぎ変える
        same_group_items = []
        while self.parent[x] >= 0:
            same_group_items.append(x)
            x = self.parent[x]
        for child in same_group_items:
            self.parent[child] = x
        return x

    def unite(self, x: int, y: int):
        """
        xを含む集合とyを含む集合を併合する
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.parent[root_x] >= self.parent[root_y]:
                self.parent[root_x] += self.parent[root_y]
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] += self.parent[root_x]
                self.parent[root_x] = root_y

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)


def solve():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            uf.unite(x, y)
        else:
            print(1 if uf.same(x, y) else 0)


if __name__ == "__main__":
    solve()

