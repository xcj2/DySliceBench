import sys
input = lambda: sys.stdin.readline().rstrip()
class SegmentTreeDual():
    def __init__(self, init, initX, unitA, g, h):
        self.g = g # (X, A, size) -> X
        self.h = h # (A, A) -> A
        self.unitA = unitA
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [initX] * (self.n * 2)
            self.size = [1] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [initX] * self.n + init + [initX] * (self.n - len(init))
            self.size = [0] * self.n + [1] * len(init) + [0] * (self.n - len(init))
    
        for i in range(self.n - 1, 0, -1):
            self.size[i] = self.size[i*2] + self.size[i*2|1]
        
        self.A = [unitA] * (self.n * 2)
        
    def calc(self, i):
        return self.g(self.X[i], self.A[i], self.size[i])
    
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
    
    def check(self, randX, randA, maxs, rep):
        from random import randrange
        for _ in range(rep):
            x = randX()
            a = randA()
            b = randA()
            c = randA()
            s = randrange(1, maxs + 1)
            err = 0
            if not h(a, unitA) == h(unitA, a) == a:
                err = 1
                print("!!!!! unitA Error !!!!!")
                print("unitA =", unitA)
                print("a =", a)
                print("f(a, unitA) =", f(a, unitA))
                print("f(unitA, a) =", f(unitA, a))
                
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
                print("!!!!! Act Error !!!!!")
                print("x, a, b, s, g(x, a, s), h(a, b) =", x, a, b, s, g(x, a, s), h(a, b))
                print("g(g(x, a, s), b, s) =", g(g(x, a, s), b, s))
                print("g(x, h(a, b), s)    =", g(x, h(a, b), s))
            
            if err:
                break
                assert h(a, unitA) == h(unitA, a) == a
                assert h(h(a, b), c) == h(a, h(b, c))
                assert g(x, unitA, s) == x
                assert g(g(x, a, s), b, s) == g(x, h(a, b), s)
        else:
            pass
            print("Monoid Check OK!")
    
    def debug(self):
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

N, K = map(int, input().split())
M = 300300
g = lambda x, a, s: max(x, a)
# h = lambda a, b: a if b == -1 else b
h = max
unitA = 0
initX = 0
st = SegmentTreeDual(M, initX, unitA, g, h)
# st = SegmentTreeDual([-inf] + [i for i in range(1, W + 1)] + [-inf] * (N - W - 1), unitX, unitA, g, h)

if False:
    from random import randrange
    randX = lambda: randrange(11)
    randA = lambda: randrange(20)
    maxs = 10
    rep = 1000
    st.check(randX, randA, maxs, rep)

for _ in range(N):
    a = int(input())
    # print("a =", a)
    x = st.getvalue(a)
    l = max(a - K, 0)
    r = min(a + K + 1, M)
    st.operate_range(l, r, x + 1)
    # print([st.getvalue(i) for i in range(N + 1)])

print(max([st.getvalue(i) for i in range(M)]))