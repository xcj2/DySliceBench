import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTree():
    def __init__(self, init, unitX, unitA, f, g, h):
        self.f = f # (X, X) -> X
        self.g = g # (X, A, size) -> X
        self.h = h # (A, A) -> A
        self.unitX = unitX
        self.unitA = unitA
        self.f = f
        if type(init) == int:
            self.n = init
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
            self.size = [1] * (self.n * 2)
        else:
            self.n = len(init)
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            self.size = [0] * self.n + [1] * len(init) + [0] * (self.n - len(init))
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
    
        for i in range(self.n - 1, 0, -1):
            self.size[i] = self.size[i*2] + self.size[i*2|1]
        
        self.A = [unitA] * (self.n * 2)
        
    def update(self, i, x):
        i += self.n
        self.propagate_above(i)
        self.X[i] = x
        self.A[i] = unitA
        self.calc_above(i)
    
    def calc(self, i):
        return self.g(self.X[i], self.A[i], self.size[i])
    
    def calc_above(self, i):
        i >>= 1
        while i:
            self.X[i] = self.f(self.calc(i*2), self.calc(i*2|1))
            i >>= 1
    
    def propagate(self, i):
        self.X[i] = self.g(self.X[i], self.A[i], self.size[i])
        self.A[i*2] = self.h(self.A[i*2], self.A[i])
        self.A[i*2|1] = self.h(self.A[i*2|1], self.A[i])
        self.A[i] = self.unitA
        
    def propagate_above(self, i):
        H = i.bit_length()
        for h in range(H, 0, -1):
            self.propagate(i >> h)
    
    def propagate_all(self):
        for i in range(1, self.n):
            self.propagate(i)
    
    def getrange(self, l, r):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        
        al = self.unitX
        ar = self.unitX
        while l < r:
            if l & 1:
                al = self.f(al, self.calc(l))
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.calc(r), ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)
    
    def getvalue(self, i):
        i += self.n
        self.propagate_above(i)
        return self.calc(i)
    
    def operate_range(self, l, r, a):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        while l < r:
            if l & 1:
                self.A[l] = self.h(self.A[l], a)
                l += 1
            if r & 1:
                r -= 1
                self.A[r] = self.h(self.A[r], a)
            l >>= 1
            r >>= 1
        
        self.calc_above(l0)
        self.calc_above(r0)
    
    def check(self, randX, randA, maxs, rep):
        from random import randrange
        for _ in range(rep):
            x = randX()
            y = randX()
            z = randX()
            a = randA()
            b = randA()
            c = randA()
            s = randrange(1, maxs + 1)
            t = randrange(1, maxs + 1)
            err = 0
            if not f(x, unitX) == f(unitX, x) == x:
                err = 1
                print("!!!!! unitX Error !!!!!")
                print("unitX =", unitX)
                print("x =", x)
                print("f(x, unitX) =", f(x, unitX))
                print("f(unitX, x) =", f(unitX, x))
            
            if not h(a, unitA) == h(unitA, a) == a:
                err = 1
                print("!!!!! unitA Error !!!!!")
                print("unitA =", unitA)
                print("a =", a)
                print("f(a, unitA) =", f(a, unitA))
                print("f(unitA, a) =", f(unitA, a))
                
            if not f(f(x, y), z) == f(x, f(y, z)):
                err = 1
                print("!!!!! Associativity Error X !!!!!")
                print("x, y, z, f(x, y), f(y, x) =", x, y, z, f(x, y), f(y, x))
                print("f(f(x, y), z) =", f(f(x, y), z))
                print("f(x, f(y, z)) =", f(x, f(y, z)))
            
            if not h(h(a, b), c) == h(a, h(b, c)):
                err = 1
                print("!!!!! Associativity Error A !!!!!")
                print("a, b, c, h(a, b), h(b, c) =", a, b, c, h(a, b), h(b, c))
                print("h(h(a, b), c) =", h(h(a, b), c))
                print("h(a, h(b, c)) =", h(a, h(b, c)))
            
            if not g(x, unitA, s) == x:
                err = 1
                print("!!!!! Identity Error !!!!!")
                print("unitA, x, s =", unitA, x, s)
                print("g(x, unitA, s) =", g(x, unitA, s))
            
            if not g(g(x, a, s), b, s) == g(x, h(a, b), s):
                err = 1
                print("!!!!! Act Error 1 !!!!!")
                print("x, a, b, s, g(x, a, s), h(a, b) =", x, a, b, s, g(x, a, s), h(a, b))
                print("g(g(x, a, s), b, s) =", g(g(x, a, s), b, s))
                print("g(x, h(a, b), s)    =", g(x, h(a, b), s))
            
            if not g(f(x, y), a, s + t) == f(g(x, a, s), g(y, a, t)):
                err = 1
                print("!!!!! Act Error 2 !!!!!")
                print("x, y, a, s, t, f(x, y), g(x, a, s), g(y, a, t) =", x, y, a, s, t, f(x, y), g(x, a, s), g(y, a, t))
                print("g(f(x, y), a, s + t)      =", g(f(x, y), a, s + t))
                print("f(g(x, a, s), g(y, a, t)) =", f(g(x, a, s), g(y, a, t)))
            
            if err:
                break
                assert f(x, unitX) == f(unitX, x) == x
                assert h(a, unitA) == h(unitA, a) == a
                assert f(f(x, y), z) == f(x, f(y, z))
                assert h(h(a, b), c) == h(a, h(b, c))
                assert g(x, unitA, s) == x
                assert g(g(x, a, s), b, s) == g(x, h(a, b), s)
                assert g(f(x, y), a, s + t) == f(g(x, a, s), g(y, a, t))
        else:
            pass
            print("Monoid Check OK!")
    
    def debug1(self):
        print("self.n =", self.n)
        deX = []
        deA = []
        deS = []
        a, b = self.n, self.n * 2
        while b:
            deX.append(self.X[a:b])
            deA.append(self.A[a:b])
            deS.append(self.size[a:b])
            a, b = a//2, a
        print("--- debug ---")
        for d in deX[::-1]:
            print(d)
        print("--- ---")
        for d in deA[::-1]:
            print(d)
        print("--- ---")
        for d in deS[::-1]:
            print(d)
        print("--- ---")
    
    def debug(self, k = 10):
        print("--- debug ---")
        print("point")
        for i in range(min(self.n - 1, k)):
            print(i, self.getvalue(i))
        print("prod")
        for i in range(min(self.n, k)):
            print(i, self.getrange(0, i))
        print("--- ---")


