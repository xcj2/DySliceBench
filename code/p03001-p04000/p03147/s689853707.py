def main():
  n = int(input())
  h = input_list()
  ans = 0
  while True:
    ans += count_section_by_zero(h)
    h = list(map(lambda x: 0 if x == 0 else x-1, h))
    if all([v == 0 for v in h]):
      break
  print(ans)

def count_section_by_zero(data):
  count = 0
  flg = False
  start = 0
  for i, d in enumerate(data):
    if flg is False and d != 0:
      count += 1
      flg = True
      
    if d == 0:
      flg = False
  return count
  
def input_list():
  return list(map(int, input().split()))

def input_list_str():
  return map(str, input().split())

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

# 2で割り切れる回数
def divide_two(arg):
  c = 0
  while True:
    if c >= 2:
      break
    if arg % 2 != 0:
      break
    arg //= 2
    c += 1
  return c

# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

import math
import fractions
import collections
from functools import reduce
main()