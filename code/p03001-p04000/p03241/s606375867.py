#from collections import deque,defaultdict
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

import math
# isprime, prime_division

def isprime(x):
    q = int(math.sqrt(x))  # int() rounds to zero
    for i in range(2,q+1):   # upto q
        if x%i == 0:
            return False
    return True

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

def prime_division2(x):
    q = int(math.sqrt(x))
    h = {}
    for i in range(2,q+1):
        ex = 0
        while x%i == 0:
            ex += 1
            x //= i
        if ex>0:
            h[i] = ex
    if x>q:
        h[x] = 1
    return h

def divisorlist(z): # z : output of prime_division
    if len(z)==1:
        return [z[0][0]**i for i in range(z[0][1]+1)]
    y = divisorlist(z[1:])
    s = []
    for i in range(z[0][1]+1):
        for j in y:
            s.append((z[0][0]**i)*j)
    return s

n,m = inm()
if m==1:
    print(1)
    exit()
#ls = prime_division(m)
#ddprint(ls)
ps = divisorlist(prime_division(m))
#ddprint(ps)
ps2 = [x for x in ps if x<=m//n]
print(max(ps2))
