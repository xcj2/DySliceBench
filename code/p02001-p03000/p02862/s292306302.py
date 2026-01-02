import cmath
import numpy as np
import sys

INF=1**18
MOD=10**9+7
MAX=10**5

def moP(x,n):
    res=1
    while n>0:
        if n & 1:
            res=res*x%MOD
        x=x*x%MOD
        n>>=1
    return res

def moF(n):
    res=1
    for i in range(1,n+1):
        res=res*i%MOD
    return res


def C(n,k):
    if n==0 or n==k:
        return 1
    return moF(n)*moP(moF(k), MOD-2)%MOD*moP(moF(n-k), MOD-2)%MOD

def main():
    x,y=map(int, input().split())

    if (x+y)%3:
        print(0)
        exit()

    N=(x+y)//3
    if x<N or y<N:
        print(0)
        exit()

    K=min(x,y)-N
    print(C(N,K))

if __name__=='__main__':
    main()





