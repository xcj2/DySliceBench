import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


class UnionFind():
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

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

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    V, E = map(int, readline().split())
    L = []
    for _ in range(E):
        s, t, w = map(int, readline().split())
        L.append([s, t, w])
    # 重みが軽い順にソート
    L.sort(key=lambda x: x[2])
    uf = UnionFind(V)
    ans = 0
    for i in range(E):
        s, t, w = L[i]
        if not uf.same(s, t):
            uf.union(s, t)
            ans += w
    print(ans)


if __name__ == '__main__':
    main()

