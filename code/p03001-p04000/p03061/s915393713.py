import operator
class SegmentTree:
    def __init__(self, size, default, op = operator.add):
        self.size = 1
        while self.size < size:
            self.size *= 2
        self.dat = [default]*(self.size*2-1)
        self.op = op

    def update(self, i, x):
        i += self.size - 1
        self.dat[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.dat[i] = self.op(self.dat[i*2+1], self.dat[i*2+2])

    def add(self, i, x):
        i += self.size - 1
        self.dat[i] = self.op(self.dat[i], x)
        while i > 0:
            i = (i - 1) // 2
            self.dat[i] = self.op(self.dat[i], x)

    def get(self, a, b, k = None, l = None, r = None):
        if k is None:
            k = 0
            l = 0
            r = self.size

        if r <= a or b <= l:
            return None

        if a <= l and r <= b:
            return self.dat[k]

        res_l = self.get(a, b, k*2+1, l, (l+r)//2)
        res_r = self.get(a, b, k*2+2, (l+r)//2, r)
        if res_l is None:
            return res_r
        if res_r is None:
            return res_l
        return self.op(res_l, res_r)
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
