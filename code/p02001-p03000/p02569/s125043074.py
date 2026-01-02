# 関数を展開した。手持ちの遅延セグ木クラス内では最速。


MOD = 998244353
mask32 = (1 << 32) - 1
mask20 = (1 << 20) - 1
mask40 = (1 << 40) - 1


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
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1

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
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1

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

def test():
    import random

    def madd(a, b):
        return (a + b) % MOD

    def mmul(a, b):
        return a * b % MOD

    lst = LazySegmentTree([0] * 10, 0, 1, madd, mmul, mmul)
    ls = [0] * 10

    for _ in range(10000000):
        if random.randint(0, 1): # effect
            l = random.randint(0, 9)
            r = random.randint(l+1, 10)
            e = random.randint(1, 782)
            lst.effect(l, r, e)
            for i in range(l, r):
                ls[i] *= e
                ls[i] %= MOD
        else:
            l = random.randint(0, 9)
            r = random.randint(l+1, 10)
            if lst.folded(l, r) != sum(ls[l:r]):
                print(ls)
                print(l, r)
                print(lst.folded(l, r))

def ruq():
    # Monoid は -1 を単位元とする。
    # Operator も -1 を単位元とする。 
    import sys
    input = sys.stdin.buffer.readline

    def f(m1, m2):
        if m2 == -1:
            return m1
        else:
            return m2

    N, Q = map(int, input().split())
    monoid_data = [2147483647] * N
    lst = LazySegmentTree(monoid_data, -1, -1, f, f, f)
    for _ in range(Q):
        q, *k = map(int, input().split())
        if q == 0:
            lst.effect(k[0], k[1] + 1, k[2])
        else:
            print(lst.folded(k[0], k[0] + 1))

def atc():
    # Monoid:   ((0の数) << 60) + ((1の数) << 40) + (転倒数)
    # Operator: 反転するか? (1 or 0) 

    import sys
    input = sys.stdin.buffer.readline

    N, Q = map(int, input().split())
    monoid_data = [1099511627776 if A == b'1' else 1152921504606846976 for A in input().split()]

    def fmm(m1, m2):
        return m1 + m2 + ((m1 >> 40) & mask20) * (m2 >> 60)

    def fmo(m1, o1):
        if o1:
            cnt = m1 & mask40
            c1 = (m1 >> 40) & mask20 
            c0 = m1 >> 60
            return (c1 << 60) + (c0 << 40) + ((c0 * c1) - cnt)
        else:
            return m1 

    def foo(o1, o2):
        return o1 ^ o2

    lst = LazySegmentTree(monoid_data, 0, 0, fmm, fmo, foo)

    for _ in range(Q):
        T, L, R = map(int, input().split())
        if T == 1:
            lst.effect(L-1, R, 1)
        else:
            print(lst.folded(L-1, R) & mask40)

def test2():
    import sys
    input = sys.stdin.buffer.readline

    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    monoid_data = [1099511627776 if A else 1152921504606846976 for A in As]

    def fmm(m1, m2):
        return m1 + m2 + ((m1 >> 40) & mask20) * (m2 >> 60)

    def fmo(m1, o1):
        if o1:
            cnt = m1 & mask40
            c1 = (m1 >> 40) & mask20 
            c0 = m1 >> 60
            return (c1 << 60) + (c0 << 40) + ((c0 * c1) - cnt)
        else:
            return m1 

    def foo(o1, o2):
        return o1 ^ o2

    lst = LazySegmentTree(monoid_data, 0, 0, fmm, fmo, foo)

    for _ in range(Q):
        T, L, R = map(int, input().split())
        if T == 1:
            lst.effect(L-1, R, 1)
            for i in range(L-1, R):
                As[i] ^= 1
        else:
            print(As)
            cnt = 0
            for i in range(L-1, R):
                for j in range(i+1, R):
                    cnt += (As[i]) * (As[j] ^ 1)
            if cnt != (lst.folded(L-1, R) & mask40):
                print("WA!")
                print(As[L-1:R])
                print(lst.folded(L-1, R) & mask40, cnt)


if __name__ == "__main__":
    atc()
