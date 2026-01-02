def main():
  c = []
  for _ in range(3):
    c.append(list(input_list()))
  
  for a1 in range(101):
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    a2 = c[1][0] - b1
    a3 = c[2][0] - b1
    if a1+b1 == c[0][0] and a1+b2 == c[0][1] and a1+b3 == c[0][2] and\
    a2+b1 == c[1][0] and a3+b1 == c[2][0] and a2+b2 == c[1][1] and a2+b3 == c[1][2] and\
    a3+b2 == c[2][1] and a3+b3 == c[2][2]:
      print('Yes')
      exit()
  print('No')
    
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