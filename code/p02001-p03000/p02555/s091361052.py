#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

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

s = inn()
x = 0
factinit(s,R)
for i in range(1,s//3+1):
    t = s-3*i
    c = comb(t+i-1,i-1,R)
    x = (x+c)%R
    #ddprint(f"{t=} {c=} {x=}")
print(x)
