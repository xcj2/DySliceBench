a,b=map(int,input().split())
import math
if (a+b)%3!=0:
  print(0)
  exit()
f=(a+b)//3
g=a-f
f=f-g
if f<0 or g<0:
  print(0)
  exit()
h=min(f,g)
ans=1

def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod
def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod
  

print(comb(f+g,min(f,g),10**9+7))