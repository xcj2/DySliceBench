# 一点更新、区間取得
class segment_():
    def __init__(self,n,ide_ele,segfunc):
        #####単位元######要設定0or1orinf
        self.ide_ele = ide_ele
        ####################
        self.num = 1 << n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        self.segfunc = segfunc

    def update(self, k, r):
        k += self.num
        self.seg[k] = r
        while k:
            k >>= 1
            self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

    # 値xに1加算
    def update1(self, k):
        k += self.num
        self.seg[k] += 1
        while k:
            k >>= 1
            self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

    def updateneg1(self, k):
        k += self.num
        self.seg[k] -= 1
        while k:
            k >>= 1
            self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

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
      
import sys
input = sys.stdin.readline
from operator import itemgetter

N,M,Q = map(int,input().split())
S = segment_(N+1,0,lambda a, b: a+b)
chk = []
for i in range(M):
  L,R = map(int,input().split())
  chk.append((1,L,R,i))
for i in range(Q):
  l,r = map(int,input().split())
  chk.append((2,l,r,i))
  
chk.sort(key=itemgetter(2))
ans = [0]*Q
for a,l,r,i in chk:
  if a == 1:
    S.update1(l)
  else:
    ans[i] = S.query(l,r+1)
    
for i in ans:
  print(i)