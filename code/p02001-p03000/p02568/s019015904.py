mod = 998244353
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

    def op(a, b):
        return (a + b) % mod

    e = 0

    mask = 2**32 - 1
    def mapping(a, x, seg_len):
        b = x >> 32
        c = x & mask
        return ((a * b)%mod + (c * seg_len)%mod)%mod

    def composition(x, y):
        b1 = x >> 32
        c1 = x & mask
        b2 = y >> 32
        c2 = y & mask
        return (((b1 * b2)%mod) << 32) + ((b2 * c1)%mod + c2)%mod

    id = 1 << 32

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
                for i in range(self.N0 - 1, 0, -1):
                    self.data[i] = op(self.data[i * 2], self.data[i * 2 + 1])
            else:
                self.data = [self.e] * (self.N0 * 2)
            self.lazy = [id] * (self.N0 * 2)

        def _ascend(self, i):
            for _ in range(i.bit_length() - 1):
                i >>= 1
                self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])

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
            self._ascend(l_ori // (l_ori & -l_ori))
            self._ascend(r_ori // (r_ori & -r_ori) - 1)

        # open interval [l, r)
        def query(self, l, r):
            l += self.N0 - 1
            r += self.N0 - 1
            self._descend(l // (l & -l))
            self._descend(r // (r & -r) - 1)
            ret = self.e
            while l < r:
                if l & 1:
                    ret = self.op(ret, self.data[l])
                    l += 1
                if r & 1:
                    ret = self.op(self.data[r - 1], ret)
                    r -= 1
                l >>= 1
                r >>= 1
            return ret

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ST = LazySegTree(A)
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 0:
            l, r, b, c = q[1:]
            l += 1
            r += 1
            ST.apply(l, r, (b << 32) + c)
        else:
            l, r = q[1:]
            l += 1
            r += 1
            print(ST.query(l, r))


if __name__ == '__main__':
    main()
