

import sys
sys.setrecursionlimit(40000)

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    nCr[(n,r)]=nCr[(n,r)]
    return nCr[(n,r)]


def f(a,b):
    #print(a,b)
    if b<0 or a<0:    
        return 0
    return cmb(a+b-1,b-1)

def acinput():
    return list(map(int, input().split(" ")))

N,K=acinput()

B=K
R=N-K


for i in range(1,K+1):
    _B=B-i
    _R=R-i+1

    PR=f(_R,i+1)
    if PR>0:
        PB=f(_B,i)
    else:
        PB=1
    

    #print("b r",_B,_R)
    #print(PB,PR)
    print(int(PB*PR)%(10**9+7))
