mod = 1000000007
eps = 10**-9


def main():
    import sys
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

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size.bit_length() - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1

    N = int(input())
    XY = []
    x2i = [0] * (N+1)
    y2i = [0] * (N+1)
    for i in range(1, N+1):
        x, y = map(int, input().split())
        XY.append((x, y))
        x2i[x] = i
        y2i[y] = i
    bit = Bit(N)
    UF = UnionFind(N)

    XY.sort(key=lambda z: z[1])
    r = N+1
    for i in range(N):
        x, y = XY[i]
        bit.add(x, 1)
        #print(x, r)
        if x < r:
            for xx in range(x, r-1):
                UF.unite(x2i[xx], x2i[xx+1])
            if bit.sum(N) - bit.sum(r-1) != N - r + 1:
                UF.unite(x2i[r-1], x2i[r])
            r = x
            if r == 1:
                break
    for i in range(1, N+1):
        print(UF.size(i))


if __name__ == '__main__':
    main()
