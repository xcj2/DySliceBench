from sys import stdin, setrecursionlimit


class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        while p[x] >= 0:
            x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        p = self.parent
        if x != y:
            if x > y:
                x, y = y, x
            p[x], p[y] = p[x] + p[y], x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parent[self.find(x)]


def main():
    n, m, k = map(int, stdin.readline().split())

    f = UnionFindTree(n)

    f_or_b = [0] * n

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        f.union(a - 1, b - 1)
        f_or_b[a - 1] += 1
        f_or_b[b - 1] += 1

    for _ in range(k):
        c, d = map(int, stdin.readline().split())
        if f.same(c - 1, d - 1):
            f_or_b[c - 1] += 1
            f_or_b[d - 1] += 1

    print(*[f.size(i) - f_or_b[i] - 1 for i in range(n)])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()