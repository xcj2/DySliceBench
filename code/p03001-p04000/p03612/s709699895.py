def main():
  n = int(input())
  p = list(input_list())
  dp = p[:]
  count = 0
  skip = False
  for i, v in enumerate(p):
    if skip:
      skip = False
      continue
    if i+1 == v:
      if i + 1 > len(p) - 1:
        count += 1
        continue
        
      count += 1
      skip = True
  print(count)
  
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
from functools import reduce
main()