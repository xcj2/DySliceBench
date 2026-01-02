mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

    class LazySegTree:
        # Range update query
        def __init__(self, A, initialize=True, segfunc=min, ident=2 ** 31 - 1):
            self.N = len(A)
            self.LV = (self.N - 1).bit_length()
            self.N0 = 1 << self.LV
            self.segfunc = segfunc
            self.ident = ident
            if initialize:
                self.data = [self.ident] * self.N0 + A + [self.ident] * (self.N0 - self.N)
                for i in range(self.N0 - 1, 0, -1):
                    self.data[i] = segfunc(self.data[i * 2], self.data[i * 2 + 1])
            else:
                self.data = [self.ident] * (self.N0 * 2)
            self.lazy = [0] * (self.N0 * 2)
            self.lazy_flg = [False] * (self.N0 * 2)

        def _ascend(self, i):
            for _ in range(i.bit_length() - 1):
                i >>= 1
                self.data[i] = self.segfunc(self.data[i * 2], self.data[i * 2 + 1])

        def _descend(self, idx):
            lv = idx.bit_length()
            block_size = 2**self.LV
            for j in range(lv - 1, 0, -1):
                i = idx >> j
                block_size >>= 1
                x = self.lazy[i]
                if not self.lazy_flg[i]:
                    continue
                self.lazy_flg[i] = False
                self.lazy[i * 2] = x
                self.lazy[i * 2 + 1] = x + block_size
                self.lazy_flg[i * 2] = True
                self.lazy_flg[i * 2 + 1] = True
                self.data[i * 2] = x
                self.data[i * 2 + 1] = x + block_size

        # open interval [l, r)
        def update(self, l, r, x):
            l += self.N0 - 1
            r += self.N0 - 1
            self._descend(l // (l & -l))
            self._descend(r // (r & -r) - 1)
            l_ori = l
            r_ori = r
            xl = x
            xr = x + (r-l)
            block_size = 1
            while l < r:
                if l & 1:
                    self.data[l] = xl
                    self.lazy[l] = xl
                    self.lazy_flg[l] = True
                    l += 1
                    xl += block_size
                if r & 1:
                    r -= 1
                    xr -= block_size
                    self.data[r] = xr
                    self.lazy[r] = xr
                    self.lazy_flg[r] = True
                l >>= 1
                r >>= 1
                block_size <<= 1
            self._ascend(l_ori // (l_ori & -l_ori))
            self._ascend(r_ori // (r_ori & -r_ori) - 1)

        # open interval [l, r)
        def query(self, l, r):
            l += self.N0 - 1
            r += self.N0 - 1
            self._descend(l // (l & -l))
            self._descend(r // (r & -r) - 1)
            ret = self.ident
            while l < r:
                if l & 1:
                    ret = self.segfunc(ret, self.data[l])
                    l += 1
                if r & 1:
                    ret = self.segfunc(self.data[r - 1], ret)
                    r -= 1
                l >>= 1
                r >>= 1
            return ret

    H, W = map(int, input().split())
    ST = LazySegTree([10**6] + [0] * W)
    for h in range(H):
        a, b = map(int, input().split())
        ST.update(a+1, b+2, ST.query(a, a+1)+1)
        ans = ST.query(2, W+2)
        if ans >= 10**6:
            print(-1)
        else:
            print(h + 1 + ans)


if __name__ == '__main__':
    main()
