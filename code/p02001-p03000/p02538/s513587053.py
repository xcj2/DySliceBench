class LazySegmentTree:


    __slots__ = ["n", "original_size", "log", "data", "lazy", "me", "oe", "fmm", "fmo", "foo"]


    def __init__(self, length_or_list, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator, func_operator_operator):
        self.me = monoid_identity
        self.oe = operator_identity
        self.fmm = func_monoid_monoid
        self.fmo = func_monoid_operator
        self.foo = func_operator_operator

        if isinstance(length_or_list, int):
            self.original_size = length_or_list
            self.log = (self.original_size - 1).bit_length()
            self.n = 1 << self.log
            self.data = [self.me] * (self.n * 2)
            self.lazy = [self.oe] * (self.n * 2)
        elif isinstance(length_or_list, list):
            self.original_size = len(length_or_list)
            self.log = (self.original_size - 1).bit_length()
            self.n = 1 << self.log
            self.data = [self.me] * self.n + length_or_list + [self.me] * (self.n - self.original_size)
            for i in range(self.n-1, 0, -1):
                self.data[i] = self.fmm(self.data[2*i], self.data[2*i+1])
            self.lazy = [self.oe] * (self.n * 2)
        else:
            raise TypeError(f"The argument 'length_or_list' must be an integer or a list, not {type(length_or_list).__name__}")
            

    def replace(self, index, value):
        if index < 0:
            index += self.original_size
        if not (0 <= index < self.original_size):
            raise IndexError("LazySegmentTree index out of range")

        index += self.n

        # propagation
        for shift in range(self.log, 0, -1):
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


    def __getitem__(self, index):
        if index < 0:
            index += self.original_size
        if not (0 <= index < self.original_size):
            raise IndexError("LazySegmentTree index out of range")

        index += self.n

        # propagation
        for shift in range(self.log, 0, -1):
            i = index >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        return self.data[index]


    def effect_single(self, index, operator):
        if index < 0:
            index += self.original_size
        if not (0 <= index < self.original_size):
            raise IndexError("LazySegmentTree index out of range")

        index += self.n

        # propagation
        for shift in range(self.log, 0, -1):
            i = index >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # update
        self.data[index] = self.fmo(self.data[index], operator)

        # recalculation
        i = index
        while i > 1:
            i //= 2
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe


    def effect(self, l, r, operator):
        if l < 0:
            l += self.original_size
        if r < 0:
            r += self.original_size
        if not 0 <= l <= r <= self.original_size:
            raise IndexError("LazySegmentTree index out of range")

        if l == r:
            return

        l += self.n
        r += self.n

        l0 = l
        r0 = r - 1
        while l0 % 2 == 0:
            l0 //= 2
        while r0 % 2 == 1:
            r0 //= 2
        
        # propagation
        for shift in range(self.log, 0, -1):
            i = l >> shift
            if i << shift != l:
                self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
                self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
                self.data[i] = self.fmo(self.data[i], self.lazy[i])
                self.lazy[i] = self.oe
            i = r >> shift
            if i << shift != r:
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
        if l < 0:
            l += self.original_size
        if r < 0:
            r += self.original_size
        if not 0 <= l <= r <= self.original_size:
            raise IndexError("LazySegmentTree index out of range")

        if l == r:
            return self.me 

        l += self.n
        r += self.n

        # propagation
        for shift in range(self.log, 0, -1):
            i = l >> shift
            if i << shift != l:
                self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
                self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
                self.data[i] = self.fmo(self.data[i], self.lazy[i])
                self.lazy[i] = self.oe
            i = r >> shift
            if i << shift != r:
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


    def all_folded(self):
        return self.data[1]

    
    def max_right(self, l, f):
        if l < 0:
            l += self.original_size
        if not (0 <= l <= self.original_size):
            raise IndexError("LazySegmentTree index out of range")
        assert f(self.me)

        if l == self.original_size:
            return self.original_size

        l += self.n

        # propagation
        for shift in range(self.log, 0, -1):
            i = l >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        left_folded = self.me
        while True:
            while l % 2 == 0:
                l //= 2
            if not f(self.fmm(left_folded, self.data[l])):
                while l < self.n:
                    i = l
                    self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
                    self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
                    self.data[i] = self.fmo(self.data[i], self.lazy[i])
                    self.lazy[i] = self.oe
                    l *= 2
                    if f(self.fmm(left_folded, self.data[l])):
                        left_folded = self.fmm(left_folded, self.data[l])
                        l += 1
                return l - self.n
            left_folded = self.fmm(left_folded, self.data[l])
            l += 1
            if l == l & -l:
                break
        return self.original_size

    def min_left(self, r, f):
        if r < 0:
            r += self.original_size
        if not (0 <= r <= self.original_size):
            raise IndexError("LazySegmentTree index out of range")
        assert f(self.me)

        if r == 0:
            return 0
        
        r += self.n

        # propagation
        for shift in range(self.log, 0, -1):
            i = r >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        right_folded = self.me
        while True:
            r -= 1
            while (r > 1 and r % 2):
                r //= 2
            if not f(self.fmm(self.data[r], right_folded)):
                while r < self.n:
                    i = r
                    self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
                    self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
                    self.data[i] = self.fmo(self.data[i], self.lazy[i])
                    self.lazy[i] = self.oe
                    r = 2 * r + 1
                    if f(self.fmm(self.data[r], right_folded)):
                        right_folded = self.fmm(self.data[r], right_folded)
                        r -= 1
                return r + 1 - self.n
            right_folded = self.fmm(self.data[r], right_folded)
            if r == r & -r:
                break
        return 0


MOD = 998244353
mask32 = (1 << 32) - 1


import sys
input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read



N, Q = map(int, input().split())


pw = [1]
for _ in range(N + 2):
    pw.append(pw[-1] * 10 % MOD)


# 値 << 32 + 長さ
def fmm(m1, m2):
    v1 = m1 >> 32
    l1 = m1 & mask32
    v2 = m2 >> 32
    l2 = m2 & mask32
    v = (v1 * pw[l2] + v2) % MOD
    l = l1 + l2
    return (v << 32) + l

inv9 = pow(9, MOD - 2, MOD)
def fmo(m, o):
    if o == -1:
        return m
    else:
        l = m & mask32
        v = o * (pw[l] - 1) * inv9 % MOD
        return (v << 32) + l

def foo(o1, o2):
    if o2 == -1:
        return o1
    else:
        return o2

lst = LazySegmentTree([(1 << 32) + 1] * N, 0, -1, fmm, fmo, foo)

LRDs = map(int, read().split())
for L, R, D in zip(LRDs, LRDs, LRDs):
    lst.effect(L - 1, R, D)
    print(lst.all_folded() >> 32)

