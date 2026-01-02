import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
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
            
            # preparing indices
            indices = []
            l0 = (l // (l & -l))     // 2
            r0 = (r // (r & -r) - 1) // 2
            while r0 > l0:
                indices.append(r0)
                r0 //= 2
            while l0 > r0:
                indices.append(l0)
                l0 //= 2
            while l0 and l0 != r0:
                indices.append(r0)
                r0 //= 2
                if l0 == r0:
                    break
                indices.append(l0)
                l0 //= 2
            while r0:
                indices.append(r0)
                r0 //= 2
    
            # propagation
            for i in reversed(indices):
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
            for i in indices:
                self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
                self.lazy[i] = self.oe
                
            
        def folded(self, l, r):
            l += self.n
            r += self.n
    
            # preparing indices
            indices = []
            l0 = (l // (l & -l))     // 2
            r0 = (r // (r & -r) - 1) // 2
            while r0 > l0:
                indices.append(r0)
                r0 //= 2
            while l0 > r0:
                indices.append(l0)
                l0 //= 2
            while l0 and l0 != r0:
                indices.append(r0)
                r0 //= 2
                if l0 == r0:
                    break
                indices.append(l0)
                l0 //= 2
            while r0:
                indices.append(r0)
                r0 //= 2
            
            # propagation
            for i in reversed(indices):
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


    mod=998244353
    N,Q=MI()
    
    POW=[1]
    for _ in range(N+5):
        a=POW[-1]
        a*=10
        a%=mod
        POW.append(a)
        
    inv9=pow(9,mod-2,mod)#9でわる
        
    MM=32
    mask=(1<<MM)-1
    # (数，今見てる数の桁数)を1つにまとめる
    def enc(a,d):
        return (a<<MM) + d
    
    def dec(v):
        a=v>>MM
        d=v&mask
        return a,d
    
    mide=enc(1,1)
    monoid_data=[mide]*N

        
    monoid_ide=0#0を足したいからこれで
    ope_ide=0
    
    def fmm(m1,m2):
        # print(m1,m2)
        a1,d1=dec(m1)
        a2,d2=dec(m2)
        
        # print(a1,d1,a2,d2)
        
        temp=a1*POW[d2]+a2
        
        return enc(temp%mod,d1+d2)#桁数は足せば良い
    
    def fmo(m1,o1):
        if o1:
            # o1がd1桁だけ続くものを返したい
            a1,d1=dec(m1)
            
            temp=(o1*(POW[d1]-1)*inv9)#1がd1桁
            return enc(temp%mod,d1)
        else:
            return m1
    
    def foo(o1,o2):
        if o2:
            return o2
        else:
            return o1
    
    Lseg=LazySegmentTree(monoid_data,monoid_ide,ope_ide,fmm,fmo,foo)
    
    for _ in range(Q):
        # print("---")
        l,r,d=MI()
        l-=1
        r-=1
        Lseg.effect(l,r+1,d)
        ans=Lseg.folded(0,N)
        a,d=dec(ans)
        print(a)
    
    
    

        



main()
