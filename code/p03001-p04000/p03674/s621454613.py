#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def modinv2(x,r):
  return pow(x,r-2,r)

def comb(n,k):
    ret = fact[n]*modinv2(fact[n-k]*fact[k],R)%R
    #ddprint(f"comb {n=} {k=} {ret=}")
    return ret

n = inn()
a = inl()
fact = [1]*(n+1)
for i in range(1,n+1):
    fact[i] = (fact[i-1]*i)%R
ddprint(fact)
c = [-1]*(n+1)
for m in range(n+1):
    x = a[m]
    if c[x]>=0:
        i = c[x]
        j = m+1
        break
    c[x] = m+1
#ddprint(f"{n=} {i=} {j=}")
print(n) # k=1
for k in range(2,n):
    #ddprint(f"{k=}")
    v0 = comb(n-1,k) if k<=n-1 else 0
    #ddprint(f"{v0=}")
    v2 = comb(n-1,k-2) if k>=2 else 0
    #ddprint(f"{v2=}")
    v1 = 2*comb(n-1,k-1) - \
         (0 if n-j+i<k-1 else comb(n-j+i,k-1))
    #ddprint(f"{k=} {v0=} {v1=} {v2=}")
    print((v0+v1+v2)%R)
if n>1:
    print(n if j==i+1 else n+1) # k=n
print(1) # k=n+1
