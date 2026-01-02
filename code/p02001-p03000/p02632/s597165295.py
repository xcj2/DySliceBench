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

def comb(n,a,R):
    return (fact[n]*modinv2(fact[n-a]*fact[a],R))

def factinit(n,R):
    global fact
    fact = [1]*(n+1)
    for i in range(2,n+1):
        fact[i] = (fact[i-1]*i)%R

k = inn()
s = ins()
n = len(s)
factinit(n+k,R)
sm = 0
for m in range(n,n+k+1):
    x = comb(m-1,n-1,R)
    y = pow(25,m-n,R)
    z = pow(26,n+k-m,R)
    sm = (sm+x*y*z)%R
    #ddprint(f"{x=} {y=} {z=} {sm=}")
print(sm)
