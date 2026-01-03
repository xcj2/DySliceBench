import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    from operator import itemgetter
    import heapq

    n = int(readline())
    cities = [list(map(int, readline().split())) + [i] for i in range(n)]
    uf = UnionFind(n)

    cx = sorted(cities, key=itemgetter(0))
    cy = sorted(cities, key=itemgetter(1))

    edge = []

    for i in range(1, n):
        dx = cx[i][0] - cx[i - 1][0]
        heapq.heappush(edge, (dx, cx[i][2], cx[i - 1][2]))

    for i in range(1, n):
        dy = cy[i][1] - cy[i - 1][1]
        heapq.heappush(edge, (dy, cy[i][2], cy[i - 1][2]))

    ans = 0
    while edge:
        cost, u, v = heapq.heappop(edge)
        if not uf.same(u, v):
            uf.union(u, v)
            ans += cost

    print(ans)


if __name__ == '__main__':
    main()
