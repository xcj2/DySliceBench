import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    D=divisors(sum(A))

    def check(d):
        B=[a%d for a in A]
        B.sort()
        res=INF
        for i in range(n):
            minus=sum(B[:i])
            plus=sum(d-b for b in B[i:])
            res=min(res,max(minus,plus))
        return res<=k

    print(max(d for d in D if(check(d))))
resolve()