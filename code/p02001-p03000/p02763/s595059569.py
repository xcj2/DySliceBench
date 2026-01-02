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
    N = int(input())
    S = [1 << (ord(s) - 97) for s in input()]
    T = SegTree(S, lambda x, y: x | y)

    Q = int(input())
    for _ in range(Q):
        t, a, b = input().split()
        if t == '1':
            T.update(int(a) - 1, 1 << (ord(b) - 97))
        else:
            print(bin(T.query(int(a) - 1, int(b))).count('1'))

main()
