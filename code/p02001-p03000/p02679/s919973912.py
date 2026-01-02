#!/usr/bin/env python
# -*- coding: utf-8 -*-
M = 1000000007


def gcd(a, b):
  while b != 0:
    a, b = b, a % b

  return a


def comb(n):
  c = 1

  for _ in range(n):
    c = (c * 2) % M

  return c - 1


def main():
  zeros = 0
  groups = {}

  for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == 0 and b == 0:
      zeros += 1
      continue

    if a == 0:
      v = (1, 0)
      i = 0
    elif b == 0:
      v = (1, 0)
      i = 1
    else:
      if b < 0:
        a = -a
        b = -b

      g = gcd(a, b)
      a //= g
      b //= g

      if a > 0:
        v = (a, b)
        i = 0
      else:
        v = (b, -a)
        i = 1

    if v not in groups:
      groups[v] = [0, 0]

    groups[v][i] += 1

  count = 1

  for k, (v1, v2) in groups.items():
    c = (comb(v1) + comb(v2) + 1) % M
    count = (count * c) % M

  count = (count - 1 + zeros) % M

  print(count)


if __name__ == '__main__':
  main()
