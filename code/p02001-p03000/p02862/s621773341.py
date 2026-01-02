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
  x, y = map(int, input().strip().split())
  m = (2*x -   y)/3
  k = ( -x + 2*y)/3
  if m - int(m) != 0 or k - int(k) != 0 \
     or m < 0 or k < 0 :
    print(0)
    return 
  m, k = map(int, [m, k])
  if m < k:
    m, k = k, m
  print(comb_mod_p((m+k), k, MAX))
  
  
if __name__=='__main__':
  main()

