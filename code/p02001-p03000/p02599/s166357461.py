import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from operator import itemgetter

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

    n, q = map(int, readline().split())
    c = [0] + list(map(int, readline().split()))
    query = []
    for i in range(q):
        l, r = map(int, readline().split())
        query.append((l, r, i))

    query.sort(key=itemgetter(1))
    idx = dict()
    cur = 0
    bit = BinaryIndexTree(n)
    res = [0] * q
    s = 0
    for i in range(q):
        l, r, j = query[i]
        while cur < r:
            cur += 1
            color = c[cur]
            if idx.get(color):
                bit.add(idx[color], -1)
            else:
                s += 1
            bit.add(cur, 1)
            idx[color] = cur
        res[j] = s - bit.sum(l - 1)

    for i in range(q):
        print(res[i])


if __name__ == '__main__':
    main()
