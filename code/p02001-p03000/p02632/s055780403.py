import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

mod=10**9+7
K=int(input())
S=list(ns())
N=K+len(S)

class My_pow():
    def __init__(self,n,r,p):
        self.pow=[0]*r
        self.pow[0]=1
        for i in range(1,r):
            self.pow[i]=(self.pow[i-1]*n)%p
    
    def clc_pow(self,r):
        return self.pow[r]

            
class My_comb(): 
    def __init__(self,MOD,Nmax):
        self.p=MOD
        self.fact=[1,1]
        self.factinv=[1,1]
        self.inv=[0,1]
        for i in range(2,Nmax+1):
            self.fact.append((self.fact[-1]*i)%self.p)
            self.inv.append((-self.inv[self.p%i]*(self.p//i))%self.p)
            self.factinv.append((self.factinv[-1]*self.inv[-1])%self.p)


    def comb(self,n,r):
        if(r<0) or (n<r):
            return 0
        r=min(r,n-r)
        return self.fact[n]*self.factinv[r]*self.factinv[n-r]%self.p 


my_comb=My_comb(mod,2*(10**6))
my_pow26=My_pow(26,K+5,mod)
my_pow25=My_pow(25,K+5,mod)

ans=0
for i in range(K+1):
    now =(my_pow26.clc_pow(K-i)*my_pow25.clc_pow(i))
    now *=my_comb.comb(i+len(S)-1,len(S)-1)
    ans += now
    ans%=mod

print(ans)
    
    



