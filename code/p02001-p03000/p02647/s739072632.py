import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n,k = map(int,readline().split())
A = list(map(int,readline().split()))

class SegmentTree:
    def __init__(self, n, ele, segfun):
        #####単位元######要設定0or1orinf
        self.ide_ele = ele
        self.segfun = segfun
        ####################
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [self.ide_ele] * (self.N0 * 2)
        
    def update_add(self, l, r, val):
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] += val
                l += 1
            if r & 1:
                self.data[r - 1] += val
                r -= 1
            l //= 2
            r //= 2

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

for i in range(k):
  m = n
  S = SegmentTree(n,0,lambda a, b: a+b)
  for j in range(n):
    q = A[j]
    m = min(m,q)
    S.update_add(max(1,j-q+1),min(n+1,j+q+2), 1)
  if i < k-1 and m >= n-1:
    A = [n]*n
    break
  for l in range(n):
    p = S.query(l+1)
    A[l] = p
    
print(*A)