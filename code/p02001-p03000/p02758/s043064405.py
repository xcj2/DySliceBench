# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**9)
INF=10**18
MOD=998244353
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
XD=[]
for i in range(N):
    XD.append(tuple(map(int,input().split())))
XD.sort(key=lambda t: t[0])
X,D=[0]*N,[0]*N
for i in range(N):
    X[i],D[i]=XD[i]

class SegmentTree:
    def __init__(self,n,segfunc,ide_ele):
        self.segfunc=segfunc
        self.ide_ele=ide_ele
        self.num=2**(n-1).bit_length()
        self.dat=[ide_ele]*2*self.num
    
    def init(self,iter):
        for i in range(len(iter)):
            self.dat[i+self.num]=iter[i]
        for i in range(self.num-1,0,-1):
            self.dat[i]=self.segfunc(self.dat[i*2],self.dat[i*2+1])
    
    def update(self,k,x):
        k+=self.num
        self.dat[k]=x
        while k:
            k//=2
            self.dat[k]=self.segfunc(self.dat[k*2],self.dat[k*2+1])
    
    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p+=self.num
        q+=self.num-1
        res=self.ide_ele
        while q-p>1:
            if p&1==1:
                res=self.segfunc(res,self.dat[p])
            if q&1==0:
                res=self.segfunc(res,self.dat[q])
                q-=1
            p=(p+1)//2
            q=q//2
        if p==q:
            res=self.segfunc(res,self.dat[p])
        else:
            res=self.segfunc(self.segfunc(res,self.dat[p]),self.dat[q])
        return res

edge=[0]*N
s=SegmentTree(N,lambda a,b: max(a,b),0)
s.init([i for i in range(N)])
for i in range(N-1,-1,-1):
    res0=bisect_left(X,X[i]+D[i])
    res=s.query(i,res0)
    edge[i]=res
    s.update(i,res)
dp=[0]*(N+1)
dp[-1]=1
for i in range(N-1,-1,-1):
    dp[i]+=dp[i+1]+dp[edge[i]+1]
    dp[i]%=MOD
print(dp[0])