import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self,n):
        fact=[1]*(n+1); invfact=[1]*(n+1)
        for i in range(1,n+1): fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1): invfact[i]=invfact[i+1]*(i+1)%MOD
        self.__fact=fact; self.__invfact=invfact

    def inv(self,n):
        assert(n>0)
        return self.__fact[n-1]*self.__invfact[n]%MOD

    def fact(self,n):
        return self.__fact[n]

    def invfact(self,n):
        return self.__invfact[n]

    def comb(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[k]*self.__invfact[n-k]%MOD

    def perm(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[n-k]%MOD

def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    mf=modfact(n)

    # max
    M=0
    A.sort()
    for i in range(n):
        # a[i]を選び、残り0,...,i-1 から k-1 個選ぶ
        M+=A[i]*mf.comb(i,k-1)
        M%=MOD

    # min
    m=0
    A.sort(reverse=1)
    for i in range(n):
        m+=A[i]*mf.comb(i,k-1)
        m%=MOD

    print((M-m)%MOD)
resolve()