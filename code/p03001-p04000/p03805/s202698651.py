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
#def main():
n,m = readInts()
a = [0] * m
b = [0] * m

graph = [[False for i in range(n)] for j in range(n)]

for i in range(m):
  a[i],b[i] = map(int,input().split())
  a[i] -=1
  b[i] -=1
  graph[a[i]][b[i]] = True
  graph[b[i]][a[i]] = True

cnt = 0
now = [0] * n

def dfs(pos,nya):
  global cnt
  if pos == n:
    if now[0] == 0:
      for i in range(n-1):
        if graph[now[i]][now[i+1]] == False:
          break
        if i == n-2:
          cnt += 1
    return
  for i in range(n):
    if nya & (1 << i):
      now[pos] = i
      dfs(pos+1,nya^(1<<i))
dfs(0,(1<<n)-1)
print(cnt)
  
#if __name__ == '__main__':
#  main()