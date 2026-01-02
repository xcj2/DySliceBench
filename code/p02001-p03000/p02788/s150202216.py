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


class SegTree:

    def __init__(self, init_val, segfunc, ide_ele):

        n = len(init_val)
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.num = 2**(n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num

        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]

        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] += x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


def main():

    N, D, A = in_nn()
    XH = sorted(in_nl2(N))
    X = [0] * N
    H = [0] * N

    for i in range(N):
        x, h = XH[i]
        X[i] = x
        H[i] = h

    seg = SegTree([0] * N, segfunc=lambda a, b: a + b, ide_ele=0)

    ans = 0
    for i in range(N):

        x, h = X[i], H[i]
        j = bisect.bisect_right(X, x + 2 * D)
        cnt_bomb = seg.query(0, i + 1)

        h -= A * cnt_bomb
        if h <= 0:
            continue

        cnt = -(-h // A)
        ans += cnt
        seg.update(i, cnt)

        if j < N:
            seg.update(j, -cnt)

        # print(i, j)
        # print(seg.seg)

    print(ans)


if __name__ == '__main__':
    main()
