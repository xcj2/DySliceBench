#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import defaultdict



MOD = 10**9+7
FACTOR = []

def factrial(n):
  global FACTOR
  FACTOR = [1 for _ in range(n+1)]
  for i in range(1,n+1):
    FACTOR[i] = (FACTOR[i-1]*i) % MOD

def mul(a,b):
  return (a*b) % MOD

def power(a,b):
  ## 二分累乗法
  if   b==0   : return 1
  elif b==1   : return a % MOD
  elif b%2==0 : return power(a,b//2)**2 % MOD
  else        : return power(a,b//2)**2 * a % MOD

def div(a,b):
  ## MOD同士の割り算
  return mul(a,power(b,MOD-2))

## 素因数分解
def factoring(m):
  fact = defaultdict(lambda:0)
  idx = 2
  while m > idx:
    if m%idx==0:
      fact[idx] += 1
      m //= idx
    else:
      idx += 1
  fact[m] += 1
  ret = []
  for k in fact:
    ret.append(fact[k])
  return ret

def combi(a,b):
  if a<b:
    return 1
  else:
    return div(FACTOR[a], (FACTOR[b]*FACTOR[abs(a-b)])%MOD)


def main():
  N,M = map(int, input().split())
  if N == 1 or M==1:
    print(1)
  else:
    fact = factoring(M)
    factrial(N+max(fact))
    ans = 1
    for f in fact:
      ans = (ans * combi(f+N-1,N-1)) % MOD
    print(ans)


if __name__ == "__main__":
  main()