# AtCoderのPyPy3環境だとこれが一番速い。

class LazySegmentTree:

    __slots__ = ["n", "data", "lazy", "me", "oe", "fmm", "fmo", "foo"]

    def __init__(self, monoid_data, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator, func_operator_operator):
        self.me = monoid_identity
        self.oe = operator_identity
        self.fmm = func_monoid_monoid
        self.fmo = func_monoid_operator
        self.foo = func_operator_operator

        self.n = len(monoid_data)
        self.data = monoid_data * 2
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.fmm(self.data[2*i], self.data[2*i+1])
        self.lazy = [self.oe] * (self.n * 2)


    def replace(self, index, value):
        index += self.n

        # propagation
        for shift in range(index.bit_length()-1, 0, -1):
            i = index >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # update
        self.data[index] = value
        self.lazy[index] = self.oe

        # recalculation
        i = index
        while i > 1:
            i //= 2
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe


    def effect(self, l, r, operator):
        l += self.n
        r += self.n
        l0 = l
        r0 = r - 1
        while l0 % 2 == 0:
            l0 //= 2
        while r0 % 2 == 1:
            r0 //= 2

        # propagation
        for shift in range(l0.bit_length()-1, 0, -1):
            i = l0 >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe
        for shift in range(r0.bit_length()-1, 0, -1):
            i = r0 >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # effect
        while l < r:
            if l % 2:
                self.lazy[l] = self.foo(self.lazy[l], operator)
                l += 1
            if r % 2:
                r -= 1
                self.lazy[r] = self.foo(self.lazy[r], operator)
            l //= 2
            r //= 2

        # recalculation
        i = l0
        while i > 1:
            i //= 2
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe
        i = r0
        while i > 1:
            i //= 2
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe
            
        
    def folded(self, l, r):
        l += self.n
        r += self.n
        l0 = l
        r0 = r - 1
        while l0 % 2 == 0:
            l0 //= 2
        while r0 % 2 == 1:
            r0 //= 2

        # propagation
        for shift in range(l0.bit_length()-1, 0, -1):
            i = l0 >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe
        for shift in range(r0.bit_length()-1, 0, -1):
            i = r0 >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # fold
        left_folded = self.me
        right_folded = self.me
        while l < r:
            if l % 2:
                left_folded = self.fmm(left_folded, self.fmo(self.data[l], self.lazy[l]))
                l += 1
            if r % 2:
                r -= 1
                right_folded = self.fmm(self.fmo(self.data[r], self.lazy[r]), right_folded)
            l //= 2
            r //= 2
        return self.fmm(left_folded, right_folded)


def yosupo():
    import sys
    input = sys.stdin.buffer.readline

    whitened = 0
    N, Q = map(int, input().split())
    xs = LazySegmentTree([N - 2] * (N - 2), N - 2, N - 2, min, min, min)
    ys = LazySegmentTree([N - 2] * (N - 2), N - 2, N - 2, min, min, min)
    for _ in range(Q):
        t, x = map(int, input().split())
        x -= 2
        # print(x)
        if t == 1:
            tmp = xs.folded(x, x + 1)
            ys.effect(0, tmp, x)
            whitened += tmp
        else:
            tmp = ys.folded(x, x + 1)
            xs.effect(0, tmp, x)
            whitened += tmp

        # print([xs.folded(i, i + 1) for i in range(N - 2)])
        # print([ys.folded(i, i + 1) for i in range(N - 2)])

    print((N - 2) ** 2 - whitened)

if __name__ == "__main__":
    yosupo()
