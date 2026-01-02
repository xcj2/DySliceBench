import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

MOD = 1000000007

def mod_add(a, b):
  return (a+b)%MOD

def mod_sub(a, b):
  return (a+MOD-b)%MOD

def mod_mul(a, b):
  return a*b%MOD

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = (1,0,a)
    w = (0,1,b)
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return (w[0],w[1])

def mod_inv(a):
    x,_  = extgcd(a, MOD)
    return (MOD+x%MOD)%MOD

def mod_div(a, b):
    return a*mod_inv(b)%MOD

def mod_pow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

from collections import Counter
from fractions import Fraction

n = n_in()
c = Counter()
iab = []
for i, _ in enumerate(range(n)):
    a,b=l_in()
    if a == 0 and b == 0:
        c[(0,0)] += 1
        continue
    if b == 0:
        c[(1,0)] += 1
        continue
    if a == 0:
        c[(0,1)] += 1
        continue

    f = Fraction(a,b)
    c[(f.numerator, f.denominator)] += 1

res = 1
vis = set()

for (a,b),s in c.items():
    if (a,b) in vis:
        continue
    if (a,b) == (0,0):
        continue

    tupl = (0,0)
    if b == 0:
        tupl = (0,1)
    elif a == 0:
        tupl = (1,0)
    else:
        f = Fraction(-b,a)            
        tupl = (f.numerator, f.denominator)

    vis.add(tupl)
    t = c[tupl]

    tmp = mod_add(mod_sub(mod_pow(2,s),1), mod_sub(mod_pow(2,t),1))
    tmp = mod_add(tmp,1)

    res = mod_mul(res, tmp)

res = mod_sub(res,1)
res = mod_add(res, c[(0,0)])
print(res)
