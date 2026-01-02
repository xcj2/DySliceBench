import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


class LazySegTree:
    data_unit = 0
    data_f = max
    operator_unit = 0
    
    @classmethod
    def operator_f(cls, x, y):
      return x + y
    
    @classmethod
    def operate(cls, x, y):
      return x + y
    
    def __init__(self, N):
        self.N = N
        self.H = (self.N - 1).bit_length()
        self.data = [self.data_unit] * (N + N)
        self.lazy = [self.operator_unit] * (N + N)

    def build(self, raw_data):
        data = self.data
        f = self.data_f
        N = self.N
        data[N:] = raw_data[:]
        for i in range(N - 1, 0, -1):
            data[i] = f(data[i << 1], data[i << 1 | 1])

    def reflect(self, k):
        x = self.lazy[k]
        if x == self.operator_unit:
            return self.data[k]
        else:
            return self.operate(self.data[k], x)

    def propagate(self, k):
        lazy = self.lazy
        if lazy[k] == self.operator_unit:
            return
        h = self.operator_f
        lazy[k << 1] = h(lazy[k << 1], lazy[k])
        lazy[k << 1 | 1] = h(lazy[k << 1 | 1], lazy[k])
        self.data[k] = self.reflect(k)
        self.lazy[k] = self.operator_unit

    def thrust(self, k):
        for i in range(self.H, 0, -1):
            self.propagate(k >> i)

    def recalc(self, k):
        data = self.data
        f = self.data_f
        while k > 1:
            k >>= 1
            data[k] = f(self.reflect(k << 1), self.reflect(k << 1 | 1))

    def update(self, L, R, x):
        lazy = self.lazy
        h = self.operator_f
        L0 = L = L + self.N
        R0 = R = R + self.N
        self.thrust(L0)
        self.thrust(R0 - 1)
        while L < R:
            if L & 1:
                lazy[L] = h(lazy[L], x)
                L += 1
            if R & 1:
                R -= 1
                lazy[R] = h(lazy[R], x)
            L >>= 1
            R >>= 1
        self.recalc(L0)
        self.recalc(R0 - 1)

    def set_val(self, i, x):
        i += self.N
        self.thrust(i)
        self.data[i] = x
        self.lazy[i] = self.operator_unit
        self.recalc(i)

    def fold(self, L, R):
        f = self.data_f
        L += self.N
        R += self.N
        self.thrust(L)
        self.thrust(R - 1)
        vl = self.data_unit
        vr = self.data_unit
        while L < R:
            if L & 1:
                vl = f(vl, self.reflect(L))
                L += 1
            if R & 1:
                R -= 1
                vr = f(self.reflect(R), vr)
            L >>= 1
            R >>= 1
        return f(vl, vr)

N, M = map(int, readline().split())
R_to_LA = [[] for _ in range(N + 1)]
m = map(int, read().split())
for L, R, A in zip(m, m, m):
    R_to_LA[R].append((L, A))

seg = LazySegTree(N+1)
 
for R in range(1, N + 1):
    x = seg.data[1]
    seg.update(R, R + 1, x)
    for L, A in R_to_LA[R]:
        seg.update(L, R + 1, A)
print(seg.fold(0, N+1))