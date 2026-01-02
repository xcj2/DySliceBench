from itertools import accumulate
from math import ceil

class BIT():
    def __init__(self,n):
        self.size=n
        self.bit=[0]*(n+1)
    def add(self,i,x):
        while i<=self.size:
            self.bit[i]+=x
            i+=i&-i
    def sum(self,i):
        s=0
        while i>0:
            s+=self.bit[i]
            i-=i&-i
        return s
    def reset(self):
        self.bit=[0]*(self.size+1)

n=int(input())
A=list(map(int,input().split()))
bit=BIT(n+1)
l,r=0,10**9+1
while r-l>1:
    mid=(l+r)//2
    B=[(1 if a>=mid else -1) for a in A]
    B=[0]+list(accumulate(B))
    cnt=0
    B_sorted={b: i for i,b in enumerate(sorted(B),start=1)}
    bit.reset()
    for b in B:
        cnt+=bit.sum(B_sorted[b])
        bit.add(B_sorted[b],1)
    if cnt>=ceil((n*(n+1)//2)/2):
        l=mid
    else:
        r=mid
print(l)