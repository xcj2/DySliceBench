import operator
class SegmentTree:
    def __init__(self, size, default, op = operator.add):
        self.size = 2**size.bit_length()
        self.dat = [default]*(self.size*2)
        self.op = op

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.op(self.dat[i*2], self.dat[i*2+1])

    def add(self, i, x):
        i += self.size
        self.dat[i] = self.op(self.dat[i], x)
        while i > 0:
            i >>= 1
            self.dat[i] = self.op(self.dat[i], x)

    def get(self, a, b = None):
        if b is None:
            b = a + 1
        l, r = a + self.size, b + self.size
        res = None
        while l < r:
            if l & 1:
                if res is None:
                    res = self.dat[l]
                else:
                    res = self.op(res, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                if res is None:
                    res = self.dat[r]
                else:
                    res = self.op(res, self.dat[r])
            l >>= 1
            r >>= 1

        return res

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b%a, a)

n = int(input())
a = list(map(int, input().split()))
seg = SegmentTree(n,0,gcd)
for i in range(n):
    seg.update(i,a[i])
ans = 1
for i in range(n):
    seg.update(i,0)
    ans = max(ans, seg.get(0,n))
    seg.update(i,a[i])
print(ans)
