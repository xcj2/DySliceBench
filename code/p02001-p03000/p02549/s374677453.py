import sys

MOD = 998244353


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


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(k)]
    dp = Bit(n)
    dp.add(1, 1)
    for i in range(2, n + 1):
        for l, r in lr:
            if i - l < 1:
                continue
            if i - r < 2:
                dp.add(i, dp.sum(i - l) % MOD)
            else:
                dp.add(i, (dp.sum(i - l) - dp.sum(i - r - 1)) % MOD)
    print((dp.sum(n) - dp.sum(n - 1)) % MOD)


if __name__ == "__main__":
    main()
