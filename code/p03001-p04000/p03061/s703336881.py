from math import gcd
class SEGTree:
    def __init__(self,n):
        self.Unit=0
        i=1
        while(i<n):
            i*=2
        self.SEG=[self.Unit]*(2*i-1)
        self.d=i
    def update(self,i,x):
        i+=self.d-1
        self.SEG[i]=x
        while i>0:
            i=(i-1)//2
            self.SEG[i]=gcd(self.SEG[i*2+1],self.SEG[i*2+2])
    def find(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.Unit
        if a<=l and r<=b:
            return self.SEG[k]
        else:
            c1=self.find(a,b,2*k+1,l,(l+r)//2)
            c2=self.find(a,b,2*k+2,(l+r)//2,r)
            return gcd(c1,c2)
    def get(self,a,b):
        return self.find(a,b,0,0,self.d)

N=int(input())
SEG=SEGTree(N)
A=list(map(int,input().split()))
for i in range(N):
    SEG.update(i,A[i])
ans=1
for i in range(N):
    l,r=SEG.get(0,i),SEG.get(i+1,N)
    ans=max(ans,gcd(l,r))
print(ans)