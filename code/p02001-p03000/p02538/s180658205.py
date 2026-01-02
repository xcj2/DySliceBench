mod = 998244353
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

    beki10 = [0] * ((1 << 19) + 1)
    beki10[0] = 1
    for i in range(20):
        beki10[1 << i] = pow(10, (1 << i), mod)

    def op(a, b, seg_len):
        return (a * beki10[seg_len] + b)%mod

    e = 0
    inv9 = pow(9, mod - 2, mod)

    def mapping(a, x, seg_len):
        return ((x * inv9)%mod * (beki10[seg_len] - 1))%mod

    def composition(x, y):
        return y

    id = -1

    class LazySegTree:
        # Range update query
        def __init__(self, A, op=op, e=e, mapping=mapping, composition=composition, id=id, initialize=True):
            self.N = len(A)
            self.LV = (self.N - 1).bit_length()
            self.N0 = 1 << self.LV
            self.op = op
            self.e = e
            self.mapping = mapping
            self.composition = composition
            self.id = id
            if initialize:
                self.data = [self.e] * self.N0 + A + [self.e] * (self.N0 - self.N)
                seg_len = 1
                beki = self.N0 // 2
                for i in range(self.N0 - 1, 0, -1):
                    self.data[i] = op(self.data[i * 2], self.data[i * 2 + 1], seg_len)
                    if i == beki:
                        seg_len <<= 1
                        beki >>= 1
            else:
                self.data = [self.e] * (self.N0 * 2)
            self.lazy = [id] * (self.N0 * 2)

        def _ascend(self, i, seg_len):
            for _ in range(i.bit_length() - 1):
                i >>= 1
                self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1], seg_len)
                seg_len <<= 1

        def _descend(self, idx):
            lv = idx.bit_length()
            seg_len = 1 << self.LV
            for j in range(lv - 1, 0, -1):
                seg_len >>= 1
                i = idx >> j
                x = self.lazy[i]
                if x == self.id:
                    continue
                self.lazy[i * 2] = self.composition(self.lazy[i * 2], x)
                self.lazy[i * 2 + 1] = self.composition(self.lazy[i * 2 + 1], x)
                self.lazy[i] = self.id
                self.data[i * 2] = self.mapping(self.data[i * 2], x, seg_len)
                self.data[i * 2 + 1] = self.mapping(self.data[i * 2 + 1], x, seg_len)

        # open interval [l, r)
        def apply(self, l, r, x):
            l += self.N0 - 1
            r += self.N0 - 1
            self._descend(l // (l & -l))
            self._descend(r // (r & -r) - 1)
            l_ori = l
            r_ori = r
            seg_len = 1
            while l < r:
                if l & 1:
                    self.data[l] = self.mapping(self.data[l], x, seg_len)
                    self.lazy[l] = self.composition(self.lazy[l], x)
                    l += 1
                if r & 1:
                    r -= 1
                    self.data[r] = self.mapping(self.data[r], x, seg_len)
                    self.lazy[r] = self.composition(self.lazy[r], x)
                l >>= 1
                r >>= 1
                seg_len <<= 1
            self._ascend(l_ori // (l_ori & -l_ori), l_ori & -l_ori)
            self._ascend(r_ori // (r_ori & -r_ori) - 1, r_ori & -r_ori)

        # open interval [l, r)
        def query(self, l, r):
            l += self.N0 - 1
            r += self.N0 - 1
            self._descend(l // (l & -l))
            self._descend(r // (r & -r) - 1)
            ret_l = self.e
            ret_r = self.e
            seg_len = 1
            while l < r:
                if l & 1:
                    ret_l = self.op(ret_l, self.data[l], seg_len)
                    l += 1
                if r & 1:
                    ret_r = self.op(self.data[r - 1], ret_r, seg_len)
                    r -= 1
                l >>= 1
                r >>= 1
                seg_len <<= 1
            return self.op(ret_l, ret_r, 1)

    N, Q = map(int, input().split())
    N0 = 1 << (N - 1).bit_length()
    ST = LazySegTree([0] * (N0-N) + [1] * N)
    inv10 = pow(10, mod-2, mod)
    ans = [0] * Q
    for q in range(Q):
        l, r, d = map(int, input().split())
        ST.apply(N0 - N + l, N0 - N + r + 1, d)
        ans[q] = (ST.query(N0 - N + 1, N0+1) * inv10)%mod
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
