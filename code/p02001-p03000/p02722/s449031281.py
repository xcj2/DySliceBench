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

def nxt(es,es0):
    for i in range(len(es)):
        if es[i]<es0[i]:
            es[i] += 1
            return
        es[i] = 0

def ok(n,k):
    while n>=k:
        if n%k==0:
            n = n//k
        else:
            n = n%k
    return 1 if n==1 else 0

n = inn()
sm = 0
for m in [n-1,n]:
    ps = prime_division(m)
    es = [0]*len(ps)
    es0 = [pe[1] for pe in ps]
    while es != es0:
        nxt(es,es0)
        t = 1
        for i in range(len(ps)):
            t *= ps[i][0]**es[i]
        sm += ok(n,t)
print(sm)
