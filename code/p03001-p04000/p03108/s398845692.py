#!/usr/bin/env python3


class UnionFind():
    def __init__(self, size):
        self.table = [-1] * size

    def find(self, x):
        while 0 <= self.table[x]:
            x = self.table[x]
        return x

    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            dx = -self.table[rx]
            dy = -self.table[ry]
            if dx != dy:
                if dx < dy:
                    self.table[rx] = ry
                else:
                    self.table[ry] = rx
            else:
                self.table[rx] -= 1
                self.table[ry] = rx
        return


def solve(n, m, a, b):

    uf = UnionFind(n)
    sizes = [1] * n

    r = n * (n - 1) // 2
    ans = [r]

    for i in range(m - 1, 0, -1):
        ca = uf.find(a[i])
        cb = uf.find(b[i])
        if ca != cb:
            r -= sizes[ca] * sizes[cb]
            ans.append(r)
            s = sizes[ca] + sizes[cb]
            sizes[ca] = sizes[cb] = s
            uf.unite(ca, cb)
        else:
            ans.append(r)


    ans.reverse()
    for r in ans:
        print(r)


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = []
    b = []
    for _ in range(m):
        ai, bi = input().split()
        ai = int(ai) - 1
        bi = int(bi) - 1
        a.append(ai)
        b.append(bi)

    solve(n, m, a, b)


if __name__ == '__main__':
    main()

