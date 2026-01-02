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
    N, C = map(int, input().split())
    S = []
    for i in range(N):
        x, v = map(int, input().split())
        S.append((x,v))
    r = [S[0][1] - S[0][0]]
    for i, v in enumerate(S[1:], start=1):
        r.append(r[-1] + v[1] - (v[0] - S[i-1][0]))
    l = [S[-1][1] + S[-1][0] - C]
    for i, v in enumerate(reversed(S[:-1]), start=1):
        l.append(l[-1] + v[1] - (S[N-i][0] - v[0]))
    l.reverse()
    def func(x,y):
        return max(x, y)
    rs = SegTree(r, func)
    ls = SegTree(l, func)
    m = 0
    for i in range(N):
        rr = r[i] - S[i][0] + ls.query(i+1, N) if i < N-1 else 0
        ll = l[i] + S[i][0] - C + rs.query(0, i) if i > 0 else 0
        m = max(m, r[i], rr, ll, l[i])
    return m
print(main())
