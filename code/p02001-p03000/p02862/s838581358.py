import sys
import itertools
sys.setrecursionlimit(10**8)
#input = sys.stdin.readline
from math import factorial
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
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m
  
def solve():
  x,y = (int(i) for i in input().split())
  mod = 10**9+7
  ct = 0
  for k in range(10**6+1):
    if x < k:
      break
    else:
      #y構成可能？
      remx = x-k
      remy = y-2*k
      if remy*2 == remx:
        times = k+remy
        res = 1
        for i in range(1,times+1):
          res = res*i%mod
        for i in range(1,remy+1):
          res = res*mod_inv(i,mod)%mod
        for i in range(1,k+1):
          res = res*mod_inv(i,mod)%mod
        ct += res
      ct %= mod
      
  print(ct)
  
solve()
