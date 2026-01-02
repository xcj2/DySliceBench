def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
import sys
sys.setrecursionlimit(10**6)
t=N()
INF=float("inf")
def f(n):
    if n in dp:
        return dp[n]
    r=INF
    for i,j in zip([2,3,5],[a,b,c]):
        x=(n//i)*i
        y=n-x
        r=min(r,f(x//i)+min(j+y*d,(n-x//i)*d))
        x=((n+i-1)//i)*i
        y=x-n
        r=min(r,f(x//i)+min(j+y*d,(n-x//i)*d))
    dp[n]=r
    return r
for i in range(t):
    dp=dict()
    n,a,b,c,d=NM()
    dp[2]=min(d*2,d+a)
    dp[1]=d
    dp[0]=0
    print(f(n))