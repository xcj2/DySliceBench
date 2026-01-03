def main():
  n = int(input())
  a = list(input_list())
  ac = collections.Counter(sorted(a))
  aa = []
  hw = []
  for v, count in ac.items():
    if count >= 2:
      aa.append(v)
    if count >= 4:
      hw.append(v)
      
  sa = sorted(aa, reverse=True)
  shw = sorted(hw, reverse=True)
  if len(shw) > 0:
    if len(sa) < 2:
      print(shw[0]*shw[0])
    else:
      print(max(shw[0]*shw[0], sa[0]*sa[1]))
    exit()
  
  if len(sa) < 2:
    print(0)
    exit()
  
  print(sa[0]*sa[1])
    
    
  
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