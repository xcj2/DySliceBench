class UnionFind():
    def __init__(self, n):
        self.parents = [-1 for _ in range(n)]  # 各要素の親 自分が根の場合は -1 * (木の要素数)

    def find(self, x):  # xが属する木の根を返す
        if self.parents[x] < 0:  # 自分が根の場合
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # xが属する木とyが属する木を合体する
        x_root = self.find(x)  # xの根
        y_root = self.find(y)  # yの根

        if x_root == y_root:  # 同じ木に属する
            return

        if abs(self.parents[x_root]) >= abs(self.parents[y_root]):  # 要素数の比較
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            self.parents[y_root] += self.parents[x_root]
            self.parents[x_root] = y_root

    def size(self, x):  # xが属する木の要素数
        return -self.parents[self.find(x)]


def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf.union(a, b)

    ans = 0
    for i in range(n):
        ans = max(ans, uf.size(i))

    print(ans)


if __name__ == "__main__":
    main()
