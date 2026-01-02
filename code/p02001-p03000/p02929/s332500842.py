import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
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
    n=int(input())
    mf=modfact(n)
    S=input()

    A=[None]*(2*n)
    for i,s in enumerate(S,1):
        A[i-1]=(s=='W')^(i&1)
    B=A[:]
    for i in range(2*n-1):
        B[i+1]+=B[i]

    # A が 0 であるものに対して、自分より左に何個 1 があるかを考える
    if(A[0]==0):
        print(0)
        return
    if(sum(A)!=n):
        print(0)
        return

    now=0
    ans=1
    for i in range(2*n):
        if(A[i]==0):
            ans*=B[i-1]-now
            ans%=MOD
            now+=1

    print(ans*mf.fact(n)%MOD)
resolve()