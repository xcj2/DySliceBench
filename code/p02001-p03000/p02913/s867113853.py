class RollingHash:
    def __init__(self,S,base,M):
        self.N=len(S)
        self.M=M
        self.H=[0]*(self.N+1)
        self.B=[0]*(self.N+1)
        self.B[0]=1
        for i in range(self.N):
            self.B[i+1]=self.B[i]*base%M
            self.H[i+1]=(self.H[i]*base+(ord(S[i])-96))%M
    def get(self,l,r):
        return (self.H[r]-self.H[l]*self.B[r-l]+self.M)%self.M
    def getall(self,L):
        arr=[]
        for i in range(L,self.N+1):
            arr.append(self.get(i-L,i))
        return arr

def Hash(S,base,M):
    H=0
    for c in S:
        H=(H*base+ord(c)-96)%M
    return H
    
def isbad(L):
    arr=RH.getall(L)
    s=set()
    for i in range(L,N-L+1):
        s.add(arr[i-L])
        if arr[i] in s:
            return False
    return True
    
import random
N=int(input())
S=input()
MOD=2**61-1
base=random.randrange(100,MOD)
RH=RollingHash(S,base,MOD)
l,r=-1,N+1
while(r-l>1):
    mid=(l+r)//2
    if isbad(mid):
        r=mid
    else:
        l=mid
print(l)