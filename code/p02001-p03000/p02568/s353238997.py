# オリジナル。読みやすいはず。


MOD = 998244353
mask = (1 << 32) - 1


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


    def _propagate(self, index_of_tree):
        for shift in range(index_of_tree.bit_length()-1, 0, -1):
            i = index_of_tree >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe


    def _recalc(self, i):
        while i > 1:
            i //= 2
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe


    def replace(self, index, value):
        index += self.n
        self._propagate(index)
        self.data[index] = value
        self.lazy[index] = self.oe
        self._recalc(index)


    def effect(self, l, r, operator):
        l += self.n
        r += self.n
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1
        self._propagate(l0)
        self._propagate(r0)
        while l < r:
            if l % 2:
                self.lazy[l] = self.foo(self.lazy[l], operator)
                l += 1
            if r % 2:
                r -= 1
                self.lazy[r] = self.foo(self.lazy[r], operator)
            l //= 2
            r //= 2
        self._recalc(l0)
        self._recalc(r0)
        
        
    def folded(self, l, r):
        l += self.n
        r += self.n
        self._propagate(l // (l & -l))
        self._propagate(r // (r & -r) - 1)
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


# Monoid は (値 << 32) + 要素数 にする。
# Operator も (b << 32) + c
def main():
    import sys
    input = sys.stdin.buffer.readline

    def fmm(m1, m2):
        m = m1 + m2
        return (((m >> 32) % MOD) << 32) + (m & mask)
    
    def fmo(m1, o1):
        val = m1 >> 32
        cnt = m1 & mask
        b = o1 >> 32
        c = o1 & mask
        return (((b * val + c * cnt) % MOD) << 32) + cnt

    def foo(o1, o2):
        b1 = o1 >> 32
        c1 = o1 & mask
        b2 = o2 >> 32
        c2 = o2 & mask
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
    main()