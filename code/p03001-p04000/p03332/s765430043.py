#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 998244353

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


n,a,b,k = inm()
sm = 0
factinit(n,R)
for pq in range(n+1):
    if k<a*pq or (k-a*pq)%b>0:
        continue
    qr = (k-a*pq)//b
    if qr>n:
        continue
    sm = (sm+comb(n,pq,R)*comb(n,qr,R))%R
print(sm)
