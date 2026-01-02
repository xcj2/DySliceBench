def main():
  a, b = input_list()
  ans = []
  for i in range(1, 1001):
    ai = i * 0.08
    bi = i * 0.1
    if int(ai) == a and int(bi) == b:
      ans.append(i)
  if len(ans) == 0:
    print(-1)
  else:
    print(min(ans))
    
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