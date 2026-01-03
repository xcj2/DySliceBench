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
    n, k, l = map(int, input().split())

    uf_road = UnionFind(n)
    uf_train = UnionFind(n)

    for _ in range(k):
        p, q = map(int, input().split())
        uf_road.merge(p - 1, q - 1)

    for _ in range(l):
        r, s = map(int, input().split())
        uf_train.merge(r - 1, s - 1)

    count_dict = dict()
    for i in range(n):
        p = (uf_road.root(i), uf_train.root(i))
        if p in count_dict:
            count_dict[p] += 1
        else:
            count_dict[p] = 1

    for i in range(n):
        print(count_dict[(uf_road.root(i), uf_train.root(i))], end=" ")


if __name__ == "__main__":
    main()
