class LazySegmentTree():
    def __init__(self, op, e, mapping, composition, im, init_array):
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.im = im

        l = len(init_array)

        def ceil_pow2(n):
            x = 0
            while (1 << x) < n:
                x += 1
            return x

        self.log = ceil_pow2(l)
        self.size = 1 << self.log
        self.d = [e() for _ in range(2 * self.size)]
        self.lz = [im() for _ in range(self.size)]

        for i, a in enumerate(init_array):
            self.d[i + self.size] = a

        for i in range(self.size - 1, 0, -1):
            self.__update(i)

    def set(self, p, x):
        p += self.size

        for i in range(self.log, 0, -1):
            self.__push(p >> i)

        self.d[p] = x

        for i in range(1, self.log + 1):
            self.__update(p >> i)

    def __getitem__(self, p):
        p += self.size
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        if l == r:
            return self.e()

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push(r >> i)

        sml = self.e()
        smr = self.e()

        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1

        return self.op(sml, smr)

    def apply(self, l, r, f):
        if l == r:
            return

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push((r - 1) >> i)

        l2, r2 = l, r
        while l < r:
            if l & 1:
                self.__all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.__all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2

        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.__update(l >> i)
            if ((r >> i) << i) != r:
                self.__update((r - 1) >> i)

    def __update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def __push(self, k):
        self.__all_apply(2 * k, self.lz[k])
        self.__all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.im()




def op(x,y):
    return x+y


def mapping(x, y):
    return min(x, y)


def composition(x,y):
    return min(x, y)


def im():
    return 100000000000


def a():
    # https://atcoder.jp/contests/practice2/submissions/16842314
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())

    def e():
        return N - 2
    ans = (N-2) * (N-2)
    ssss = [N-2] * (N-1)
    st = LazySegmentTree(op, e, mapping, composition, im,ssss)
    sa = LazySegmentTree(op, e, mapping, composition, im,ssss)
    for _ in range(Q):
        t, l = map(int, input().split())
        if t == 1:
            t = st.__getitem__(l-1) + 1
            sa.apply(1, t, l-2)
            ans -= t-1
        else:
            t = sa.__getitem__(l-1) + 1
            st.apply(1, t, l-2)
            ans -= t-1
    print(ans)

if __name__ == "__main__":
    a()