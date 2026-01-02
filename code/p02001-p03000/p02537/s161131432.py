import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class SegTree:
    X_unit = 0

    def __init__(self, n):
        self.n = n
        self.length = n
        self.data = [self.X_unit] * 2 * self.length

    def update(self, i, x):
        i += self.length
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = max(self.data[i << 1 | 0], self.data[i << 1 | 1])

    def get(self, l, r):
        x = self.X_unit
        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                x = max(x, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                x = max(x, self.data[r])
            l >>= 1
            r >>= 1
        return x


def main():
    N, K, *A = map(int, read().split())
    Amax = max(A)
    tree = SegTree(Amax + 1)

    for a in A:
        x = tree.get(max(a - K, 0), min(a + K, Amax) + 1)
        tree.update(a, x + 1)

    print(tree.get(0, Amax + 1))
    return


if __name__ == '__main__':
    main()
