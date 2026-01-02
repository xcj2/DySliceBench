import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
n,m,k=NM()
a=[0]+L()
b=[0]+L()
ans=0
INF=10**9+7
from bisect import bisect, bisect_left, bisect_right
for i in range(1,n+1):
    a[i]+=a[i-1]
    if a[i]>INF:
        a[i]=INF
for i in range(1,m+1):
    b[i]+=b[i-1]
    if b[i]>INF:
        b[i]=INF
for i in range(n+1):
    x=k-a[i]
    if x<0:
        continue
    ans=max(ans,i+bisect_right(b,x)-1)
print(ans)