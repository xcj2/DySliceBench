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
    n = int(readline())
    a = list(map(int, readline().split()))
    idx = dict()
    for i, x in enumerate(a, 1):
        idx[x] = i

    bt = BinaryIndexTree(n + 1)
    bt.add(n + 1, 1)
    ans = 0
    for num in range(1, n + 1):
        i = idx[num]
        s = bt.sum(i)
        left = bt.lower_bound(s)
        right = bt.lower_bound(s + 1)
        ans += num * (i - left) * (right - i)
        bt.add(i, 1)

    print(ans)


if __name__ == '__main__':
    main()
