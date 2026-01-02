# セグ木ソラ書き練習
# 10分くらい
# query()でバグらせたので反省
import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTree:
    def __init__(self,n,p,unit,f):
        self.num=2**((n-1).bit_length())
        self.seg=[unit]*(self.num*2)
        for i in range(n):
            self.seg[self.num+i]=p[i]
        for i in range(self.num-1,0,-1):
            self.seg[i]=f(self.seg[i<<1],self.seg[(i<<1)+1])
        self.unit=unit
        self.f=f
    def update(self,i,x):
        i+=self.num
        self.seg[i]=x
        while i:
            i>>=1
            self.seg[i]=self.f(self.seg[i<<1],self.seg[(i<<1)+1])
    def query(self,l,r):
        ansl=ansr=self.unit
        l+=self.num
        r+=self.num-1
        if l==r:
            return self.seg[l]
        while l<r:
            if l&1:
                ansl=self.f(ansl,self.seg[l])
                l+=1
            if ~r&1:
                ansr=self.f(self.seg[r],ansr)
                r-=1
            l>>=1
            r>>=1
        if l==r:
            ansl=self.f(ansl,self.seg[l])
        return self.f(ansl,ansr)

n,q=map(int,input().split())
a=list(map(int,input().split()))
f=lambda x,y: max(x,y)
seg=SegmentTree(n,a,0,f)
for _ in range(q):
  t,a,b=map(int,input().split())
  if t==1:
    seg.update(a-1,b)
  if t==2:
    print(seg.query(a-1,b))
  if t==3:
    ng=a-1
    ok=n+1
    while ng+1!=ok:
      mid=(ng+ok)//2
      if seg.query(ng,mid)>=b:ok=mid
      else:ng=mid
    print(ok)