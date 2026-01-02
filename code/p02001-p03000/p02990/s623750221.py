#!/usr/bin/env python3
import math
def comb(a, b):
    return math.factorial(a) // (math.factorial(a - b) * math.factorial(b))

def c(a, b):
  return comb(a, b)

def f2(a, b):
  return c(a+b-1, b-1)

def f(a, b):
  if a < b:
    return 0
  if a == 0 and b == 0:
    return 1
  if b < 1:
    return 0
  return f2(a-b, b)

n, k = map(int, input().split())
mod = 10**9+7

def main():
  for i in range(1, k+1, 1):
    blue = f(k, i)
    red = 0
    red += f(n-k, i-1)
    red += f(n-k, i)
    red += f(n-k, i)
    red += f(n-k, i+1)

    ans = blue * red
    print(ans%mod)

main()
