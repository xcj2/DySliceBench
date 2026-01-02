class UnionFind:
    def __init__(self, n):
        self.v = [-1] * n

    def find(self, x):
        if self.v[x] < 0:
            return x
        else:
            self.v[x] = self.find(self.v[x])
            return self.v[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.v[x] > self.v[y]:
                x, y = y, x
            self.v[x] += self.v[y]
            self.v[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.v[self.find(x)]


def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    es = []
    for _ in range(M):
        a, b = (int(x) - 1 for x in input().split())
        es.append((a, b))
    es.reverse()
    es.pop()

    uf = UnionFind(N)
    ans = [N * (N - 1) // 2]
    t = ans[-1]
    for a, b in es:
        if not uf.same(a, b):
            t -= uf.size(a) * uf.size(b)
        ans.append(t)
        uf.unite(a, b)
    ans.reverse()

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
