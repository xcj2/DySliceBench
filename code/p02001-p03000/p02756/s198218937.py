def main():
  w = input()
  s = collections.deque(w)
  n = int(input())
  
  order = True
  for _ in range(n):
    q = list(input_list_str())
    if len(q) == 1:
      order = False if order else True
      continue
    t, f, c = q
    if int(f) == 1:
      if order:
        s.appendleft(c)
      else:
        s.append(c)
    else:
      if order:
        s.append(c)
      else:
        s.appendleft(c)
  if order is False:
    s.reverse()
  print(''.join(s))

    
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
import collections
from functools import reduce
main()