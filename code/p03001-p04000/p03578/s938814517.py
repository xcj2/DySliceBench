def main():
  n = int(input())
  m = list(input_list())
  d = int(input())
  t = list(input_list())
  if n < d:
    print('NO')
    exit()
  mc = collections.Counter(m)
  tc = collections.Counter(t)
  for key, count in tc.items():
    if mc[key] < count:
      print('NO')
      exit()
  print('YES')
  
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

import math
import fractions
import collections
from functools import reduce
main()