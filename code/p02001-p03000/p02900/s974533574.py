#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 最大公約数
def gcd(a, b):
  while b != 0:
    a, b = b, a % b

  return a


# 素因数分解
def primes(v):
  ps = []

  for i in range(2, int(v ** 0.5) + 1):
    if i ** 2 > v:
      break

    if v % i == 0:
      ps.append([i, 1])
      v //= i

      while v % i == 0:
        ps[-1][1] += 1
        v //= i

  if v > 1:
    ps.append([v, 1])

  return ps


def main():
  a, b = map(int, input().split())
  g = gcd(a, b)
  print(len(primes(g)) + 1)


if __name__ == '__main__':
  main()
