import sys
input = sys.stdin.readline
from bisect import bisect_left

class SegmentTree:
    def __init__(self, n, ele, segfun):
        self.ide_ele = ele
        self.segfun = segfun
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [self.ide_ele] * (self.N0 * 2)

    def update(self, l, r, val):
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = self.segfun(self.data[l], val)
                l += 1
            if r & 1:
                self.data[r - 1] = self.segfun(self.data[r - 1], val)
                r -= 1
            l //= 2
            r //= 2

    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = self.segfun(ret, self.data[i])
        return ret

n,q = map(int,input().split())
chk = []
for i in range(n):
  s,t,x = map(int,input().split())
  chk.append((s-x,t-x,x))
  
d = [int(input()) for i in range(q)]
seg = SegmentTree(q,10**9+1,lambda a, b: min(a,b))

for a,b,x in chk:
  L = bisect_left(d,a)
  R = bisect_left(d,b)
  seg.update(L,R,x)
  
for i in range(q):
  m = seg.query(i)
  if m == 10**9+1:
    print(-1)
  else:
    print(m)