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
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    ans = n - m
    f = UnionFindTree(n)
    for _ in range(m):
        x, y, z = map(int, input().split())
        if f.same(x - 1, y - 1):
            ans += 1
        f.union(x - 1, y - 1)
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
