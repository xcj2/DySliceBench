import sys

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


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
        ret = dict()
        for i in range(self.n):
            r = self.find(i)
            if r in ret:
                ret[r].append(i)
            else:
                ret[r] = [i]
        return ret

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():

    N = in_n()
    x = [0] * N
    y = [0] * N

    for i in range(N):
        x[i], y[i] = in_nn()

    sort_ind_x = sorted(range(N), key=lambda i: x[i])
    sort_ind_y = sorted(range(N), key=lambda i: y[i])

    cost = []
    for i in range(N - 1):
        j1, j2 = sort_ind_x[i], sort_ind_x[i + 1]
        c = abs(x[j1] - x[j2])
        cost.append((c, j1, j2))

        j1, j2 = sort_ind_y[i], sort_ind_y[i + 1]
        c = abs(y[j1] - y[j2])
        cost.append((c, j1, j2))

    cost.sort()
    uni = UnionFind(N)
    ans = 0

    for c, v1, v2 in cost:
        if not uni.same(v1, v2):
            ans += c
            uni.union(v1, v2)

    print(ans)


if __name__ == '__main__':
    main()
