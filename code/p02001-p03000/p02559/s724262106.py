import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class BinaryIndexTree:
    def __init__(self, n):
        self.size = n
        self._container = [0] * (n + 1)
        self.depth = n.bit_length()

    def sum(self, i):
        if i == 0:
            return 0
        s = 0
        while i > 0:
            s += self._container[i]
            i -= i & (-i)
        return s

    def add(self, i, x):
        if i == 0:
            return
        while i <= self.size:
            self._container[i] += x
            i += i & (-i)

    def lower_bound(self, x):
        if x == 0:
            return 0

        s = 0
        idx = 0
        for i in range(self.depth, -1, -1):
            k = idx + (1 << i)
            if k <= self.size and s + self._container[k] < x:
                s += self._container[k]
                idx += 1 << i
        return idx + 1

    def __repr__(self):
        return str(self._container)


def main():
    N, Q = map(int, readline().split())
    a = list(map(int, readline().split()))
    bit = BinaryIndexTree(N + 1)

    for i, x in enumerate(a, 1):
        bit.add(i, x)

    for _ in range(Q):
        a, b, c = map(int, readline().split())
        if a == 0:
            b += 1
            bit.add(b, c)
        else:
            b += 1
            c += 1
            print(bit.sum(c - 1) - bit.sum(b - 1))


if __name__ == '__main__':
    main()
