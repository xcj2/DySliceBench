MOD = 998244353
class LazySegmentTree:  # from https://atcoder.jp/contests/practice2/submissions/16598122
    __slots__ = ["n", "data", "lazy", "me", "oe", "fmm", "fmo", "foo"]

    def __init__(self, monoid_data, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator,
                func_operator_operator):
        self.me = monoid_identity
        self.oe = operator_identity
        self.fmm = func_monoid_monoid
        self.fmo = func_monoid_operator
        self.foo = func_operator_operator

        self.n = len(monoid_data)
        self.data = monoid_data*2
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.fmm(self.data[2*i], self.data[2*i+1])
        self.lazy = [self.oe]*(self.n*2)

    def replace(self, index, value):
        index += self.n

        # propagation
        for shift in range(index.bit_length()-1, 0, -1):
            i = index>>shift
            self.lazy[2*i] = self.foo(self.lazy[2*i], self.lazy[i])
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
            self.data[i] = self.fmm(self.fmo(self.data[2*i], self.lazy[2*i]),
                                    self.fmo(self.data[2*i+1], self.lazy[2*i+1]))
            self.lazy[i] = self.oe

    def effect(self, l, r, operator):
        l += self.n
        r += self.n

        # preparing indices
        indices = []
        l0 = (l//(l&-l)) >> 1
        r0 = (r//(r&-r)-1) >> 1
        while r0 > l0:
            indices.append(r0)
            r0 >>= 1
        while l0 > r0:
            indices.append(l0)
            l0 >>= 1
        while l0 and l0 != r0:
            indices.append(r0)
            r0 >>= 1
            if l0 == r0:
                break
            indices.append(l0)
            l0 >>= 1
        while r0:
            indices.append(r0)
            r0 >>= 1

        # propagation
        for i in reversed(indices):
            self.lazy[2*i] = self.foo(self.lazy[2*i], self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # effect
        while l < r:
            if l&1:
                self.lazy[l] = self.foo(self.lazy[l], operator)
                l += 1
            if r&1:
                r -= 1
                self.lazy[r] = self.foo(self.lazy[r], operator)
            l >>= 1
            r >>= 1

        # recalculation
        for i in indices:
            self.data[i] = self.fmm(self.fmo(self.data[2*i], self.lazy[2*i]),
                                    self.fmo(self.data[2*i+1], self.lazy[2*i+1]))
            self.lazy[i] = self.oe

    def folded(self, l, r):
        l += self.n
        r += self.n

        # preparing indices
        indices = []
        l0 = (l//(l&-l))//2
        r0 = (r//(r&-r)-1)//2
        while r0 > l0:
            indices.append(r0)
            r0 >>= 1
        while l0 > r0:
            indices.append(l0)
            l0 >>= 1
        while l0 and l0 != r0:
            indices.append(r0)
            r0 >>= 1
            if l0 == r0:
                break
            indices.append(l0)
            l0 >>= 1
        while r0:
            indices.append(r0)
            r0 >>= 1

        # propagation
        for i in reversed(indices):
            self.lazy[2*i] = self.foo(self.lazy[2*i], self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # fold
        left_folded = self.me
        right_folded = self.me
        while l < r:
            if l&1:
                left_folded = self.fmm(left_folded, self.fmo(self.data[l], self.lazy[l]))
                l += 1
            if r&1:
                r -= 1
                right_folded = self.fmm(self.fmo(self.data[r], self.lazy[r]), right_folded)
            l >>= 1
            r >>= 1
        return self.fmm(left_folded, right_folded)
class ModInt:

    def __init__(self, x):
        self.x = x.x if isinstance(x, ModInt) else x % MOD

    __str__ = lambda self:str(self.x)
    __repr__ = __str__
    __int__ = lambda self: self.x
    __index__ = __int__

    __add__ = lambda self, other: ModInt(self.x + ModInt(other).x)
    __sub__ = lambda self, other: ModInt(self.x - ModInt(other).x)
    __mul__ = lambda self, other: ModInt(self.x * ModInt(other).x)
    __pow__ = lambda self, other: ModInt(pow(self.x, ModInt(other).x, MOD))
    __truediv__ = lambda self, other: ModInt(self.x * pow(ModInt(other).x, MOD - 2, MOD))
    __floordiv__ = lambda self, other: ModInt(self.x // ModInt(other).x)
    __radd__ = lambda self, other: ModInt(other + self.x)
    __rsub__ = lambda self, other: ModInt(other - self.x)
    __rpow__ = lambda self, other: ModInt(pow(other, self.x, MOD))
    __rmul__ = lambda self, other: ModInt(other * self.x)
    __rtruediv__ = lambda self, other: ModInt(other * pow(self.x, MOD - 2, MOD))
    __rfloordiv__ = lambda self, other: ModInt(other // self.x)

    __lt__ = lambda self, other: self.x < ModInt(other).x
    __gt__ = lambda self, other: self.x > ModInt(other).x
    __le__ = lambda self, other: self.x <= ModInt(other).x
    __ge__ = lambda self, other: self.x >= ModInt(other).x
    __eq__ = lambda self, other: self.x == ModInt(other).x
    __ne__ = lambda self, other: self.x != ModInt(other).x
def main():
    import sys
    sys.setrecursionlimit(311111)
    # import numpy as np
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    n,q  = ina()

    tmp = [(1,1) for i in range(0,n)]
    tmpx = 1
    tmpx1 = 1
    ten = []
    one = []
    for i in range(311111):
        ten.append(tmpx)
        one.append(tmpx1)
        tmpx1*=10
        tmpx1+=1
        tmpx*=10
        tmpx1%=MOD
        tmpx%=MOD
    # print(ten)
    def op(x1,x2):
        val1,size1 = x1
        val2,size2 = x2
        size = size1+size2
        val = (val1*ten[size2])+val2
        return val%MOD,size
    e = (0,0)
    def maptmp(s,f):
        if(f == -1):
            return s
        else:
            return f*one[s[1]-1]%MOD,s[1]
    def comp(g,f):
        return f if f!=-1 else g

    ident = -1
    tmptree = LazySegmentTree(tmp,e,ident,op,maptmp,comp)

    for _ in range(q):
        l,r,x = ina()
        tmptree.effect(l-1,r,x)
        print(tmptree.folded(0,n)[0])
        

        
















    
    



    


        
        
        


    
        


        


    




















if __name__ == "__main__":
    main()
