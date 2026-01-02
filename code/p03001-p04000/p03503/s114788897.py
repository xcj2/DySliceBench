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
# 二分探索
"""import bisect # 二分探索
print(A,bisect.bisect_left(A,4))
print(C,n - bisect.bisect_right(C,4))
print(sum(bisect.bisect_left(A,b) * (n-bisect.bisect_right(C,b)) for b in B))"""

def readInts():
  return list(map(int,input().split()))
mod = 10**9 + 7

def main():
  n = int(input())
  F = [readInts() for _ in range(n)]
  P = [readInts() for _ in range(n)]
  
  max_score = -float('inf')
  
  for i in range(1, 2**10):
    op_num = [0] * n
    for j in range(10):
      if i & 1 << j:
        for n_i in range(n):
          op_num[n_i] += F[n_i][j]
    max_score = max(max_score, sum([p_i[op_num_i] for p_i, op_num_i in zip(P,op_num)]))
  print(max_score)
if __name__ == '__main__':
  main()