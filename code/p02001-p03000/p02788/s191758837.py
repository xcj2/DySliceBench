import sys
import bisect

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
            self.n = 1 << le.bit_length()  # le を超える最小の 2 冪
            self.values = values = [0] * (self.n + 1)
            values[1:le + 1] = a[:]
            for i in range(1, self.n):
                values[i + (i & -i)] += values[i]
        elif isinstance(a, int):
            self.n = 1 << a.bit_length()
            self.values = [0] * (self.n + 1)
        else:
            raise TypeError

    def add(self, i, val):
        n, values = self.n, self.values
        while i <= n:
            values[i] += val
            i += i & -i

    def sum(self, i):  # (0, i]
        values = self.values
        res = 0
        while i > 0:
            res += values[i]
            i -= i & -i
        return res

    def bisect_left(self, v):  # self.sum(i) が v 以上になる最小の i
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

    N, D, A = in_nn()
    XH = sorted(in_nl2(N))
    X = [0] * N
    H = [0] * N

    for i in range(N):
        x, h = XH[i]
        X[i] = x
        H[i] = h

    bit = Bit(N)

    ans = 0
    for i in range(N):

        x, h = X[i], H[i]
        j = bisect.bisect_right(X, x + 2 * D)
        cnt_bomb = bit.sum(i + 1)

        h -= A * cnt_bomb
        if h <= 0:
            continue

        cnt = -(-h // A)
        ans += cnt
        bit.add(i + 1, cnt)
        bit.add(j + 1, -cnt)

    print(ans)


if __name__ == '__main__':
    main()
