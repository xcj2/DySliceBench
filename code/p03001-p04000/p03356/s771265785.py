def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    # Union-Find木
    class UnionFind():
        def __init__(self, n):
            self.tree = [i for i in range(n)]

        def root(self, x):
            if(self.tree[x] == x):
                return x
            self.tree[x] = self.root(self.tree[x])
            return self.tree[x]  # 経路圧縮

        def same(self, x, y):  # xとyが同じ木に属するか
            return self.root(x) == self.root(y)

        def unite(self, x, y):
            x = self.root(x)
            y = self.root(y)
            if(x == y):
                return
            self.tree[x] = y

    uf = UnionFind(n)

    for _ in range(m):
        x, y = map(int, input().split())
        uf.unite(x-1, y-1)
    ans = 0
    for i in range(n):
        if uf.same(i, p[i]-1):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
