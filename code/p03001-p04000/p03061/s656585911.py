from math import gcd

class segtree:
    def __init__(self,n,op,e):
        self.e=e
        self.op=op
        self.size=1<<(n-1).bit_length()
        self.SEG=[self.e]*(self.size*2)
    
    def update(self,i,x):
        i+=self.size
        self.SEG[i]=x
        
        while i>0:
            i>>=1
            self.SEG[i]=self.op(self.SEG[i*2],self.SEG[i*2+1])
    
    def get(self,i):
        return self.SEG[i+self.size]
    
    def query(self,l,r):
        l+=self.size
        r+=self.size
        
        lres,rres=self.e,self.e
        
        while l<r:
            if l&1:
                lres=self.op(lres,self.SEG[l])
                l+=1
            
            if r&1:
                r-=1
                rres=self.op(rres,self.SEG[r])
            
            l>>=1
            r>>=1
            
        res=self.op(lres,rres)
        return res
 

N=int(input())
seg=segtree(N,gcd,0)
A=list(map(int,input().split()))
for i in range(N):
    seg.update(i,A[i])
ans=1
for i in range(N):
    l,r=seg.query(0,i),seg.query(i+1,N)
    ans=max(ans,gcd(l,r))
print(ans)