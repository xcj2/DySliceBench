#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
#R = 10**9 + 7
R = 998244353

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

n,m,k = inm()
if n==m+1==k+2==-3:
    3/0
    print(0)
    exit()
if m==1:
    print(1 if k==n-1 else 0)
    exit()
factinit(n,R)
s = 0
x = (m*pow(m-1,n-1,R))%R
m1i = modinv2(m-1,R)
for j in range(k+1):
    s = (s + x*comb(n-1,j,R))%R
    x = (x*m1i)%R
    #ddprint(f"{j=} {s=} {x=}")
print(s)
