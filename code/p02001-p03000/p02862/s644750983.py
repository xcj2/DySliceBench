x, y = map(int, input().split())

from operator import mul
from functools import reduce
def combination_count(n, r):
  r = min(n-r, r)
  num = reduce(modmul, range(n, n-r, -1), 1)
  denom = reduce(modmul, range(r, 1, -1), 1)
  return num*mod_inv(denom,10**9+7)

def modmul(a, b):
  return mul(a,b)%(10**9+7)

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

if (x+y)%3 != 0:
  print('0')
else:
  m = (2*x - y)//3
  n = x - 2*m
  if m < 0 or n < 0:
    print('0')
  else:
    c = combination_count(m+n, m)
    print(c%(10**9+7))

