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


def readInts():
  return list(map(int,input().split()))
mod = 10**9 + 7
def main():
  n = int(input())
  A = readInts()
  
  cur = 0
  ans1 = 0
  for i in range(n):
    cur += A[i]
    if i % 2:
      if cur <= 0:
        ans1 += -cur+1
        cur = 1
    else:
      if cur >= 0:
        ans1 += cur + 1
        cur = -1
  cur = 0
  ans2 = 0
  for i in range(n):
    cur += A[i]
    if i % 2:
      if cur >= 0:
        ans2 += cur + 1
        cur = -1
    else:
      if cur <= 0:
        ans2 += -cur + 1
        cur = 1
  print(min(ans1,ans2))
if __name__ == '__main__':
  main()