import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, Q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    def segfunc(x, y):
        return max(x, y)

    class SegmentTree:
        def __init__(self, init_val, ide_ele):
            self.n = len(init_val)
            self.ide_ele = ide_ele
            self.num = 2 ** (self.n - 1).bit_length()
            self.seg = [self.ide_ele] * 2 * self.num
            for i in range(self.n):
                self.seg[i + self.num - 1] = init_val[i]

            for i in range(self.num - 2, -1, -1):
                self.seg[i] = segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

        def update(self, k, x):
            k += self.num - 1
            self.seg[k] = x
            while k:
                k = (k - 1) // 2
                self.seg[k] = segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

        def query(self, p, q):
            if q <= p:
                return self.ide_ele
            p += self.num - 1
            q += self.num - 2
            res = self.ide_ele
            while q - p > 1:
                if p & 1 == 0:
                    res = segfunc(res, self.seg[p])
                if q & 1 == 1:
                    res = segfunc(res, self.seg[q])
                    q -= 1
                p = p // 2
                q = (q - 1) // 2
            if p == q:
                res = segfunc(res, self.seg[p])
            else:
                res = segfunc(segfunc(res, self.seg[p]), self.seg[q])
            return res

    s = SegmentTree(A, 0)

    def isOK(mid, m, value):
        a = s.query(m, mid)
        return a >= value

    B = A[::]

    for _ in range(Q):
        T, X, V = [int(x) for x in input().split()]
        if T == 1:
            s.update(X - 1, V)
            B[X - 1] = V
        elif T == 2:
            print(s.query(X - 1, V))
        else:
            a = s.query(X - 1, N)
            if a < V:
                print(N + 1)
            else:
                if B[X - 1] >= V:
                    print(X)
                    continue
                ok = N - 1
                ng = X - 1

                while abs(ok - ng) > 1:
                    mid = (ok + ng) // 2
                    if isOK(mid, X - 1, V):
                        ok = mid
                    else:
                        ng = mid

                print(ok)


if __name__ == '__main__':
    main()
