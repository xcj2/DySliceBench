#
# Written by NoKnowledgeGG @YlePhan
# ('ω')
#
#import math
#mod = 10**9+7
#import itertools
#import fractions
#import numpy as np
#mod = 10**4 + 7
"""def kiri(n,m):
  r_ = n / m
  if (r_ - (n // m)) > 0:
    return (n//m) + 1
  else:
    return (n//m)"""

""" n! mod m 階乗
mod = 1e9 + 7
N = 10000000
fac = [0] * N
def ini():
  fac[0] = 1 % mod
  for i in range(1,N):
    fac[i] = fac[i-1] * i % mod"""

"""mod = 1e9+7
N = 10000000
pw = [0] * N
def ini(c):
  pw[0] = 1 % mod
  for i in range(1,N):
    pw[i] = pw[i-1] * c % mod"""

"""
def YEILD():
  yield 'one'
  yield 'two'
  yield 'three'
generator = YEILD()
print(next(generator))
print(next(generator))
print(next(generator))
"""
"""def gcd_(a,b):
  if b == 0:#結局はc,0の最大公約数はcなのに
    return a
  return gcd_(a,a % b) # a = p * b + q"""
"""def extgcd(a,b,x,y):
  d = a
  if b!=0:
    d = extgcd(b,a%b,y,x)
    y -= (a//b) * x
    print(x,y)
  else:
    x = 1
    y = 0
  return d"""
# 最大公約数 と 最小公倍数
"""def gcd(a,b):
  if b == 0:
    return a
  return gcd(b, a % b)
def lcm(a,b):
  g = gcd(a,b)
  return (a * b) // g"""

def readInts():
  return list(map(int,input().split()))
mod = 10**9 + 7

def main():
  A,B,C,D,E,F = readInts()
  dic = {}
  for a in range(31):# 30まで
    for b in range(31): # 30まで
      for c in range(101): # 100まで
        for d in range(101):
          w = (100*A)*a + (100 * B ) *b
          s = C * c + D * d
          if w == 0:
            break
          if w + s > F:
            break
          else:
            if w/100 * E >= s:
              mitudo = 100 * s / (w + s)
              dic[a,b,c,d] = mitudo
  maxV = max(dic.values())
  for k,v in dic.items():
    if v == maxV:
      print((100*A)*k[0] + (100*B)*k[1] + C*k[2] + D*k[3],C*k[2] + D*k[3])
      exit()
if __name__ == '__main__':
  main()