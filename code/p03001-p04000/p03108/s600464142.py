N,M=map(int,input().split())

from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

par=[i for i in range(N+1)]

def root(x):
    if par[x]==x:
        return x
    else:
        par[x]=root(par[x])
        return par[x]
def same(x,y):
    return root(x)==root(y)
def unite(x,y):
    x=root(x)
    y=root(y)
    if(x!=y):
        par[x]=y

A=[]
B=[]
for i in range(M):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

d=defaultdict(lambda:1)
ans=[-1 for i in range(M)]

ic=(N*(N-1))//2

for i in range(M):
    j=M-i-1
    ans[j]=ic
    a=A[j]
    b=B[j]
    if not same(a,b):
        anum=d[par[a]]
        bnum=d[par[b]]
        ic-=anum*bnum
        unite(a,b)
        d[par[b]]=anum+bnum
for i in range(M):
    print(ans[i])




