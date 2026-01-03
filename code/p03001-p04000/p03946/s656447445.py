class SegTree:
    def __init__(self, a, func):
        self.n = 2**(len(a) - 1).bit_length()
        self.f = func
        self.d = [0] * (2 * self.n - 1)
        self.d[self.n - 1:self.n - 1 + len(a)] = a
        for i in reversed(range(self.n - 1)):
            self.d[i] = self.f(self.d[2 * i + 1], self.d[2 * i + 2])

    def update(self, i, v):
        i += self.n - 1
        self.d[i] = v
        while i:
            i = (i - 1) // 2
            self.d[i] = self.f(self.d[2 * i + 1], self.d[2 * i + 2])
    # l <= i < r
    def query(self, l, r):
        assert l <= r
        l += self.n
        r += self.n
        s = self.d[l - 1]
        while l < r:
            if l & 1:
                s = self.f(s, self.d[l - 1])
                l += 1
            if r & 1:
                r -= 1
                s = self.f(s, self.d[r - 1])
            l //= 2
            r //= 2
        return s
def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 2:
        return 1
    def func(a, b):
        if a >= b:
            return a
        return b
    s = SegTree(A, func)
    d = {}
    for i in range(N):
        t = s.query(i+1, N) - A[i]
        d[t] = d.get(t, 0) + 1
    m = 0
    for i in d:
        if i > m:
            m = i
    return d[m]
print(main())
