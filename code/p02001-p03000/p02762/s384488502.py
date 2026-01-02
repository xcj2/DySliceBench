# ABC157d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    class UnionFind:
        def __init__(self, n):
            self.tree = [i for i in range(n)]
            self.member = [1]*n

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
            new = self.member[x]+self.member[y]
            self.member[x] = new
            self.member[y] = new
            self.tree[x] = y

    n, m, k = map(int, input().split())
    tree = UnionFind(n)

    friend = [set() for i in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a - 1].add(b - 1)
        friend[b - 1].add(a - 1)
        tree.unite(a-1, b-1)
    block = [set() for i in range(n)]
    for _ in range(k):
        c, e = map(int, input().split())
        if tree.same(c - 1, e - 1):
            block[c - 1].add(e - 1)
            block[e - 1].add(c - 1)
    ans = []
    for i in range(n):
        #print(i, tree.member[tree.root(i)], len(friend[i]), len(block[i]))
        ans.append(tree.member[tree.root(i)]-len(friend[i])-len(block[i])-1)
    print(*ans)


if __name__ == '__main__':
    main()
