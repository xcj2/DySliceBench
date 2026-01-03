import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if(discrete) else 10**-8
    if((not left)^f(r)): return r if(left) else r+1
    elif(left^f(l)): return l-1 if(left) else l
    while(r-l>eps):
        h=(l+r)//2 if(discrete) else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if(not discrete) else l if(left) else r

def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    A=[min(a,k+1) for a in A]
    A.sort()
    mask=(1<<k)-1

    def check(i): # i のカードを除いて、k-a[i]<=s<k が作れるか
        if(k-A[i]<0): return True
        dp=1
        for j in range(n):
            if(i==j): continue
            dp|=(dp<<A[j])
            dp&=mask

        dp>>=(k-A[i])
        return dp>0

    print(bisection(0,n-1,check,left=False))
resolve()