# ↓和を使うときはこっちの方が少し高速
# from operator import add
# f = lambda a, b: (a[0] * b[0] % P, (a[1] * b[0] + b[1]) % P) # 1次関数の合成


P = 998244353
inv9 = 443664157
mm = (1 << 18) - 1

def f(x, y):
    # print("f", x, y)
    l1, su1 = x & mm, x >> 18
    l2, su2 = y & mm, y >> 18
    return (((su1 + su2) % P) << 18) + l1

def g(x, a, s):
    l, su = x & mm, x >> 18
    return (((po10[s] - 1) * inv9 % P * po10[l] * a % P) << 18) + l if a else x
    
h = lambda a, b: b if b else a

unitX = 0
unitA = 0
N, Q = map(int, input().split())
x = 1
X = []
po10 = []
for i in range(N):
    X.append((x << 18) + i)
    po10.append(x)
    x = x * 10 % P
po10.append(x)

st = SegmentTree(X, unitX, unitA, f, g, h)

if False:
    from random import randrange
    randX = lambda: (randrange(-10, 11), randrange(-10, 11))
    randA = lambda: ["", "A", "B"][randrange(3)]
    maxs = 10
    rep = 1000
    st.check(randX, randA, maxs, rep)

for _ in range(Q):
    l, r, d = map(int, input().split())
    l, r = N - r, N - l + 1
    st.operate_range(l, r, d)
    print(st.X[1] >> 18)
