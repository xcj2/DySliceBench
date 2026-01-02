import sys
input = sys.stdin.readline


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


def main():
    N, M = map(int, input().split())
    Q = []
    for _ in range(M):
        a, b = map(int, input().split())
        Q.append((a, b))
    Q.reverse()

    uf = UnionFind(N+1)
    ans = [N*(N-1)//2]
    for a, b in Q:
        if uf.same(a, b):
            ans.append(ans[-1])
        else:
            sa = uf.size(a)
            sb = uf.size(b)
            uf.union(a, b)
            ans.append(ans[-1] - sa*sb)
    ans.pop()

    ans.reverse()
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
