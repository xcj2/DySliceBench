# -*- coding: utf-8 -*-

from math import factorial

def readInts():
  return [int(s) for s in input().split(" ")]

def combi(n, r):
  r = min(n-r, r)
  if r == 0:
    return 1
  if r == 1:
    return n
  ret = 1
  for i in range(r):
    ret *= (n - i)
  return ret // factorial(r)

mod = 10 ** 9 + 7

def solve(N, K, i):
  if i == 1:
    return combi(N - K + 1, 1) % mod
  if N - K < i - 1:
    return 0

  ret = combi(K - 1, i - 1) % mod
  if N - K - (i - 1) > 0:
    ret *= combi(N - K - (i - 1) + i, i) % mod
  return ret % mod

def main():
  N, K = readInts()
  for i in range(1, K+1):
    print(solve(N, K, i))

if __name__ == "__main__":
  main()
