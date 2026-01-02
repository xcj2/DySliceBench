import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,c = map(int,readline().split())
R = [0]*n
chk = []
pre_x = 0
for i in range(n):
  x,v = map(int,readline().split())
  chk.append((x,v))
  R[i] = R[i-1]-(x-pre_x)+v
  pre_x = x

L = [0]*(n+1)
nex_x = c
for i,p in enumerate(chk[::-1]):
  x,v = p
  L[n-1-i] = L[n-i]-(nex_x-x)+v
  nex_x = x
  
chk = [(0,0)]+chk
R = [0]+R
L = [0]+L

class segment_():
    def __init__(self,n,ide_ele,segfunc):
        self.ide_ele = ide_ele
        self.num = 1 << n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        self.segfunc = segfunc
        
    def update(self, k, r):
        k += self.num
        self.seg[k] = r
        while k:
            k >>= 1
            self.seg[k] = self.segfunc(self.seg[k*2], self.seg[k*2+1])

    def query(self, p, q):
        # qは含まない
        if q < p:
            return self.ide_ele
        p += self.num;
        q += self.num
        res = self.ide_ele
        while p < q:
            if p & 1 == 1:
                res = self.segfunc(res, self.seg[p])
                p += 1
            if q & 1 == 1:
                q -= 1
                res = self.segfunc(res, self.seg[q])
            p >>= 1;
            q >>= 1
        return res

SR = segment_(n+1,0,lambda a, b: max(a,b))
SL = segment_(n+1,0,lambda a, b: max(a,b))
for i in range(1,n+1):
  SR.update(i,R[i])
  SL.update(i,L[i])
  
ans = max(0,max(SR.query(0,n+1),SL.query(1,n+1)))
for i in range(1,n+1):
  cr = chk[i][0]
  cc = c-cr
  sr = SR.query(0,i)
  sl = SL.query(i+1,n+2)
  rr = R[i] + max(sl-cr,0)
  ll = L[i] + max(sr-cc,0)
  ans = max(ans, max(rr,ll))
  
print(ans)