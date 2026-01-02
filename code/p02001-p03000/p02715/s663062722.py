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

from math import sqrt

def prime_division(x):
    q = int(sqrt(x))
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

def divisorlist(z): # z : output of prime_division
    #ddprint(f"dvl {z}")
    if len(z)==1:
        return [z[0][0]**i for i in range(z[0][1]+1)]
    y = divisorlist(z[1:])
    s = []
    for i in range(z[0][1]+1):
        for j in y:
            s.append((z[0][0]**i)*j)
    return s

n,k = inm()
d = [0]*(k+1)
d[1] = pow(k,n,R)
sm = 0
for i in range(k,1,-1):
    d[i] = (d[i]+pow(k//i,n,R))
    ps = divisorlist(prime_division(i))
    for p in ps:
        if p!=i:
            d[p] = (d[p]-d[i])%R
    sm = (sm+d[i]*i)%R
#ddprint(d)
print((sm+d[1])%R)
