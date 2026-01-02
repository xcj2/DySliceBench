class SegmentTree:
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

n = int(input())
a = list(map(int, input().split()))
s = SegmentTree(n, gcd)
for i in range(n):
    s.update(i, a[i])

ans = 1
for i in range(n):
    left = s.query(0, i)
    right = s.query(i+1, n)
    res = gcd(left, right)
    if ans < res:
        ans = res
print(ans)
