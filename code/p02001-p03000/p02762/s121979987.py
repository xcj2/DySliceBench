def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.buffer.readline

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.root = [-1] * (n + 1)
            self.rnk = [0] * (n + 1)

        def find_root(self, x):
            while self.root[x] >= 0:
                x = self.root[x]
            return x

        def unite(self, x, y):
            x = self.find_root(x)
            y = self.find_root(y)
            if x == y:
                return
            elif self.rnk[x] > self.rnk[y]:
                self.root[x] += self.root[y]
                self.root[y] = x
            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                if self.rnk[x] == self.rnk[y]:
                    self.rnk[y] += 1

        def isSameGroup(self, x, y):
            return self.find_root(x) == self.find_root(y)

        def size(self, x):
            return -self.root[self.find_root(x)]

    N, M, K = map(int, input().split())
    UF = UnionFind(N+1)
    fr_num = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        UF.unite(a, b)
        fr_num[a] += 1
        fr_num[b] += 1

    ans = [0] * (N+1)
    for i in range(1, N+1):
        ans[i] = UF.size(i) - 1 - fr_num[i]

    for _ in range(K):
        c, d = map(int, input().split())
        if UF.isSameGroup(c, d):
            ans[c] -= 1
            ans[d] -= 1
    print(*ans[1:])


if __name__ == '__main__':
    main()
