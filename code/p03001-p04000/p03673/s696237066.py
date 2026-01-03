def main():
  n = int(input())
  a = list(input_list_str())
  index = n - 1
  ans = [a[index]]
  
  is_add = False
  for i in range(n-1):
    if is_add:
      index += 2
    else:
      index -= 2
    if index < 0:
      index = 0
      is_add = True
      
    ans.append(a[index])
    
    if index == 0 and is_add is False:
      index = -1
      is_add = True
    
      
  print(' '.join(ans))


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