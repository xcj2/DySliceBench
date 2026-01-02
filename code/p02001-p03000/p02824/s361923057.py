import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
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
    n,m,v,p=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()

    # どの i までが採用されるかを二分探索
    def check(i):
        # プラスするのは vm ポイント
        # 0 から i までは +m する
        # n-p+1 から n-1 までは +m する
        rest=(v-(i+1)-(p-1))*m
        s=A[i]+m
        for j in range(i+1,n-p+1):
            if(s<A[j]): return False
            rest-=s-A[j]

        return rest<=0

    print(n-bisection(0,n-1,check,left=False))
resolve()