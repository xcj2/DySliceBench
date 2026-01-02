# -*- coding: utf-8 -*-

from math import factorial

MOD = 10 ** 9 + 7

def readInts():
  return [int(s) for s in input().split(" ")]

def combi(n, r):
  num = 1
  den1 = 1
  den2 = 1

  for i in range(1, n + 1):
    num = (num * i) % MOD

  for i in range(1, r + 1):
    den1 = (den1 * i) % MOD

  for i in range(1, n - r + 1):
    den2 = (den2 * i) % MOD

  return (num * pow(den1 * den2, MOD - 2, MOD)) % MOD

def solve():
  X, Y = readInts()

  X, Y = max(X, Y), min(X, Y)

  if (X + Y) % 3 != 0:
    return 0

  a = (2 * X - Y) // 3
  b = (2 * Y - X) // 3

  if a < 0 or b < 0:
    return 0

  return combi(a + b, min(a, b)) % MOD

def main():
  print(solve())

if __name__ == "__main__":
  main()
