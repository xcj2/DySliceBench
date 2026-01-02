def gcd(n, m):
  while m:
    n, m = m, n%m
  return n

def isprime(n):
  if n == 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if (n % i == 0):
      return False
  return True

def divi(n):
  res = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      res.append(i)
      if i != n // i:
        res.append(n // i)
  return res

import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  a, b = na()
  gcd_ = gcd(a, b)
  ans = 1
  for d in divi(gcd_):
    if isprime(d):
      ans += 1
  print(ans)

main()