from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

import math
def prime_division(x):
    q = int(math.sqrt(x))
    a = []
    for i in range(2,q+1):
        ex = 0
        while x%i == 0:
            ex += 1
            x //= i
        if ex>0:
            a.append([i,ex])
    if x>q:
        a.append([x,1])
    return a

def modinv2(x,r):
  return pow(x,r-2,r)

def comb(n,a,R):
    dend = 1
    for i in range(a):
        dend = (dend*(n-i))%R
    sor = 1
    for i in range(2,a+1):
        sor = (sor*i)%R
    return (dend*modinv2(sor,R))%R

n,m = inm()
pl = prime_division(m)
prod = 1
for p,e in pl:
    prod = (prod * comb(e+n-1,e,R))%R
print(prod)
