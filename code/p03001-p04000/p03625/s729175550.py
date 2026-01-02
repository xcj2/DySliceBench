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
  n = int(input())
  dic = {}
  for nya in map(int,input().split()):
    if nya in dic:
      dic[nya] += 1
    else:
      dic[nya] = 1
  
  LIST = []
  
  for k,v in dic.items():
    if v // 2 >= 1 and v > 1: # 最低限2個以上は必要
      LIST.append([k,v])
  LIST = sorted(LIST,reverse = True)
  #print(LIST) # [[5, 3], [4, 3], [3, 4]]
  cnt = 0
  pr_ = 0
  for k,v in LIST:
    #print(k,v)
    if v // 2 >= 2 and cnt == 0:
      print(k * k)
      exit()
    elif v // 2 == 1 and cnt == 0:
      cnt += 2
      pr_ = k
    elif v // 2 >= 1 and cnt == 2:
      print(pr_ * k)
      exit()
  print(0)
  
if __name__ == '__main__':
  main()