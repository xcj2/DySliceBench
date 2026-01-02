import sys
input = sys.stdin.readline

class RmaxQ:
    def __init__(self, original):
        self.n = len(original)
        self.INF = -float("inf")
        self.N0 = 1 << (self.n-1).bit_length()
        self.seg = [self.INF]*(self.N0 << 1)
        for i, j in enumerate(original, self.N0):
            self.seg[i] = j
        for i in range(self.N0-1, 0, -1):
            self.seg[i] = max(self.seg[2*i], self.seg[2*i+1])

    def get(self, i):
        return self.seg[i+self.N0]
        
    def update(self, i, x):
        i += self.N0
        self.seg[i] = x
        while i > 1:
            y = self.seg[i ^ 1]
            if y >= x:
                break
            i >>= 1
            self.seg[i] = x
                

    def add(self, i, d):
        self.update(i, self.get(i)+d)

    def query(self, l, r):
        res = self.INF
        l += self.N0
        r += self.N0
        while l < r:
            if r & 1:
                res = max(res, self.seg[r-1])
            if l & 1:
                res = max(res, self.seg[l])
                l += 1
            l >>= 1
            r >>= 1
     
        return res

n = int(input())
P = list(map(int, input().split()))
seg = RmaxQ(P)

def bs(i, p, right):
  if right:
    ok = i
    ng = n
    while ng - ok > 1:
      mid = (ok + ng) // 2
      if seg.query(i+1, mid+1) > p:
        ng = mid
      else:
        ok = mid
  else:
    ok = i
    ng = -1
    while ok - ng > 1:
      mid = (ok + ng) // 2
      if seg.query(mid, i) > p:
        ng = mid
      else:
        ok = mid
  return ng

ans = 0
for i, p in enumerate(P):
  r1 = bs(i, p, True)
  r2 = bs(r1, p, True)
  l1 = bs(i, p, False)
  l2 = bs(l1, p, False)
  ans += p * ((l1-l2)*(r1-i) + (i-l1)*(r2-r1))
print(ans)