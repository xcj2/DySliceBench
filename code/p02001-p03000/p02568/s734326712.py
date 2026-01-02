# AtCoderのPyPy3環境だとこれが一番速い。

MOD = 998244353
mask32 = (1 << 32) - 1

class LazySegmentTree:

    __slots__ = ["n", "data", "lazy", "me", "oe", "fmm", "fmo", "foo"]

    def __init__(self, monoid_data, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator, func_operator_operator):
        self.me = monoid_identity
        self.oe = operator_identity
        self.fmm = func_monoid_monoid
        self.fmo = func_monoid_operator
        self.foo = func_operator_operator

        assert monoid_data
        self.n = len(monoid_data)
        self.data = monoid_data * 2
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.fmm(self.data[2*i], self.data[2*i+1])
        self.lazy = [self.oe] * (self.n * 2)


    def replace(self, index, value):
        assert 0 <= index < self.n
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
        assert 0 <= l < r <= self.n
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
        assert 0 <= l < r <= self.n
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
    # Monoid は (値 << 32) + 要素数 にする。
    # Operator も (b << 32) + c    
    import sys
    input = sys.stdin.buffer.readline

    def fmm(m1, m2):
        m = m1 + m2
        return (((m >> 32) % MOD) << 32) + (m & mask32)
    
    def fmo(m1, o1):
        val = m1 >> 32
        cnt = m1 & mask32
        b = o1 >> 32
        c = o1 & mask32
        return (((b * val + c * cnt) % MOD) << 32) + cnt

    def foo(o1, o2):
        b1 = o1 >> 32
        c1 = o1 & mask32
        b2 = o2 >> 32
        c2 = o2 & mask32
        b = b1 * b2 % MOD
        c = (c1 * b2 + c2) % MOD
        return (b << 32) + c

    N, Q = map(int, input().split())
    monoid_data = [(A << 32) + 1 for A in map(int, input().split())]
    lst = LazySegmentTree(monoid_data, 1, 1 << 32, fmm, fmo, foo)
    for _ in range(Q):
        q, *k = map(int, input().split())
        if q == 0:
            o = (k[2] << 32) + k[3]
            lst.effect(k[0], k[1], o)
        else:
            print(lst.folded(k[0], k[1]) >> 32)

if __name__ == "__main__":
    yosupo()
