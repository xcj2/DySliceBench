import sys
input = sys.stdin.buffer.readline

MOD = 10 ** 9 + 7
INF = 2 * 10**18

in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]


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

    N, M = in_nn()
    uni = UnionFind(N)

    for i in range(M):
        a, b = in_nn()
        a, b = a - 1, b - 1
        uni.union(a, b)

    ans = uni.group_count() - 1
    print(ans)


if __name__ == '__main__':
    main()
