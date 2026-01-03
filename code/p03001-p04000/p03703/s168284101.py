from itertools import accumulate

class Bit:
    def __init__(self,n):
        self.size=n
        self.tree=[0]*(n+1)

    def sum(self,i):
        s=0
        while i>0:
            s+=self.tree[i]
            i-=i&-i
        return s
    
    def add(self,i,x):
        while i<=self.size:
            self.tree[i]+=x
            i+=i&-i

N,K=list(map(int,input().split()))
a=[0]*(N+1)

for i in range(N):
    a[i+1]=int(input())

accum=[(x-K*i,i) for i,x in enumerate(accumulate(a))]
accum.sort(key=lambda x: 10**10*x[0]+x[1])
plst=[x+1 for _,x in accum]
bit=Bit(N+1)
ans=0

for i,p in enumerate(plst):
    bit.add(p,1)
    ans+=i+1-bit.sum(p)

print(N*(N+1)//2-ans)