import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTreeDual():
    def __init__(self, init, unitX, unitA, g, h):
        self.g = g # (X, A, size) -> X
        self.h = h # (A, A) -> A
        self.unitA = unitA
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
            self.size = [1] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
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
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
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

H, W = map(int, input().split())
inf = 1 << 18
g = lambda x, a, s: x if a == -1 else a
h = lambda a, b: a if b == -1 else b
unitA = -1
unitX = inf
N = W + 2
st1 = SegmentTreeDual([-inf] + [i for i in range(1, W + 1)] + [-inf] * (N - W - 1), unitX, unitA, g, h)

f2 = lambda x, y: min(x, y)
g2 = lambda x, a, s: x if a == -1 else a
h2 = lambda a, b: a if b == -1 else b
unitX = inf
unitA = -1
st2 = SegmentTree([inf] + [0 for i in range(1, W + 1)] + [inf] * (N - W - 1), unitX, unitA, f2, g2, h2)
for i in range(H):
    a, b = map(int, input().split())
    b += 1
    l = st1.getvalue(a-1)
    st2.operate_range(a, a+1, a - l)
    st2.operate_range(a+1, b, inf)
    r = st1.getvalue(b)
    st2.operate_range(b, b+1, b - r)
    st1.operate_range(a, b, l)
    print(st2.X[1] + i + 1 if st2.X[1] < inf else -1)
