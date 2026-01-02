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

    collapse_schedule = []
    for _ in range(M):
        A, B = (int(x) - 1 for x in input().split())
        collapse_schedule.append((A, B))
    collapse_schedule.reverse()

    uf = UnionFind(N)

    def evaluate(size):
        return size * (size - 1) // 2

    all_dropped = evaluate(N)
    curr = all_dropped

    ret = [-1] * M
    ret[-1] = all_dropped

    for i, (a, b) in zip(reversed(range(M - 1)), collapse_schedule):
        if not uf.same(a, b):
            sa, sb = uf.size(a), uf.size(b)
            ea, eb = evaluate(sa), evaluate(sb)

            curr += ea + eb

            uf.unite(a, b)

            sa = uf.size(a)
            ea = evaluate(sa)

            curr -= ea

        ret[i] = curr

    print(*ret, sep='\n')


if __name__ == '__main__':
    main()
