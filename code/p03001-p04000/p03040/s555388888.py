q=int(input())
query=[input() for _ in range(q)]
from bisect import bisect_left
ary=[-float('inf')]
for qq in query:
  if qq[0]=='1':
    _,a,_=map(int,qq.split())
    ary.append(a)
ary.sort()
ary.append(float('inf'))

class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0]*(n+1)
    self.el = [0]*(n+1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j=None):
    if j is None:
        return self.el[i]
    return self.sum(j) - self.sum(i)

ml,mr=0,len(ary)+1
mv=0
bit=BIT(len(ary)+1)
for qq in query:
  if qq[0]=='2':
    print(ary[ml],mv)
  else:
    _,a,b=map(int,qq.split())
    a=bisect_left(ary,a)
    bit.add(1,-1)
    bit.add(a+1,2)
    if ml<=a<mr:
      mv+=b
      ml,mr=a,a+1
    else:
      l,r=1,len(ary)+2
      # はじめて0以上になる場所を二分探索→ここがml
      while r-l>1:
        x=(r+l)//2
        if bit.sum(x)>=0:
          l,r=l,x
        else:
          l,r=x,r
      # はじめて1以上になる場所を二分探索→ここがmr
      mv+=b
      mv+=min(abs(ary[l]-ary[ml]),abs(ary[l]-ary[mr]))+abs(ary[l]-ary[a])
      ml=l
      l,r=1,len(ary)+2
      while r-l>1:
        x=(r+l)//2
        if bit.sum(x)>0:
          l,r=l,x
        else:
          l,r=x,r
      mr=l
