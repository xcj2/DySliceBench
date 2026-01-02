class UnionFind():
    def __init__(self, n):
        self.parents = [-1 for _ in range(n)]  # 各要素の親 自分が根の場合は -1 * (木の要素数)

    def root(self, x):  # xが属する木の根を返す
        if self.parents[x] < 0:  # 自分が根の場合
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def merge(self, x, y):  # xが属する木とyが属する木を合体する
        x_root = self.root(x)  # xの根
        y_root = self.root(y)  # yの根

        if x_root == y_root:  # 同じ木に属する
            return

        if abs(self.parents[x_root]) >= abs(self.parents[y_root]):  # 要素数の比較
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            self.parents[y_root] += self.parents[x_root]
            self.parents[x_root] = y_root

    def size(self, x):  # xが属する木の要素数
        return -self.parents[self.root(x)]

    def same(self, x, y):  # xとyが同じ木に属するか判定
        return self.root(x) == self.root(y)

    def roots(self):  # すべての根を求める
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # 木が何個あるか
        return len(self.roots())


def main():
    n, m = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(m)]
    ans = 0

    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i == j:
                continue
            uf.merge(ab_list[j][0] - 1, ab_list[j][1] - 1)
        if uf.group_count() != 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
