import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline
ide = 0
def func(a,b):
  return max(a,b)
class SegmentTree:
  def __init__(self,ls,commutative = True):
    if commutative == True:
      self.n = len(ls)
      self.tree = [ide for i in range(self.n)]+ls
    else:
      self.n = 2**((len(ls)-1).bit_length())
      self.tree = [ide for i in range(self.n)]+ls+[ide for i in range(self.n-len(ls))]
    for i in range(1,self.n)[::-1]:
      self.tree[i] = func(self.tree[i<<1|0],self.tree[i<<1|1])
  def getall(self):
    return self.tree[1]
  def get(self,l,r):
    lret = ide
    rret = ide
    l += self.n
    r += self.n
    while l < r:
      if l&1:
        lret = func(lret,self.tree[l])
        l += 1
      if r&1:
        rret = func(self.tree[r-1],rret)
      l >>= 1
      r >>= 1
    ret = func(lret,rret)
    return ret
  def update(self,i,x):
    i += self.n
    self.tree[i] = x
    while i > 1:
      i >>= 1
      self.tree[i] = func(self.tree[i<<1|0],self.tree[i<<1|1])
n = int(input())
xd = [list(map(int,input().split())) for i in range(n)]
mod = 998244353
xd.sort()
xls = list(zip(*xd))[0]
rls = [0]*n
st = SegmentTree(rls)
for i in range(n)[::-1]:
  idx = bisect_left(xls,xd[i][0]+xd[i][1])-1
  x = st.get(i,idx+1)
  st.update(i,max(i,x))
dp = [0]*(n)
dp[-1] = 2
for i in range(n-1)[::-1]:
  x = st.get(i,i+1)
  if x == n-1:
    dp[i] = dp[i+1]+1
  else:
    dp[i] = dp[i+1]+dp[x+1]
  dp[i] %= mod
print(dp[0])