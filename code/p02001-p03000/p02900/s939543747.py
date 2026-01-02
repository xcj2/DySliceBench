#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 最大公約数
def gcd(a, b):
  while b != 0:
    a, b = b, a % b

  return a


# 素因数分解
def factorization(n):
  arr = []
  temp = n

  for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
    if temp % i == 0:
      cnt = 0
      while temp % i == 0:
        cnt += 1
        temp //= i
      arr.append([i, cnt])

  if temp != 1:
    arr.append([temp, 1])

  if arr == []:
    arr.append([n, 1])

  return arr


def main():
  a, b = map(int, input().split())
  g = gcd(a, b)
  fs = [v for v, _ in factorization(g) if v != 1]
  print(len(fs) + 1)


if __name__ == '__main__':
  main()
