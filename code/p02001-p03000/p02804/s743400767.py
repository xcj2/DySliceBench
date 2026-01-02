#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random

MAX = 10**9 + 7

def pow_mod_p(n, k, p):
  x = 1
  while k > 0:
    if k % 2 == 1:
      x *= n
      x %= p
    n **= 2
    n %= p
    k >>= 1
  return x

def comb_mod_p(n, k, p):
  x = 1
  for ik in range(k):
    x *= ((n-ik) * pow_mod_p(ik+1, p-2, p))
    x %= p
  return x

def main():
  n, k = map(int, input().strip().split())
  As = list(map(int, input().strip().split()))
  As.sort()
  min = 0
  max = 0
  x = comb_mod_p(n-1, k-1, MAX)
  for i in range(n-k+1):
    min += As[i]      * int(x)
    min %= MAX
    max += As[-(i+1)] * int(x)
    max %= MAX
    x *= (pow_mod_p(n-(i+1), MAX-2, MAX) * (n-(i+1)-(k-1)))
    x %= MAX
  print((max - min) % (MAX))

if __name__=='__main__':
  main()
