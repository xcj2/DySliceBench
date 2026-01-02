import sys
input = sys.stdin.readline


class UnionFind:

    def __init__(self, N):
        self.parents = list(range(N))
        self.depth = [0] * N

    def find(self, x):
        while True:
            if self.parents[x] == x:
                return x
            else:
                x = self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.depth[x] == self.depth[y]:
            self.depth[x] += 1
            self.parents[y] = x
        elif self.depth[x] > self.depth[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for i in range(M):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1)
    num = [0] * N
    for i in range(N):
        p = uf.find(i)
        num[p] += 1
    ans = max(num)
    print(ans)


if __name__ == '__main__':
    main()
