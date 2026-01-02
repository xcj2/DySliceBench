# https://onlinejudge.u-aizu.ac.jp/problems/1127


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]

    def root(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[y] = x
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)


def distance(x1, y1, z1, x2, y2, z2):
    dxx = (x1 - x2) ** 2
    dyy = (y1 - y2) ** 2
    dzz = (z1 - z2) ** 2
    return (dxx + dyy + dzz) ** (1/2)


def solve(n, rows):
    # (start, end, corridors_length)
    edges = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            x1, y1, z1, r1 = rows[i]
            x2, y2, z2, r2 = rows[j]
            d = distance(x1, y1, z1, x2, y2, z2)
            # print(i, j, d)
            if d > r1 + r2:
                edges.append((i, j, d-r1-r2))
            else:
                edges.append((i, j, 0))

    edges.sort(key=lambda x: x[2])
    # print(edges)

    result = 0
    uf = UnionFind(n)
    for edge in edges:
        s, t, d = edge
        unioned = uf.union(s, t)
        if unioned:
            result += d

    print('{:.3f}'.format(result))


if __name__ == "__main__":
    while(True):
        n = int(input())
        if n == 0:
            break
        rows = [list(map(float, input().split())) for _ in range(n)]
        solve(n, rows)

