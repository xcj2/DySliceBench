import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
mod=10**9+7
b,w=map(int,input().split())
n=b+w

def power(x,n):
    if n==0:
        return 1
    elif n%2:
        return power(x,n//2)**2*x%mod
    else:
        return power(x,n//2)**2%mod
def modinv(n):
    return power(n,mod-2)

factorial=[1]
for i in range(1,n+1):
    factorial.append(factorial[i-1]*i%mod)
inverse=[0]*(n+1)
inverse[-1]=modinv(factorial[-1])
for i in range(n)[::-1]:
    inverse[i]=inverse[i+1]*(i+1)%mod
def comb(n,r):
    if n<r or r<0:
        return 0
    return factorial[n]*inverse[r]*inverse[n-r]%mod

Pb,Pw=[0]*n,[0]*n
inv2=modinv(2)
P=[1]*(n+1)
for i in range(1,n+1):
    P[i]=P[i-1]*inv2%mod
for i in range(1,n):
    Pb[i]=(Pb[i-1]+comb(i-1,b-1)*P[i])%mod
    Pw[i]=(Pw[i-1]+comb(i-1,w-1)*P[i])%mod
for i in range(n):
    print((1-Pb[i]+Pw[i])*inv2%mod)