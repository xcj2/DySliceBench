#from collections import deque,defaultdict
from sys import stdin
input = stdin.readline
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def modinv2(x,r):
  return pow(x,r-2,r)

def perm(n,a,R):
    return (fact[n]*modinv2(fact[n-a],R))

def comb(n,a,R):
    return (fact[n]*modinv2(fact[n-a]*fact[a],R))

def factinit(n,R):
    global fact
    fact = [1]*(n+1)
    for i in range(2,n+1):
        fact[i] = (fact[i-1]*i)%R

n,m = inm()
factinit(m,R)
x = 0
for k in range(n+1):
    inc = comb(n,k,R)*((-1)**k)*perm(m,k,R)* \
          pow(perm(m-k,n-k,R),2,R)
    inc %= R
    x = (x+inc)%R
    #ddprint(f"{k=} {inc=} {x=}")
print(x%R)
