import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


class Bit:

    def __init__(self, a):
        if hasattr(a, "__iter__"):
            le = len(a)
            self.n = 1 << le.bit_length()
            self.values = values = [0] * (self.n + 1)
            values[1:le + 1] = a[:]
            for i in range(1, self.n):
                values[i + (i & -i)] += values[i]
        elif isinstance(a, int):
            self.n = 1 << a.bit_length()
            self.values = [0] * (self.n + 1)
        else:
            raise TypeError

    # A[i] += val
    def add(self, i, val):
        n, values = self.n, self.values
        while i <= n:
            values[i] += val
            i += i & -i

    # A[1, i]の累積和
    def sum(self, i):
        values = self.values
        res = 0
        while i > 0:
            res += values[i]
            i -= i & -i
        return res

    # A[1, i]の累積和 が v 以上になる最小の i
    def bisect_left(self, v):
        n, values = self.n, self.values
        if v > values[n]:
            return None
        i, step = 0, n >> 1
        while step:
            if values[i + step] < v:
                i += step
                v -= values[i]
            step >>= 1
        return i + 1


def main():

    N, K = in_nn()
    LR = []
    for i in range(K):
        l, r = in_nn()
        LR.append((l, r))

    init_dp = [0] * N
    init_dp[0] = 1
    init_dp[1] = -1
    bit = Bit(init_dp)

    mod = 998244353
    for i in range(1, N + 1):
        for k in range(K):
            l, r = LR[k]
            now = bit.sum(i) % mod
            bit.add(i + l, now)
            bit.add(i + r + 1, -now)

    print(bit.sum(N) % mod)


if __name__ == '__main__':
    main()
