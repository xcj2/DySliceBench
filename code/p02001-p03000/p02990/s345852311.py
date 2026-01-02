#!/usr/bin/python3
# -*- coding:utf-8 -*-

MAX = 10**9 + 7

def pow_mod_p(n, k, p):
  x = 1
  while k:
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
  a, b = comb_mod_p(n-k+1, 1, MAX), comb_mod_p(k-1, 1-1, MAX)
  for i in range(1,k+1):
    if i != 1:
      a = (a * (n-k+1-(i-1))) * pow_mod_p(i, MAX-2, MAX)
      b = (b * (k-1-((i-1)-1))) * pow_mod_p(i-1, MAX-2, MAX)
    print((a * b) % MAX)

if __name__=='__main__':
  main()

