#!/usr/bin/python3
# -*- coding: utf-8 -*-


MOD = 10**9+7

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

Fact = [1 for i in range(2001)]
for i in range(1,2001):
  Fact[i] = mul(i,Fact[i-1])


N,K = map(int, input().split())
for k in range(1,K+1):
  ans = 0
  if k <= N-K+1:
    a1 = div(Fact[N-K+1],mul(Fact[k],Fact[N-K+1-k]))
    if k==1:
      a2 = 1
    else:
      a2 = div(Fact[K-1],mul(Fact[k-1],Fact[K-k]))
    ans = mul(a1,a2)
  print(ans)
