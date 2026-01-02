class LazySegmentTree():
    def __init__(self, array, f, g, h, ti, ei):
        self.f = f
        self.g = g
        self.h = h
        self.ti = ti
        self.ei = ei
        self.height = height = len(array).bit_length()
        self.n = n = 2**height
        self.dat = dat = [ti] * n + array + [ti] * (n - len(array))
        self.laz = [ei] * (2 * n)
        for i in range(n - 1, 0, -1):  # build
            dat[i] = f(dat[i << 1], dat[i << 1 | 1])
 
    def reflect(self, k):
        # 遅延配列の値から真のノードの値を求める
        dat = self.dat
        ei = self.ei
        laz = self.laz
        g = self.g
        return self.dat[k] if laz[k] is ei else g(dat[k], laz[k])
 
    def evaluate(self, k):
        # 遅延配列を子ノードに伝播させる
        laz = self.laz
        ei = self.ei
        reflect = self.reflect
        dat = self.dat
        h = self.h
        if laz[k] is ei:
            return
        laz[(k << 1) | 0] = h(laz[(k << 1) | 0], laz[k])
        laz[(k << 1) | 1] = h(laz[(k << 1) | 1], laz[k])
        dat[k] = reflect(k)
        laz[k] = ei
 
    def thrust(self, k):
        height = self.height
        evaluate = self.evaluate
        for i in range(height, 0, -1):
            evaluate(k >> i)
 
    def recalc(self, k):
        dat = self.dat
        reflect = self.reflect
        f = self.f
        while k:
            k >>= 1
            dat[k] = f(reflect((k << 1) | 0), reflect((k << 1) | 1))
 
    def update(self, a, b, x):
        # 半開区間[a,b)の遅延配列の値をxに書き換える
        thrust = self.thrust
        n = self.n
        h = self.h
        laz = self.laz
        recalc = self.recalc
        a += n
        b += n - 1
        l = a
        r = b + 1
        thrust(a)
        thrust(b)
        while l < r:
            if l & 1:
                laz[l] = h(laz[l], x)
                l += 1
            if r & 1:
                r -= 1
                laz[r] = h(laz[r], x)
            l >>= 1
            r >>= 1
        recalc(a)
        recalc(b)
 
    def set_val(self, a, x):
        # aの値を変更する
        n = self.n
        thrust = self.thrust
        dat = self.dat
        laz = self.laz
        recalc = self.recalc
        ei = self.ei
        a += n
        thrust(a)
        dat[a] = x
        laz[a] = ei
        recalc(a)
 
    def query(self, a, b):
        # 半開区間[a,b)に対するクエリに答える
        f = self.f
        ti = self.ti
        n = self.n
        thrust = self.thrust
        reflect = self.reflect
        a += n
        b += n - 1
        thrust(a)
        thrust(b)
        l = a
        r = b + 1
        vl = vr = ti
        while l < r:
            if l & 1:
                vl = f(vl, reflect(l))
                l += 1
            if r & 1:
                r -= 1
                vr = f(reflect(r), vr)
            l >>= 1
            r >>= 1
        return f(vl, vr)
    
def pow_k(x,n,p=10**9+7):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2!=0:
            K=(K*x)%p
        x=(x*x)%p
        n//=2
    return (K*x)%p


import sys
input = sys.stdin.readline
MI=lambda:map(int,input().split())
N,Q=MI()
H=10**9+7

mod=998244353
tenmod=[pow_k(10,i,mod) for i in range(N+1)]

inv9=pow_k(9,mod-2,mod)
def f(a, b):
    an,ah=divmod(a,H)
    bn,bh=divmod(b,H)
    return ((an*tenmod[bh]+bn)%mod)*H + ah+bh
 
def g(a, b):
    ah=a%H
    return (((tenmod[ah]-1)*inv9)%mod*b)*H + ah

h = lambda a, b: b
ti = 0
ei = 0


lst=LazySegmentTree([1*H+1]*N,f=f,g=g,h=h,ti=ti,ei=ei)

for _ in [0]*Q:
    l,r,d=MI()
    lst.update(l-1,r,d)
    print(lst.query(0,N)//H)