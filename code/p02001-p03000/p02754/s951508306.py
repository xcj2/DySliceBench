def main():
  n, blue, red = input_list()
  d = n % (blue+red)
  if d == 0:
    print(blue * (n // (blue+red)))
  else:
    if d > blue:
      d = blue
    print(blue * (n // (blue+red))+d)
    
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