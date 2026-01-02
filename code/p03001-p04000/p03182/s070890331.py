import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


class LazySegmentTree:
    """ range add and range max"""

    def __init__(self, A):
        INF = 10 ** 18
        self.unit = -INF
        self.N = len(A)
        self.H = (self.N - 1).bit_length()
        self.W = 1 << self.H
        self.lazy = [0] * (2 * self.W)
        self.build(A)

    def build(self, A):
        W = self.W
        data = [self.unit] * (2 * W)
        for i, x in enumerate(A):
            data[W + i] = x
        for i in range(W - 1, 0, -1):
            data[i] = max(data[i << 1], data[i << 1 | 1])
        self.data = data

    def apply(self, p, value):
        self.data[p] += value
        self.lazy[p] += value

    def build_local(self, i):
        while i > 1:
            i >>= 1
            self.data[i] = max(self.data[i << 1], self.data[i << 1 | 1]) + self.lazy[i]

    def propagate(self, p):
        for s in range(self.H, 0, -1):
            i = p >> s
            x = self.lazy[i]
            self.apply(i << 1, x)
            self.apply(i << 1 | 1, x)
            self.lazy[i] = 0

    def range_add(self, L, R, x):
        """ add x to [L,R) """
        L += self.W
        R += self.W
        L0 = L
        R0 = R
        while L < R:
            if L & 1:
                self.apply(L, x)
                L += 1
            if R & 1:
                R -= 1
                self.apply(R, x)
            L >>= 1
            R >>= 1
        self.build_local(L0)
        self.build_local(R0 - 1)

    def range_max(self, L, R):
        """ max of [L,R) """
        L += self.W
        R += self.W
        self.propagate(L)
        self.propagate(R - 1)
        ret = self.unit
        while L < R:
            if L & 1:
                x = self.data[L]
                if ret < x:
                    ret = x
                L += 1
            if R & 1:
                R -= 1
                x = self.data[R]
                if ret < x:
                    ret = x
            L >>= 1
            R >>= 1


N, M = map(int, readline().split())
R_to_LA = [[] for _ in range(N + 1)]
m = map(int, read().split())
for L, R, A in zip(m, m, m):
    R_to_LA[R].append((L, A))

seg = LazySegmentTree([0] * (N + 1))

for R in range(1, N + 1):
    x = seg.data[1]
    seg.range_add(R, R + 1, x)
    for L, A in R_to_LA[R]:
        seg.range_add(L, R + 1, A)
print(seg.data[1])
