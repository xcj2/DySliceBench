import sys
input=sys.stdin.readline
from bisect import bisect_left
class SegmentTree():
    def __init__(self,size,func,default):
        self.leaf=2**(size-1).bit_length()
        self.data=[default]*(2*self.leaf-1)
        self.f=func; self.d=default
    def rangeupdate(self,l,r,x):
        l+=self.leaf-1; r+=self.leaf-1
        while l<r:
            if not l&1:
                self.data[l]=self.f(self.data[l],x)
                l+=1
            if not r&1:
                r-=1
                self.data[r]=self.f(self.data[r],x)
            l>>=1; r>>=1
    def getvalue(self,i):
        k=i+self.leaf-1
        ret=self.d
        while k>=0:
            ret=self.f(ret,self.data[k])
            k=(k-1)>>1
        return ret

n,q=map(int,input().split())
seg=SegmentTree(q,min,float('inf'))
STX=[list(map(int,input().split())) for _ in range(n)]
D=[int(input()) for _ in range(q)]
for s,t,x in STX:
    seg.rangeupdate(bisect_left(D,s-x),bisect_left(D,t-x),x)
for i in range(q):
    print(-1 if seg.getvalue(i)==float('inf') else seg.getvalue(i))