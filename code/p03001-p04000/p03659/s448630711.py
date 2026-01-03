def main():
  n = int(input())
  a = list(input_list())
  sa = sum(a)
  ans = 10**10
  r = 0
  for v in list(a)[:-1]:
    r += v
    ans = min(ans, abs(sa - (2*r)))
  print(ans)

def input_list():
  return map(int, input().split())

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

import math
import fractions
from functools import reduce
main()