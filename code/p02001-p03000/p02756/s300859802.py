def main():
  w = input()
  s = collections.deque(w)
  n = int(input())
  
  reverse_count = 0
  for i in range(n):
    t = list(input_list_str())
    if len(t) == 1:
      reverse_count = 1 - reverse_count
      continue
    q, f, c = t
    if int(f) + reverse_count == 2:
      s.append(c)
    else:
      s.appendleft(c)
  if reverse_count == 1:
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