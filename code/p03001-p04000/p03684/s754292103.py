import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def check(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N = int(input())
    coord = {}
    for i in range(N):
        x, y = map(int, input().split())
        coord[i] = (x, y)

    coord_x_sort = sorted(coord.items(), key=lambda x: x[1][0])
    coord_y_sort = sorted(coord.items(), key=lambda x: x[1][1])
    dist = []
    for i in range(N - 1):
        dx = abs(coord_x_sort[i][1][0] - coord_x_sort[i + 1][1][0])
        c1 = coord_x_sort[i][0]
        c2 = coord_x_sort[i + 1][0]
        dist.append((dx, c1, c2))

        dy = abs(coord_y_sort[i][1][1] - coord_y_sort[i + 1][1][1])
        c1 = coord_y_sort[i][0]
        c2 = coord_y_sort[i + 1][0]
        dist.append((dy, c1, c2))

    dist.sort(key=lambda x: x[0])

    tree = UnionFind(N)

    ans = 0
    for d, i, j in dist:
        if not tree.check(i, j):
            ans += d
            tree.unite(i, j)

    print(ans)


if __name__ == "__main__":
    main()
