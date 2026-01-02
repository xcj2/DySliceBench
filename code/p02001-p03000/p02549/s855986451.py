import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 998244353


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.step = pow(2, n.bit_length() - 1)

    def add(self, i, x=1):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get_sum(self, i):
        i += 1
        x = 0
        while i > 0:
            x += self.data[i]
            i -= i & -i
        return x

    # Return sum for [l, r)
    def get_sum_range(self, l, r):
        return self.get_sum(r - 1) - self.get_sum(l - 1)


def main():
    N, K, *LR = map(int, read().split())

    interval = [(l, r) for l, r in zip(*[iter(LR)] * 2)]

    bit = BIT(N + 2)
    bit.add(1, 1)
    bit.add(2, -1)

    for i in range(N):
        cur = bit.get_sum(i) % MOD
        for l, r in interval:
            bit.add(i + l, cur)
            bit.add(i + r + 1, -cur)

    print(bit.get_sum(N) % MOD)
    return


if __name__ == '__main__':
    main()
